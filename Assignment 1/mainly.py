from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import random
import time
import urllib.parse

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

hw1_json = {}

def search(query):
    links = set() 
    try:
        # Delay between 10 and 100 seconds
        delay = random.uniform(10, 100)
        print(f"Sleeping for {delay:.2f} seconds")
        time.sleep(delay)

        url = f"https://www.duckduckgo.com/html/?q={query}"
        driver.get(url)

        results = driver.find_elements(By.CSS_SELECTOR, 'a.result__a')

        count = 0
        for result in results:
            link = result.get_attribute('href') 
            # Extract the direct link from the DuckDuckGo redirect URL
            parsed_link = urllib.parse.parse_qs(urllib.parse.urlparse(link).query).get('uddg')
            if parsed_link:
                direct_link = parsed_link[0]
                if direct_link not in links: 
                    links.add(direct_link)
                    count += 1
                if count >= 10:  # Limit to 10 results
                    break

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    return list(links)  # Return as a list to store in JSON


def main():
    queries = []

    with open('100QueriesSet4 - Copy.txt', 'r') as f:
        for line in f:
            queries.append(line.strip())
    
    # Search for each query and store the results
    for query in queries:
        print(f"Searching for: {query}")
        output = search(query)
        if output:
            hw1_json[query] = output

    with open('hw1.json', 'w') as f:
        json.dump(hw1_json, f, indent=4)
    print("Results saved to json")

    
    driver.quit()


if __name__ == '__main__':
    main()
