#!/bin/bash
# Loop autónomo de postulación Computrabajo.
# - Abre cada oferta, lee el cuerpo, aplica filtros duros (modalidad / stack / renta).
# - Postula si pasa. Si aparecen killer questions, las deja anotadas y sigue (se resuelven aparte).
# - Registra todo en run.log / applied.txt / skipped.txt / kq_pending.txt
set -u
cd "$(dirname "$0")"
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
CDA() { timeout 45 chrome-devtools-axi "$@" 2>/dev/null; }

TARGET=${TARGET:-40}
START=${START:-2}
: > run.log
: > applied.txt
: > skipped.txt
: > kq_pending.txt

log() { echo "[$(date +%H:%M:%S)] $*" >> run.log; }

COUNT=0
i=0
while IFS= read -r U; do
  i=$((i+1))
  [ "$i" -lt "$START" ] && continue
  [ "$COUNT" -ge "$TARGET" ] && break

  CDA open "$U" >/dev/null
  sleep 3

  BODY=$(CDA eval '() => { const t=document.body.innerText.replace(/\s+/g," ").trim(); const k=t.indexOf("Descripción de la oferta"); const h1=(document.querySelector("h1")||{}).textContent||""; const tag=Array.from(document.querySelectorAll("span.tag.postulated")).filter(e=>!e.className.includes("hide")).length; return "TAG="+tag+"||"+h1.trim()+"||"+t.slice(k>0?k:0,(k>0?k:0)+1500); }' --full | sed 's/^result: //')

  if [ -z "$BODY" ]; then log "SKIP $i sin-cuerpo $U"; echo "$i|NOBODY|$U" >> skipped.txt; continue; fi

  # ---- ya postulada segun el tag renderizado ----
  if echo "$BODY" | grep -q 'TAG=[1-9]'; then
    log "SKIP $i ya-postulada(tag) $U"; echo "$i|TAG_POSTULADA|$U" >> skipped.txt; continue
  fi

  LOW=$(echo "$BODY" | tr 'A-ZÁÉÍÓÚÑ' 'a-záéíóúñ')

  # ---- filtro modalidad: 100% presencial ----
  if echo "$LOW" | grep -qE '100% presencial|jornada presencial|totalmente presencial|presencialidad total|100 % presencial'; then
    log "SKIP $i presencial $U"; echo "$i|PRESENCIAL|$U" >> skipped.txt; continue
  fi

  # ---- filtro stack excluyente ----
  if echo "$LOW" | grep -qE '\.net core|asp\.net|c# |c#,|lenguaje c#|cobol|salesforce|murex|dynamics 365|servicenow|prestashop|abap|genexus|flexcube|uipath'; then
    log "SKIP $i stack-excluyente $U"; echo "$i|STACK|$U" >> skipped.txt; continue
  fi

  # ---- filtro renta publicada bajo piso ----
  SAL=$(echo "$BODY" | grep -oE '\$ ?[0-9]{1,3}(\.[0-9]{3})+' | head -1 | tr -d '$ .')
  if [ -n "$SAL" ] && [ "$SAL" -lt 1800000 ] 2>/dev/null; then
    log "SKIP $i renta-baja($SAL) $U"; echo "$i|RENTA:$SAL|$U" >> skipped.txt; continue
  fi

  # ---- postular ----
  CLICK=$(CDA eval '() => { const b=Array.from(document.querySelectorAll("a,button")).filter(e=>/^\s*Postularme\s*$/i.test(e.textContent.trim())&&e.offsetParent!==null); if(!b.length) return "NO_BTN"; b[0].click(); return "OK"; }')
  if echo "$CLICK" | grep -q NO_BTN; then
    log "SKIP $i sin-boton $U"; echo "$i|NOBTN|$U" >> skipped.txt; continue
  fi
  sleep 6

  DEST=$(CDA eval '() => JSON.stringify({u:location.href, ta:document.querySelectorAll("textarea").length, rd:document.querySelectorAll("input[type=radio]").length})')

  case "$DEST" in
    *candidate/kq*)
      log "KQ  $i killer-questions $U"
      echo "$i|$U" >> kq_pending.txt
      ;;
    *candidate/postapply*)
      CDA eval '() => { const a=Array.from(document.querySelectorAll("button,a,input[type=submit]")).find(e=>/^\s*Actualizar\s*$/i.test((e.textContent||e.value||"").trim())&&e.offsetParent!==null); if(a){a.click();return "CARTA_OK";} return "SIN_ACTUALIZAR"; }' >/dev/null
      sleep 3
      COUNT=$((COUNT+1))
      log "OK  $i ($COUNT/$TARGET) postapply+carta $U"
      echo "$i|$U" >> applied.txt
      ;;
    *match/?oi=*|*match/*oi=*)
      COUNT=$((COUNT+1))
      log "OK  $i ($COUNT/$TARGET) directa $U"
      echo "$i|$U" >> applied.txt
      ;;
    *)
      log "??? $i destino-desconocido $DEST $U"
      echo "$i|UNKNOWN|$U" >> skipped.txt
      ;;
  esac
done < queue_urls.txt

log "FIN. Postuladas=$COUNT  KQ pendientes=$(wc -l < kq_pending.txt)"
echo "DONE count=$COUNT"
