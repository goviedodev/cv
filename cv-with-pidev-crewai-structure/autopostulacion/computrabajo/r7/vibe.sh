#!/bin/bash
# Loop unificado: leer aviso -> filtrar -> Postularme -> killer questions -> carta.
# Solo cuenta como postulacion nueva el destino /candidate/postapply.
set -u
cd "$(dirname "$0")"
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
CDA() { timeout 60 chrome-devtools-axi "$@" </dev/null 2>/dev/null; }
FILL=$(cat kq_fill.js)
LIST=${1:-vibe_urls.txt}

: > vibe.log
: > vibe_applied.txt
: > vibe_skipped.txt
log() { echo "[$(date +%H:%M:%S)] $*" >> vibe.log; }

mapfile -t URLS < "$LIST"
for U in "${URLS[@]}"; do
  [ -z "$U" ] && continue
  HEX="${U##*-}"
  SHORT="${U##*/oferta-de-trabajo-de-}"; SHORT="${SHORT:0:55}"

  OK=0
  for t in 1 2 3; do
    CDA open "$U" >/dev/null; sleep 5
    CUR=$(CDA eval '() => location.href')
    echo "$CUR" | grep -qF "$HEX" && { OK=1; break; }
    sleep 3
  done
  [ "$OK" = "0" ] && { log "SKIP pagina-equivocada $SHORT"; echo "PAGINA|$U" >> vibe_skipped.txt; continue; }

  BODY=$(CDA eval '() => { const t=document.body.innerText.replace(/\s+/g," ").trim(); const k=t.indexOf("Descripción de la oferta"); return t.slice(k>0?k:0,(k>0?k:0)+1600); }' --full)
  LOW=$(echo "$BODY" | tr 'A-ZÁÉÍÓÚÑ' 'a-záéíóúñ')

  # modalidad: incluye "Presencial en <ciudad>" (el tag real del portal) y el slug
  if echo "$LOW" | grep -qE '100% presencial|jornada presencial|totalmente presencial|presencialidad total|presencial en [a-záéíóúñ]'; then
    log "SKIP presencial $SHORT"; echo "PRESENCIAL|$U" >> vibe_skipped.txt; continue
  fi
  if echo "$U" | grep -qiE 'presencial'; then
    log "SKIP presencial-en-slug $SHORT"; echo "PRESENCIAL_SLUG|$U" >> vibe_skipped.txt; continue
  fi
  # stack excluyente: ".net" pegado a la palabra anterior ("en.NET") NO lo capturaba \.net core
  if echo "$LOW" | grep -qE '\.net|dotnet|\bc#|vb\.net|cobol|salesforce|murex|dynamics 365|servicenow|\babap\b|genexus|flexcube|uipath|arcgis|powerbuilder|delphi|siebel|laravel|\bphp\b|symfony|codeigniter|woocommerce|odoo|prestashop|drupal'; then
    log "SKIP stack $SHORT"; echo "STACK|$U" >> vibe_skipped.txt; continue
  fi
  # el cargo debe ser realmente de software: descarta "Programador" de produccion/mineria/mantencion
  if echo "$LOW" | grep -qE 'miner[ií]a|proyectista|aseo y mantenimiento|continuidad operacional|planificaci[oó]n de (obra|producci[oó]n)|maestranza|maquinaria'; then
    log "SKIP no-es-software $SHORT"; echo "NO_SOFTWARE|$U" >> vibe_skipped.txt; continue
  fi
  SAL=$(echo "$BODY" | grep -oE '\$ ?[0-9]{1,3}(\.[0-9]{3})+' | head -1 | tr -d '$ .')
  if [ -n "$SAL" ] && [ "$SAL" -lt 1800000 ] 2>/dev/null; then
    log "SKIP renta($SAL) $SHORT"; echo "RENTA:$SAL|$U" >> vibe_skipped.txt; continue
  fi

  CDA eval '() => { const b=Array.from(document.querySelectorAll("a,button")).filter(e=>/^\s*Postularme\s*$/i.test(e.textContent.trim())&&e.offsetParent!==null); if(!b.length) return "NO_BTN"; b[0].click(); return "ok"; }' >/dev/null
  sleep 7
  D=$(CDA eval '() => location.href')

  if echo "$D" | grep -q 'candidate/kq'; then
    echo "$D" | grep -qF "$HEX" || { log "SKIP kq-de-otra-oferta $SHORT"; echo "KQ_ERRONEA|$U" >> vibe_skipped.txt; continue; }
    R=$(CDA eval "$FILL")
    case "$R" in
      *READY*)
        CDA eval '() => { const b=Array.from(document.querySelectorAll("button,a,input[type=submit],span")).find(e=>/^\s*Enviar mi CV\s*$/i.test((e.textContent||e.value||"").trim())&&e.offsetParent!==null); if(b){b.click();return "sent";} return "NO_SUBMIT"; }' >/dev/null
        sleep 7
        D=$(CDA eval '() => location.href') ;;
      *) log "SKIP $R $SHORT"; echo "${R:0:30}|$U" >> vibe_skipped.txt; continue ;;
    esac
  fi

  if echo "$D" | grep -q 'postapply'; then
    CDA eval '() => { const a=Array.from(document.querySelectorAll("button,a,input[type=submit]")).find(e=>/^\s*Actualizar\s*$/i.test((e.textContent||e.value||"").trim())&&e.offsetParent!==null); if(a){a.click();return "carta";} return "sin-carta"; }' >/dev/null
    sleep 3
    log "OK   postulada+carta $SHORT"
    echo "$U" >> vibe_applied.txt
  elif echo "$D" | grep -q 'match/'; then
    log "SKIP ya-postulada(/match/) $SHORT"; echo "YA_POSTULADA|$U" >> vibe_skipped.txt
  else
    log "SKIP destino-desconocido $D $SHORT"; echo "DESCONOCIDO|$U" >> vibe_skipped.txt
  fi
done
log "FIN. postuladas=$(wc -l < vibe_applied.txt) descartadas=$(wc -l < vibe_skipped.txt)"
echo DONE
