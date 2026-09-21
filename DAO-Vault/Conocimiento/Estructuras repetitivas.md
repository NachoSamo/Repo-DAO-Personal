---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, bucles, repetitivas]
---

# Estructuras repetitivas

## for
Itera sobre cualquier [[Secuencias|secuencia]] (rango, lista, tupla, diccionario), entregando cada elemento en la variable de iteración.
```python
for fruta in frutas:
    print(fruta)
```

## while
Se repite mientras la condición sea verdadera; usado cuando no se conoce de antemano la cantidad de iteraciones (p. ej. procesar los dígitos de un número usando `%` y `//`, ver [[Operadores]]).

## Saltos: break, continue
- `break` corta el bucle más interno.
- `continue` salta a la siguiente iteración sin ejecutar el resto del bloque.

## Cláusula else en bucles
Se ejecuta solo si el bucle terminó **sin** interrupción por `break`. Patrón típico: búsqueda con bandera implícita (buscar una letra en un texto y usar `else` para el caso "no encontrado").

## Validación de entrada (patrón recurrente)
Ejercicios de la cátedra (estación de servicio, temperaturas) resuelven la validación de un `input()` con un `while` que repite la pregunta hasta que el valor entra en rango — ver también [[Funciones]] (`ingresar_numero_entre`).

## Relacionado
- [[Estructuras condicionales]]
- [[Funciones]] — funciones auxiliares de validación reutilizables
- [[Secuencias]]
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=7|semana1.pdf, §1.4 Estructuras repetitivas (p. 7-10)]]
