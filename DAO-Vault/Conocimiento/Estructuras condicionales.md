---
tipo: concepto
materia: DAO
unidad: 1
tags: [python, condicionales]
---

# Estructuras condicionales

## if / elif / else
```python
if x > 0:
    print("x es positivo")
elif x < 0:
    print("x es negativo")
else:
    print("x es cero")
```

## Condiciones idiomáticas
- Para banderas booleanas: `if existe:` en vez de `if existe == True:`; `if not existe:` en vez de `if existe == False:`.
- Aprovechando *truthiness* ([[Tipos de datos]]): `if not lista:` para detectar vacío, `if not edad:` para detectar 0.
- Combinación de rangos y trampas de encadenamiento: ver [[Operadores]]#Combinación de condiciones.

## Relacionado
- [[Operadores]] — operadores de comparación y lógicos que alimentan las condiciones
- [[Estructuras repetitivas]] — condiciones de corte de bucles `while`
- [[Python - Mapa de Contenidos]]

## Visto en
- [[Unidad 1 - Programación estructurada y secuencias]] · [[semana1.pdf#page=4|semana1.pdf, §1.3 Estructuras condicionales (p. 4-7)]]
