const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();
  
  const url = "https://cl.computrabajo.com/trabajo-de-analista-en-rmetropolitana-en-santiago-las-condes?utm_source=auto_cand_alertacargosdiaria&utm_campaign=auto_cand_alertacargosdiaria_gmail&utm_medium=email&oi=6C7B2FE9F143873B61373E686DCF3405&prov=14&q=analista-programador&om=F509438085EBCBBEFFBD009C36CBAE72DF7CC3BA1826A603AF641451F48FD82F38F1FFB17434AC35C132D5A7E06450F46465E0F56A3B9F9FA282BB733B556831A26D0E21D8F775F77D1AF5614416819D&fgoa=True#3B55A8B13DB4E34A61373E686DCF3405";
  
  await page.goto(url, { waitUntil: 'networkidle' });
  
  // Try to find the specific job detail panel or text
  const html = await page.content();
  const fs = require('fs');
  fs.writeFileSync('computrabajo_page.html', html);
  
  const detailText = await page.locator('div.box_detail').textContent().catch(() => 'No detail found');
  console.log("Detail Length:", detailText.length);
  if(detailText.length > 20) {
     console.log("Detail Preview:", detailText.substring(0, 500));
     fs.writeFileSync('computrabajo_detail.txt', detailText);
  }
  
  await browser.close();
})();
