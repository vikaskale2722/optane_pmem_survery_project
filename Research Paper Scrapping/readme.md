How to Install
  1. Download python
  2. pip install selenium fake_useragent
  3. Update the "primary_keyword", "secondary_keyword" and "TOTAL" variable
  4. run the file
  5. If the chrome browser propmts for captcha, solve them and press Enter in the running python terminal

How it Works
  1. Loops over pages of Scholar (0, 10, 20 … up to 290) until it’s got 300 entries.
    For each page it:
      ->Launches a (headed) Chrome window with a random user-agent string.
      ->Goes to the Scholar search URL.
      ->Checks if a CAPTCHA popped up—if so, it stops and asks you to solve it in that window.
      ->Waits (up to 60 s) for the list of results to appear.
      ->Pulls out each paper’s title, link, publication year, and citation count.
      ->Fills in the extra fields for keywords, relevance (pre-2019 = “No”), and leaves the reviewer/duplicate/etc. blank
      ->Closes that browser tab and sleeps for a few seconds (to look less like a bot).
  2. After it’s done (or hit your 300-paper cap), it writes everything into optane_data_structure_papers.csv
