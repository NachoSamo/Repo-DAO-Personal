<h1 align="center">Desarrollo de Aplicaciones con Objetos (DAO)</h1>

<p align="center">
  <b>Dominio de Python: desde algoritmos estructurados hasta arquitectura orientada a objetos y testing sistemático.</b>
</p>

<p align="center">
  Facultad · 4.° Año · Ciclo Lectivo 2026 · Cátedra Prof. Serrano
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PYTHON-3.10+-1E1E1E?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python" />
  <img src="https://img.shields.io/badge/PARADIGMA-POO%20%2F%20OOP-1E1E1E?style=for-the-badge&logo=diagram-next&logoColor=F59E0B" alt="POO" />
  <img src="https://img.shields.io/badge/TESTING-PYTEST-1E1E1E?style=for-the-badge&logo=pytest&logoColor=0A9EDC" alt="Pytest" />
  <img src="https://img.shields.io/badge/PKM-OBSIDIAN%20VAULT-1E1E1E?style=for-the-badge&logo=obsidian&logoColor=7C3AED" alt="Obsidian" />
  <img src="https://img.shields.io/badge/DATA-CSV%20%2F%20JSON-1E1E1E?style=for-the-badge&logo=json&logoColor=FFFFFF" alt="Data" />
  <img src="https://img.shields.io/badge/SIMULACROS-PARCIALES%202026-6366F1?style=for-the-badge" alt="Simulacros" />
</p>

<p align="center">
  <b>DAO Personal Workspace</b> by <a href="https://github.com/NachoSamo">NachoSamo</a>
</p>

---

El desarrollo de software profesional exige trascender la resolución algorítmica procedimental. En la materia **Desarrollo de Aplicaciones con Objetos (DAO)**, la transición desde la programación estructurada hacia la **Programación Orientada a Objetos (POO)** en Python se aborda como un cambio de mentalidad arquitectónica: pasar de manipular estructuras de datos aisladas a modelar el dominio de negocio mediante abstracciones cohesivas, encapsulamiento riguroso, relaciones jerárquicas y polimorfismo dinámico.

Este repositorio consolida el ecosistema integral de aprendizaje y desarrollo para la cursada 2026. Centraliza las resoluciones oficiales de las guías de cátedra, implementaciones y experimentos prácticos de producción propia, una base de conocimiento interconectada en **Obsidian** (DAO-Vault) con notas atómicas y wikilinks, y bancos completos de **simulacros de examen parcial** respaldados por datasets reales (`.csv`, `.json`) y baterías de pruebas automatizadas con `pytest`.

---

## 📑 Tabla de Contenidos

