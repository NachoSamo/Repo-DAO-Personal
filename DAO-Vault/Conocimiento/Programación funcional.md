---
tipo: concepto
materia: DAO
unidad: 2
tags: [python, programacion-funcional, paradigmas]
---

# Programación funcional

Uno de los paradigmas de programación (junto al estructurado y al orientado a objetos). Pocos lenguajes son "puros" funcionales, pero lenguajes de uso cotidiano (Python, Java, C#, JavaScript) incorporan elementos de este paradigma gracias a tratar la **función como un tipo de dato**: una variable puede almacenar código ejecutable, no solo un valor.

```python
imprimir = print          # sin paréntesis: no se invoca, se referencia
imprimir("Hola, mundo!")  # ahora sí se ejecuta
```

## Funciones de orden superior
Son [[Funciones|funciones]] o métodos que reciben una función como parámetro y/o retornan una función. Permiten que un método ejecute un comportamiento sin conocer su implementación exacta.

## Colecciones de funciones
Una lista o diccionario puede almacenar funciones como elementos, indexándolas por una clave (p. ej. una calculadora que selecciona `suma`, `resta`, `multiplicacion`, `division` según la opción de un menú):
```python
operaciones = [None, suma, resta, multiplicacion, division]
resultado = operaciones[opcion](a, b)
```

## Relacionado
- [[Funciones lambda]] — forma compacta de definir estas funciones
- [[Filter, Map y Reduce]] — funciones de orden superior sobre [[Secuencias|secuencias]]
- [[Funciones]] — base de `def`, parámetros y retorno
- [[Programación orientada a objetos]] — el otro paradigma de la cátedra, donde las variables contienen objetos
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 2 - Programación funcional]] · [[semana2.pdf#page=1|semana2.pdf, §6.1-§6.4 (p. 1-3)]]
