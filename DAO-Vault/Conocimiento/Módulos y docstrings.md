---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, modulos, docstrings, import]
---

# Módulos y docstrings

## Módulos
Un módulo es un archivo `.py` cuyas [[Funciones|funciones]] (y clases) se reutilizan desde otros archivos con `import`. En los ejercicios de la cátedra los programas se parten así:
- `validacion.py` — `ingresar_numero_entre(mensaje, minimo, maximo)` repite el `input` hasta que el valor esté en rango.
- `proceso_listas.py` — `cantidad_menor`, `cantidad_mayor`, `promedio`, `existe` (ver [[Listas]]).
- `temperaturas.py` — el programa; importa los otros dos:

```python
from validacion import *
from proceso_listas import *
```

El mismo módulo `proceso_listas` se reutiliza en el ejercicio de `numeros.txt` (ver [[Archivos]]). Las clases se organizan igual: una clase por archivo con el mismo nombre (`persona.py`) importada con `from persona import *` — ver [[Clases y objetos]].

## El bloque `if __name__ == "__main__"`
La lógica principal se escribe en una función `principal()` y al final del archivo:

```python
def principal():
    temperaturas = cargar_temperaturas()
    calcular(temperaturas)

if __name__ == "__main__":
    principal()
```

`__name__` vale `"__main__"` solo cuando el archivo se ejecuta directamente; si otro archivo lo importa, el bloque no corre y solo quedan disponibles sus definiciones.

## Docstrings
Cadena de triple comilla justo debajo del `def` que documenta la función. La cátedra usa el estilo con campos `:param:`, `:type:`, `:returns:` y `:rtype:`:

```python
def cantidad_menor(lista, techo):
    """
    Cuenta los elementos de una lista que sean menores a un tope
    :param lista: lista de valores
    :type lista: lista de datos que soporte comparación por menor
    :param techo: valor máximo para filtrar
    :type techo: el mismo de los elementos de la lista
    :returns: la cantidad de elementos cuyo valor sea menor al techo
    :rtype: entero
    """
    c = 0
    for x in lista:
        if x < techo:
            c += 1
    return c
```

## Librerías usadas en los ejemplos
- `random` (estándar): `random.randint(0, 36)` en la ruleta ([[Recursividad]]).
- `rich` (de terceros, se instala con `pip install rich`): salida de consola con colores — `Console`, `Panel`, `Table` — usada en la ruleta y en `tips.py` ([[Archivos]]).
- Más adelante: `functools` ([[Filter, Map y Reduce]]), `abc` ([[Clases abstractas]]) y `pytest` ([[Pytest]]).

## Conceptos relacionados
- [[Funciones]] — lo que se documenta y se reutiliza entre módulos
- [[Listas]] — `proceso_listas` es el módulo compartido
- [[Archivos]] — reutiliza `proceso_listas`
- [[Clases y objetos]] — una clase por archivo
- [[Pytest]] — las pruebas importan el módulo a probar (`from numeros import Numeros`)

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=16|semana1.pdf, §1.6.2 Temperaturas (p. 16-19)]]
