---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, listas]
---

# Listas

[[Secuencias|Secuencia]] ordenada y **mutable**, definida con corchetes:
```python
lista1 = [1, 2, 3]
lista3 = [0] * 20   # 20 elementos, todos 0
```

## Operaciones habituales
- `append(x)` agrega al final.
- `remove(x)` elimina la primera aparición.
- `len(lista)` cantidad de elementos.
- `reverse()` invierte in-place.
- `sort()` ordena in-place.

## Funciones comunes sobre listas (patrón de la cátedra)
Los apuntes reutilizan un trío de funciones auxiliares en varios ejercicios (ver [[Funciones]]):
- `cantidad_menor(lista, techo)` / `cantidad_mayor(lista, piso)` — cuenta elementos que cumplen una comparación.
- `promedio(lista)` — retorna 0 si la lista está vacía.
- `existe(lista, buscado)` — búsqueda lineal, retorna `bool`.

Estas mismas funciones se reutilizan tanto en el ejercicio de temperaturas (memoria) como en la lectura de `numeros.txt` (ver [[Archivos]]), mostrando el mismo módulo `proceso_listas` compartido entre programas.

## Relacionado
- [[Secuencias]]
- [[Tuplas]] — equivalente inmutable
- [[Comprensión de listas]] — forma concisa de generar listas
- [[Archivos]] — listas cargadas desde archivos de texto
- [[Composición]] — una lista dentro de una clase contenedora
- [[Módulos y docstrings]] — el módulo compartido `proceso_listas`
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=27|semana1.pdf, §2.4 Listas (p. 27-28)]]
