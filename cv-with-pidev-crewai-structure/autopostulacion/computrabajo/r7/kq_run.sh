#!/bin/bash
# Resuelve las ofertas con killer questions: abre, pulsa Postularme, rellena el
# formulario con el banco de respuestas veraz (kq_fill.js), valida y envia.
# Aborta la oferta si el cuestionario revela un stack excluyente.
set -u
cd "$(dirname "$0")"
export CHROME_DEVTOOLS_AXI_AUTO_CONNECT=1
CDA() { timeout 60 chrome-devtools-axi "$@" </dev/null 2>/dev/null; }
FILL=$(cat kq_fill.js)

: > kq_run.log
: > kq_applied.txt
: > kq_skipped.txt
log() { echo "[$(date +%H:%M:%S)] $*" >> kq_run.log; }

mapfile -t LINES < kq_pending.txt
for L in "${LINES[@]}"; do
  IDX="${L%%|*}"; U="${L#*|}"
  [ -z "$U" ] && continue

  HEX="${U##*-}"

  # GUARDA con reintentos: la pestaña debe estar realmente en la oferta esperada
  OKPAGE=0
  for try in 1 2 3; do
    CDA open "$U" >/dev/null; sleep 5
    CUR=$(CDA eval '() => location.href')
    if echo "$CUR" | grep -qF "$HEX"; then OKPAGE=1; break; fi
    sleep 3
  done
  if [ "$OKPAGE" = "0" ]; then
    log "SKIP $IDX pagina-equivocada-tras-3-intentos $U"
    echo "$IDX|PAGINA_ERRONEA|$U" >> kq_skipped.txt
    continue
  fi

  CDA eval '() => { const b=Array.from(document.querySelectorAll("a,button")).filter(e=>/^\s*Postularme\s*$/i.test(e.textContent.trim())&&e.offsetParent!==null); if(!b.length) return "NO_BTN"; b[0].click(); return "ok"; }' >/dev/null
  sleep 6

  # GUARDA: el formulario debe corresponder a la misma oferta
  CUR2=$(CDA eval '() => location.href')
  if ! echo "$CUR2" | grep -qF "$HEX"; then
    log "SKIP $IDX kq-de-otra-oferta $CUR2"
    echo "$IDX|KQ_ERRONEA|$U" >> kq_skipped.txt
    continue
  fi

  R=$(CDA eval "$FILL")
  case "$R" in
    *READY*)
      CDA eval '() => { const b=Array.from(document.querySelectorAll("button,a,input[type=submit],span")).find(e=>/^\s*Enviar mi CV\s*$/i.test((e.textContent||e.value||"").trim())&&e.offsetParent!==null); if(!b) return "NO_SUBMIT"; b.click(); return "sent"; }' >/dev/null
      sleep 6
      D=$(CDA eval '() => location.href')
      if echo "$D" | grep -q 'postapply'; then
        CDA eval '() => { const a=Array.from(document.querySelectorAll("button,a,input[type=submit]")).find(e=>/^\s*Actualizar\s*$/i.test((e.textContent||e.value||"").trim())&&e.offsetParent!==null); if(a){a.click();return "carta";} return "sin-carta"; }' >/dev/null
        sleep 3
        log "OK   $IDX enviada+carta $U"
        echo "$IDX|$U" >> kq_applied.txt
      elif echo "$D" | grep -q 'candidate/kq'; then
        log "FAIL $IDX sigue-en-kq $U"
        echo "$IDX|SIGUE_KQ|$U" >> kq_skipped.txt
      else
        log "OK   $IDX enviada ($D) $U"
        echo "$IDX|$U" >> kq_applied.txt
      fi
      ;;
    *ABORT:stack-excluyente*)
      log "SKIP $IDX stack-excluyente-en-preguntas $U"
      echo "$IDX|STACK|$U" >> kq_skipped.txt ;;
    *)
      log "SKIP $IDX $R $U"
      echo "$IDX|${R:0:40}|$U" >> kq_skipped.txt ;;
  esac
done
log "FIN. enviadas=$(wc -l < kq_applied.txt) descartadas=$(wc -l < kq_skipped.txt)"
echo DONE
