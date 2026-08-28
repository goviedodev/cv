#!/bin/bash
# Dump the killer-questions form: question text, field ids, radio labels.
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
chrome-devtools-axi eval '(()=>{if(!location.href.includes("/candidate/kq"))return "NOT_KQ "+location.href;
 const out=[];
 document.querySelectorAll("textarea").forEach(t=>out.push("TEXTAREA "+t.id+" max="+t.maxLength+" Q="+((t.closest("li,div,fieldset")||{}).innerText||"").replace(/\s+/g," ").slice(0,220)));
 const groups={};
 document.querySelectorAll("input[type=radio]").forEach(r=>{(groups[r.name]=groups[r.name]||[]).push(r);});
 Object.keys(groups).forEach(name=>{
   const rs=groups[name];
   const q=((rs[0].closest("li,fieldset,div.box_i")||{}).innerText||"").replace(/\s+/g," ").slice(0,220);
   const opts=rs.map(r=>{const l=document.querySelector("label[for=\""+r.id+"\"]"); return r.id+"="+((l&&l.innerText)||r.value||"?").trim();});
   out.push("RADIO "+name+" Q="+q+" || OPTS: "+opts.join(" ; "));
 });
 document.querySelectorAll("select").forEach(s=>out.push("SELECT "+s.id+" opts="+Array.from(s.options).map(o=>o.value+":"+o.text).join(" ; ").slice(0,300)));
 return out.join("\n---\n")||"NO_FIELDS";})()' 2>&1 \
  | grep '^result: ' | head -1 | sed 's/^result: //' \
  | node -e 'let d="";process.stdin.on("data",c=>d+=c);process.stdin.on("end",()=>{let v=d.trim();for(let i=0;i<3;i++){try{v=JSON.parse(v)}catch(e){break}if(typeof v!=="string")break}console.log(v)})'
