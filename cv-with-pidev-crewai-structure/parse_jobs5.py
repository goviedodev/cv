import urllib.request
import re
import json

url = "https://cl.computrabajo.com/trabajo-de-analista-en-rmetropolitana-en-santiago-las-condes?utm_source=auto_cand_alertacargosdiaria&utm_campaign=auto_cand_alertacargosdiaria_gmail&utm_medium=email&oi=6C7B2FE9F143873B61373E686DCF3405&prov=14&q=analista-programador&om=F509438085EBCBBEFFBD009C36CBAE72DF7CC3BA1826A603AF641451F48FD82F38F1FFB17434AC35C132D5A7E06450F46465E0F56A3B9F9FA282BB733B556831A26D0E21D8F775F77D1AF5614416819D&fgoa=True#3B55A8B13DB4E34A61373E686DCF3405"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    
    # search for the ID in the html
    matches = re.finditer(r'3B55A8B13DB4E34A61373E686DCF3405', html, re.IGNORECASE)
    for m in matches:
        start = max(0, m.start() - 100)
        end = min(len(html), m.end() + 100)
        print("MATCH context:", html[start:end])
        print("---")
except Exception as e:
    print("Error:", e)
