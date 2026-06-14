import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://cl.computrabajo.com/trabajo-de-analista-en-rmetropolitana-en-santiago-las-condes?q=analista+programador"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    articles = soup.find_all('article')
    for article in articles:
        title_el = article.find('h2')
        if title_el:
            print("Title:", title_el.text.strip())
            link = article.find('a', class_='js-o-link')
            if link:
                print("Link:", link.get('href'))
                
            print("---")
except Exception as e:
    print("Error:", e)
