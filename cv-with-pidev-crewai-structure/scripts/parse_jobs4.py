import urllib.request
from bs4 import BeautifulSoup

url = "https://cl.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-3B55A8B13DB4E34A61373E686DCF3405"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.find('h1')
    if title: print("Title:", title.text.strip())
    
    company = soup.find('a', class_='tx_link_emp')
    if company: print("Company:", company.text.strip())
    
    desc = soup.find('div', class_='box_detail')
    if desc: print("Desc:", desc.text.strip())
except Exception as e:
    print("Error:", e)
