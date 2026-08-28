#!/bin/bash
# Read each candidate offer detail into a single dossier file
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
IN="$1"; OUT="$2"
: > "$OUT"
n=0
while read -r U; do
  n=$((n+1))
  chrome-devtools-axi open "$U" >/dev/null 2>&1
  sleep 3
  echo "===== #$n $U" >> "$OUT"
  chrome-devtools-axi eval '(()=>{if(!location.href.includes("/ofertas-de-trabajo/"))return "WRONG_URL "+location.href; const m=document.querySelector("main")||document.body; const c=m.cloneNode(true); c.querySelectorAll("script,style,noscript").forEach(e=>e.remove()); const applied=!!Array.from(m.querySelectorAll("*")).find(e=>e.children.length===0&&/Ya aplicaste a esta oferta/.test(e.textContent)&&e.offsetParent!==null); return "APPLIEDFLAG="+applied+"\n"+c.innerText.replace(/[ \t]+/g," ").replace(/\n[\s\n]*/g,"\n").trim().slice(0,2400);})()' 2>&1 \
    | grep '^result: ' | head -1 | sed 's/^result: //' \
    | node -e 'let d="";process.stdin.on("data",c=>d+=c);process.stdin.on("end",()=>{let v=d.trim();for(let i=0;i<3;i++){try{v=JSON.parse(v)}catch(e){break}if(typeof v!=="string")break}console.log(v)})' >> "$OUT"
done < "$IN"
echo "done $n"
