---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, funciones]
---

# Funciones

```python
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
```
Sin `return` (o con `return` sin valor), la función retorna `None`.

## Tipos de parámetros
- **Posicionales**: obligatorios, en el orden definido.
- **Con valor predeterminado**: `def saludar(nombre, edad=30):` — opcionales.
- **De palabra clave**: `saludar(edad=40, nombre="Carlos")` — se pueden reordenar.
- **Variables (`*args`)**: se agrupan en una tupla.
- **Palabra clave variables (`**kwargs`)**: se agrupan en un diccionario.

## Retorno múltiple
Una función puede retornar varios valores separados por coma; en realidad retorna una [[Tuplas|tupla]], que se puede desestructurar al recibirla:
```python
def promedio_suma(numeros):
    ...
    return promedio, suma

promedio, suma = promedio_suma(lista)
```

## Funciones como datos
En Python una función es también un valor: puede asignarse a una variable, pasarse como parámetro o guardarse en una lista/diccionario. Esta idea es la base de la [[Programación funcional]].

## Relacionado
- [[Estructuras repetitivas]] — funciones de validación reutilizadas en bucles
- [[Programación funcional]] — funciones de orden superior, [[Funciones lambda]]
- [[Listas]] — funciones que reciben y devuelven listas (`cantidad_menor`, `promedio`, `existe`)
- [[Recursividad]] — una función que se llama a sí misma
- [[Módulos y docstrings]] — reutilizar funciones entre archivos y documentarlas
- [[Métodos]] — en POO, una función asociada a un objeto
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=10|semana1.pdf, §1.5 Funciones (p. 10-13)]]
