---
tipo: concepto
materia: DAO
unidad: 4
tags: [poo, encapsulamiento, abstraccion]
---

# Encapsulamiento

Principio por el cual los objetos se comportan como **cápsulas**: unidades cerradas que protegen su implementación interna. Los detalles de la lógica, los atributos y los métodos de un objeto están ocultos y no son accesibles directamente desde otros objetos; en lugar de acceso directo, los objetos se comunican únicamente por **paso de mensajes** (ver [[Métodos]]). El objeto receptor atiende el mensaje, puede devolver un resultado o enviar otro mensaje a un tercero, y así los objetos colaboran.

La finalidad es proteger la integridad y coherencia del objeto y darle modularidad y flexibilidad al diseño: cada objeto puede cambiar su implementación sin afectar a los que interactúan con él. Al ocultar los detalles se refuerza la abstracción y se trabaja sobre la **interfaz pública** —los métodos pensados para que otros los usen—.

## Ventajas

### 1. Ocultamiento de la implementación
Un objeto puede modificar su forma de funcionar sin afectar a los demás. Ejemplo: un objeto responsable de guardar datos de forma persistente los guarda primero en un archivo de texto; en una versión futura pasa a una base de datos o a la nube. Los demás solo le envían mensajes ("guardá este dato", "recuperá el dato") y confían en su interfaz; no necesitan saber dónde se almacenan.

### 2. Validez del estado interno
Si los atributos estuvieran expuestos, cualquier objeto podría asignarles valores que violen las restricciones lógicas, y el objeto tendría que revalidarlos cada vez que opera. Por eso se recomienda ocultar los atributos y exigir que toda consulta o modificación pase por mensajes específicos: el objeto valida el nuevo valor en el momento y, si es inválido, lo rechaza —lanzando una [[Excepciones|excepción]], enviando un mensaje de error o tomando otra acción—.

- *Precio*: un producto no puede tener precio negativo; el intento de modificarlo va por un mensaje que verifica la regla.
- *Billetera*: cada persona tiene una billetera. Si otra persona pudiera acceder directo a ella, tomaría dinero sin permiso y el dueño podría decidir mal por no saber que su dinero disminuyó. Con encapsulamiento, el dinero solo se conoce si alguien pregunta y un préstamo solo ocurre si el dueño decide prestar.

Así el objeto garantiza tener siempre datos válidos y las validaciones y la lógica de negocio quedan concentradas dentro de él.

### 3. Atributos calculados
El objeto decide si mostrar o no los datos de sus atributos cuando se los consultan, y puede responder **calculándolos** a partir de otros atributos. Quien consulta no necesita saber si el dato está almacenado o se calcula al momento. Un `Circulo` con `radio` y `centro` puede exponer `diametro`, `superficie` y `circunferencia` sin almacenarlos:

```python
class Circulo:
    def __init__(self, radio, centro):
        self.radio = radio
        self.centro = centro

    def diametro(self):
        return self.radio * 2   # se calcula al consultar, no se guarda
```

## Cómo se implementa en Python
La forma preferida es con [[Propiedades|propiedades]] (`@property`): el cliente usa la sintaxis de un atributo pero por detrás se ejecutan métodos que pueden contener la lógica de consulta y validación.

## Conceptos relacionados
- [[Propiedades]] — `@property` y `@x.setter`
- [[Métodos]] — el canal de comunicación
- [[Programación orientada a objetos]] — uno de los cuatro principios
- [[Excepciones]] — rechazar valores inválidos
- [[Clases y objetos]] — atributos que se ocultan
- [[Testing unitario]] — las pruebas verifican que el encapsulamiento se mantenga

## Visto en
- [[Unidad 4 - Clases, encapsulamiento y composición]] · [[semana4.pdf#page=13|semana4.pdf, §8.1-§8.2 Encapsulamiento (p. 13-17)]]
