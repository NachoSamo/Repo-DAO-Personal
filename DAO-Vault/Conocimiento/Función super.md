---
tipo: concepto
materia: DAO
unidad: 5
tags: [poo, herencia, super]
---

# Función `super()`

A diferencia de `self` —que cada método recibe automáticamente como parámetro al invocarse sobre una instancia—, `super` **no es una referencia** disponible de antemano: es una **función incorporada** del lenguaje que hay que llamar explícitamente, con paréntesis, cada vez que se la necesita. Python no la expone como un miembro que las instancias reciban por pertenecer a una jerarquía de [[Herencia|herencia]].

Invocada sin argumentos dentro de un método de una clase derivada, `super()` construye y devuelve un objeto **proxy**: no guarda datos propios sino que delega la búsqueda de los miembros pedidos hacia la clase base, permitiendo acceder a los miembros heredados sin nombrar la base. Por eso `self` nunca se "llama" (ya está ahí) y `super()` sí.

## Cuándo usarla (y cuándo no)
Se usa a menudo de forma errónea para acceder a cualquier miembro de la base. Eso evidencia no haber entendido la herencia: **todo miembro de la base es heredado y accesible con `self`**.

El uso de `super()` se limita a un único escenario: cuando se **sobreescribió** un método en la derivada y se necesita invocar la versión de la base ([[Sobreescritura de métodos]]):
- `__init__`: al redefinirse en la derivada no se ejecuta automáticamente el de la base, así que hay que llamarlo con `super().__init__(...)` para completar la inicialización (ver [[Constructor]]).
- Cualquier otro método redefinido, como `__str__`: `super().__str__()` reutiliza la representación de la base y la extiende con los atributos nuevos.

```python
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)     # completa la inicialización heredada
        self.carrera = carrera

    def __str__(self):
        return f"{super().__str__()}, Carrera: {self.carrera}"   # reutiliza la de la base
```

## Por qué no `self` dentro de la redefinición
Si dentro de la propia redefinición se invocara el método con `self`, se iniciaría una **llamada recursiva** sobre sí misma. `super()` permite acceder a la versión original sin recursión:

```python
# Incorrecto: self.__str__() vuelve a ejecutar esta misma redefinición
# (recursión infinita)
def __str__(self):
    return f"{self.__str__()}, Carrera: {self.carrera}"
```

## Con el constructor
Los parámetros del constructor de la derivada normalmente no coinciden con los que se reenvían a la base: recibe además otros propios, y es responsabilidad de la derivada elegir cuáles van a `super().__init__()`. Ejemplo completo en [[Herencia]] (`Cliente`, `ClienteOnline`, `ClientePresencial`) y de `__str__` en [[Polimorfismo]] (`Persona`, `Estudiante`, `Profesor`).

## Conceptos relacionados
- [[Herencia]] — el contexto donde se usa
- [[Sobreescritura de métodos]] — la razón para necesitarla
- [[Constructor]] — `super().__init__()`
- [[Métodos mágicos]] — `__init__` y `__str__`
- [[Polimorfismo]]

## Visto en
- [[Unidad 5 - Herencia, polimorfismo y testing]] · [[semana5.pdf#page=4|semana5.pdf, §10.3.2 Función super (p. 4-5)]] · [[semana5.pdf#page=9|§11.1.3 Uso de super (p. 9-10)]]
