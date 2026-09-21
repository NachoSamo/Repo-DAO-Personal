---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, operadores]
---

# Operadores

Un operador actúa sobre uno o más valores (constantes, variables o expresiones). La mayoría son binarios; existen algunos unarios y un único ternario.

## Aritméticos
`+ - * / // % **`
- `/` siempre retorna `float`; `//` trunca a `int`; `%` retorna el resto.
- `+` sobre cadenas concatena; `*` entre cadena y entero repite la cadena.
- Si se opera entre `int` y `float`, el resultado se promueve a `float`.

## Asignación
`= += -= *= /= **=` … combinan una operación aritmética con la asignación.

## Comparación
`== != > < >= <=`. Existe además el **operador ternario**, único en su tipo:

```python
saldo = "Acreedor" if importe > 0 else "Deudor"
```

## Lógicos
`and`, `or` (con cortocircuito), `not` (unario). Operan sobre valores de verdad, convirtiendo implícitamente tipos no booleanos (ver [[Tipos de datos]]#Conversión implícita a boolean).

## Combinación de condiciones (particularidad de Python)
Python permite encadenar comparaciones sobre la misma variable:
```python
if 0 < nota <= 10:   # equivalente a nota > 0 and nota <= 10
```
**Trampa habitual**: `if a and b > 5` NO verifica que ambas sean mayores a 5 (evalúa `a` como truthy/falsy); y `if a > b > 5` agrega una restricción extra (`b` mayor que 5 **y** `a` mayor que `b`) no solicitada.

## Relacionado
- [[Tipos de datos]]
- [[Estructuras condicionales]] — uso de operadores de comparación/lógicos en `if`
- [[Métodos mágicos]] — sobrecarga de operadores en clases propias
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=2|semana1.pdf, §1.2 Operadores (p. 2-4)]]
