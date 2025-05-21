import time
import random
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

#Configuration


primary_keyword   = "optane"
'''
secondary_keywords = ["data structure"(done), "index structure"(done), "database(done)", "storage engine(done)", "file system(done)", "high performance computing(done)"]
'''
secondary_keyword = "database"
# QUERY             = f"'{primary_keyword}' + '{secondary_keyword}'"
QUERY = f"%27{primary_keyword}%27+%2B+%27{secondary_keyword}%27"
TOTAL             = 300
PER_PAGE          = 10
PROXY_LIST        = []  # e.g. ["123.45.67.89:8080", "socks5://98.76.54.32:1080"]
print(QUERY)
UA = UserAgent()

#Helper Functions
def get_options(proxy: str = None):
    opts = webdriver.ChromeOptions()
    # run in headed mode so you can solve CAPTCHAs
    opts.headless = False
    # randomize User-Agent
    opts.add_argument(f"--user-agent={UA.random}")
    # disable selenium flags
    opts.add_argument("--disable-blink-features=AutomationControlled")
    # optional proxy
    if proxy:
        if not proxy.startswith(("http://","https://","socks4://","socks5://")):
            proxy = "http://" + proxy
        opts.add_argument(f"--proxy-server={proxy}")
    return opts

def parse_page(driver):
    out = []
    entries = driver.find_elements(By.CSS_SELECTOR, "div.gs_ri")
    for e in entries:
        # Title & link
        try:
            h3 = e.find_element(By.CSS_SELECTOR, "h3.gs_rt")
            a  = h3.find_element(By.TAG_NAME, "a")
            title = a.text
            link  = a.get_attribute("href")
        except:
            title = e.find_element(By.CSS_SELECTOR, "h3.gs_rt").text or ""
            link  = ""

        # Meta line (authors/journal/year)
        meta_txt = ""
        try:
            meta_txt = e.find_element(By.CSS_SELECTOR, "div.gs_a").text
        except:
            pass

        # Extract year
        year = ""
        m = re.search(r"\b(19|20)\d{2}\b", meta_txt)
        if m:
            year = m.group(0)

        # Number of citations
        cited_by = 0
        try:
            for a in e.find_elements(By.TAG_NAME, "a"):
                txt = a.text
                if txt.startswith("Cited by"):
                    cited_by = int(txt.split()[-1])
                    break
        except:
            pass

        # Build record with extra columns
        out.append({
            "Paper title": title,
            "Paper link": link,
            "Year of publishing": year,
            "Number of citations": cited_by,
            "Keywords": f'"{primary_keyword.capitalize()}" "{secondary_keyword.title()}"',
            "Relevant for study": "Yes" if year and int(year) >= 2019 else "No",
            "Duplicate": "",
            "Reviewer": "",
            "Applicable/Non Applicable": "",
            "Reason for choosing/ not choosing the research paper": ""
        })
    return out

#Main Scraper
def scrape():
    results = []
    for offset in range(0, TOTAL, PER_PAGE):
        proxy  = random.choice(PROXY_LIST) if PROXY_LIST else None
        opts   = get_options(proxy)
        driver = webdriver.Chrome(options=opts)

        url = (
            "https://scholar.google.com/scholar?"
            f"hl=en&q={QUERY.replace(' ', '+')}&start={offset}"
        )
        driver.get(url)

        # Detect CAPTCHA
        page_src = driver.page_source.lower()
        if any(kw in page_src for kw in ["captcha", "unusual traffic", "verify you are human"]):
            print(f"CAPTCHA detected at offset={offset}.")
            print("Please solve it in the opened browser, then press Enter here to continue.")
            input("Press Enter once CAPTCHA is solved…")

        try:
            # allow up to 60s for results to load
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.gs_ri"))
            )
            batch = parse_page(driver)
            if not batch:
                print(f"[!] No results parsed at start={offset}")
            else:
                print(f"[+] Fetched {len(batch)} results @ start={offset}")
                results.extend(batch)
        except Exception as e:
            print(f"[!] Error @ start={offset}: {e}")
        finally:
            driver.quit()

        #delay
        time.sleep(random.uniform(5, 10))
        if len(results) >= TOTAL:
            break

    return results[:TOTAL]

def save_csv(data, path="optane_data_structure_papers.csv"):
    fieldnames = [
        "Paper title",
        "Paper link",
        "Year of publishing",
        "Number of citations",
        "Keywords",
        "Relevant for study",
        "Duplicate",
        "Reviewer",
        "Applicable/Non Applicable",
        "Reason for choosing/ not choosing the research paper"
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"Saved {len(data)} records to {path}")

#Entry Point
if __name__ == "__main__":
    papers = scrape()
    save_csv(papers)
