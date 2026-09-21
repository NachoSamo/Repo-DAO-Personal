---
tipo: concepto
materia: DAO
unidad: 3
tags: [python, conjuntos, sets]
---

# Conjuntos (set)

Colección sin duplicados, sin acceso indexado, con búsqueda de pertenencia en **O(1) promedio** (a diferencia de la búsqueda lineal en [[Listas]]/[[Tuplas]]).

## Creación
1. `set()` — conjunto vacío.
2. Enumeración: `{1, 2, 3}`.
3. Comprensión de conjuntos: `{random.randint(1,10000) for x in range(100)}` (ver [[Comprensión de listas]]).

## Inserción / eliminación
| Método | Efecto |
|---|---|
| `add(x)` | Agrega si no existe (sin error si ya está) |
| `update(iterable)` | Agrega todos los elementos de un iterable |
| `remove(x)` | Elimina; **error** si no existe |
| `discard(x)` | Elimina; sin error si no existe |
| `pop()` | Elimina y devuelve un elemento arbitrario |
| `clear()` | Vacía el conjunto |

## Recorrido
`for x in conjunto:` no respeta ningún orden garantizado. Para recorrer ordenado: `sorted(conjunto)` (devuelve una nueva lista, no modifica el conjunto).

## Operaciones de conjuntos
| Operación | Método | Variante in-place |
|---|---|---|
| Unión | `union()` | `update()` |
| Intersección | `intersection()` | `intersection_update()` |
| Diferencia | `difference()` | `difference_update()` |
| Diferencia simétrica | `symmetric_difference()` | `symmetric_difference_update()` |

Pertenencia: `x in conjunto` (O(1) promedio).

## Caso de uso: eliminar duplicados de una lista
```python
lista_sin_duplicados = list(set(lista))
```

## Relacionado
- [[Listas]] — contraste de eficiencia en búsquedas
- [[Comprensión de listas]]
- [[Diccionarios]] — misma familia de colecciones avanzadas
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 3 - Archivos, colecciones avanzadas y excepciones]] · [[semana3.pdf#page=17|semana3.pdf, §4.1 Conjuntos (p. 17-23)]]
