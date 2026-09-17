# Guía de Repaso Técnico — Entrevista FullStack (Java/Spring + Angular + GCP)

> **Origen:** temario de `integracion.txt`.
> **Objetivo:** repasar a fondo cada tema, con definición, ejemplo de código, errores comunes y la respuesta que conviene dar en entrevista.
> **Cómo usarla:** cada sección tiene `Qué es` → `Cómo lo explico` → `Código` → `Preguntas típicas`. Lo marcado con 🎯 es lo que muy probablemente te pregunten.

---

## Índice

1. [Perfil FullStack](#1-perfil-fullstack)
2. [Angular](#2-angular)
3. [CI/CD e Integración Continua](#3-cicd-e-integración-continua)
4. [Agilidad y ceremonias](#4-agilidad-y-ceremonias)
5. [Programación funcional en Java](#5-programación-funcional-en-java)
6. [Concurrencia y Virtual Threads](#6-concurrencia-y-virtual-threads)
7. [Spring Boot](#7-spring-boot)
8. [Seguridad: JWT, OAuth2 y Spring Security](#8-seguridad-jwt-oauth2-y-spring-security)
9. [GCP: Pub/Sub, Functions, Cloud Run](#9-gcp-pubsub-functions-cloud-run)
10. [Kafka](#10-kafka)
11. [Firebase / Firestore y NoSQL](#11-firebase--firestore-y-nosql)
12. [Docker](#12-docker)
13. [Kubernetes](#13-kubernetes)
14. [Patrones de diseño](#14-patrones-de-diseño)
15. [Arquitectura y buenas prácticas](#15-arquitectura-y-buenas-prácticas)
16. [Preguntas de entrevista y respuestas modelo](#16-preguntas-de-entrevista-y-respuestas-modelo)
17. [Negociación salarial](#17-negociación-salarial)
18. [Plan de repaso de 7 días](#18-plan-de-repaso-de-7-días)
19. [Cheat sheets](#19-cheat-sheets)

---

## 1. Perfil FullStack

### Qué es
Un perfil FullStack domina el ciclo completo: **frontend** (Angular/React), **backend** (Java/Spring Boot), **persistencia** (SQL/NoSQL), **infraestructura** (Docker, Kubernetes, cloud) y **entrega** (CI/CD). No significa ser experto en todo: significa poder llevar una funcionalidad de punta a punta sin bloquearse.

### Cómo lo explico en entrevista 🎯
> "Trabajo el flujo completo: modelo el contrato REST, implemento el backend en Spring Boot con su capa de servicio y repositorio, expongo el endpoint asegurado con JWT, consumo desde Angular con un servicio y un interceptor, y me hago cargo del pipeline que lo despliega en contenedores. Mi centro de gravedad es el backend Java, pero el frontend no me frena."

**Regla de oro:** declara tu *centro de gravedad*. Decir "soy experto en todo" resta credibilidad; decir "backend fuerte + frontend sólido" suma.

### Mapa mental del stack

| Capa | Tecnología | Qué debo saber responder |
|---|---|---|
| UI | Angular, TypeScript, RxJS | Componentes, estado, formularios, interceptores |
| API | Spring Boot, REST | Controllers, DTOs, validación, manejo de errores |
| Seguridad | Spring Security, JWT, OAuth2 | Filtros, flujos de token, roles |
| Datos | PostgreSQL / Firestore | JPA, transacciones, modelado NoSQL |
| Mensajería | Pub/Sub, Kafka | Eventos, idempotencia, orden |
| Infra | Docker, Kubernetes, GCP | Imagen, deployment, escalamiento |
| Entrega | CI/CD, Git | Pipeline, ramas, estrategia de release |

### Preguntas típicas
- *"¿Qué parte del stack prefieres?"* → Responde con el centro de gravedad + evidencia.
- *"Cuéntame una funcionalidad que hiciste end-to-end."* → Usa formato STAR (ver §16).
- *"¿Cómo decides si una lógica va en el front o en el back?"* → Regla: **validación de UX en el front, validación de verdad en el back**. El front nunca es fuente de confianza.

---

## 2. Angular

### 2.1 Fundamentos

**Angular** es un framework SPA basado en TypeScript, con inyección de dependencias, enrutamiento, formularios reactivos y RxJS integrados. Desde Angular 14+ la tendencia es **standalone components** (sin NgModules) y desde Angular 16/17 **Signals** para reactividad fina.

#### Bloques del framework

| Concepto | Para qué sirve |
|---|---|
| Component | Unidad de UI: clase + template + estilos |
| Directive | Modifica comportamiento del DOM (`*ngIf`, `*ngFor`, custom) |
| Pipe | Transforma datos en el template (`date`, `currency`, custom) |
| Service | Lógica reutilizable / acceso a datos, inyectable |
| Module / Standalone | Agrupa y declara dependencias |
| Router | Navegación, lazy loading, guards |

### 2.2 Componente típico (standalone + signals)

```typescript
import { Component, inject, signal, computed } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UsuarioService } from './usuario.service';

@Component({
  selector: 'app-usuarios',
  standalone: true,
  imports: [CommonModule],
  template: `
    <h2>Usuarios activos: {{ totalActivos() }}</h2>
    @if (cargando()) {
      <p>Cargando…</p>
    } @else {
      <ul>
        @for (u of usuarios(); track u.id) {
          <li>{{ u.nombre }}</li>
        }
      </ul>
    }
  `
})
export class UsuariosComponent {
  private readonly service = inject(UsuarioService);

  readonly usuarios = signal<Usuario[]>([]);
  readonly cargando = signal(true);
  readonly totalActivos = computed(() =>
    this.usuarios().filter(u => u.activo).length
  );

  ngOnInit(): void {
    this.service.listar().subscribe({
      next: data => { this.usuarios.set(data); this.cargando.set(false); },
      error: () => this.cargando.set(false)
    });
  }
}
```

### 2.3 Ciclo de vida 🎯

| Hook | Cuándo se ejecuta | Uso habitual |
|---|---|---|
| `ngOnChanges` | Cambia un `@Input` | Reaccionar a props |
| `ngOnInit` | Una vez, tras el primer bind | Carga inicial de datos |
| `ngDoCheck` | Cada ciclo de detección | Detección custom (usar con cuidado) |
| `ngAfterViewInit` | Vista hija lista | Acceso a `@ViewChild`, librerías DOM |
| `ngOnDestroy` | Al destruir | **Liberar suscripciones**, timers |

**Error clásico:** hacer la llamada HTTP en el constructor. El constructor es para inyectar; `ngOnInit` es para inicializar.

### 2.4 RxJS — lo mínimo que te van a preguntar 🎯

```typescript
// Buscador con debounce: el patrón que más piden explicar
this.form.get('q')!.valueChanges.pipe(
  debounceTime(300),              // espera a que deje de tipear
  distinctUntilChanged(),         // ignora si el valor no cambió
  switchMap(q => this.api.buscar(q)),  // cancela la búsqueda anterior
  takeUntilDestroyed(this.destroyRef)  // evita memory leaks
).subscribe(res => this.resultados.set(res));
```

**Operadores de aplanado — pregunta trampa frecuente:**

| Operador | Comportamiento | Caso de uso |
|---|---|---|
| `switchMap` | Cancela la anterior | Búsqueda / autocomplete |
| `mergeMap` | Ejecuta todas en paralelo | Subidas independientes |
| `concatMap` | Encola y respeta orden | Guardados secuenciales |
| `exhaustMap` | Ignora nuevas mientras haya una activa | Botón "login" anti doble-click |

**Memory leaks:** toda suscripción manual debe cerrarse (`takeUntil`, `takeUntilDestroyed`) o evitarse usando el pipe `async` en el template.

### 2.5 Formularios

```typescript
// Reactive Forms (recomendado para lógica real)
this.form = this.fb.group({
  email: ['', [Validators.required, Validators.email]],
  clave: ['', [Validators.required, Validators.minLength(8)]]
});

if (this.form.invalid) { this.form.markAllAsTouched(); return; }
this.api.login(this.form.getRawValue()).subscribe(...);
```

- **Template-driven** (`ngModel`): formularios simples, poca lógica.
- **Reactive**: validación compleja, testeable, tipado. **Es el que debes defender.**

### 2.6 HTTP + Interceptor (aquí se conecta con JWT) 🎯

```typescript
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(TokenService).get();
  const authReq = token
    ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
    : req;

  return next(authReq).pipe(
    catchError((err: HttpErrorResponse) => {
      if (err.status === 401) inject(AuthService).logout();
      return throwError(() => err);
    })
  );
};
```

### 2.7 Routing, lazy loading y guards

```typescript
export const routes: Routes = [
  { path: '', component: HomeComponent },
  {
    path: 'admin',
    canActivate: [authGuard],
    loadChildren: () => import('./admin/admin.routes').then(m => m.ADMIN_ROUTES)
  },
  { path: '**', component: NotFoundComponent }
];

export const authGuard: CanActivateFn = () =>
  inject(AuthService).estaAutenticado() || inject(Router).createUrlTree(['/login']);
```

**Lazy loading** = cada módulo/ruta se descarga solo cuando se navega → bundle inicial más chico → mejor tiempo de carga.

### 2.8 Change detection 🎯

- **Default:** Angular revisa todo el árbol ante cualquier evento.
- **OnPush:** el componente solo se revisa si cambia una referencia de `@Input`, se emite un evento propio, o se dispara manualmente (`markForCheck`).
- **Signals:** reactividad granular, actualiza solo lo que depende de la señal. Es la dirección hacia donde va Angular (zoneless).

> Respuesta corta: *"Uso OnPush con objetos inmutables, o signals en proyectos nuevos, para que Angular no recorra todo el árbol en cada evento."*

### 2.9 Testing

```typescript
describe('UsuariosComponent', () => {
  beforeEach(() => TestBed.configureTestingModule({
    imports: [UsuariosComponent],
    providers: [provideHttpClientTesting()]
  }));

  it('cuenta usuarios activos', () => {
    const fixture = TestBed.createComponent(UsuariosComponent);
    fixture.componentInstance.usuarios.set([{id:1,activo:true},{id:2,activo:false}]);
    expect(fixture.componentInstance.totalActivos()).toBe(1);
  });
});
```
Jasmine + Karma (clásico), Jest (frecuente en empresas), Cypress/Playwright para E2E.

### 2.10 Preguntas típicas de Angular
- Diferencia entre `Observable` y `Promise` → *Observable es un stream, lazy, cancelable y multi-valor; Promise es un valor único, eager y no cancelable.*
- `switchMap` vs `mergeMap` → tabla de arriba.
- ¿Cómo evitas memory leaks?
- ¿Qué es la inyección de dependencias en Angular y qué es un `providedIn: 'root'`?
- ¿Cómo manejas el estado global? → Servicio con `BehaviorSubject`/signals para casos simples, NgRx si hay muchos eventos y trazabilidad.
- ¿Cómo aseguras rutas? → Guards + validación real en el backend.

---

## 3. CI/CD e Integración Continua

### 3.1 Definiciones que hay que separar bien 🎯

| Término | Qué significa |
|---|---|
| **CI — Integración Continua** | Cada push se integra a la rama principal y dispara build + tests automáticos. Objetivo: detectar conflictos y regresiones en minutos, no en semanas. |
| **CD — Entrega Continua (Delivery)** | Todo commit que pasa el pipeline queda **listo para desplegar**; el despliegue a producción es un botón manual. |
| **CD — Despliegue Continuo (Deployment)** | Ese artefacto se despliega **automáticamente** a producción si pasa todas las puertas de calidad. |

> Respuesta corta de entrevista: *"CI es integrar y validar temprano; Delivery es tener siempre un artefacto desplegable; Deployment es que ese artefacto llegue solo a producción."*

### 3.2 Anatomía de un pipeline

```
commit → build → tests unitarios → análisis estático (SonarQube)
       → tests de integración → build de imagen Docker
       → push al registry (Artifact Registry / ECR)
       → deploy a DEV → tests E2E → deploy a QA (aprobación) → deploy a PROD
```

**Puertas de calidad (quality gates)** habituales: cobertura mínima (80%), 0 vulnerabilidades críticas, 0 code smells bloqueantes, build reproducible.

### 3.3 Ejemplo: GitHub Actions para Spring Boot

```yaml
name: ci
on:
  push: { branches: [main] }
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { java-version: '21', distribution: 'temurin', cache: maven }
      - name: Tests
        run: mvn -B verify
      - name: Análisis estático
        run: mvn sonar:sonar -Dsonar.projectKey=mi-api
      - name: Build imagen
        run: docker build -t europe-docker.pkg.dev/$PROJECT/repo/api:${{ github.sha }} .
      - name: Push
        run: docker push europe-docker.pkg.dev/$PROJECT/repo/api:${{ github.sha }}
```

### 3.4 Ejemplo: Cloud Build (GCP)

```yaml
steps:
  - name: maven:3.9-eclipse-temurin-21
    entrypoint: mvn
    args: ['verify']
  - name: gcr.io/cloud-builders/docker
    args: ['build','-t','gcr.io/$PROJECT_ID/api:$SHORT_SHA','.']
  - name: gcr.io/cloud-builders/gcloud
    args: ['run','deploy','api','--image','gcr.io/$PROJECT_ID/api:$SHORT_SHA','--region','us-central1']
images: ['gcr.io/$PROJECT_ID/api:$SHORT_SHA']
```

### 3.5 Estrategias de ramas 🎯

| Estrategia | Descripción | Cuándo |
|---|---|---|
| **GitFlow** | `develop`, `release/*`, `hotfix/*`, `main` | Releases con fecha, varios entornos, software versionado |
| **Trunk Based** | Ramas cortas (<1 día) contra `main`, feature flags | CI/CD real, despliegues diarios |
| **GitHub Flow** | Rama por feature → PR → `main` → deploy | Equipos web, entrega continua |

Trunk Based es lo que suele buscarse cuando la empresa dice "queremos CI de verdad": ramas largas = integración tardía = conflictos.

### 3.6 Estrategias de despliegue 🎯

- **Rolling update:** reemplaza pods de a poco (default en Kubernetes).
- **Blue/Green:** dos entornos idénticos, se cambia el tráfico de golpe. Rollback instantáneo, cuesta el doble de infra.
- **Canary:** 5% del tráfico a la versión nueva, se observa, se sube gradualmente.
- **Feature flags:** el código va a producción apagado; se enciende por configuración. Desacopla *deploy* de *release*.

### 3.7 Conceptos complementarios
- **Artefacto inmutable:** se construye una vez y se promueve el *mismo* binario/imagen entre entornos. Nunca recompilar por ambiente.
- **IaC (Terraform):** la infraestructura también se versiona.
- **Secretos:** nunca en el repo. Secret Manager / GitHub Secrets / Kubernetes Secrets.
- **DORA metrics:** frecuencia de despliegue, lead time, MTTR, % de fallos de cambio. Si preguntan "¿cómo mides que el CI/CD funciona?", esta es la respuesta.

---

## 4. Agilidad y ceremonias

### 4.1 Scrum en una pantalla 🎯

**Roles**
- **Product Owner:** dueño del *qué* y del valor; prioriza el Product Backlog.
- **Scrum Master:** facilita, remueve impedimentos, cuida el proceso. No es jefe.
- **Development Team:** autoorganizado, multifuncional, dueño del *cómo*.

**Artefactos**
- **Product Backlog** — lista priorizada de todo.
- **Sprint Backlog** — lo comprometido para este sprint.
- **Incremento** — software potencialmente entregable + *Definition of Done*.

**Ceremonias**

| Ceremonia | Duración (sprint 2 sem.) | Propósito |
|---|---|---|
| **Sprint Planning** | ≤ 4 h | Definir objetivo del sprint y seleccionar historias |
| **Daily Standup** | 15 min | Sincronizar, detectar bloqueos |
| **Sprint Review** | ≤ 2 h | Mostrar el incremento a stakeholders, recibir feedback |
| **Retrospectiva** | ≤ 1,5 h | Mejorar el proceso: qué mantener, qué cambiar |
| **Refinement** (continuo) | ~10% del sprint | Detallar y estimar historias futuras |

### 4.2 La Daily 🎯
Tres preguntas: **¿qué hice ayer?**, **¿qué haré hoy?**, **¿qué me bloquea?**

Buenas prácticas que puedes mencionar y te hacen ver senior:
- Es una **sincronización del equipo**, no un reporte al jefe.
- Los problemas se *detectan* en la daily y se *resuelven después* ("parking lot").
- 15 minutos, de pie o cámara encendida, misma hora siempre.
- Se habla del **tablero**, no de las personas: se recorren las historias de derecha a izquierda (lo más cerca de "Done" primero).

### 4.3 Estimación
- **Story points** con Fibonacci (1,2,3,5,8,13): miden *complejidad + incertidumbre + esfuerzo*, no horas.
- **Planning Poker** para estimar en equipo y aflorar supuestos distintos.
- **Velocidad** = puntos completados por sprint; sirve para *pronosticar*, no para comparar equipos ni presionar.

### 4.4 Kanban (por si trabajan con flujo continuo)
- Visualizar el flujo, **limitar WIP**, gestionar el flujo, políticas explícitas, mejora continua.
- Métricas: **lead time**, **cycle time**, **throughput**, diagrama de flujo acumulado.
- Se usa mucho en equipos de soporte/mantención donde no se puede comprometer un sprint fijo.

### 4.5 Definiciones que suelen preguntar
- **DoR (Definition of Ready):** criterios para que una historia pueda entrar al sprint (criterios de aceptación claros, dependencias resueltas, estimada).
- **DoD (Definition of Done):** criterios para decir que está terminada (código revisado, tests, desplegado en DEV, documentado).
- **Historia de usuario:** *Como \<rol\>, quiero \<acción\>, para \<beneficio\>* + criterios de aceptación (Gherkin: Dado/Cuando/Entonces).

### 4.6 Preguntas típicas
- *"¿Qué haces si una historia no alcanza a terminarse en el sprint?"* → Vuelve al backlog, se re-estima el remanente; no se "extiende" el sprint.
- *"¿Qué haces si el PO agrega trabajo a mitad de sprint?"* → Se conversa el impacto en el objetivo del sprint; si entra algo, sale algo.
- *"¿Cómo aporta un dev a la agilidad?"* → Historias pequeñas, PRs chicos, integración diaria, avisar bloqueos temprano, participar del refinement.

---

## 5. Programación funcional en Java

### 5.1 Base: interfaces funcionales 🎯

| Interfaz | Firma | Uso |
|---|---|---|
| `Function<T,R>` | `R apply(T)` | `map` |
| `Predicate<T>` | `boolean test(T)` | `filter` |
| `Consumer<T>` | `void accept(T)` | `forEach` |
| `Supplier<T>` | `T get()` | lazy, fábricas |
| `BiFunction<T,U,R>` | `R apply(T,U)` | combinaciones |
| `UnaryOperator<T>` | `T apply(T)` | transformación mismo tipo |

### 5.2 Streams: `filter`, `map`, `reduce`, `collect`

```java
record Pedido(String id, String cliente, BigDecimal monto, Estado estado) {}

// filter + map + collect
List<String> idsPagados = pedidos.stream()
    .filter(p -> p.estado() == Estado.PAGADO)      // Predicate
    .map(Pedido::id)                                // Function
    .toList();

// reduce: suma de montos
BigDecimal total = pedidos.stream()
    .map(Pedido::monto)
    .reduce(BigDecimal.ZERO, BigDecimal::add);

// agrupar
Map<Estado, List<Pedido>> porEstado = pedidos.stream()
    .collect(Collectors.groupingBy(Pedido::estado));

// agrupar + contar
Map<String, Long> porCliente = pedidos.stream()
    .collect(Collectors.groupingBy(Pedido::cliente, Collectors.counting()));

// flatMap: aplanar listas anidadas
List<Item> items = pedidos.stream()
    .flatMap(p -> p.items().stream())
    .toList();
```

### 5.3 Operaciones intermedias vs terminales 🎯

- **Intermedias (lazy):** `filter`, `map`, `flatMap`, `sorted`, `distinct`, `limit`, `peek`. No ejecutan nada hasta que llega una terminal.
- **Terminales:** `collect`, `toList`, `forEach`, `reduce`, `count`, `anyMatch`, `findFirst`.

> Pregunta trampa: *"¿Qué imprime un stream con solo `filter` y `map`?"* → **Nada.** Sin operación terminal no se evalúa.

### 5.4 Optional — cómo usarlo bien

```java
// MAL: Optional con get() es igual de peligroso que null
String nombre = repo.findById(id).get();

// BIEN
String nombre = repo.findById(id)
    .map(Usuario::nombre)
    .orElseThrow(() -> new UsuarioNoEncontradoException(id));

// Con valor por defecto perezoso
Config c = buscar(id).orElseGet(Config::porDefecto);
```
Reglas: `Optional` se usa como **retorno**, no como parámetro ni como campo de entidad.

### 5.5 "Funcional Lambda" (del temario) — dos lecturas
El apunte `Funcional Lambda / Programación Funcional / filter, map` mezcla dos cosas que conviene separar en la entrevista:

1. **Lambdas y streams de Java** (lo de arriba): estilo declarativo, sin mutación, funciones como valores.
2. **Functions as a Service** (Cloud Functions en GCP, Lambda en AWS): unidad de cómputo sin servidor, disparada por eventos (ver §9.3).

Si te preguntan "¿has trabajado con funcional/lambda?", aclara cuál de las dos: *"En Java uso ampliamente lambdas y Streams; en GCP he trabajado Cloud Functions disparadas por Pub/Sub, que es el equivalente a AWS Lambda."*

### 5.6 Principios funcionales que puedes citar
- **Inmutabilidad:** `record`, `List.copyOf`, no mutar el objeto de entrada → menos bugs, seguro en concurrencia.
- **Funciones puras:** mismo input → mismo output, sin efectos secundarios → testeables.
- **Composición:** `f.andThen(g)`, `predicado.and(otro)`.
- **Declarativo sobre imperativo:** el *qué* en lugar del *cómo*.

### 5.7 Cuándo NO usar streams
Loops con mucha mutación de estado, salidas tempranas complejas, o código en un hot path donde el `for` es más legible y rápido. Un stream ilegible es peor que un `for` claro.

---

## 6. Concurrencia y Virtual Threads

### 6.1 Modelo clásico 🎯

- **Thread de plataforma** = hilo del SO. Costoso (~1 MB de stack). Por eso usamos **pools** (`ExecutorService`) en vez de crear hilos a mano.
- Problema histórico: en aplicaciones web **la mayoría del tiempo el hilo está bloqueado esperando I/O** (base de datos, HTTP). Con 200 hilos en el pool, 200 requests concurrentes lentos saturan el servidor.
- Soluciones previas: programación reactiva (WebFlux, `Mono`/`Flux`) — escala, pero el código es difícil de leer y depurar.

```java
ExecutorService pool = Executors.newFixedThreadPool(10);
Future<String> f = pool.submit(() -> servicio.llamar());
String r = f.get();           // bloquea
pool.shutdown();
```

### 6.2 Virtual Threads (Project Loom, estable desde Java 21) 🎯

**Qué son:** hilos ligerísimos gestionados por la JVM, no por el SO. Puedes tener **millones**. Cuando un virtual thread se bloquea en I/O, la JVM lo "desmonta" del hilo portador (carrier thread) y deja ese hilo del SO libre para otro virtual thread.

**Por qué importan:** permiten escribir código **bloqueante y secuencial** (fácil de leer y depurar) con la escalabilidad del modelo reactivo.

```java
// Crear uno
Thread.startVirtualThread(() -> procesar(pedido));

// Executor: un virtual thread por tarea
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    List<Future<Resultado>> futuros = pedidos.stream()
        .map(p -> executor.submit(() -> procesar(p)))
        .toList();
}   // el close() espera a que todas terminen
```

**En Spring Boot 3.2+** se habilita con una línea:
```properties
spring.threads.virtual.enabled=true
```
Cada request HTTP pasa a atenderse en un virtual thread.

### 6.3 Trampas que te pueden preguntar 🎯

| Tema | Detalle |
|---|---|
| **No hacer pool de virtual threads** | Son baratos: uno por tarea. Un pool fijo anula el beneficio. |
| **Pinning** | Si el hilo se bloquea dentro de un `synchronized` (o JNI), queda "clavado" al carrier thread. Solución: usar `ReentrantLock`. (En Java 24+ el pinning por `synchronized` se eliminó). |
| **No sirven para CPU-bound** | Su ventaja es I/O. Para cálculo intensivo el límite siguen siendo los núcleos. |
| **ThreadLocal** | Sigue funcionando, pero con millones de hilos puede ser costoso; alternativa: `ScopedValue`. |
| **El cuello de botella se mueve** | Si atiendes 10.000 requests pero el pool de conexiones a BD tiene 20, el problema ahora es la BD. |

### 6.4 Structured Concurrency (preview)

```java
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    var usuario = scope.fork(() -> usuarioService.buscar(id));
    var pedidos = scope.fork(() -> pedidoService.listar(id));
    scope.join().throwIfFailed();
    return new Vista(usuario.get(), pedidos.get());
}   // si una falla, la otra se cancela automáticamente
```

### 6.5 Fundamentos que siguen cayendo en entrevista
- **`synchronized` vs `ReentrantLock`:** el segundo permite `tryLock`, timeout, equidad e interrupción.
- **`volatile`:** garantiza visibilidad entre hilos, **no** atomicidad.
- **Atomics:** `AtomicInteger`, `LongAdder` para contadores sin bloqueo (CAS).
- **Colecciones concurrentes:** `ConcurrentHashMap`, `CopyOnWriteArrayList`, `BlockingQueue`.
- **Race condition / deadlock / starvation:** define los tres y cómo los evitas (orden consistente de locks, timeouts, inmutabilidad).
- **`CompletableFuture`:** composición asíncrona (`thenApply`, `thenCompose`, `allOf`).

---

## 7. Spring Boot

### 7.1 Por qué Spring Boot
Autoconfiguración, servidor embebido, *starters*, `application.yml` por perfil, Actuator para observabilidad. Convención sobre configuración.

### 7.2 Arquitectura en capas

```
Controller (REST, DTOs, validación)
   ↓
Service (lógica de negocio, @Transactional)
   ↓
Repository (Spring Data JPA)
   ↓
Entity / Base de datos
```
**Regla:** las entidades JPA **no** salen por el controller. Se mapean a DTOs (MapStruct o mapeo manual) para no filtrar el modelo interno ni provocar lazy-loading fuera de transacción.

### 7.3 Controller completo

```java
@RestController
@RequestMapping("/api/v1/pedidos")
@RequiredArgsConstructor
public class PedidoController {

    private final PedidoService service;

    @GetMapping("/{id}")
    public PedidoResponse obtener(@PathVariable Long id) {
        return service.obtener(id);
    }

    @GetMapping
    public Page<PedidoResponse> listar(@PageableDefault(size = 20) Pageable pageable) {
        return service.listar(pageable);
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public PedidoResponse crear(@Valid @RequestBody CrearPedidoRequest req) {
        return service.crear(req);
    }
}
```

### 7.4 Manejo global de errores 🎯

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(RecursoNoEncontradoException.class)
    public ResponseEntity<ApiError> noEncontrado(RecursoNoEncontradoException e) {
        return ResponseEntity.status(404).body(new ApiError("NOT_FOUND", e.getMessage()));
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ApiError> validacion(MethodArgumentNotValidException e) {
        var detalles = e.getBindingResult().getFieldErrors().stream()
            .map(f -> f.getField() + ": " + f.getDefaultMessage())
            .toList();
        return ResponseEntity.badRequest().body(new ApiError("VALIDATION_ERROR", detalles));
    }
}
```
Nunca devolver el stacktrace al cliente: filtra información sensible.

### 7.5 Inyección de dependencias 🎯
- **Por constructor** (recomendado): permite `final`, facilita tests, detecta dependencias circulares al arrancar.
- Por setter: dependencias opcionales.
- Por campo (`@Autowired` en el atributo): desaconsejado, no testeable sin contenedor.

**Scopes:** `singleton` (default), `prototype`, `request`, `session`.

### 7.6 Transacciones 🎯
```java
@Transactional
public void transferir(Long origen, Long destino, BigDecimal monto) { ... }
```
- Por defecto hace rollback ante `RuntimeException`, **no** ante excepciones *checked* (`rollbackFor = Exception.class` para cambiarlo).
- **Self-invocation:** llamar a un método `@Transactional` desde otro método de la misma clase **no** activa el proxy → la transacción no se aplica. Pregunta clásica.
- Propagación: `REQUIRED` (default), `REQUIRES_NEW`, `SUPPORTS`, `MANDATORY`.

### 7.7 N+1 queries 🎯
Síntoma: una consulta por cada elemento de una lista.
Soluciones: `JOIN FETCH` en JPQL, `@EntityGraph`, `@BatchSize`, o proyecciones DTO.

```java
@Query("select p from Pedido p join fetch p.items where p.estado = :estado")
List<Pedido> buscarConItems(@Param("estado") Estado estado);
```

### 7.8 Perfiles y configuración
```yaml
# application.yml
spring:
  profiles:
    active: ${SPRING_PROFILES_ACTIVE:dev}
---
spring:
  config.activate.on-profile: prod
  datasource:
    url: ${DB_URL}
    username: ${DB_USER}
    password: ${DB_PASSWORD}   # desde Secret Manager / env, nunca hardcodeado
```

### 7.9 Actuator y observabilidad
`/actuator/health` (liveness/readiness para Kubernetes), `/actuator/metrics`, `/actuator/prometheus`. Trazas distribuidas con Micrometer Tracing + OpenTelemetry.

### 7.10 Testing
- `@SpringBootTest` — contexto completo (lento, para integración).
- `@WebMvcTest` — solo la capa web, con `MockMvc`.
- `@DataJpaTest` — solo la capa de persistencia.
- **Testcontainers** — levanta PostgreSQL/Kafka real en Docker para tests de integración. Mencionarlo suma puntos.

---

## 8. Seguridad: JWT, OAuth2 y Spring Security

> El temario dice **"JWT / OAuth2 — esto sí o sí"**. Es el tema más probable de la entrevista. Prepáralo hasta poder dibujarlo.

### 8.1 Autenticación vs Autorización 🎯
- **Autenticación (AuthN):** *¿quién eres?* → login, credenciales, token.
- **Autorización (AuthZ):** *¿qué puedes hacer?* → roles, scopes, permisos.

### 8.2 JWT — estructura

```
header.payload.signature
```
```json
// header
{ "alg": "RS256", "typ": "JWT" }
// payload (claims)
{ "sub": "user-123", "iss": "https://auth.miapp.com", "aud": "api-pedidos",
  "exp": 1735689600, "iat": 1735686000, "roles": ["ADMIN"] }
```
- **Firmado ≠ cifrado.** El payload es Base64URL: **cualquiera puede leerlo**. Nunca pongas datos sensibles dentro.
- La firma garantiza **integridad y autenticidad**, no confidencialidad.
- **HS256** (secreto compartido, simétrico) vs **RS256** (clave privada firma / pública verifica, asimétrico). En microservicios se prefiere RS256: los servicios solo necesitan la clave pública (JWKS).

### 8.3 Sesión vs JWT 🎯

| | Sesión en servidor | JWT |
|---|---|---|
| Estado | Guardado en servidor/Redis | Stateless, va en el token |
| Escalado | Requiere sticky sessions o store compartido | Escala horizontal sin estado |
| Revocación | Inmediata (borras la sesión) | **Difícil**: el token vale hasta que expira |
| Tamaño | Cookie pequeña | Token grande en cada request |

**Mitigación de la revocación:** access tokens cortos (5–15 min) + **refresh token** largo, almacenado y revocable en servidor; lista de revocación (denylist) para casos críticos.

### 8.4 Dónde guardar el token en el frontend 🎯
- `localStorage`: simple, pero **vulnerable a XSS** (cualquier script lo lee).
- **Cookie `HttpOnly` + `Secure` + `SameSite=Strict/Lax`**: inaccesible a JS, mitiga XSS, pero requiere protección **CSRF**.
- Respuesta madura: *"Para apps con backend propio prefiero cookie HttpOnly con SameSite y CSRF token; si es un SPA contra API de terceros, access token en memoria y refresh en cookie HttpOnly."*

### 8.5 OAuth2 — roles y flujos 🎯

**Roles:** Resource Owner (usuario), Client (la app), Authorization Server (quien emite tokens), Resource Server (la API protegida).

| Flujo | Cuándo usarlo |
|---|---|
| **Authorization Code + PKCE** | SPAs y apps móviles. **Es el estándar actual.** |
| **Client Credentials** | Máquina a máquina (servicio → servicio), sin usuario |
| **Refresh Token** | Renovar el access token sin re-login |
| Implicit / Password (ROPC) | **Obsoletos**, no recomendarlos |

**OAuth2 vs OpenID Connect:** OAuth2 es **autorización** (dar acceso a un recurso). **OIDC** es una capa sobre OAuth2 que agrega **autenticación** e introduce el `id_token` (un JWT con la identidad del usuario). Si te preguntan "login con Google", la respuesta correcta es **OIDC**.

### 8.6 Flujo Authorization Code + PKCE (dibújalo)

```
1. Angular genera code_verifier + code_challenge
2. Redirige al Authorization Server con code_challenge
3. Usuario se autentica y consiente
4. AS redirige de vuelta con ?code=XYZ
5. Angular canjea code + code_verifier → access_token (+ refresh + id_token)
6. Angular llama a la API con Authorization: Bearer <access_token>
7. La API valida firma, iss, aud y exp contra el JWKS del AS
```
PKCE evita que un atacante que intercepte el `code` pueda canjearlo sin el `code_verifier`.

### 8.7 Spring Security — configuración moderna (Spring Boot 3, sin `WebSecurityConfigurerAdapter`) 🎯

```java
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {

    @Bean
    SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http
            .csrf(csrf -> csrf.disable())                     // API stateless con Bearer
            .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/v1/auth/**", "/actuator/health").permitAll()
                .requestMatchers("/api/v1/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated())
            .oauth2ResourceServer(oauth -> oauth.jwt(Customizer.withDefaults()))
            .exceptionHandling(e -> e
                .authenticationEntryPoint((req, res, ex) -> res.sendError(401))
                .accessDeniedHandler((req, res, ex) -> res.sendError(403)))
            .build();
    }

    @Bean
    PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();   // nunca MD5/SHA1 para contraseñas
    }
}
```

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://auth.miapp.com   # descarga el JWKS solo
```

**Filtro JWT propio** (cuando emites tus propios tokens, sin Authorization Server externo):

```java
public class JwtAuthFilter extends OncePerRequestFilter {
    @Override
    protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res,
                                    FilterChain chain) throws ServletException, IOException {
        String header = req.getHeader("Authorization");
        if (header != null && header.startsWith("Bearer ")) {
            String token = header.substring(7);
            if (jwtService.esValido(token)) {
                var auth = new UsernamePasswordAuthenticationToken(
                        jwtService.getSubject(token), null, jwtService.getAuthorities(token));
                SecurityContextHolder.getContext().setAuthentication(auth);
            }
        }
        chain.doFilter(req, res);
    }
}
```

### 8.8 Cadena de filtros de Spring Security 🎯
La petición pasa por una cadena: `SecurityContextPersistenceFilter` → filtros de autenticación (`UsernamePasswordAuthenticationFilter`, `BearerTokenAuthenticationFilter`) → `ExceptionTranslationFilter` → `FilterSecurityInterceptor/AuthorizationFilter`.
Piezas clave: `AuthenticationManager` → `AuthenticationProvider` → `UserDetailsService` → `SecurityContextHolder`.

### 8.9 Autorización a nivel de método
```java
@PreAuthorize("hasRole('ADMIN')")
public void borrar(Long id) { ... }

@PreAuthorize("#id == authentication.name or hasRole('ADMIN')")
public Usuario ver(String id) { ... }
```

### 8.10 Validaciones que un revisor espera escuchar
Al validar un JWT hay que comprobar: **firma**, **`exp`** (expiración), **`iss`** (emisor), **`aud`** (destinatario), algoritmo esperado (rechazar `alg: none` y evitar confusión HS/RS), y que el usuario siga activo.

### 8.11 OWASP Top 10 aplicado
Broken Access Control (validar autorización en el servidor, no ocultar botones), Inyección (consultas parametrizadas / JPA), XSS (sanitizar; Angular escapa por defecto), CSRF (tokens en flujos con cookie), configuración insegura (CORS abierto, actuator expuesto), secretos en el repo, dependencias vulnerables (`mvn dependency-check`, Dependabot).

---

## 9. GCP: Pub/Sub, Functions, Cloud Run

### 9.1 Servicios que debes ubicar

| Categoría | Servicio | Uso |
|---|---|---|
| Cómputo | Compute Engine / GKE / **Cloud Run** / **Cloud Functions** | VM / K8s gestionado / contenedor serverless / función serverless |
| Mensajería | **Pub/Sub** | Eventos asíncronos, desacople |
| Datos | Cloud SQL, **Firestore**, BigQuery, Bigtable, Spanner | Relacional / documental / analítica |
| Almacenamiento | Cloud Storage (GCS) | Archivos, buckets |
| Seguridad | IAM, **Secret Manager**, KMS | Permisos, secretos, llaves |
| Entrega | Cloud Build, **Artifact Registry** | CI/CD, imágenes |
| Observabilidad | Cloud Logging, Monitoring, Trace | Logs, métricas, trazas |

### 9.2 Pub/Sub a fondo 🎯

**Modelo:** *Publisher* → **Topic** → **Subscription(s)** → *Subscriber*. Es **pub/sub** (uno a muchos): cada suscripción recibe una copia de cada mensaje.

```
Publisher ──► Topic ──┬──► Subscription A ──► Cloud Run (push)
                      └──► Subscription B ──► Worker (pull)
```

**Conceptos clave:**
- **Push vs Pull:** en *push* Pub/Sub hace un POST a tu endpoint HTTPS; en *pull* tu servicio pide mensajes. Push es cómodo con Cloud Run; pull da mejor control de flujo.
- **Ack / Nack y `ackDeadline`:** si no confirmas (ack) dentro del plazo, el mensaje se re-entrega.
- **At-least-once:** el modo por defecto **puede entregar duplicados** → tu consumidor **debe ser idempotente**. (Existe *exactly-once delivery* dentro de una región, con restricciones).
- **Orden:** no garantizado salvo que actives *ordering keys* (mensajes con la misma clave llegan en orden).
- **Dead Letter Topic (DLQ):** tras N intentos fallidos el mensaje va a un topic muerto para inspección.
- **Retención y replay:** retención configurable (hasta 7 días por defecto, más con snapshots) y `seek` para reprocesar.

**Publicar y consumir desde Spring:**
```java
// Publicar
@Autowired PubSubTemplate pubSubTemplate;
pubSubTemplate.publish("pedidos-topic", new ObjectMapper().writeValueAsString(evento));

// Consumir (pull con subscriber)
pubSubTemplate.subscribe("pedidos-sub", message -> {
    var evento = parse(message.getPubsubMessage().getData().toStringUtf8());
    if (yaProcesado(evento.id())) { message.ack(); return; }   // idempotencia
    procesar(evento);
    message.ack();
});
```

**Idempotencia — el patrón que debes nombrar:** guardar el `messageId` (o un id de negocio) en una tabla/colección de "procesados" y descartar duplicados; o hacer que la operación sea naturalmente idempotente (`UPSERT` en vez de `INSERT`).

### 9.3 Cloud Functions ("Funcional Lambda")

FaaS: código que se ejecuta ante un evento, sin administrar servidores. Escala a cero.

```java
public class ProcesarPedido implements BackgroundFunction<PubSubMessage> {
    @Override
    public void accept(PubSubMessage message, Context context) {
        String data = new String(Base64.getDecoder().decode(message.data), UTF_8);
        // procesar
    }
}
```

**Disparadores:** HTTP, Pub/Sub, Cloud Storage (archivo subido), Firestore (documento creado/actualizado), Cloud Scheduler (cron).

**Limitaciones que debes conocer:** *cold start* (mitigable con min-instances), timeout máximo, statelessness, límite de memoria. Para cargas más grandes o contenedores propios: **Cloud Run**.

**Cloud Functions vs Cloud Run:** Functions = una función, un evento, runtime gestionado. Cloud Run = tu contenedor Docker, cualquier lenguaje, HTTP o eventos, más control, también escala a cero. Para una app Spring Boot dockerizada, **Cloud Run** es la opción natural.

### 9.4 IAM en una línea
`Principal` (usuario/service account) + `Role` (conjunto de permisos) + `Resource`. Principio de **mínimo privilegio**: una service account por servicio, con los roles justos. Nunca uses la cuenta por defecto con rol Editor en producción.

### 9.5 Equivalencias GCP ↔ AWS (por si preguntan)

| GCP | AWS |
|---|---|
| Cloud Functions | Lambda |
| Cloud Run | Fargate / App Runner |
| Pub/Sub | SNS + SQS |
| Firestore | DynamoDB |
| Cloud Storage | S3 |
| GKE | EKS |
| Cloud SQL | RDS |
| Secret Manager | Secrets Manager |
| Artifact Registry | ECR |

---

## 10. Kafka

### 10.1 Conceptos 🎯

- **Topic:** canal lógico de eventos, dividido en **particiones**.
- **Partición:** log **ordenado e inmutable**; el orden se garantiza **dentro de una partición**, no en el topic completo.
- **Offset:** posición del consumidor en la partición. Kafka no borra al consumir: retiene por tiempo/tamaño.
- **Producer key:** determina la partición (`hash(key) % nPart`) → misma clave = misma partición = orden garantizado para esa entidad.
- **Consumer Group:** cada partición es consumida por **un solo consumidor** del grupo. Paralelismo máximo = número de particiones.
- **Rebalance:** al entrar o salir un consumidor se redistribuyen las particiones.
- **Broker / Cluster / Replication factor / ISR:** replicación entre brokers para tolerancia a fallos.

### 10.2 Garantías de entrega 🎯
- **At-most-once:** commit del offset antes de procesar (puedes perder mensajes).
- **At-least-once:** procesar y luego commitear (puedes duplicar) — **el más usado**.
- **Exactly-once (EOS):** productor idempotente + transacciones (`transactional.id`, `read_committed`). Tiene costo de rendimiento.

### 10.3 Kafka vs Pub/Sub 🎯

| | Kafka | Pub/Sub |
|---|---|---|
| Operación | Lo administras tú (o Confluent) | Totalmente gestionado |
| Orden | Por partición | Solo con ordering keys |
| Retención / replay | Log persistente, replay nativo por offset | Retención limitada + snapshots |
| Escalado | Manual (particiones) | Automático |
| Caso fuerte | Streaming, event sourcing, alto throughput | Desacople y eventos en GCP sin ops |

### 10.4 Spring Kafka

```java
@Component
public class PedidoConsumer {
    @KafkaListener(topics = "pedidos", groupId = "facturacion")
    public void consumir(ConsumerRecord<String, PedidoEvento> record, Acknowledgment ack) {
        try {
            servicio.procesar(record.value());
            ack.acknowledge();                  // commit manual
        } catch (Exception e) {
            log.error("Fallo offset {}", record.offset(), e);
            throw e;                            // va a retry/DLT
        }
    }
}

@Bean
public NewTopic pedidos() {
    return TopicBuilder.name("pedidos").partitions(6).replicas(3).build();
}
```
Configuración típica: `enable.auto.commit=false`, `ack-mode: MANUAL`, `DefaultErrorHandler` con `DeadLetterPublishingRecoverer`.

### 10.5 Preguntas frecuentes
- *"¿Cómo garantizas el orden de eventos de un cliente?"* → clave de partición = id del cliente.
- *"¿Qué pasa si hay más consumidores que particiones?"* → los sobrantes quedan ociosos.
- *"¿Cómo manejas un mensaje que siempre falla (poison pill)?"* → reintentos con backoff + Dead Letter Topic.
- *"¿Cómo evitas procesar dos veces?"* → idempotencia con id de evento o EOS transaccional.

---

## 11. Firebase / Firestore y NoSQL

### 11.1 Qué es
**Firestore** es una base de datos **NoSQL documental**, serverless, con escalado automático, sincronización en tiempo real y soporte offline. Parte de Firebase y disponible también dentro de GCP.

**Jerarquía:** `Colección → Documento → Campos` (y subcolecciones anidadas).

```
usuarios (colección)
  └── user_123 (documento)
        ├── nombre: "Ana"
        ├── email: "ana@x.cl"
        └── pedidos (subcolección)
              └── ped_1 { total: 15000, estado: "PAGADO" }
```

### 11.2 SQL vs NoSQL 🎯

| | Relacional (PostgreSQL) | Documental (Firestore) |
|---|---|---|
| Esquema | Rígido, migraciones | Flexible por documento |
| Relaciones | JOIN nativo | Sin JOIN: se desnormaliza o se hacen varias lecturas |
| Transacciones | ACID completo | Transacciones y batch, con límites |
| Consultas | SQL arbitrario, agregaciones | Consultas limitadas, requieren índices |
| Escalado | Vertical, réplicas de lectura | Horizontal automático |
| Cuándo | Datos relacionales, reportes, integridad | Alta escala, tiempo real, esquema cambiante |

**Regla mental:** en SQL modelas según **cómo se relacionan los datos**; en NoSQL modelas según **cómo vas a consultarlos**.

### 11.3 Modelado en Firestore
- **Desnormalizar** es normal: duplicar el nombre del usuario dentro del pedido para evitar una segunda lectura.
- Documento máximo 1 MiB; evitar arrays que crecen sin límite.
- **Hotspotting:** IDs secuenciales (timestamps monotónicos) concentran escrituras en un rango → usar IDs aleatorios.
- **Contadores distribuidos** (sharded counters) cuando hay muchas escrituras al mismo documento (límite ~1 escritura/seg por documento).

### 11.4 Consultas e índices

```javascript
// Angular / Web SDK
const q = query(
  collection(db, 'pedidos'),
  where('estado', '==', 'PAGADO'),
  where('total', '>=', 10000),
  orderBy('total', 'desc'),
  limit(20)
);
const snap = await getDocs(q);
```
- Índices **simples automáticos**; **compuestos manuales** (la consola te da el link para crearlos cuando falla).
- Sin `OR` nativo entre campos distintos (se resuelve con múltiples consultas o `in`).
- Paginación con `startAfter(ultimoDoc)`, no con offset.
- **Costo por operación**: se paga por lectura/escritura/borrado de documento, no por CPU. Consultar con `limit` no es solo rendimiento: es dinero.

### 11.5 Tiempo real y offline
```javascript
onSnapshot(q, snap => {
  this.pedidos.set(snap.docs.map(d => ({ id: d.id, ...d.data() })));
});
```
El SDK mantiene caché local y reintenta cuando vuelve la conexión — es la razón principal para elegir Firestore en apps móviles.

### 11.6 Security Rules 🎯
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /usuarios/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    match /pedidos/{pedidoId} {
      allow read: if request.auth != null
                  && resource.data.usuarioId == request.auth.uid;
      allow create: if request.auth != null
                    && request.resource.data.total is number;
    }
  }
}
```
Las reglas son la capa de autorización cuando el cliente accede **directamente** a Firestore. Si el acceso pasa por tu backend con el Admin SDK, las reglas **se saltan** y la autorización es responsabilidad del backend.

### 11.7 Otros servicios Firebase que suelen aparecer
Authentication (integra con OIDC/Google/email), Cloud Messaging (push), Remote Config (feature flags), Hosting, Crashlytics, Cloud Functions for Firebase.

---

## 12. Docker

### 12.1 Conceptos 🎯
- **Imagen:** plantilla inmutable en capas. **Contenedor:** instancia en ejecución de una imagen.
- **Contenedor vs VM:** el contenedor comparte el kernel del host y aísla procesos (namespaces + cgroups); la VM emula hardware completo con su propio SO. Contenedor: arranque en segundos, MBs. VM: minutos, GBs.
- **Capas y caché:** cada instrucción del Dockerfile crea una capa; si una cambia, se invalida el caché de todas las siguientes → **ordena de lo que menos cambia a lo que más cambia**.
- **Volumen:** persistencia fuera del ciclo de vida del contenedor.

### 12.2 Dockerfile multi-stage para Spring Boot 🎯

```dockerfile
# ---- build ----
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn -B dependency:go-offline          # capa cacheada: solo cambia si cambia el pom
COPY src ./src
RUN mvn -B clean package -DskipTests

# ---- runtime ----
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
RUN addgroup -S app && adduser -S app -G app   # no ejecutar como root
COPY --from=build /app/target/*.jar app.jar
USER app
EXPOSE 8080
HEALTHCHECK --interval=30s CMD wget -qO- http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java","-XX:MaxRAMPercentage=75","-jar","app.jar"]
```

**Por qué multi-stage:** la imagen final no lleva Maven ni el código fuente → de ~700 MB a ~200 MB, menos superficie de ataque.

### 12.3 Buenas prácticas
- Imagen base ligera (`-alpine`, `-jre` en vez de `-jdk`, o *distroless*).
- `.dockerignore` (excluir `target/`, `node_modules/`, `.git`).
- **Nunca** secretos en el Dockerfile ni en `ENV`: van por variables de entorno o Secret Manager en tiempo de ejecución.
- Tag explícito por commit (`api:1.4.2` o `api:$SHA`), no `latest` en producción.
- Un proceso por contenedor.
- Escanear imágenes (Trivy, Artifact Registry scanning).

### 12.4 Comandos que debes saber decir de memoria
```bash
docker build -t api:1.0 .
docker run -d -p 8080:8080 -e SPRING_PROFILES_ACTIVE=prod --name api api:1.0
docker ps / docker logs -f api / docker exec -it api sh
docker stop api && docker rm api
docker image prune -a
```

### 12.5 docker-compose para desarrollo local
```yaml
services:
  api:
    build: .
    ports: ["8080:8080"]
    environment:
      SPRING_DATASOURCE_URL: jdbc:postgresql://db:5432/app
    depends_on:
      db: { condition: service_healthy }
  db:
    image: postgres:16-alpine
    environment: { POSTGRES_PASSWORD: dev, POSTGRES_DB: app }
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
```

---

## 13. Kubernetes

### 13.1 Qué resuelve
Orquesta contenedores: despliegue declarativo, autoescalado, autorreparación, descubrimiento de servicios, balanceo y rolling updates.

### 13.2 Objetos esenciales 🎯

| Objeto | Para qué |
|---|---|
| **Pod** | Unidad mínima: uno o más contenedores que comparten red y volúmenes |
| **ReplicaSet** | Mantiene N réplicas de un pod |
| **Deployment** | Gestiona ReplicaSets: rolling updates y rollback |
| **Service** | IP estable y balanceo hacia los pods (ClusterIP / NodePort / LoadBalancer) |
| **Ingress** | Enrutamiento HTTP(S) externo, TLS, por host/path |
| **ConfigMap** | Configuración no sensible |
| **Secret** | Datos sensibles (base64, cifrar en reposo / usar Secret Manager) |
| **HPA** | Autoescalado horizontal por CPU/memoria/métricas |
| **Namespace** | Aislamiento lógico (dev/qa/prod) |
| **StatefulSet** | Cargas con estado e identidad estable (bases de datos) |
| **Job / CronJob** | Tareas puntuales o programadas |

### 13.3 Deployment comentado

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate: { maxSurge: 1, maxUnavailable: 0 }   # cero downtime
  selector:
    matchLabels: { app: api }
  template:
    metadata:
      labels: { app: api }
    spec:
      containers:
        - name: api
          image: europe-docker.pkg.dev/proj/repo/api:1.4.2
          ports: [{ containerPort: 8080 }]
          env:
            - name: SPRING_PROFILES_ACTIVE
              value: prod
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef: { name: db-secret, key: password }
          resources:
            requests: { cpu: "250m", memory: "512Mi" }   # lo que reserva
            limits:   { cpu: "1",    memory: "1Gi" }     # el techo
          readinessProbe:      # ¿puede recibir tráfico?
            httpGet: { path: /actuator/health/readiness, port: 8080 }
            initialDelaySeconds: 20
          livenessProbe:       # ¿hay que reiniciarlo?
            httpGet: { path: /actuator/health/liveness, port: 8080 }
            initialDelaySeconds: 40
---
apiVersion: v1
kind: Service
metadata: { name: api }
spec:
  selector: { app: api }
  ports: [{ port: 80, targetPort: 8080 }]
  type: ClusterIP
```

### 13.4 Probes 🎯
- **liveness:** si falla, Kubernetes **reinicia** el contenedor (proceso colgado).
- **readiness:** si falla, lo **saca del balanceador** sin reiniciarlo (aún calentando o dependencia caída).
- **startup:** para apps de arranque lento; evita que liveness mate el pod durante el boot.

Confundirlas es un error clásico: un liveness mal configurado provoca reinicios en cascada bajo carga.

### 13.5 HPA
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata: { name: api }
spec:
  scaleTargetRef: { apiVersion: apps/v1, kind: Deployment, name: api }
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource: { name: cpu, target: { type: Utilization, averageUtilization: 70 } }
```

### 13.6 Troubleshooting (lo que preguntan en entrevistas prácticas) 🎯
```bash
kubectl get pods -n prod
kubectl describe pod api-xxx          # eventos: por qué no arranca
kubectl logs -f api-xxx --previous    # logs del contenedor que murió
kubectl exec -it api-xxx -- sh
kubectl rollout status deployment/api
kubectl rollout undo deployment/api   # rollback
kubectl top pods                      # consumo
```

| Estado | Causa típica |
|---|---|
| `ImagePullBackOff` | Imagen/tag inexistente o sin credenciales del registry |
| `CrashLoopBackOff` | La app muere al arrancar (config, secreto faltante, puerto) |
| `Pending` | No hay nodo con recursos suficientes / PVC sin enlazar |
| `OOMKilled` | Excedió el `limits.memory` → ajustar límite o heap de la JVM |

### 13.7 Complementos
Helm (empaquetar manifiestos), Kustomize (overlays por entorno), ArgoCD/Flux (**GitOps**: el repo es la fuente de verdad del clúster), service mesh (Istio/Linkerd) para mTLS, retries y canary.

---

## 14. Patrones de diseño

> El temario dice literalmente **"¿Qué patrones de diseño has trabajado?"**. Prepara **3 patrones que realmente hayas usado**, con el problema concreto que resolviste. Es mucho mejor que recitar los 23 del GoF.

### 14.1 Creacionales

| Patrón | Problema que resuelve | Ejemplo real |
|---|---|---|
| **Singleton** | Una única instancia compartida | Los beans de Spring son singleton por defecto |
| **Factory Method** | Crear sin acoplar al tipo concreto | `ProcesadorPagoFactory.crear(tipo)` |
| **Abstract Factory** | Familias de objetos relacionados | Drivers por proveedor cloud |
| **Builder** | Construir objetos con muchos parámetros opcionales | `Pedido.builder().cliente(x).item(y).build()`, Lombok `@Builder` |
| **Prototype** | Clonar objetos costosos | Copias de configuraciones base |

```java
// Builder — el más citable en Java
Pedido pedido = Pedido.builder()
    .cliente("ana")
    .items(List.of(item1, item2))
    .cupon("VERANO20")
    .build();
```

### 14.2 Estructurales

| Patrón | Problema | Ejemplo |
|---|---|---|
| **Adapter** | Adaptar una interfaz externa a la tuya | Envolver el SDK de un banco tras tu propia interfaz |
| **Decorator** | Agregar comportamiento sin heredar | `BufferedReader`, caching sobre un repositorio |
| **Facade** | Simplificar un subsistema complejo | Un `PagoService` que esconde 4 integraciones |
| **Proxy** | Controlar el acceso | Proxies de Spring AOP (`@Transactional`, `@Cacheable`) |
| **Composite** | Árboles de objetos tratados uniformemente | Menús, estructuras de permisos |

### 14.3 De comportamiento

| Patrón | Problema | Ejemplo |
|---|---|---|
| **Strategy** | Intercambiar algoritmos en runtime | Medios de pago, reglas de descuento |
| **Observer** | Notificar a N interesados | `ApplicationEventPublisher` de Spring, RxJS |
| **Template Method** | Esqueleto fijo con pasos variables | `JdbcTemplate`, clases abstractas de proceso |
| **Chain of Responsibility** | Cadena de manejadores | Filtros de Spring Security, interceptores |
| **Command** | Encapsular una acción como objeto | Tareas encoladas, undo |
| **State** | Comportamiento según estado | Máquina de estados de un pedido |

**Strategy con Spring — el ejemplo que mejor queda en entrevista:**

```java
public interface ProcesadorPago {
    boolean soporta(MedioPago medio);
    Recibo procesar(Pago pago);
}

@Component class ProcesadorTarjeta implements ProcesadorPago { ... }
@Component class ProcesadorTransferencia implements ProcesadorPago { ... }

@Service
@RequiredArgsConstructor
public class PagoService {
    private final List<ProcesadorPago> procesadores;   // Spring inyecta todas

    public Recibo pagar(Pago pago) {
        return procesadores.stream()
            .filter(p -> p.soporta(pago.medio()))
            .findFirst()
            .orElseThrow(() -> new MedioNoSoportadoException(pago.medio()))
            .procesar(pago);
    }
}
```
> Valor que comunica: *"agregar un medio de pago nuevo es crear una clase; no toco el código existente"* → **principio abierto/cerrado**.

### 14.4 Patrones de arquitectura y microservicios 🎯

| Patrón | Qué resuelve |
|---|---|
| **Circuit Breaker** | Deja de llamar a un servicio caído para no propagar la falla (Resilience4j) |
| **Retry + Backoff** | Reintenta fallas transitorias con espera creciente y jitter |
| **Bulkhead** | Aísla recursos para que un servicio lento no consuma todos los hilos |
| **API Gateway** | Punto único de entrada: auth, rate limiting, routing |
| **Saga** | Transacciones distribuidas por pasos con compensación (no hay 2PC) |
| **Outbox** | Publicar eventos de forma consistente con la escritura en BD |
| **CQRS** | Separar el modelo de escritura del de lectura |
| **Event Sourcing** | Guardar los eventos, no solo el estado final |
| **Sidecar / Ambassador** | Funcionalidad transversal junto al contenedor principal |
| **Strangler Fig** | Migrar un monolito por partes sin un big-bang |
| **Idempotency Key** | Evitar efectos duplicados en reintentos |

```java
@CircuitBreaker(name = "bancoApi", fallbackMethod = "fallback")
@Retry(name = "bancoApi")
public Saldo consultar(String cuenta) { return client.get(cuenta); }

private Saldo fallback(String cuenta, Throwable t) {
    return Saldo.noDisponible();   // degradación elegante
}
```

### 14.5 SOLID (te lo pueden pedir junto con patrones) 🎯
- **S**ingle Responsibility — una razón para cambiar.
- **O**pen/Closed — abierto a extensión, cerrado a modificación (Strategy).
- **L**iskov — un subtipo debe poder sustituir a su tipo base sin romper nada.
- **I**nterface Segregation — interfaces pequeñas y específicas.
- **D**ependency Inversion — depender de abstracciones, no de implementaciones (la base de la DI de Spring).

### 14.6 Anti-patrones que puedes nombrar
God Object, Anemic Domain Model, Singleton con estado mutable global, inyección por campo, `catch (Exception e) {}` vacío, *lasagna/spaghetti architecture*, microservicios distribuidos que comparten base de datos.

---

## 15. Arquitectura y buenas prácticas

### 15.1 REST bien hecho 🎯
- Sustantivos en plural: `/api/v1/pedidos/{id}/items`. Sin verbos en la URL.
- Verbos HTTP: `GET` (leer, seguro), `POST` (crear), `PUT` (reemplazar, idempotente), `PATCH` (parcial), `DELETE` (idempotente).
- Códigos: `200`, `201` + `Location`, `204`, `400`, `401`, `403`, `404`, `409` (conflicto), `422`, `429` (rate limit), `500`, `503`.
- Paginación (`?page=&size=` o cursor), filtros, ordenamiento.
- Versionado en la URL (`/v1/`) o por header; versiona antes de romper contratos.
- Errores consistentes (RFC 7807 *Problem Details*).
- **Idempotencia** en `POST` sensibles vía `Idempotency-Key`.

### 15.2 Observabilidad
Los tres pilares: **logs** (estructurados en JSON, con `traceId`), **métricas** (Micrometer/Prometheus: latencia p95/p99, tasa de error, throughput), **trazas** (OpenTelemetry a través de servicios). Alertas sobre SLO, no sobre CPU.

### 15.3 Rendimiento
Cachés (`@Cacheable`, Redis), paginación obligatoria, índices en BD, evitar N+1, compresión, CDN para estáticos, conexiones agrupadas (HikariCP), timeouts en **toda** llamada externa.

### 15.4 Calidad
Cobertura ≥ 80% con tests que valen (no tests triviales), PRs pequeños, revisión de código, análisis estático (SonarQube), escaneo de dependencias, logs sin datos personales, *feature flags* para desacoplar deploy de release.

---

## 16. Preguntas de entrevista y respuestas modelo

### 16.1 Estructura STAR para preguntas de experiencia 🎯
**S**ituación → **T**area → **A**cción → **R**esultado (con números).

> *"En un servicio de pedidos teníamos un endpoint con p95 de 3 segundos **(S)**. Me pidieron bajarlo sin cambiar el contrato **(T)**. Perfilé con Actuator, encontré un N+1 en el listado, lo resolví con `@EntityGraph` y agregué caché en el catálogo **(A)**. El p95 bajó a 400 ms y los timeouts del front desaparecieron **(R)**."*

Ten preparadas 4 historias: un problema técnico difícil, un conflicto con otra persona, un error que cometiste, y un logro del que estés orgulloso.

### 16.2 Banco de preguntas técnicas

**FullStack / generales**
- Recorre una petición desde el clic en Angular hasta la base de datos.
- ¿Cómo depuras un bug que solo ocurre en producción?
- ¿Qué haces si un endpoint se pone lento?

**Java**
- `==` vs `equals`; contrato `equals`/`hashCode`.
- Checked vs unchecked exceptions.
- `HashMap` por dentro; qué pasa si el `hashCode` es malo.
- Streams: intermedias vs terminales; `map` vs `flatMap`.
- Inmutabilidad y `record`.
- Garbage collection: generaciones, cuándo te preocupa.

**Spring**
- Cómo funciona la inyección por constructor y por qué es la preferida.
- `@Component` vs `@Service` vs `@Repository` (semántica + traducción de excepciones).
- Ciclo de vida de un bean; `@PostConstruct`.
- Por qué falla `@Transactional` en una llamada interna.
- Cómo manejas errores de forma global.

**Seguridad**
- Explica JWT y por qué no guardas datos sensibles en el payload.
- Diferencia OAuth2 / OIDC.
- Cómo revocas un JWT.
- CORS: qué es y cómo lo configuras bien.

**Bases de datos**
- Índices: cuándo ayudan y cuándo estorban.
- Transacciones y niveles de aislamiento; lectura sucia / no repetible / fantasma.
- Cuándo NoSQL en vez de SQL.

**Cloud / DevOps**
- Diferencia entre Cloud Run, Cloud Functions y GKE.
- Cómo despliegas sin downtime.
- Qué haces si un pod está en `CrashLoopBackOff`.

### 16.3 Preguntas que TÚ debes hacer (evalúan mucho esto) 🎯
- ¿Cómo está compuesto el equipo y cómo es el proceso de trabajo (sprints, refinement)?
- ¿Cómo es el pipeline de despliegue? ¿Con qué frecuencia van a producción?
- ¿Qué porcentaje del trabajo es feature nueva vs mantención de legado?
- ¿Cómo miden el éxito de esta posición en los primeros 3 y 6 meses?
- ¿Hay turnos de soporte / on-call?
- ¿Cuál es el mayor desafío técnico del equipo hoy?
- ¿Cuáles son los pasos siguientes del proceso y en qué plazo?

### 16.4 Banderas rojas a evitar en tus respuestas
Hablar mal de empleadores anteriores, responder "no sé" y detenerse (mejor: *"no lo he usado en producción, pero el concepto es X y lo abordaría así"*), inventar experiencia (se detecta al profundizar), respuestas de una palabra, o monólogos de 10 minutos.

---

## 17. Negociación salarial

> Apunte del temario: **Sueldo 2.0 – 2.3**. Tu rango objetivo es **2,0 a 2,3 millones** (líquidos, salvo que acuerden otra cosa). Aclara siempre **líquido vs bruto**: es el error más caro.

### 17.1 Principios
1. **No des el número primero si puedes evitarlo.** Devuelve la pregunta: *"¿Cuál es el rango presupuestado para la posición?"*
2. Si insisten, **da un rango cuyo piso ya te sirva**: nunca menciones un número que no aceptarías.
3. Ancla **arriba** de tu objetivo: si quieres 2,2, pide 2,3–2,5.
4. Negocia el **paquete completo**, no solo el sueldo base.

### 17.2 Guiones listos 🎯

**Te preguntan temprano por la expectativa:**
> *"Antes de dar un número me gustaría entender bien el alcance del rol. ¿Manejan un rango definido para esta posición? Con eso puedo decirte si estamos alineados."*

**Insisten:**
> *"Considerando mi experiencia en Java/Spring, Angular y GCP, y el alcance fullstack de la posición, mi expectativa está en el rango de **2,3 a 2,5 millones líquidos**, con flexibilidad según el paquete completo: modalidad, bonos y desarrollo profesional."*

**La oferta llega bajo (ej. 1,9):**
> *"Agradezco la oferta y el rol me interesa mucho. Para tomar la decisión con tranquilidad necesito acercarme a **2,3**. Considerando que el cargo incluye backend, frontend y despliegue en GCP, ¿existe espacio para ajustar la base, o podríamos compensar con un bono de desempeño o una revisión a los 6 meses?"*

**Te preguntan tu sueldo actual:**
> *"Prefiero enfocar la conversación en el valor del rol y el rango de mercado para esta posición más que en mi historial salarial."*

**Cierre cuando te satisface:**
> *"Con esos números estoy conforme. ¿Me lo pueden enviar por escrito con fecha de inicio, modalidad y detalle de beneficios para confirmar formalmente?"*

### 17.3 Variables negociables además del sueldo
Bono anual o por desempeño, días de vacaciones adicionales, modalidad remota/híbrida, horario flexible, presupuesto de capacitación y certificaciones (GCP Professional Cloud Developer), seguro complementario, equipo de trabajo, revisión salarial a los 6 meses, título del cargo (impacta tu siguiente salto).

### 17.4 Errores caros
- Confundir líquido con bruto (la diferencia es ~20% o más).
- Aceptar en el momento por nervios: *"Déjame revisarlo con calma, te respondo mañana"* siempre es aceptable.
- Dar un número sin saber el alcance del cargo.
- Negociar antes de tener la oferta (pierdes apalancamiento).
- No pedir la oferta por escrito.

### 17.5 Preparación previa
Ten a mano: tu piso real (bajo el cual dices que no), tu objetivo (2,2–2,3), tu techo creíble (2,5), y **tres logros con números** que justifiquen el rango.

---

## 18. Plan de repaso de 7 días

| Día | Foco | Entregable de práctica |
|---|---|---|
| 1 | **JWT + OAuth2 + Spring Security** (prioridad máxima) | Dibujar el flujo Authorization Code + PKCE de memoria; escribir un `SecurityFilterChain` sin mirar |
| 2 | Spring Boot + JPA + patrones de diseño | Implementar Strategy con inyección de `List<T>`; explicar N+1 y su fix |
| 3 | Programación funcional + concurrencia + Virtual Threads | Resolver 5 ejercicios de Streams; explicar pinning y por qué no se hace pool |
| 4 | GCP: Pub/Sub, Cloud Functions, Firestore + Kafka | Diseñar un flujo evento→función→Firestore; comparar Kafka vs Pub/Sub en voz alta |
| 5 | Docker + Kubernetes + CI/CD | Escribir un Dockerfile multi-stage y un Deployment de memoria; explicar liveness vs readiness |
| 6 | Angular + agilidad | Explicar `switchMap` vs `mergeMap`, OnPush, interceptor JWT; repasar ceremonias |
| 7 | Simulacro completo + negociación | Responder 20 preguntas en voz alta cronometrado; ensayar los guiones de sueldo |

**Método:** cada tema no está listo hasta que puedas **explicarlo en voz alta en 2 minutos sin leer**. Grábate: si dudas, vuelve a esa sección.

---

## 19. Cheat sheets

### 19.1 Respuestas de 30 segundos

| Pregunta | Respuesta comprimida |
|---|---|
| ¿Qué es CI/CD? | Integrar y validar cada commit automáticamente; tener siempre un artefacto desplegable; y opcionalmente desplegarlo solo si pasa las puertas de calidad. |
| ¿Qué es un JWT? | Un token firmado con tres partes (header, payload, firma) que transporta claims verificables sin consultar al servidor. Firmado, no cifrado. |
| ¿OAuth2 vs OIDC? | OAuth2 autoriza acceso a recursos; OIDC agrega autenticación e `id_token` sobre OAuth2. |
| ¿Qué es Pub/Sub? | Mensajería gestionada de GCP: publishers a un topic, subscriptions que reciben copias; at-least-once, por lo que el consumidor debe ser idempotente. |
| ¿Virtual Threads? | Hilos livianos de la JVM (Java 21) que permiten código bloqueante con escalabilidad reactiva; uno por tarea, sin pool, ideales para I/O. |
| ¿Docker vs VM? | El contenedor comparte kernel y aísla procesos; la VM emula hardware con su propio SO. Segundos y MBs vs minutos y GBs. |
| ¿Para qué Kubernetes? | Orquestar contenedores: escalado, autorreparación, descubrimiento y despliegues sin downtime de forma declarativa. |
| ¿Liveness vs readiness? | Liveness reinicia el pod; readiness lo saca del balanceador sin reiniciarlo. |
| ¿SQL o NoSQL? | SQL para datos relacionales, integridad y consultas variadas; NoSQL para escala, esquema flexible y patrones de consulta conocidos de antemano. |
| ¿Qué patrones usas? | Strategy para algoritmos intercambiables, Builder para objetos complejos y Circuit Breaker para resiliencia — con ejemplos reales. |
| ¿`switchMap` vs `mergeMap`? | `switchMap` cancela la petición anterior (búsquedas); `mergeMap` las ejecuta todas en paralelo. |
| ¿Qué es la daily? | Sincronización de 15 minutos del equipo para alinear el trabajo del día y levantar bloqueos, no un reporte de estado al jefe. |

### 19.2 Comandos rápidos
```bash
# Docker
docker build -t app:1.0 . && docker run -p 8080:8080 app:1.0
docker logs -f <id>   |   docker exec -it <id> sh

# Kubernetes
kubectl get pods -n prod
kubectl describe pod <pod>   |   kubectl logs -f <pod> --previous
kubectl rollout undo deployment/api

# GCP
gcloud pubsub topics publish mi-topic --message='{"id":1}'
gcloud run deploy api --image gcr.io/proj/api:sha --region us-central1
gcloud functions deploy procesar --trigger-topic mi-topic

# Maven
mvn clean verify   |   mvn spring-boot:run -Dspring-boot.run.profiles=dev
```

### 19.3 Checklist antes de la entrevista
- [ ] Puedo dibujar el flujo OAuth2/JWT en una hoja.
- [ ] Tengo 3 patrones de diseño con ejemplo real propio.
- [ ] Tengo 4 historias STAR listas.
- [ ] Puedo explicar la diferencia entre CI, Delivery y Deployment.
- [ ] Puedo explicar Virtual Threads y su trampa (pinning, no hacer pool).
- [ ] Sé decir mi rango salarial sin titubear, aclarando líquido.
- [ ] Tengo 5 preguntas preparadas para ellos.
- [ ] Probé cámara, micrófono y conexión.

---

## Anexo: cómo continuar este documento con otra IA

Pega este prompt junto con el archivo `guia-entrevista.md`:

> "Este es mi documento de repaso para una entrevista técnica FullStack (Java/Spring Boot, Angular, GCP, Docker/Kubernetes, CI/CD, agilidad, seguridad JWT/OAuth2). Quiero que lo continúes manteniendo exactamente el mismo formato: secciones numeradas, tablas comparativas, bloques de código comentados, marcador 🎯 para lo más preguntado, y una subsección de 'preguntas típicas' al final de cada tema. Amplía [TEMA] con el mismo nivel de detalle y no reescribas lo ya existente."

Temas naturales para ampliar más adelante: pruebas de rendimiento, arquitectura hexagonal en detalle, GraphQL, WebSockets, observabilidad con OpenTelemetry, Terraform, algoritmos y estructuras de datos para la ronda de live coding, y system design (diseñar un acortador de URLs, un sistema de notificaciones, un checkout).

---

## Anexo B: comandos del Gem de repaso

Modos de operación del Gem **Sparring Técnico FullStack** (Gemini). Referencia detallada en `comandos-gem.md`; configuración del Gem en `gem-gemini.md`.

| Comando | Para qué sirve | Cuándo usarlo |
|---|---|---|
| `/diagnostico` | 8 preguntas de distintos temas + plan priorizado | Al empezar, o cada 3–4 días para medir avance |
| `/simulacro [tema] [nivel]` | Entrevista simulada, una pregunta a la vez, con nota y feedback | Cuando ya repasaste y quieres presión real |
| `/repasar <tema>` | Explicación completa con código y preguntas típicas | Tema que no manejas o que viste hace tiempo |
| `/profundizar <tema>` | Trade-offs, casos borde, qué falla en producción | Tema que ya entiendes y quieres defender a fondo |
| `/ampliar-guia <tema>` | Sección nueva en Markdown para pegar en este documento | Cuando detectas un hueco en la guía |
| `/flashcards <tema> [n]` | Tarjetas pregunta/respuesta de 3 líneas | Repaso rápido, metro, día previo |
| `/codigo <ejercicio>` | Live coding con solución comparada | Preparar la ronda de código |
| `/design <problema>` | System design guiado | Entrevistas de arquitectura o cargos senior |
| `/star <situación>` | Tu experiencia convertida en respuesta STAR con números | Preguntas de comportamiento |
| `/sueldo <situación>` | Guion textual de negociación, listo para decir | Antes de RRHH o al recibir una oferta |

### Rutinas

**Sesión de 30 minutos:** `/flashcards <tema> 10` → `/repasar <lo que fallaste>` → `/simulacro <ese tema>`.

**Día previo:** `/diagnostico` → `/flashcards seguridad 20` → `/sueldo` → `/simulacro` cronometrado.

**Al encontrar un hueco:** `/ampliar-guia <tema>` → pegar en `guia-entrevista.md` → `node build-html.js`.
