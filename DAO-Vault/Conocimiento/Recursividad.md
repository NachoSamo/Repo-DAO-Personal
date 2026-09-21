---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, recursividad, funciones]
---

# Recursividad

Técnica en la que una [[Funciones|función]] se llama a sí misma para resolver un subproblema más chico, hasta llegar a un **caso base** que corta la cadena de llamadas y devuelve un resultado sin recursión. Cada llamada resuelve un paso y delega el resto en la siguiente.

## Ejemplo de la cátedra: `reducir_numero`
Reduce un entero a un único dígito sumando sus dígitos una y otra vez. El caso base es "el número ya tiene un solo dígito"; si no, suma los dígitos y se vuelve a llamar con esa suma.

```python
def reducir_numero(numero: int) -> int:
    # Caso base: si el número tiene un solo dígito, devolverlo tal cual
    if numero < 10:
        return numero
    # Convertir el número en una lista de dígitos
    digitos = [int(digito) for digito in str(numero)]
    # Calcular la suma de los dígitos
    suma_digitos = sum(digitos)
    # Llamar recursivamente a la función con la suma de los dígitos
    return reducir_numero(suma_digitos)
```

Traza con `29`: `2 + 9 = 11` → 11 todavía tiene dos dígitos, así que `1 + 1 = 2` → caso base, devuelve `2`.

La lista de dígitos se arma con una [[Comprensión de listas|comprensión de listas]] sobre `str(numero)`.

## Aplicación: color de cada número en el simulador de ruleta
Para conocer el color de un número en el paño de una ruleta real se usa `reducir_numero`:
- `0` → verde (`'V'`).
- `10` y `28` → negros (`'N'`), excepciones a la regla.
- Cualquier otro: negro si su número reducido es **par**, rojo (`'R'`) si es impar.

```python
def get_color(nro: int) -> str:
    if nro == 0:
        return 'V'
    elif nro == 10 or nro == 28:
        return 'N'
    else:
        # Los números negros son aquellos cuya reducción es par
        if reducir_numero(nro) % 2 == 0:
            return 'N'
        else:
            return 'R'
```

`generar_ruleta()` recorre `range(0, 37)` y arma una lista de [[Tuplas|tuplas]] `(numero, color)`, de modo que cada número quede guardado en su mismo índice (por ejemplo `(10, "N")` en la posición 10). El resto del programa genera 1000 tiradas con `random.randint(0, 36)`, consulta `ruleta[tirada_nro][1]` para el color y acumula pares/impares, rojos/negros, docenas y ceros.

## Conceptos relacionados
- [[Funciones]] — la recursión es una función que se invoca a sí misma
- [[Comprensión de listas]] — usada para obtener los dígitos
- [[Tuplas]] y [[Listas]] — estructura del paño de la ruleta
- [[Operadores]] — `%` para la paridad
- [[Módulos y docstrings]] — `random` y `rich` en el ejercicio

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=30|semana1.pdf, §2.6.1 Simulador de ruleta (p. 30-33)]]
