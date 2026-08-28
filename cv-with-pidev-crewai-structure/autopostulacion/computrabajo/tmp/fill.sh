#!/bin/bash
# Fill one KQ textarea by index using the native setter (fires framework bindings).
# Usage: fill.sh <index> <text>
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
IDX="$1"; TXT="$2"
export IDX TXT
node -e '
const {execFileSync}=require("child_process");
const idx=process.env.IDX, txt=process.env.TXT;
const js=`(()=>{if(!location.href.includes("/candidate/kq"))return "ABORT "+location.href;
 const t=document.getElementById("KillerQuestions_${idx}__OpenQuestion");
 if(!t)return "NO_FIELD";
 const v=${JSON.stringify(txt)};
 if(v.length>(t.maxLength>0?t.maxLength:500))return "TOO_LONG "+v.length;
 Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype,"value").set.call(t,v);
 t.dispatchEvent(new Event("input",{bubbles:true}));
 t.dispatchEvent(new Event("change",{bubbles:true}));
 return "OK "+t.value.length;})()`;
const out=execFileSync("chrome-devtools-axi",["eval",js],{encoding:"utf8",stdio:["pipe","pipe","pipe"]});
const line=out.split("\n").find(l=>l.startsWith("result: "));
console.log(line||out.slice(0,200));
'
