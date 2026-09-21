---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, cadenas, strings]
---

# Cadenas (str)

Secuencia de caracteres ([[Secuencias]]), inmutable, delimitada por comillas simples o dobles.

## Operaciones básicas
- `+` concatena, `*` repite (`"A" * 10` → `AAAAAAAAAA`).
- Acceso indexado y rebanadas igual que cualquier [[Secuencias|secuencia]].
- `upper()`, `lower()`.

## Otros métodos frecuentes
| Método | Uso |
|---|---|
| `startswith` / `endswith` | Verifica inicio/fin |
| `find` | Posición de una subcadena |
| `join` | Concatena una secuencia con delimitador |
| `replace` | Reemplaza subcadenas |
| `strip` | Elimina espacios al inicio/fin |
| `split` | Divide en una lista según delimitador |

## Cadenas con formato (f-strings)
```python
saludo = f"Hola {apellido}, {nombre}! ¿cómo estás?"
```
Cada *placeholder* admite alineación y ancho: `{expresion:direccion ancho}`.
- `>` derecha, `<` izquierda, `^` centrado.
- Cadenas se alinean a la izquierda por defecto; números a la derecha.
- Para `float`: `{variable:8.2f}` (ancho total 8, 2 decimales).

## Relacionado
- [[Secuencias]]
- [[Archivos]] — `split(";")` / `split(",")` para parsear líneas de CSV
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=23|semana1.pdf, §2.2 Cadenas (p. 23-25)]]