1. [Arquitectura del Repositorio](#-arquitectura-del-repositorio)
2. [Ejes Temáticos del Programa](#-ejes-temáticos-del-programa)
   - [Tema 01: Programación Estructurada y Funcional](#tema-01--programación-estructurada-y-funcional)
   - [Tema 02: Programación Orientada a Objetos](#tema-02--programación-orientada-a-objetos-poo)
3. [DAO-Vault: Base de Conocimiento (Obsidian)](#-dao-vault-base-de-conocimiento-obsidian)
4. [Simulacros y Modelos de Examen](#-simulacros-y-modelos-de-examen)
5. [Testing y Control de Calidad](#-testing-y-control-de-calidad)
6. [Guía de Puesta en Marcha](#-guía-de-puesta-en-marcha)
7. [Convenciones de Código](#-convenciones-de-código)

---

## 📚 Ejes Temáticos del Programa

### Tema 01 — Programación Estructurada y Funcional

Comprende el dominio del lenguaje Python en su vertiente estructurada, analizando el costo algorítmico, el uso eficiente de colecciones integradas y las herramientas de transformación declarativa de datos.

| Módulo | Conceptos Clave | Prácticas Destacadas |
| :--- | :--- | :--- |
| **Sintaxis & Control** | Tipos mutables e inmutables, operadores lógicos/aritméticos, `if/elif/else`, bucles `for`/`while`, desempaquetado de secuencias. | Validación de estaciones de servicio, cálculo de temperaturas. |
| **Colecciones Integradas** | Listas, tuplas, conjuntos (`set`, intersección, unión, diferencia) y diccionarios (`dict`, claves únicas, orden de inserción). | Análisis de frecuencias léxicas en *El Quijote*, ruleta probabilística. |
| **I/O & Serialización** | Context managers (`with`), lectura/escritura de streams de texto, `csv.reader`/`DictReader`, JSON anidado y multinivel. | Análisis estadístico de propinas (`tips.csv`), facturación en JSON. |
| **Programación Funcional** | Funciones de primera clase, funciones anónimas (`lambda`), `map()`, `filter()`, `reduce()` (`functools`) y comprensiones de listas/diccionarios. | Pipelines funcionales de filtrado y agregación de métricas. |

---

### Tema 02 — Programación Orientada a Objetos (POO)

El núcleo de la materia: diseñar software acoplado al modelo del mundo real mediante abstracciones, delegación de responsabilidades y diseño dirigido por pruebas.

* **Abstracción & Encapsulamiento**: Declaración de clases con `__init__`, atributos protegidos (`_attr`), métodos mutadores y accesores mediante `@property` y `@<name>.setter`.
* **Herencia & Composición**: Especialización de comportamiento con `super().__init__()`, evitando jerarquías frágiles en favor de composición cuando corresponde.
* **Polimorfismo & Duck Typing**: Intercambiabilidad de objetos que responden a la misma interfaz pública sin necesidad de acoplamiento rígido de tipos en tiempo de compilación.
* **Manejo Robusto de Errores**: Creación de excepciones de dominio heredando de `Exception`, asegurando que la lógica de negocio notifique estados anómalos de manera limpia.
* **Testing Automatizado**: Estructura de pruebas unitarias (`test_*.py`), validación de aserciones (`assert`), tests parametrizados y detección de regresiones.

---

## 🧠 DAO-Vault: Base de Conocimiento (Obsidian)

Ubicado en [`DAO-Vault/`](./DAO-Vault/), este directorio alberga un sistema de gestión del conocimiento personal (**PKM**) configurado en **Obsidian**. Cada concepto teórico visto a lo largo del año cuenta con una nota atómica conectada mediante wikilinks bidireccionales, permitiendo navegar visualmente por el grafo del conocimiento de la materia:

### Índice de Conceptos en el Vault
* **Sintaxis & Fundamentos:** [Tipos de datos](./DAO-Vault/Conocimiento/Tipos%20de%20datos.md) • [Operadores](./DAO-Vault/Conocimiento/Operadores.md) • [Estructuras condicionales](./DAO-Vault/Conocimiento/Estructuras%20condicionales.md) • [Estructuras repetitivas](./DAO-Vault/Conocimiento/Estructuras%20repetitivas.md) • [Funciones](./DAO-Vault/Conocimiento/Funciones.md)
* **Estructuras & Datos:** [Secuencias](./DAO-Vault/Conocimiento/Secuencias.md) • [Cadenas](./DAO-Vault/Conocimiento/Cadenas.md) • [Listas](./DAO-Vault/Conocimiento/Listas.md) • [Tuplas](./DAO-Vault/Conocimiento/Tuplas.md) • [Conjuntos](./DAO-Vault/Conocimiento/Conjuntos.md) • [Diccionarios](./DAO-Vault/Conocimiento/Diccionarios.md) • [Archivos](./DAO-Vault/Conocimiento/Archivos.md)
* **Paradigma POO:** [Programación orientada a objetos](./DAO-Vault/Conocimiento/Programación%20orientada%20a%20objetos.md) • [Clases y objetos](./DAO-Vault/Conocimiento/Clases%20y%20objetos.md) • [Constructor](./DAO-Vault/Conocimiento/Constructor.md) • [Encapsulamiento](./DAO-Vault/Conocimiento/Encapsulamiento.md) • [Propiedades](./DAO-Vault/Conocimiento/Propiedades.md) • [Métodos](./DAO-Vault/Conocimiento/Métodos.md) • [Referencias](./DAO-Vault/Conocimiento/Referencias.md)
* **Manejo de Errores & Testing:** [Excepciones](./DAO-Vault/Conocimiento/Excepciones.md) • [Módulos y docstrings](./DAO-Vault/Conocimiento/Módulos%20y%20docstrings.md)

---

## 🎯 Simulacros y Modelos de Examen

En [`SimulacrosParcial/`](./SimulacrosParcial/) se encuentran los enunciados y resoluciones tipo examen parcial, enfocados en resolver problemas de negocio integrando carga de datos, modelado de objetos y cálculos financieros o logísticos:

| Simulacro | Dominio del Problema | Clases & Polimorfismo | Datos (`data/`) | Tests Automatizados |
| :--- | :--- | :--- | :--- | :--- |
| [**Hospital**](./SimulacrosParcial/Hospital-20260918/) | Gestión de atenciones médicas y de farmacia, pacientes habituales, políticas de descuentos e importes a cobrar. | `Hospital`, `Atencion` (base), `AtencionMedica`, `AtencionFarmacia`, `Paciente`. | `pacientes.csv`<br/>`atenciones_medicas.csv`<br/>`atenciones_farmacia.csv` | [`test_hospital_autocontenido.py`](./SimulacrosParcial/Hospital-20260918/tests/test_hospital_autocontenido.py) |
| [**Empresa de Transporte**](./SimulacrosParcial/Empresa%20de%20Transporte-20260918/) | Logística de envíos, packing de cajas y bidones con cubitaje, restricciones de peso y asignación a camiones. | `Camion`, `Carga`, `Caja`, `Bidon`, `Packing`. | `cajas.csv`<br/>`bidones.csv`<br/>`packing.csv` | Validación de reglas de despacho y capacidad volumétrica. |
| [**Mantenimiento**](./SimulacrosParcial/Mantenimiento-20260918/) | Seguimiento de flotas de vehículos, servicios mecánicos preventivos y correctivos, liquidación de costos. | `Flota`, `Vehiculo`, `Servicio`, `Mantenimiento`. | `mantenimientos.csv` | Control de presupuestos y periodicidad de revisiones. |

---

## 🧪 Testing y Control de Calidad

El proyecto adopta **Pytest** como estándar para garantizar que cada método de negocio cumpla con las especificaciones del dominio y conserve su comportamiento ante refactorizaciones:

```bash
# Ejecutar la suite completa de un simulacro específico
pytest "SimulacrosParcial/Hospital-20260918/tests/test_hospital_autocontenido.py" -v

# Ejecutar las pruebas de la guía de POO (ejemplo: ascensor o inmobiliaria)
pytest "2026GuiasProfeSerrano/tema-02-programacion-orientada-objetos/testing/ascensor/test_ascensor.py" -v
```

Las suites de prueba validan:
- Correcto cálculo de importes con descuentos cruzados (efectivo vs. tarjeta, condición de habitualidad).
- Manejo adecuado de listas vacías y valores frontera (`0`, negativos, floats con redondeo).
- Levantamiento de excepciones apropiadas ante estados no válidos.

---

## 📐 Convenciones de Código

* **PEP 8**: Adherencia a nombres en `snake_case` para funciones y variables, y `PascalCase` para nombres de clases.
* **Separación de Responsabilidades**: Las clases del dominio **no** realizan impresiones por terminal (`print`), sino que devuelven datos o delegan en métodos de representación (`__str__`, `__repr__`).
* **Tipado Gradual**: Uso progresivo de Type Hints (`typing`: `List`, `Dict`, `Optional`, `Union`) para favorecer el autocompletado y la legibilidad.
* **Documentación**: Docstrings en módulos y clases explicando responsabilidades y contratos de métodos clave.

---

<p align="center">
  <b>Materia:</b> Desarrollo de Aplicaciones con Objetos · <b>Año:</b> 2026<br/>
  Repositorio mantenido por <b>Nacho Samo</b>
</p>
