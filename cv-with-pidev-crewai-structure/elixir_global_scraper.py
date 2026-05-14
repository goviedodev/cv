# elixir_global_scraper.py
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json

def scrape_global_elixir():
    results = []
    url = "https://remoteok.com/remote-elixir-jobs"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        )
        try:
            page.goto(url, wait_until='domcontentloaded')
            page.wait_for_selector('table#jobsboard', timeout=20000)
            
            # Capturamos todas las filas de trabajo que la página ofrece para "Elixir"
            job_rows = page.locator('tr.job').all()

            for row in job_rows:
                title_element = row.locator('h2[itemprop="title"]')
                # Nos aseguramos de que "Elixir" esté en el título para evitar resultados no relacionados
                title_text = title_element.inner_text()
                if 'elixir' not in title_text.lower():
                    continue

                company = row.get_attribute('data-company')
                relative_url = row.get_attribute('data-url')
                
                if relative_url:
                    full_url = "https://remoteok.com" + relative_url
                    results.append({
                        "url": full_url,
                        "title": title_text,
                        "company": company,
                        "source": "Remote OK"
                    })
                
                if len(results) >= 10: # Aumentamos el límite para una red más amplia
                    break
        except PlaywrightTimeoutError:
            page.screenshot(path='elixir_global_error.png')
            
        browser.close()
    return results

if __name__ == "__main__":
    jobs = scrape_global_elixir()
    print(json.dumps(jobs, indent=2))
