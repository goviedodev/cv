# remoteok_scraper_europa.py
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json

def search_remote_ok_europe():
    results = []
    # Usamos el término de búsqueda directamente en la URL para "Elixir"
    search_url = "https://remoteok.com/remote-elixir-jobs"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        )
        try:
            page.goto(search_url, wait_until='domcontentloaded')
            page.wait_for_selector('table#jobsboard', timeout=20000)
            
            # Buscamos filas que contengan "Elixir" y opcionalmente filtramos por ubicación si es posible
            job_rows = page.locator('tr.job:has-text("Elixir")').all()

            for row in job_rows:
                # Extraer el título para inspección
                title = row.locator('h2[itemprop="title"]').inner_text()
                
                # Extraer la URL
                relative_url = row.get_attribute('data-url')
                if not relative_url:
                    continue
                
                full_url = "https://remoteok.com" + relative_url
                
                # Extraer la compañía
                company = row.get_attribute('data-company')
                
                # Aquí podemos añadir lógica de filtrado más compleja si es necesario
                # Por ahora, aceptaremos cualquier rol de Elixir que no sea explícitamente "Lead" o "Principal"
                if 'lead' not in title.lower() and 'principal' not in title.lower():
                    results.append({
                        "url": full_url,
                        "title": title,
                        "company": company,
                        "source": "Remote OK"
                    })

                if len(results) >= 5:
                    break
        except PlaywrightTimeoutError:
            page.screenshot(path='remoteok_europe_error.png')
            
        browser.close()
    return results

if __name__ == "__main__":
    jobs = search_remote_ok_europe()
    print(json.dumps(jobs, indent=2))
