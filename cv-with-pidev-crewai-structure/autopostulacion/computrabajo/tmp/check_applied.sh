#!/bin/bash
# Reliable applied-check: on the rendered detail page, "Postularme" carries class
# "hide" and a visible "Postulado" anchor is present when already applied.
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
while IFS='|' read -r n t c s U; do
  chrome-devtools-axi open "$U" >/dev/null 2>&1
  sleep 4
  R=$(chrome-devtools-axi eval '(()=>{if(!location.href.includes("/ofertas-de-trabajo/"))return "WRONG_URL";
   const m=document.querySelector("main")||document.body;
   const as=Array.from(m.querySelectorAll("a,button,input[type=submit]"));
   const postularme=as.filter(e=>/^\s*Postularme\s*$/i.test((e.innerText||e.value||"").trim()));
   const postulado=as.filter(e=>/^\s*Postulado\s*$/i.test((e.innerText||e.value||"").trim()));
   const pVis=postularme.some(e=>e.offsetParent!==null);
   const dVis=postulado.some(e=>e.offsetParent!==null);
   if(pVis&&!dVis)return "OPEN";
   if(!pVis&&dVis)return "APPLIED";
   return "AMBIG p="+pVis+" d="+dVis;})()' 2>&1 | grep '^result: ' | head -1 | sed 's/^result: //' | tr -d '\\"')
  echo "$R | $n | $t | $c"
done < "$1"
