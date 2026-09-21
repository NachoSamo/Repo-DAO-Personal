---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, tuplas]
---

# Tuplas

[[Secuencias|Secuencia]] ordenada e **inmutable**. Se define con paréntesis o simplemente separando por comas:
```python
tupla1 = (1, 2, 3)
tupla2 = "a", "b", "c"
```
No se pueden agregar, eliminar ni modificar elementos una vez creada. Útil para datos que no deben cambiar (coordenadas, registros fijos).

Cuando una [[Funciones|función]] retorna varios valores separados por coma, en realidad retorna una tupla.

## Desestructuración
Permite asignar varias variables a la vez desde una secuencia a la derecha:
```python
x, y = 23, 44
pre1, pre2, pre3 = [58, 22, 99]
a, b = b, a  # intercambio de variables sin auxiliar
```
Con `*` se recolecta el resto en una lista:
```python
nombre, apellido, *otros_datos = persona
```

## Ejemplo de aplicación: simulador de ruleta
La cátedra modela el paño de la ruleta como una lista de tuplas `(numero, color)`, indexando cada tupla por su propio número — ver también [[Listas]].

## Relacionado
- [[Secuencias]]
- [[Listas]] — equivalente mutable
- [[Funciones]] — retorno múltiple
- [[Recursividad]] — cálculo del color de la ruleta, cuyo paño se arma con tuplas
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=25|semana1.pdf, §2.3 Tuplas (p. 25-27)]]
