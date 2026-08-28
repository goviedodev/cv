#!/bin/bash
# Read one offer detail page: prints cleaned main text
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
U="$1"
chrome-devtools-axi open "$U" >/dev/null 2>&1
sleep 3
chrome-devtools-axi eval '(()=>{if(!location.href.includes("/ofertas-de-trabajo/"))return "WRONG_URL "+location.href; const m=document.querySelector("main")||document.body; const c=m.cloneNode(true); c.querySelectorAll("script,style,noscript").forEach(e=>e.remove()); return c.innerText.replace(/[ \t]+/g," ").replace(/\n[\s\n]*/g,"\n").trim().slice(0,2600);})()' 2>&1 \
  | grep '^result: ' | head -1 | sed 's/^result: //' \
  | node -e 'let d="";process.stdin.on("data",c=>d+=c);process.stdin.on("end",()=>{let v=d.trim();for(let i=0;i<3;i++){try{v=JSON.parse(v)}catch(e){break}if(typeof v!=="string")break}console.log(v)})'
