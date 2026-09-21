---
tipo: concepto
materia: DAO
unidad: 4
tags: [poo, metodos, self, paso-de-mensajes]
---

# Métodos

La POO propone construir programas a partir de la interacción entre objetos: cuando un objeto envía un **mensaje** a otro le está pidiendo que realice una acción o que informe algo (*paso de mensajes*). El objeto receptor atiende el mensaje ejecutando el método correspondiente. Los **métodos** son las funciones asociadas a un objeto que definen su comportamiento y permiten que otros objetos interactúen con él; pueden recibir parámetros, acceder a los atributos del objeto y devolver una respuesta.

## Sintaxis
Se agregan dentro del bloque `class` con `def`, y su primer parámetro es `self` (por convención), una referencia al propio objeto que recibe el mensaje y que le permite acceder a sus atributos y otros métodos:

```python
class Persona:
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
```

## Enviar un mensaje
Se usa un punto seguido del nombre del método con paréntesis. En la lista de parámetros **no se incluye `self`**: se completa implícitamente.

```python
per = Persona(123, "Juan", "Perez", 20)
print(per.nombre_completo())
```

El operador punto recorre la "flecha" de la [[Referencias|referencia]] hasta el objeto apuntado y es a ese objeto al que se le envía el mensaje.

## Referencias vacías
Si la referencia a la que se envía el mensaje está vacía o vale `None`, se produce un error: no hay ningún objeto al que pedirle nada. El programador debe garantizar que no esté vacía, por lo general con un condicional antes de enviar el mensaje:

```python
if per is not None:
    print(per.nombre_completo())
```

## Colaboración entre objetos
Un objeto puede necesitar la ayuda de otros para cumplir su objetivo: dentro de un método puede acceder a otros objetos, enviarles mensajes (con los parámetros que necesiten), esperar sus respuestas y usarlas para armar la respuesta al mensaje original.

## Conceptos relacionados
- [[Referencias]] — el operador punto sigue la flecha
- [[Constructor]] — el primer método que se ejecuta
- [[Encapsulamiento]] — los objetos solo se comunican por mensajes
- [[Métodos mágicos]] — métodos invocados implícitamente
- [[Funciones]] — un método es una función con `self`
- [[Programación orientada a objetos]]

## Visto en
- [[Unidad 4 - Clases, encapsulamiento y composición]] · [[semana4.pdf#page=10|semana4.pdf, §7.6 Métodos (p. 10-12)]]
