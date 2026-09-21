---
tipo: concepto
materia: DAO
unidad: 2
tags: [python, filter, map, reduce, programacion-funcional]
---

# Filter, Map y Reduce

Funciones de orden superior ([[Programación funcional]]) que operan sobre [[Secuencias|secuencias]], normalmente combinadas con [[Funciones lambda|lambdas]].

## filter
Conserva solo los elementos para los que la función pasada devuelve un valor verdadero. Retorna un iterador — se convierte con `list()` o `set()`.
```python
es_par = lambda x: x % 2 == 0
pares = list(filter(es_par, numeros))
```
Equivalente a una [[Comprensión de listas|comprensión de listas]] con `if`.

## map
Genera una nueva secuencia aplicando una función a cada elemento.
```python
cuadrados = list(map(lambda x: x ** 2, numeros))
```
Equivalente a una comprensión de listas sin condición.

## reduce
Reduce toda la secuencia a un único valor, aplicando una función de **dos parámetros** de forma acumulativa (par de elementos → resultado → siguiente elemento…). Requiere `from functools import reduce` (fue movida fuera de los built-ins).
```python
from functools import reduce
total = reduce(suma, [23, 6, 9])  # 38
```

## Relacionado
- [[Comprensión de listas]] — alternativa sintáctica a `filter`/`map`
- [[Funciones lambda]]
- [[Programación funcional]]
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 2 - Programación funcional]] · [[semana2.pdf#page=5|semana2.pdf, §6.6 Secuencias y operaciones funcionales (p. 5-6)]]
