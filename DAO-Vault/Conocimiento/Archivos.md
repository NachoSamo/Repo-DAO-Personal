---
tipo: concepto
materia: DAO
unidad: 3
tags: [python, archivos, io]
---

# Archivos

Mecanismo básico y universal de persistencia: cualquier programa que entienda el formato puede leer/escribir el archivo, a diferencia de una base de datos (más rápida, con seguridad y consistencia, pero específica de un sistema).

## Texto vs. binario
- **Texto**: secuencia de caracteres legibles (UTF-8, ASCII), delimitada por saltos de línea. Apto para datos legibles por humanos.
- **Binario**: representación no legible directamente, requiere un formato propio para delimitar los datos (números, imágenes, audio, etc.).

## Apertura y cierre
`open(nombre_archivo, modo)` devuelve un objeto archivo; `close()` libera el recurso y garantiza que las últimas escrituras se vuelquen a disco. Conviene mantener el archivo abierto el menor tiempo posible.

## Modos de apertura
| Modo | Descripción |
|---|---|
| `r` | Lectura (texto) |
| `w` | Escritura — crea o **trunca** el archivo existente |
| `x` | Escritura exclusiva — error si el archivo ya existe |
| `a` | Adjuntar (append) — escribe a continuación sin borrar |
| `r+` | Lectura y escritura |
| sufijo `b` | Modo binario (`rb`, `wb`, `xb`, `ab`, `r+b`) |

Por defecto (sin letras) el modo es `"rt"` (lectura de texto).

## Lectura de texto
- `read()` — todo el contenido en un solo `str`. Simple pero carga todo en memoria.
- `readline()` — una línea por llamada; ideal para archivos grandes (poca memoria). Devuelve `""` al llegar al final.
- `readlines()` — todas las líneas como lista de `str`; ocupa más memoria que `readline`.

```python
archivo = open("datos.txt")
linea = archivo.readline()
while linea:
    print(linea)
    linea = archivo.readline()
archivo.close()
```

## Escritura de texto
- `write(cadena)` — no agrega `\n` automáticamente.
- `writelines(lista)` — igual, sin saltos de línea automáticos; el programador debe incluirlos.

## Patrón `with`
El ejercicio de `tips.csv` abre el archivo con `with open(...) as file:`, que cierra el archivo automáticamente al salir del bloque (alternativa más segura a llamar `close()` manualmente).

## Casos de la cátedra
- **`numeros.txt`**: lectura línea a línea con `readline()`, conversión a `int` y reutilización de las funciones de [[Listas]] (`promedio`, `cantidad_mayor`).
- **`cp.csv`**: lectura con `readlines()`, cada línea se separa con `split(";")` y se guarda como [[Tuplas|tupla]] `(provincia, código, nombre)` — ver [[Cadenas]] para `split`.
- **`tips.csv`**: recorrido directo del objeto archivo con `for fila in file:` (equivalente a `readline` en bucle), acumulando estadísticas en variables y una lista de 4 posiciones.

## Relacionado
- [[Cadenas]] — `split()` para parsear líneas
- [[Listas]] / [[Tuplas]] — estructuras donde se cargan los datos leídos
- [[Excepciones]] — `FileNotFoundError` al abrir un archivo inexistente
- [[Módulos y docstrings]] — el ejercicio de `numeros.txt` reutiliza `proceso_listas`
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 3 - Archivos, colecciones avanzadas y excepciones]] · [[semana3.pdf#page=1|semana3.pdf, cap. 3 Archivos (p. 1-16)]]
