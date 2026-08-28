import urllib.request
from bs4 import BeautifulSoup

url = "https://cl.computrabajo.com/trabajo-de-analista-en-rmetropolitana-en-santiago-las-condes?utm_source=auto_cand_alertacargosdiaria&utm_campaign=auto_cand_alertacargosdiaria_gmail&utm_medium=email&oi=6C7B2FE9F143873B61373E686DCF3405&prov=14&q=analista-programador&om=F509438085EBCBBEFFBD009C36CBAE72DF7CC3BA1826A603AF641451F48FD82F38F1FFB17434AC35C132D5A7E06450F46465E0F56A3B9F9FA282BB733B556831A26D0E21D8F775F77D1AF5614416819D&fgoa=True#3B55A8B13DB4E34A61373E686DCF3405"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # The specific job from the hash
    target_id = "3B55A8B13DB4E34A61373E686DCF3405"
    
    articles = soup.find_all('article')
    print(f"Found {len(articles)} articles")
    for article in articles:
        if target_id in str(article):
            print("\n--- FOUND TARGET JOB ---")
            title = article.find('h2')
            if title: print("Title:", title.text.strip())
            company = article.find('a', class_='tx_link_emp')
            if not company: company = article.find('p', class_='fs16')
            if company: print("Company:", company.text.strip())
            desc = article.find('p', class_='fc_aux')
            if desc: print("Desc:", desc.text.strip())
            
            link = article.find('a', class_='js-o-link')
            if link: 
                print("Link:", link.get('href'))
                full_url = "https://cl.computrabajo.com" + link.get('href')
                print("Full URL:", full_url)
                
                # Fetch full job
                job_req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
                job_html = urllib.request.urlopen(job_req).read().decode('utf-8')
                job_soup = BeautifulSoup(job_html, 'html.parser')
                details = job_soup.find('div', class_='box_detail')
                if details:
                    print("\n--- FULL DESCRIPTION ---")
                    # print some plain text
                    print(details.get_text(separator='\n', strip=True))
                
except Exception as e:
    print("Error:", e)
