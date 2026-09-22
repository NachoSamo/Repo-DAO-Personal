# Resolución de Ejercicio Tipo Parcial (DAO)

> 📺 **Video de referencia:** [Ver resolución en YouTube](https://www.youtube.com/watch?v=KdFpJJxdcBI)

> [!TIP]
> **Estrategia inicial:** Solo con mirar los `import` del archivo de tests (`test_*.py`) ya podemos deducir qué nombres de archivos, módulos y clases necesitaremos crear antes de escribir cualquier otra línea de código.

---

## 1. Materiales entregados en el parcial

Al momento del examen, se recibe una carpeta con los siguientes archivos base:

* **Archivo Markdown:** Contiene el enunciado detallado con los requerimientos de negocio y lo que se debe programar.
* **Archivo de datos (`*.csv`):** Contiene los registros necesarios para realizar la lectura, parseo y procesamiento desde el programa principal.
* **Archivo con casos de prueba (`test_*.py`):** Contiene las pruebas unitarias automatizadas con `pytest`. Sirven como contrato del diseño, especifican cómo deben llamarse las clases/métodos y permiten verificar el avance en tiempo real.

---

## 2. Lectura y procesamiento del archivo CSV

### ¿Aunque los tests no usen el CSV, es obligatorio leerlo?

> [!IMPORTANT]
> **Sí, es obligatorio.** El archivo CSV (`inmuebles.csv`) debe leerse dentro de la función `main()`.

Aunque las pruebas unitarias de `pytest` validan directamente la lógica interna instanciando objetos en memoria, el enunciado exige formalmente que la función principal:

1. Abra y recorra el archivo de texto/CSV.
2. Parsee cada línea y convierta los tipos de datos (`int`, `float`, `bool`).
3. Instancie los objetos correspondientes (`Casa` o `Departamento`) y los cargue en el objeto contenedor (`Inmobiliaria`).
4. Finalice imprimiendo en consola los resultados de los métodos solicitados:
   - Suma total de alquileres recaudables.
   - Cantidad de casas premium.
   - Propietario del departamento con el alquiler definitivo más bajo.

---

## 3. Consejos y recomendaciones del profesor

* **Organización del Workspace en VS Code:**  
  Abrir **únicamente la carpeta del parcial** en Visual Studio Code (no la carpeta raíz de la materia ni de la facultad). Esto asegura que la raíz de trabajo coincida con las rutas relativas del CSV y los `imports` de `pytest`.
* **Configuración del entorno de pruebas:**  
  Tener instalada la extensión de Python y configurar `pytest` desde el panel de Testing (ícono del matraz/frasquito), seleccionando la carpeta actual de trabajo.
* **Práctica sin asistentes de IA:**  
  Practicar sin GitHub Copilot ni asistentes automáticos, ya que en el parcial presencial no se contará con acceso a internet y es indispensable dominar la sintaxis y depuración por cuenta propia.
* **Guiarse por los tests:**  
  Los casos de prueba de `pytest` definen con precisión los nombres de atributos, métodos y firmas esperadas. Son la mejor guía de especificación.
* **Gestión del tiempo:**  
  No trabarse en detalles teóricos secundarios. Con práctica suficiente, la estructura base del examen está pensada para resolverse en aproximadamente **1 hora y media**.

---

## 4. Estructura y tipo de ejercicios

El examen consiste en implementar un modelo de dominio aplicando **Programación Orientada a Objetos (POO)**:

* **Composición de objetos:** Crear clases contenedoras (ej. `Inmobiliaria`) que encapsulan y gestionan una colección de objetos (`Casa`, `Departamento`).
* **Herencia y polimorfismo:** Definir una clase base abstracta (`Inmueble`) y clases derivadas que sobrescriben métodos clave (como `alquiler()`) adaptando la fórmula de cálculo según cada tipo.
* **Lectura y procesamiento de archivos:** Lógica en `main()` para transformar texto plano en objetos de dominio.
* **Pruebas unitarias:** Ejecución continua de `pytest` para garantizar regresión cero y cobertura de consignas.

---

## 5. Programación funcional: `map` y `filter`

### ¿Se pueden usar funciones de orden superior?
**Sí.** Su uso es válido y recomendable si ayudan a simplificar la lógica de colecciones.

* **Ventajas:** Permiten filtrar (`filter`) o transformar (`map`) listas de forma concisa y declarativa frente a los bucles tradicionales.
* **No son obligatorias:** Se pueden resolver los mismos problemas mediante bucles `for` o comprensiones de listas (*list comprehensions*).
* **Restricción importante:** La solución debe mantenerse dentro de las herramientas nativas de Python y los conceptos de la cátedra. **No se permite el uso de librerías externas pesadas (como `pandas`)**.

---

## 6. Pilares de POO evaluados

1. **Herencia:** Extender una clase base común para reutilizar atributos (código, propietario, superficie, alquiler base).
2. **Polimorfismo:** Compartir una interfaz unificada (`alquiler()`) cuyo comportamiento varía según el tipo de inmueble.
3. **Composición:** Mantener una colección interna de inmuebles dentro de la clase administradora.
4. **Encapsulamiento:** Ocultar detalles internos y evitar operar o modificar atributos privados/internos directamente desde el `main`.
5. **Sobrescritura de métodos (Override):** Redefinir métodos de la clase abstracta en las clases hijas manteniendo exactamente la misma firma.
