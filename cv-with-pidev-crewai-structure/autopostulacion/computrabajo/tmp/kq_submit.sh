#!/bin/bash
# Validate textarea lengths, then submit "Enviar mi CV". Aborts on overflow.
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
V=$(chrome-devtools-axi eval '(()=>{if(!location.href.includes("/candidate/kq"))return "NOT_KQ "+location.href;
 const bad=Array.from(document.querySelectorAll("textarea")).filter(t=>t.value.length>(t.maxLength>0?t.maxLength:500)).map(t=>t.id+":"+t.value.length);
 const empty=Array.from(document.querySelectorAll("textarea")).filter(t=>!t.value.trim()).map(t=>t.id);
 if(bad.length)return "OVERFLOW "+bad.join(",");
 if(empty.length)return "EMPTY "+empty.join(",");
 return "LEN_OK";})()' 2>&1 | grep '^result: ' | head -1)
echo "$V"
case "$V" in *LEN_OK*) ;; *) echo "ABORT"; exit 1;; esac

chrome-devtools-axi eval '(()=>{if(!location.href.includes("/candidate/kq"))return "ABORT "+location.href;
 const b=Array.from(document.querySelectorAll("button,a,input[type=submit]"))
  .filter(e=>e.offsetParent!==null && /Enviar mi CV/i.test((e.innerText||e.value||"")));
 if(!b.length)return "NO_SUBMIT";
 b[0].click(); return "SUBMITTED";})()' 2>&1 | grep '^result: ' | head -1
sleep 6
chrome-devtools-axi eval '(()=>location.href)()' 2>&1 | grep '^result: ' | head -1
