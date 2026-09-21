---
tipo: concepto
materia: DAO
unidad: 5
tags: [testing, pruebas-unitarias, calidad]
---

# Testing unitario

Práctica que consiste en escribir y ejecutar **pruebas automatizadas** que verifican que las unidades individuales de código funcionen correctamente **de manera aislada**. Una *unidad* suele ser un método, una función o una clase: la porción más pequeña de código que puede probarse de forma independiente.

El propósito principal es **detectar errores en las primeras etapas**, cuando son más fáciles y baratos de corregir. Si cada componente funciona como se espera, hay más confianza de que el sistema completo funcionará cuando se integren las partes.

## Relevancia en POO
Por la naturaleza modular y encapsulada de las clases, el testing unitario cobra especial relevancia: cada clase cumple un conjunto específico de responsabilidades y mantiene su estado interno coherente. Las pruebas permiten verificar que los métodos produzcan los resultados esperados, que las validaciones internas funcionen y que el [[Encapsulamiento|encapsulamiento]] se mantenga.

## Beneficios
- Detección temprana de errores.
- **Refactoring seguro**: las pruebas son una red de seguridad; cualquier regresión al modificar el código se detecta de inmediato.
- Documentación implícita del comportamiento esperado de cada componente.
- Menos tiempo para localizar y corregir defectos.

## Qué se le pide a una buena prueba
Ser **rápida** de ejecutar, **independiente** de las demás, **repetible** y **fácil de mantener**. Cada prueba verifica un comportamiento específico y, cuando falla, da información clara sobre qué aspecto del código falló.

## En Python
El framework estándar de facto es [[Pytest]], que usa `assert` común; los distintos tipos de verificación están en [[Aserciones en pytest]].

## Conceptos relacionados
- [[Pytest]] — la herramienta
- [[Aserciones en pytest]] — las verificaciones
- [[Encapsulamiento]] — lo que se prueba a través de la interfaz pública
- [[Excepciones]] — se prueban los casos de error
- [[Clases y objetos]] — las unidades típicas en POO

## Visto en
- [[Unidad 5 - Herencia, polimorfismo y testing]] · [[semana5.pdf#page=17|semana5.pdf, §12.1 Introducción (p. 17-18)]]
