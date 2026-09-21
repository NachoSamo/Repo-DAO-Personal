---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, tipos-de-datos]
---

# Tipos de datos

Python ofrece tipos de datos agrupados por categoría:

| Categoría | Tipo | Nombre | Uso |
|---|---|---|---|
| Texto | Cadena | `str` | Cadenas de caracteres de longitud arbitraria |
| Numérico | Entero | `int` | Números enteros |
| Numérico | Flotante | `float` | Números con punto flotante |
| Numérico | Complejo | `complex` | Números complejos |
| Lógico | Booleano | `bool` | Valores de verdad |
| Secuencia | Tupla | `tuple` | Secuencia inmutable |
| Secuencia | Lista | `list` | Secuencia mutable |
| Secuencia | Rango | `range` | Secuencia inmutable de enteros |
| Conjunto | Conjunto | `set` | Valores sin repetición, búsqueda rápida |
| Asociación | Diccionario | `dict` | Pares clave/valor |
| Vacío | Sin tipo | `None` | Variable sin valor ni tipo |

## Conversión implícita a boolean (truthiness)
Todo valor puede evaluarse como verdadero (*truthy*) o falso (*falsy*). Se considera **falsy** todo dato "vacío": `0`, `""`, `None`, secuencias/estructuras vacías. El resto es *truthy*. Ver uso idiomático en [[Estructuras condicionales]].

## Relacionado
- [[Operadores]] — manipulan estos tipos
- [[Secuencias]] — desarrollo de tupla, lista y rango
- [[Conjuntos]] y [[Diccionarios]] — colecciones avanzadas
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=1|semana1.pdf, §1.1 Tipos de datos (p. 1)]] · [[semana1.pdf#page=6|§1.3.3 Conversiones a boolean (p. 6)]]
