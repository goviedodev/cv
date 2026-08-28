# Plan: Usar los modelos Anthropic de la suscripción en pi

**Fecha:** 2026-08-03 · **Fase:** Planificación (sin implementación aún)

## Contexto

- El usuario tiene auth **OAuth de suscripción Anthropic (Claude Pro/Max)** ya configurada en `~/.pi/agent/auth.json` (`"anthropic": { "type": "oauth", ... }`, con access + refresh token).
- pi 0.80.3 detecta esa auth y expone los modelos Anthropic **built-in** del provider `anthropic` — verificado con `pi --list-models anthropic`: 23 modelos (claude-sonnet-4-5, claude-opus-4-8, claude-haiku-4-5, claude-sonnet-5, claude-fable-5, etc.).
- **El problema:** `~/.pi/agent/settings.json` tiene `defaultProvider: "omniroute"` y `defaultModel: "auto"`, o sea que pi arranca siempre contra el proxy local `localhost:20128` y **nunca usa la suscripción** salvo que se seleccione el provider `anthropic` explícitamente.
- El access token OAuth expira **2026-08-03T23:52 UTC** (hoy). pi lo refresca automáticamente con el refresh token; si el refresh falla, la solución es re-ejecutar `/login`.

## Objetivos

1. Poder seleccionar y usar los modelos Claude de la suscripción (provider `anthropic`) de forma interactiva, por CLI y como default.
2. No romper el acceso actual a `omniroute` — debe seguir disponible como alternativa.
3. Verificar funcionamiento real (petición de prueba) sin exponer secretos.

## Alcance

- Solo toca config **global** de pi: `~/.pi/agent/settings.json` y, opcionalmente, `~/.pi/agent/models.json`.
- **No** toca archivos del proyecto CV (`cv.md`, `AGENTS.md`, etc.).
- `~/.pi/agent/auth.json` es solo lectura — los tokens no se imprimen ni modifican.

## Archivos que se tocarán

| Archivo | Acción |
|---|---|
| `~/.pi/agent/settings.json` | Editar `defaultProvider` → `"anthropic"` y `defaultModel` → modelo elegido |
| `~/.pi/agent/models.json` | Opcional: alias/overrides para modelos Anthropic (p. ej. `modelOverrides` con `thinkingLevelMap`/`name`) |
| `~/.pi/agent/auth.json` | Solo lectura (verificar estado del OAuth) |

## Pasos numerados

1. **Verificar la auth de suscripción** (solo lectura): confirmar en `~/.pi/agent/auth.json` la clave `anthropic` con `type: "oauth"`. Si falta o está corrupta → ejecutar `/login` en pi y seleccionar Anthropic.
2. **Verificar modelos disponibles:** `pi --list-models anthropic` (ya verificado en planificación: 23 modelos, incluye sonnet 4.5, opus 4.8, haiku 4.5).
3. **Prueba puntual por CLI:** `pi --provider anthropic --model claude-sonnet-4-5 "Responde OK"` (equivalente: `pi --model anthropic/claude-sonnet-4-5 ...`). Aquí se gatilla el auto-refresh del access token si expiró. Comprobar que responde sin errores 401.
4. **Prueba interactiva (TUI):** dentro de una sesión pi, `/provider anthropic` y luego `/model` → elegir modelo (p. ej. `claude-sonnet-4-5` o `claude-opus-4-8`). Verificar que el footer muestra el provider/modelo correcto.
5. **Cambiar el default global:** editar `~/.pi/agent/settings.json` → `"defaultProvider": "anthropic"`, `"defaultModel": "claude-sonnet-4-5"` (o el modelo preferido del usuario). Aplica a todas las sesiones nuevas; no requiere reiniciar pi.
6. **(Opcional) Overrides en models.json:** si se quiere un nombre amigable, `thinkingLevelMap` (off/minimal/low/medium/high/xhigh) o ajustes de contexto/maxTokens, agregar un bloque `providers.anthropic` con `modelOverrides` (no duplica la lista completa; los built-ins se mantienen).
7. **Verificación final:**
   - Nueva sesión `pi` → el footer muestra el modelo de suscripción.
   - Responder un prompt real de prueba.
   - `/model` muestra los modelos Anthropic disponibles.
   - Volver a omniroute con `--provider omniroute` / `/provider omniroute` para confirmar que sigue operativo.

## Riesgos y tradeoffs

- **Uso por token:** según la doc de providers, el uso de la suscripción desde harness de terceros se factura por token ("extra usage"), no descuenta del límite del plan. El costo real depende del volumen de uso.
- **Expiración del access token:** expira hoy 23:52 UTC; pi lo refresca solo vía refresh token. Si el refresh falla (token revocado en claude.ai), las peticiones dan 401 y hay que rehacer `/login`.
- **Rate limits de suscripción** pueden ser más restrictivos que una API key en ráfagas largas (p. ej. batch de scraping del proyecto CV).
- **Cambio de default global** afecta a todas las sesiones de pi en la máquina, no solo a este proyecto. Alternativa de menor impacto: no cambiar el default y usar `/provider` o `--provider` por sesión.
- **Regresión de omniroute:** si el proxy local no está corriendo al volver a él, las sesiones con ese default fallarían. El plan no borra la config de omniroute; solo cambia el default.
- **Secretos:** jamás imprimir ni loguear los tokens; `auth.json` ya tiene permisos `0600`.

## Checklist de aceptación (ejecutable)

1. `pi --list-models anthropic` muestra ≥ 5 modelos Claude sin error.
2. `pi --provider anthropic --model claude-sonnet-4-5 "di OK"` responde sin errores de auth (401/403).
3. En TUI: `/provider anthropic` + `/model claude-sonnet-4-5` funciona y el footer muestra el modelo activo.
4. `~/.pi/agent/settings.json` tiene `defaultProvider: "anthropic"` y `defaultModel` = modelo elegido.
5. Una sesión nueva de pi arranca con el modelo de suscripción por defecto (verificable en el footer).
6. `pi --provider omniroute --model auto "di OK"` sigue funcionando (omniroute no se rompió).
7. Ningún token aparece en logs, output o archivos generados durante el proceso.
