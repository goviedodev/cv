#!/bin/bash
# Scrape public search results: title | company | location | tags | applied | url
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
BASEURL="$1"
OUT="$2"
MAXP="${3:-6}"
for p in $(seq 1 "$MAXP"); do
  if [ "$p" = "1" ]; then U="$BASEURL"; else U="$BASEURL?p=$p"; fi
  chrome-devtools-axi open "$U" >/dev/null 2>&1
  sleep 3
  chrome-devtools-axi eval '(()=>{const arts=Array.from(document.querySelectorAll("article")); const out=arts.map(a=>{const link=a.querySelector("h2 a")||a.querySelector("a[href*=\"/ofertas-de-trabajo/\"]"); const t=(a.innerText||"").replace(/\s+/g," ").trim(); return {u:link?link.href:"", t:t};}).filter(x=>x.u); return JSON.stringify(out);})()' 2>&1 \
    | grep '^result: ' | sed 's/^result: //' \
    | node -e 'let d="";process.stdin.on("data",c=>d+=c);process.stdin.on("end",()=>{try{let v=JSON.parse(d.trim());while(typeof v==="string")v=JSON.parse(v);v.forEach(x=>console.log(x.u+" ||| "+x.t));}catch(e){console.error("parsefail")}})' >> "$OUT"
done
