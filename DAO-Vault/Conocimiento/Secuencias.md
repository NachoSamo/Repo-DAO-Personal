---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, secuencias]
---

# Secuencias

Concepto general que engloba a [[Cadenas]], [[Tuplas]] y [[Listas]] (y `range`): almacenan varios datos bajo un único identificador y son recorribles con `for`.

## Tamaño
`len(secuencia)` retorna la cantidad de elementos.

## Acceso indexado
`secuencia[i]` — índices desde 0; índices negativos cuentan desde el final (`-1` es el último).

## Rebanadas (slicing)
`secuencia[inicio:fin:salto]` — el corte incluye `inicio` pero excluye `fin`. Sin argumentos, `inicio=0` y `fin=último`. Un salto negativo recorre hacia atrás; `secuencia[::-1]` invierte la secuencia. El resultado es siempre una **nueva** secuencia (no modifica la original).

```python
titulo = "Paisaje"
titulo[1:3]    # "ai"
titulo[::2]    # "Piae"
titulo[::-1]   # "ejasiaP"
```

## Relacionado
- [[Cadenas]]
- [[Tuplas]]
- [[Listas]]
- [[Comprensión de listas]]
- [[Estructuras repetitivas]] — recorrido con `for`
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=21|semana1.pdf, §2.1 Introducción (p. 21-22)]]
