const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  const url = "https://cl.computrabajo.com/trabajo-de-analista-en-rmetropolitana-en-santiago-las-condes?utm_source=auto_cand_alertacargosdiaria&utm_campaign=auto_cand_alertacargosdiaria_gmail&utm_medium=email&oi=6C7B2FE9F143873B61373E686DCF3405&prov=14&q=analista-programador&om=F509438085EBCBBEFFBD009C36CBAE72DF7CC3BA1826A603AF641451F48FD82F38F1FFB17434AC35C132D5A7E06450F46465E0F56A3B9F9FA282BB733B556831A26D0E21D8F775F77D1AF5614416819D&fgoa=True#3B55A8B13DB4E34A61373E686DCF3405";
  await page.goto(url, {waitUntil: 'networkidle2'});
  
  const fs = require('fs');
  const html = await page.content();
  fs.writeFileSync('computrabajo_page.html', html);
  
  const detail = await page.evaluate(() => {
     const d = document.querySelector('div.box_detail');
     return d ? d.innerText : '';
  });
  console.log("Detail extracted:", detail.substring(0, 500));
  fs.writeFileSync('computrabajo_detail.txt', detail);
  
  await browser.close();
})();
