# remoteok_scraper.py
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json

def search_remote_ok():
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        )
        try:
            # Remote OK tiene una URL directa para las etiquetas de búsqueda
            page.goto("https://remoteok.com/remote-elixir-jobs", wait_until='domcontentloaded')

            # Esperar a que la tabla de trabajos esté cargada
            page.wait_for_selector('table#jobsboard', timeout=15000)
            
            # Obtener los enlaces de las ofertas de trabajo
            # El atributo 'data-url' contiene el enlace relativo
            job_rows = page.locator('tr.job:has-text("Elixir")').all()

            for row in job_rows:
                # Filtrar por "Junior" o roles sin nivel especificado
                title_text = row.locator('h2[itemprop="title"]').inner_text()
                if 'senior' not in title_text.lower() and 'lead' not in title_text.lower() and 'principal' not in title_text.lower():
                    relative_url = row.get_attribute('data-url')
                    if relative_url:
                        full_url = "https://remoteok.com" + relative_url
                        if full_url not in results:
                            results.append(full_url)
                if len(results) >= 5:
                    break
        except PlaywrightTimeoutError:
            page.screenshot(path='remoteok_error.png')
            
        browser.close()
    return results

if __name__ == "__main__":
    jobs = search_remote_ok()
    print(json.dumps(jobs, indent=2))
