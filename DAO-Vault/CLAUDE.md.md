# CLAUDE.md — Harness para el vault de la materia

Este archivo vive en la raíz del vault y lo lee el agente (Claude Code CLI o Claudian) cuando Samo le pega un prompt que entrega la skill `toma-de-notas-en-clase` de Claude Desktop — ya sea del cierre de una clase en vivo o de la carga retroactiva de una clase vieja a partir de un `.docx`. En los dos casos el prompt tiene la misma forma (materia, fecha, unidad, temas, contenido y conceptos detectados) y este archivo define cómo distribuirlo en el vault sin depender de MCP.

Si en la misma conversación llegan varios prompts seguidos (por ejemplo, cargando varias clases viejas de una), aplicar este proceso para cada uno por separado: mostrar y confirmar antes de escribir uno, y recién ahí pasar al siguiente. No encadenar varias escrituras sin mostrar ninguna.

## Estructura fija del vault

Toda nota va a una de estas tres carpetas, nunca a la raíz ni a subcarpetas por tema (las carpetas no arman conexiones en el grafo, solo ordenan archivos — la red la arman los wikilinks):

- `Clases/` — una nota por clase.
- `Conocimiento/` — una nota por concepto.
- `Unidades/` — una nota hub por unidad.

## Qué hacer con cada prompt de cierre de clase

### 1. Nota de clase (`Clases/`)

- Crear `YYYY-MM-DD - <tema breve>.md` con el contenido sintetizado tal como llega en el prompt. El trabajo acá es de ubicación y enlace, no de edición de contenido: el prompt ya trae la síntesis final (la misma que el `.docx` entregado en Desktop), no se resume de nuevo ni se recorta.
- Frontmatter: `materia`, `fecha` (ISO `YYYY-MM-DD`), `tipo` (ej. `clase-teorica`, según indique el prompt), `unidad` (número o lista), `temas` (lista de conceptos con nombre propio), `tags` (incluyendo `#unidad/N` por cada unidad).
- Debajo del título, una línea `Unidad: [[Unidad N - <tema>]]` por cada unidad que toque.
- `[[wikilinks]]` en todos los conceptos con nombre propio listados en el prompt, no solo los centrales. No enlazar términos genéricos.

### 2. Notas de concepto (`Conocimiento/`)

Antes de crear una nota nueva para un concepto:

- Buscar en el vault (por nombre de archivo y encabezados) si ya existe con un nombre parecido: variaciones de tildación, singular/plural, sinónimos evidentes.
- **Si ya existe**: reusar exactamente esa forma en el wikilink de la nota de clase (ajustarlo si hace falta para que apunte al nombre real que ya está en el vault, nunca crear una variante). Actualizar la nota existente: agregar el link de la clase nueva bajo `## Visto en`, y ampliar la definición o `## Conceptos relacionados` solo si esta clase aportó algo que la nota todavía no dice. No reescribir lo que ya está bien.
- **Si no existe**: crearla con frontmatter (`tipo: concepto`, `materia`, `unidad`), una definición propia de 2 a 4 líneas armada a partir de lo que trae el prompt — autocontenida, entendible sin abrir la clase —, sección `## Conceptos relacionados` con wikilinks a conceptos derivados o vinculados mencionados junto a este, y sección `## Visto en` con el link a la clase.
- Ningún wikilink queda apuntando a una nota vacía o inexistente: todo concepto que se linkea desde la nota de clase termina con una nota real.

### 3. Nota hub de la unidad (`Unidades/`)

- Si no existe: crear `Unidad N - <tema breve>.md` con frontmatter (`tipo: unidad`, `materia`, `unidad`) y secciones `## Clases` y `## Conceptos`.
- Si existe: agregar el link de la clase nueva bajo `## Clases` y los conceptos nuevos bajo `## Conceptos`, sin duplicar los que ya estén.

## No perder información de la clase

El prompt que llega ya es la síntesis final, no un resumen para resumir de nuevo. La tarea es **distribuirla completa**, no condensarla más:

- Cada bloque temático del prompt queda reflejado en la nota de clase.
- Cada concepto con nombre propio mencionado llega a tener su nota de concepto (nueva o actualizada) con definición e información real, no solo el wikilink suelto.
- Un ejercicio resuelto paso a paso o una fórmula con su desarrollo, si vienen en el prompt, quedan completos en la nota de clase — no se recortan a una mención genérica.

Si algo del prompt es ambiguo para decidir en qué nota va o cómo redactarlo, preguntar antes de escribir en vez de decidir a criterio propio y arriesgar perder o distorsionar contenido.

## Antes de escribir

Mostrar todo lo que se va a crear o modificar — la nota de clase completa, y la lista de notas de concepto y hubs a crear/actualizar (para las nuevas, su definición; para las existentes, qué se les agrega) — y esperar confirmación antes de escribir ningún archivo.