#!/bin/bash
# On /candidate/postapply: press "Actualizar" to attach the pre-loaded cover letter.
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
chrome-devtools-axi eval '(()=>{if(!location.href.includes("/candidate/postapply"))return "NOT_POSTAPPLY "+location.href;
 let ta=document.getElementById("CoverLetterPostApply_CoverLetter_Description");
 if(!ta){const ed=Array.from(document.querySelectorAll("button,a")).find(e=>/^\s*Editar\s*$/i.test(e.textContent.trim())&&e.offsetParent!==null); if(ed)ed.click();
   ta=document.getElementById("CoverLetterPostApply_CoverLetter_Description");}
 if(!ta)return "NO_TEXTAREA";
 if(!ta.value.trim())return "EMPTY_LETTER";
 const up=Array.from(document.querySelectorAll("button,a,input[type=submit]")).find(e=>/^\s*Actualizar\s*$/i.test((e.innerText||e.value||"").trim())&&e.offsetParent!==null);
 if(!up)return "NO_ACTUALIZAR";
 up.click(); return "COVER_CLICKED";})()' 2>&1 | grep '^result: ' | head -1
sleep 4
chrome-devtools-axi eval '(()=>{const t=document.body.innerText; const m=t.match(/Hemos adjuntado[^\n]{0,120}/); return m?m[0]:"NO_CONFIRM";})()' 2>&1 | grep '^result: ' | head -1
