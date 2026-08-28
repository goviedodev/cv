# Plan: Usar los modelos Anthropic de la suscripción vía OmniRoute en pi

**Fecha:** 2026-08-03 · **Fase:** Planificación (sin implementación aún)
**Tema:** "Tengo Anthropic por suscripción con omniroute, pero no sé si puedo usar los modelos de Anthropic"

---

## Contexto

- El usuario tiene una **suscripción Anthropic (Claude Max)** conectada a la pasarela OmniRoute vía **OAuth** (provider `claude`, cuenta `goviedo.sevenit@gmail.com`, `organizationType: claude_max`, tier `default_claude_max_5x`). Verificado en `~/.omniroute/storage.sqlite` → tabla `provider_connections` (estado `active`).
- La pasarela **OmniRoute v16.2.12** corre en `http://localhost:20128` (proceso `omniroute serve`).
- `/v1/models` de la pasarela **expone modelos Anthropic** con referencias directas: `claude/claude-opus-5`, `claude/claude-sonnet-5`, `claude/claude-fable-5`, `claude/claude-haiku-4-5-20251001`, variantes de esfuerzo de razonamiento (`-low/-medium/-high/-xhigh`), variantes `no-think/*`, y aliases `cc/*` y `opencode/*`/`oc/*`.
- **Verificado en vivo durante la planificación** (peticiones de prueba con `max_tokens` mínimo, sin modificar nada):
  - `POST /v1/messages` (formato Anthropic) con `claude/claude-opus-5` → respuesta real con bloque `thinking` + `signature`. ✅
  - `POST /v1/chat/completions` (formato OpenAI) con `claude/claude-opus-5` → contenido real, `usage` real y `x-omniroute-response-cost=0.00056 USD` → **la suscripción se está consumiendo a través de la pasarela**. ✅
  - **Tool-calling** en formato OpenAI con `claude/claude-opus-5` → devuelve `tool_calls` correcto (función + argumentos). ✅ (pi necesita tool-calling sí o sí)
  - El combo `auto/claude-opus` ruteó un prompt simple a `gemini-3.1-flash-lite` (el auto-routing elige modelos gratuitos/baratos para tareas simples). ⚠️ → para **garantizar** Claude hay que usar referencias explícitas `claude/*`, no combos `auto/*`.
- Claude Code ya usa la pasarela: `~/.claude/settings.json.bak-*` define `ANTHROPIC_BASE_URL=http://localhost:20128` + token de gateway.
- **El bloqueo actual en pi:** `~/.pi/agent/models.json` solo lista `auto`, `auto/coding` y `free-goviedo` bajo el provider `omniroute` (`api: openai-completions`, `baseUrl: http://localhost:20128/v1`). Los modelos `claude/*` **no están listados**, y pi solo permite seleccionar modelos listados → hoy no se pueden elegir desde pi aunque la pasarela sí los sirva.
- Nota: existe el plan `plan-como.md` para la vía **directa** (provider nativo `anthropic` de pi con OAuth propio en `~/.pi/agent/auth.json`). Este plan cubre la vía **omniroute** (la suscripción dentro de la pasarela). Ambas coexisten; son OAuth independientes.

## Objetivos

1. Habilitar la selección y uso de los modelos Anthropic de la suscripción desde pi, a través de la pasarela omniroute.
2. Elegir la ruta de integración con mejor fidelidad para pi: formato OpenAI (mínimo, ya verificado con tool-calling) vs. provider `anthropic-messages` (fidelidad nativa: thinking/signatures/cache).
3. Garantizar Claude de forma determinista (referencias explícitas `claude/*`), evitando la ambigüedad de los combos `auto/*`.
4. No romper lo existente: combos `free-goviedo`, `auto`, `auto/coding` y el resto de proveedores de la pasarela siguen operativos.
5. Validación end-to-end sin exponer secretos (tokens nunca se imprimen).

## Alcance

- **Solo configuración global de pi:** `~/.pi/agent/models.json` (agregar modelos Claude) y, opcionalmente, `~/.pi/agent/settings.json` (default de modelo).
- **No** se tocan archivos del proyecto CV (`cv.md`, `AGENTS.md`, etc.).
- **No** se toca la configuración de omniroute (storage.sqlite, combos, cuentas OAuth) — solo lectura.
- `~/.pi/agent/auth.json` y los tokens de omniroute son solo lectura.

## Archivos que se tocarán

| Archivo | Acción |
|---|---|
| `~/.pi/agent/models.json` | Backup previo + agregar modelos `claude/*` al provider `omniroute` (y/o nuevo provider `omniroute-claude` con `api: anthropic-messages`) |
| `~/.pi/agent/settings.json` | Opcional: `defaultModel` → modelo Claude elegido (manteniendo provider `omniroute`) |
| `~/.omniroute/storage.sqlite` | Solo lectura (diagnóstico) |
| `~/.pi/agent/auth.json` | Solo lectura |

