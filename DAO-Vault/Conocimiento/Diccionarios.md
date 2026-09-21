---
tipo: concepto
materia: DAO
unidad: 3
tags: [python, diccionarios, dict]
---

# Diccionarios (dict)

Estructura de pares **clave → valor** (arreglo asociativo). Búsqueda por clave en **O(1) promedio**, sin importar el tamaño. No admite claves duplicadas; desde Python 3.7 preserva el orden de inserción. La clave puede ser cualquier tipo válido (a diferencia del índice numérico de una [[Listas|lista]]), lo que evita tener que usar, por ejemplo, un DNI de 8 dígitos como índice de un arreglo gigante.

## Creación
1. `dict()` — vacío.
2. Enumeración: `{1: "Lunes", 2: "Martes"}`.
3. Comprensión de diccionarios (ver [[Comprensión de listas]]).

## Acceso
- `diccionario[clave]` — O(1); lanza `KeyError` si no existe (ver [[Excepciones]]).
- `get(clave, valor_defecto=None)` — no lanza error, devuelve `None` o el valor por defecto.
- `setdefault(clave, valor_defecto)` — devuelve el valor si existe, o lo crea con el valor por defecto si no.
- `len(diccionario)`.

## Inserción / borrado
- `diccionario[clave] = valor` — inserta o actualiza.
- `del diccionario[clave]` / `pop(clave, defecto)` — elimina una entrada.
- `clear()` — vacía el diccionario. `del diccionario` elimina la variable completa.

## Recorrido
- `keys()` — vista de claves (sin repetidos, operable como conjunto).
- `values()` — vista de valores (pueden repetirse).
- `items()` — vista de pares, desestructurable en el `for`:
```python
for numero, nombre in diccionario.items():
    print(f"El día {numero} se llama {nombre}")
```
Las vistas reflejan cambios posteriores del diccionario.

## Relacionado
- [[Conjuntos]] — misma familia, `keys()` se comporta como un conjunto
- [[Listas]] — contraste: índice numérico vs. clave arbitraria
- [[Excepciones]] — `KeyError`
- [[Composición]] — un diccionario puede ser la colección de la clase contenedora
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 3 - Archivos, colecciones avanzadas y excepciones]] · [[semana3.pdf#page=23|semana3.pdf, §4.2 Diccionarios (p. 23-27)]]
