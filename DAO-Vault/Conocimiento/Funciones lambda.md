---
tipo: concepto
materia: DAO
unidad: 2
tags: [python, lambda, programacion-funcional]
---

# Funciones lambda

Funciones anónimas, pequeñas y de **una sola expresión** (no admiten múltiples líneas ni estructuras de control; para eso se necesita una función regular con `def`, ver [[Funciones]]).

```python
lambda argumentos: expresión

suma = lambda a, b: a + b
resta = lambda a, b: a - b
```

Reemplazan definiciones `def` triviales cuando la función se usa una sola vez o se pasa como argumento — típicamente a [[Filter, Map y Reduce|`filter`, `map` o `reduce`]]:
```python
es_par = lambda x: x % 2 == 0
pares = list(filter(es_par, numeros))
```

## Relacionado
- [[Programación funcional]] — funciones como valores
- [[Filter, Map y Reduce]] — principal consumidor de lambdas
- [[Funciones]]
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 2 - Programación funcional]] · [[semana2.pdf#page=4|semana2.pdf, §6.5 Funciones lambda (p. 4)]]