## Pasos numerados

1. **Backup de config:** `cp ~/.pi/agent/models.json ~/.pi/agent/models.json.bak-omniroute-claude-$(date +%Y%m%d-%H%M%S)` (patrón ya usado en la máquina).
2. **Sanidad del gateway (ya verificado en planificación, re-ejecutar solo si algo falla):**
   - `curl /v1/models` lista `claude/claude-opus-5`, `claude/claude-sonnet-5`, `claude/claude-haiku-4-5-20251001`.
   - Test formato OpenAI + Anthropic con `max_tokens` mínimo (como en planificación).
   - Si 401/errores: el token OAuth de la cuenta `claude` expira **2026-08-03T23:44 UTC**; omniroute lo refresca con el refresh_token. Si el refresh falló → re-autenticar la cuenta en omniroute (CLI/dashboard) antes de seguir.
3. **Editar `~/.pi/agent/models.json` — ruta A (mínima, prioritaria):** dentro del provider `omniroute` existente (`api: openai-completions`), agregar:
   - `claude/claude-opus-5` — razonamiento profundo (`reasoning: true`; opcional: `-high`/`-xhigh` como modelos separados).
   - `claude/claude-sonnet-5` — default balanceado (`reasoning: true`).
   - `claude/claude-haiku-4-5-20251001` — rápido/ligero.
   - Mantener `auto`, `auto/coding` y `free-goviedo` intactos.
   - Campos por modelo: `contextWindow: 200000`, `maxTokens` prudente (p. ej. 32000), `reasoning: true`, `input: ["text","image"]` y `cost` a 0 (la pasarela reporta costo real en `x-omniroute-response-cost`; las métricas de pi no deben duplicar).
   - Validar JSON con `python3 -m json.tool`.
4. **Verificar visibilidad en pi:** `pi --list-models omniroute` debe incluir los 3 modelos nuevos.
5. **Prueba CLI one-shot (tool-calling implícito):** `pi --provider omniroute --model claude/claude-sonnet-5 "responde solo OK"` y una petición que fuerce una tool (p. ej. "¿qué archivos hay en ~?"). Confirmar que responde sin errores y completa el ciclo tool→resultado.
6. **Confirmar ruteo a Claude:** con curl al mismo modelo verificar los headers `x-omniroute-decision` / `x-omniroute-model` → `provider=claude`, `model=claude-*` (garantiza que NO cae en un modelo free).
7. **Ruta B (opcional, fidelidad nativa):** agregar un provider `omniroute-claude` en models.json con:
   - `baseUrl: "http://localhost:20128"` (pi añade `/v1/messages`; validar en la prueba que la URL final sea `http://localhost:20128/v1/messages`, que ya responde correctamente).
   - `api: "anthropic-messages"`, `apiKey`: mismo token de gateway.
   - Mismos modelos `claude/*` con `compat.forceAdaptiveThinking: true` si el modelo requiere thinking adaptativo (claude-opus-5 lo mostró en el test de planificación).
   - Elegir A o B (o ambas) según resultados: A es el mínimo verificado; B conserva thinking/signatures nativos.
8. **Prueba interactiva (TUI):** `/provider omniroute` → `/model` → seleccionar `claude/claude-opus-5`; verificar footer con el modelo activo y responder un prompt real.
9. **Default (opcional, solo si el usuario lo pide):** en `~/.pi/agent/settings.json`, `defaultModel` → `claude/claude-sonnet-5` manteniendo `defaultProvider: "omniroute"`. ⚠️ Hoy `settings.json` tiene `defaultProvider: "anthropic"` (vía nativa de plan-como) con `defaultModel: "claude-3-haiku-20240307"` (id obsoleto) — documentar el estado actual antes de tocar y decidir con el usuario si se corrige aquí o en plan-como.
10. **Regresión:** `pi --provider omniroute --model free-goviedo "di OK"` y `auto` siguen funcionando; `/v1/models` sigue completo.
11. **Verificación de consumo:** en los call_logs/dashboard de omniroute, las llamadas `claude/*` deben registrar costo > 0 (la suscripción se está usando).

## Riesgos y tradeoffs

