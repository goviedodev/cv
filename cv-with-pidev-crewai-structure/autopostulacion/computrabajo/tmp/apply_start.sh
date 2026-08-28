#!/bin/bash
# Open an offer, verify URL, click "Postularme", report resulting route + dump KQ form.
# Usage: apply_start.sh <offer_url>
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
U="$1"
chrome-devtools-axi open "$U" >/dev/null 2>&1
sleep 4

# Guard: abort unless we are on the expected offer detail page
GUARD=$(chrome-devtools-axi eval '(()=>location.href)()' 2>&1 | grep '^result: ' | head -1)
case "$GUARD" in
  *"/ofertas-de-trabajo/"*) ;;
  *) echo "ABORT wrong url: $GUARD"; exit 1;;
esac

# Click Postularme scoped to the offer detail container
chrome-devtools-axi eval '(()=>{if(!location.href.includes("/ofertas-de-trabajo/"))return "ABORT "+location.href;
 const m=document.querySelector("main")||document.body;
 const b=Array.from(m.querySelectorAll("button,a,input[type=submit]"))
   .filter(e=>e.offsetParent!==null && /^\s*Postularme\s*$/i.test((e.innerText||e.value||"").trim()));
 if(!b.length)return "NO_BUTTON";
 b[0].click(); return "CLICKED";})()' 2>&1 | grep '^result: ' | head -1
sleep 6
chrome-devtools-axi eval '(()=>location.href)()' 2>&1 | grep '^result: ' | head -1
