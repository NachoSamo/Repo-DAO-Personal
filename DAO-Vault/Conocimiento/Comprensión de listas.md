---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, comprension-listas, list-comprehension]
---

# Comprensión de listas (list comprehension)

Sintaxis concisa para crear una lista a partir de una expresión y una iteración:
```python
nueva_lista = [expresión for elemento in secuencia]

cuadrados = [numero ** 2 for numero in numeros]
pares = [numero for numero in numeros if numero % 2 == 0]
```

Es la contraparte "sintáctica" de las funciones [[Filter, Map y Reduce|`filter` y `map`]] de la [[Programación funcional|programación funcional]]: donde `map`/`filter` reciben una función, la comprensión escribe la expresión y la condición inline.

También existe la variante para [[Conjuntos]] (comprensión de conjuntos, con `{}`) y para [[Diccionarios]] (comprensión de diccionarios, con `clave: valor`).

## Relacionado
- [[Listas]]
- [[Filter, Map y Reduce]]
- [[Conjuntos]]
- [[Diccionarios]]
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=28|semana1.pdf, §2.5 Generación de listas por comprensión (p. 28-29)]]
