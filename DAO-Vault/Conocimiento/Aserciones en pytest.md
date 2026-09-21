---
tipo: concepto
materia: DAO
unidad: 5
tags: [testing, pytest, assert, aserciones]
---

# Aserciones en pytest

Una **aserción** es una verificación hecha con la instrucción `assert` dentro de una prueba: si la condición es falsa, la prueba falla y [[Pytest|pytest]] reporta el valor esperado frente al obtenido. Como usa el `assert` estándar de Python junto con los [[Operadores|operadores]] habituales, no hace falta aprender métodos propios del framework.

## Igualdad
Las más comunes: verifican que un valor obtenido sea exactamente igual al esperado.

```python
def test_igualdad_numerica():
    assert 5 == 5
    assert 2.5 == 2.5

def test_igualdad_cadenas():
    assert "hola" == "hola"
    assert "Python".lower() == "python"

def test_igualdad_listas():
    assert [1, 2, 3] == [1, 2, 3]
    assert sorted([3, 1, 2]) == [1, 2, 3]
```

Desigualdad con `!=`:

```python
def test_desigualdad():
    assert 5 != 3
    assert "hola" != "adiós"
```

## Comparación
Relaciones de orden con los operadores estándar:

```python
def test_comparaciones_numericas():
    assert 5 > 3
    assert 2 < 10
    assert 5 >= 5
    assert 3 <= 7

def test_comparaciones_cadenas():
    assert "abc" < "def"   # orden alfabético
    assert "z" > "a"
```

## Pertenencia
Verifican si un elemento está en una colección con `in` / `not in`:

```python
def test_pertenencia_listas():
    numeros = [1, 2, 3, 4, 5]
    assert 3 in numeros
    assert 6 not in numeros

def test_pertenencia_cadenas():
    texto = "Hola mundo"
    assert "mundo" in texto
    assert "Python" not in texto

def test_pertenencia_diccionarios():
    datos = {"nombre": "Juan", "edad": 25}
    assert "nombre" in datos
    assert "apellido" not in datos
```

## Tipo
Con la función `isinstance()`:

```python
def test_tipos():
    assert isinstance(5, int)
    assert isinstance(3.14, float)
    assert isinstance("texto", str)
    assert isinstance([1, 2, 3], list)
    assert isinstance({"a": 1}, dict)
```

## Excepciones
Para verificar que el código **lance** una excepción bajo ciertas condiciones se usa el *context manager* `pytest.raises()`; con `match=` se comprueba además el mensaje (una expresión regular). Ver [[Excepciones]].

```python
import pytest

def test_excepcion_division_cero():
    with pytest.raises(ZeroDivisionError):
        resultado = 10 / 0

def test_excepcion_valor_incorrecto():
    with pytest.raises(ValueError):
        int("texto_invalido")

def test_excepcion_con_mensaje():
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")
```

## Aproximación
Con valores de punto flotante la comparación exacta puede fallar por imprecisiones de representación. `pytest.approx()` compara con tolerancia (`rel=` para la tolerancia relativa):

```python
import pytest

def test_aproximacion():
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 3.14159 == pytest.approx(3.14, rel=1e-2)
```

## Conceptos relacionados
- [[Pytest]] — el framework donde se usan
- [[Testing unitario]] — para qué se escriben
- [[Excepciones]] — `pytest.raises`
- [[Operadores]] — `==`, `!=`, `<`, `>`, `in`
- [[Tipos de datos]] — `isinstance` sobre `int`, `float`, `str`, `list`, `dict`

## Visto en
- [[Unidad 5 - Herencia, polimorfismo y testing]] · [[semana5.pdf#page=19|semana5.pdf, §12.3 Pruebas (p. 19-22)]]
