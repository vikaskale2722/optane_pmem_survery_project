import requests
import pandas as pd
import time
import random
from bs4 import BeautifulSoup

#Configuration
USERNAME = "vikaskale_6h9cq"
PASSWORD = "" # Add your password here
primary_keywords = ["Optane"]
secondary_keywords = ["data structure", "index structure", "database", "storage engine", "file system", "high performance computing"]
max_pages_per_query = 50
output_file = "research_papers.csv"

#Containers
papers = []
seen_titles = set()
zero_result_keywords = []

#Helper Functions

def get_html_for_page(url):
    payload = {"url": url, "source": "google"}
    response = requests.post(
        "https://realtime.oxylabs.io/v1/queries",
        auth=(USERNAME, PASSWORD),
        json=payload,
    )
    response.raise_for_status()
    return response.json()["results"][0]["content"]

def safe_get_html(url, retries=3):
    for attempt in range(retries):
        try:
            html = get_html_for_page(url)
            if "gs_ri" in html:
                return html
        except Exception as e:
            print(f"Retry {attempt + 1}/{retries} failed: {e}")
        time.sleep(random.uniform(2, 4))
    print(f"All retries failed for {url}")
    return None

def get_url_for_page(query, page_index):
    query_encoded = "+".join(query.split())
    return f"https://scholar.google.com/scholar?start={page_index}&q={query_encoded}&hl=en&as_sdt=0,5"

def add_paper(title, year, link, keyword, source):
    key = (title.lower(), link.lower())
    is_duplicate = "duplicate" if key in seen_titles else "not duplicate"
    applicable = "applicable" if str(year).isdigit() and int(year) >= 2019 else "non applicable"
    if is_duplicate == "not duplicate":
        seen_titles.add(key)
    papers.append({
        "Paper Title": title,
        "Year of Publishing": year,
        "Paper Link": link,
        "Search Keyword": keyword,
        "Source": source,
        "Applicable": applicable,
        "Duplicate": is_duplicate
    })

def extract_year(text):
    import re
    match = re.search(r"\b(20\d{2}|19\d{2})\b", text)
    return match.group(0) if match else "N/A"

def scrape_google_scholar(query):
    print(f"Scraping: {query}")
    found_any = False
    for page in range(0, max_pages_per_query * 10, 10):
        url = get_url_for_page(query, page)
        html = safe_get_html(url)
        if not html:
            continue
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find_all("div", class_="gs_ri")
        if not results:
            print(f"No results found for '{query}' on page {page // 10 + 1}")
            continue

        found_any = True
        for result in results:
            title_elem = result.find("h3", class_="gs_rt")
            link_elem = title_elem.find("a") if title_elem else None
            title = title_elem.get_text(strip=True) if title_elem else "N/A"
            link = link_elem["href"] if link_elem and "href" in link_elem.attrs else "N/A"
            year = extract_year(result.find("div", class_="gs_a").text)
            add_paper(title, year, link, query, "Google Scholar")
        time.sleep(random.uniform(2, 4))
    if not found_any:
        zero_result_keywords.append(query)

#Main Execution

def main():
    for primary in primary_keywords:
        for secondary in secondary_keywords:
            combined_query = f'"{primary}" "{secondary}"'
            scrape_google_scholar(combined_query)

    df = pd.DataFrame(papers)
    df.to_csv(output_file, index=False)
    print(f"\nDone. {len(papers)} papers saved to '{output_file}'")

    if zero_result_keywords:
        print("\nNo results found for these queries:")
        for q in zero_result_keywords:
            print("  -", q)

if __name__ == "__main__":
    main()
