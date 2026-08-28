#!/bin/bash
# Scrape "Mis postulaciones" baseline across pages
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
OUT="$1"
: > "$OUT"
for p in $(seq 1 12); do
  chrome-devtools-axi open "https://candidato.cl.computrabajo.com/candidate/match?st=1&p=$p" >/dev/null 2>&1
  sleep 3
  chrome-devtools-axi eval '(()=>{if(!location.href.includes("candidate/match"))return "WRONG_URL"; const L=document.body.innerText.split("\n").map(s=>s.trim()).filter(s=>s.length); const out=[]; L.forEach((l,i)=>{if(l==="Postulado"&&i>=3&&L[i+1]&&/^(Hace|Ayer|Hoy)/.test(L[i+1])){out.push(L[i-3]+" @@ "+L[i-2]);}}); return JSON.stringify(out);})()' 2>&1 \
    | grep '^result: ' | sed 's/^result: //' \
    | node -e 'let d="";process.stdin.on("data",c=>d+=c);process.stdin.on("end",()=>{try{let v=JSON.parse(d.trim());while(typeof v==="string")v=JSON.parse(v);v.forEach(x=>console.log(x));}catch(e){console.error("parse fail "+e.message)}})' >> "$OUT"
done
grep -c '@@' "$OUT"
