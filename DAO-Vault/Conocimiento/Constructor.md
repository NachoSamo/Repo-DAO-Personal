---
tipo: concepto
materia: DAO
unidad: 4
tags: [poo, constructor, init, self]
---

# Constructor

El método constructor se llama `__init__`. Para funcionar requiere recibir como primer parámetro formal una variable que referencia al objeto que se está construyendo; puede tener cualquier nombre válido, pero la convención es `self`. Su uso más habitual es **asignar valores iniciales a los atributos**, ya sea recibidos como parámetros o asignados en forma arbitraria.

Una clase solo puede tener **un único constructor**, pero se pueden dar valores por defecto a los parámetros (ver [[Funciones]]) para que al crear el objeto se indiquen valores concretos o se usen los predeterminados.

```python
class Persona:
    def __init__(self, documento=0, nombre="No", apellido="No", edad=0):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
```

## Cómo se instancia
No se invoca `__init__` de forma explícita: se escribe el nombre de la clase seguido de paréntesis con los parámetros. El primer parámetro (`self`) **no se envía**: llega solo al constructor, referenciando al objeto que se está creando.

```python
# Los atributos se inicializan con valores por defecto
a = Persona()

# Los atributos se inicializan con los valores indicados
b = Persona(1234, "Juan", "Perez", 23)

# documento y apellido con los valores enviados, el resto por defecto
c = Persona(documento=1234, apellido="Castro")
```

`__init__` es un [[Métodos mágicos|método mágico]]: no se llama por su nombre, sino que Python lo ejecuta automáticamente al crear la instancia.

## En clases derivadas
El constructor de una clase derivada recibe parámetros propios y heredados, y reenvía a la base solo los que le corresponden con `super().__init__(...)`. Ver [[Herencia]] y [[Función super]].

## Conceptos relacionados
- [[Clases y objetos]] — donde se definen los atributos
- [[Métodos mágicos]] — `__init__` es el más conocido
- [[Métodos]] — `self` como primer parámetro
- [[Función super]] — invocar el constructor de la base
- [[Composición]] — el constructor decide qué partes recibe o crea

## Visto en
- [[Unidad 4 - Clases, encapsulamiento y composición]] · [[semana4.pdf#page=6|semana4.pdf, §7.4 Constructor (p. 6-8)]]
