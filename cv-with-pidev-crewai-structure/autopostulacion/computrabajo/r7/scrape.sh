#!/bin/bash
# Barre las paginas renderizadas de una busqueda de Computrabajo y vuelca
# href + titulo + tag de postulado + metadatos de cada tarjeta.
set -u
cd "$(dirname "$0")"
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
C() { timeout 50 chrome-devtools-axi "$@" </dev/null 2>/dev/null; }
BASE=${1:-https://cl.computrabajo.com/trabajo-de-java}
OUT=${2:-pages2.jsonl}
MAXP=${3:-30}
: > "$OUT"
for p in $(seq 1 "$MAXP"); do
  if [ "$p" = "1" ]; then U="$BASE"; else U="$BASE?p=$p"; fi
  C open "$U" >/dev/null
  sleep 4
  R=$(C eval '() => { const a=Array.from(document.querySelectorAll("article")); return JSON.stringify(a.map(x=>{const t=x.querySelector("span.tag.postulated"); const l=x.querySelector("h2 a"); const li=x.innerText.split("\n").map(s=>s.trim()).filter(Boolean); return {h:l?l.getAttribute("href"):null,t:l?l.textContent.trim():"?",ap:!!(t&&!t.className.includes("hide")),meta:li.slice(1,6).join(" | ")};})); }' --full)
  echo "PAGE $p $R" >> "$OUT"
  N=$(echo "$R" | grep -o "oferta-de-trabajo-de" | wc -l)
  echo "p$p:$N"
  [ "$N" = "0" ] && break
done
echo DONE
