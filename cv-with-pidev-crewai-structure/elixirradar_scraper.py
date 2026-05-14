# elixirradar_scraper.py
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json

def scrape_elixir_radar():
    results = []
    url = "https://elixir-radar.com/jobs"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        )
        try:
            page.goto(url, wait_until='domcontentloaded')
            page.wait_for_selector('.jobs-list-item', timeout=15000)
            
            job_items = page.locator('.jobs-list-item').all()

            for item in job_items:
                title_element = item.locator('.job-title')
                company_element = item.locator('.job-company-name')
                
                title = title_element.inner_text()
                company = company_element.inner_text()
                relative_url = title_element.get_attribute('href')
                full_url = "https://elixir-radar.com" + relative_url
                
                # Buscamos roles que no sean explícitamente de alto nivel
                if 'senior' not in title.lower() and 'lead' not in title.lower() and 'principal' not in title.lower() and 'staff' not in title.lower():
                    results.append({
                        "url": full_url,
                        "title": title,
                        "company": company,
                        "source": "Elixir Radar"
                    })
                
                if len(results) >= 5:
                    break
        except PlaywrightTimeoutError:
            page.screenshot(path='elixirradar_error.png')
            
        browser.close()
    return results

if __name__ == "__main__":
    jobs = scrape_elixir_radar()
    print(json.dumps(jobs, indent=2))