- **Formato OpenAI pierde thinking/signature nativos** (el test mostró solo contenido, sin bloque thinking). Para razonamiento profundo, usar variantes `-high`/`-xhigh` o la ruta B (`anthropic-messages`).
- **`auto/*` no garantiza Claude** (verificado: `auto/claude-opus` → `gemini-3.1-flash-lite`). Solo las referencias explícitas `claude/*` garantizan Claude.
- **Rate limits:** tier 5x compartido con Claude Code; ráfagas largas (p. ej. batch de scraping del proyecto CV) pueden tocar límites de la suscripción.
- **Costo:** el uso desde harness de terceros vía gateway se factura como uso adicional de la suscripción (mismo criterio que en plan-como). Vigilar call_logs.
- **Expiración OAuth (hoy 23:44 UTC):** omniroute refresca solo con refresh_token; si falla → 401 → re-login de la cuenta `claude` en omniroute.
- **models.json es global:** afecta todas las sesiones de pi en la máquina; JSON mal formado rompe el arranque de pi → backup + validación obligatorios.
- **Ruta B:** puede requerir flags `compat` (forceAdaptiveThinking, eager tool streaming) y el comportamiento de `/v1/messages` de la pasarela puede diferir del Anthropic real → validar antes de adoptarla como default.
- **No tocar** la config de omniroute ni `auth.json` (secretos, permisos 0600). Nunca imprimir tokens.

## Checklist de aceptación (ejecutable)

1. `python3 -m json.tool ~/.pi/agent/models.json` → JSON válido, y existe backup `.bak-omniroute-claude-*`.
2. `pi --list-models omniroute` incluye `claude/claude-opus-5`, `claude/claude-sonnet-5`, `claude/claude-haiku-4-5-20251001`.
3. `pi --provider omniroute --model claude/claude-sonnet-5 "di OK"` responde sin errores de auth.
4. Un prompt con tool-calling en pi completa el ciclo tool→resultado sin errores.
5. Header de respuesta (curl) muestra `x-omniroute-model: claude-*` / `provider=claude` para los modelos `claude/*`.
6. `pi --provider omniroute --model free-goviedo "di OK"` sigue funcionando (sin regresión).
7. Los call_logs/dashboard de omniroute registran las llamadas `claude/*` con costo > 0.
8. Ningún token aparece en logs, output ni archivos generados durante el proceso; `auth.json` intacto.

---

## Progreso de implementación (2026-08-03)

**Ruta A (provider `omniroute`, formato OpenAI) — IMPLEMENTADA Y VERIFICADA ✅**

| # | Checklist | Estado | Evidencia |
|---|---|---|---|
| 1 | JSON válido + backup | ✅ | `models.json.bak-omniroute-claude-20260803-121833`; `python3 -m json.tool` OK |
| 2 | `pi --list-models omniroute` incluye 3 modelos Claude | ✅ | opus-5, sonnet-5, haiku-4-5 (200K / 32K / thinking / images) |
| 3 | `pi --provider omniroute --model claude/claude-sonnet-5 "di OK"` | ✅ | Responde "OK" |
| 4 | Tool-calling completo | ✅ | `ls /tmp` vía herramienta bash → output real |
| 5 | Ruteo a Claude confirmado | ✅ | `x-omniroute-model: claude-sonnet-5`, provider `cc`/`claude`, cost 0.000336 USD |
| 6 | Sin regresión (free-goviedo/auto) | ✅ | `combo/free-goviedo` → 200 (nvidia/glm-5.2); `pi --model auto` → OK |
| 7 | Consumo registrado en call_logs | ✅ | Llamadas `claude/*` provider `claude`, status 200, tokens reales (hasta 24.5K in en tool-calling) |
| 8 | Sin secretos expuestos | ✅ | auth.json intacto; solo se listaron claves, nunca valores |

**Ruta B (provider `omniroute-claude`, formato Anthropic nativo) — IMPLEMENTADA Y VERIFICADA ✅**

- `pi --list-models omniroute-claude` → opus-5 y sonnet-5 (200K / 32K / thinking / images).
- `pi --provider omniroute-claude --model claude/claude-opus-5 "Responde solamente: OK"` → responde.
- Tool-calling nativo: `echo HOLA-NATIVO` vía bash → output correcto.
- Flags usados: `compat.forceAdaptiveThinking: true` (opus-5 requiere thinking adaptativo).

**Hallazgo durante implementación:** la pasarela devuelve `upstream_empty_response` (502) con `claude/*` en formato OpenAI cuando `max_tokens` es muy bajo (8). Con 16+ funciona. Los `maxTokens: 32000` configurados en pi evitan el problema.

**Pendiente (decisión del usuario):**
- **Paso 9 (default global):** NO se cambió `~/.pi/agent/settings.json`. Hoy tiene `defaultProvider: "anthropic"` (vía nativa de plan-como) con `defaultModel: "claude-3-haiku-20240307"` (id obsoleto). Decidir si se corrige aquí o en plan-como.
- **Paso 8 (verificación TUI):** las pruebas CLI cubren la funcionalidad; para ver los modelos en la TUI reiniciar pi (o sesión nueva) → `/provider omniroute` → `/model` → elegir `claude/claude-opus-5`.
