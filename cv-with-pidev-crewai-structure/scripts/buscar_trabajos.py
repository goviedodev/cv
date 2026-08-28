# buscar_trabajos.py
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import json
import re

def search_jobs():
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        )
        page.goto("https://www.google.com/search?q=site%3Agetonbrd.com+elixir+developer", wait_until='domcontentloaded')

        # --- Manejar pop-ups de consentimiento de cookies ---
        consent_button_selectors = [
            'button:has-text("Accept all")',
            'button:has-text("Aceptar todo")',
            'button:has-text("I agree")',
            'div[role="button"]:has-text("Accept")',
            'div[role="button"]:has-text("Aceptar")'
        ]
        
        try:
            # Esperar a que aparezca uno de los selectores, con un tiempo de espera corto
            consent_locator = page.locator(", ".join(consent_button_selectors))
            consent_locator.first.click(timeout=5000)
            page.wait_for_load_state('domcontentloaded', timeout=5000)
        except PlaywrightTimeoutError:
            # Si no se encuentra ningún botón de consentimiento después de 5s, asumir que no está y continuar.
            pass
            
        # --- Esperar los resultados y extraerlos ---
        try:
            # Esperar a que el contenedor principal de resultados de búsqueda esté presente
            page.wait_for_selector('#search', timeout=15000)
            
            # Encontrar todos los enlaces dentro del contenedor #search
            links = page.locator('#search a[href]').all()

            for link in links:
                href = link.get_attribute('href')
                if href and re.search(r'https://(www.)?getonbrd.com/empleos/', href):
                     # Limpiar la URL de redirección de Google si está presente
                    if '/url?q=' in href:
                        href = href.split('/url?q=')[1].split('&sa=')[0]
                    if href not in results:
                        results.append(href)
                if len(results) >= 5:
                    break
        except PlaywrightTimeoutError:
            # Si no se pueden encontrar los resultados, es probable que haya un CAPTCHA.
            page.screenshot(path='error_screenshot.png')

        browser.close()
    return results

if __name__ == "__main__":
    jobs = search_jobs()
    # Imprimir los resultados como un JSON para que sea fácil de procesar
    print(json.dumps(jobs, indent=2))
