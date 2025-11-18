🧱 Cálculo del Volumen de Concreto en Elementos Estructurales  
### Práctica 5 – Modelado de Problemas en Ingeniería Civil  

---

## 📘 1. Introducción

El cálculo del volumen de concreto es una actividad fundamental en la Ingeniería Civil, especialmente en la fase de diseño estructural y construcción. A partir de este valor se realizan estimaciones de:

- Presupuestos de obra
- Cantidades de materiales
- Programación de colados
- Control de calidad y logística

En esta práctica se modela programáticamente el cálculo del volumen de distintos elementos estructurales de uso común:

- **Losa**
- **Zapata**
- **Columna rectangular**
- **Columna circular**

El propósito es aplicar el proceso completo de modelado de un problema real:  
📌 *Análisis → Diseño → Implementación → Pruebas → Presentación mediante interfaz gráfica.*

---

## 🧠 2. Marco teórico

Los elementos estructurales analizados pueden aproximarse como cuerpos geométricos simples, lo que permite calcular su volumen mediante fórmulas básicas de geometría.

---

### 🟦 2.1 Losa de concreto

Una losa de entrepiso o azotea puede modelarse como un **prisma rectangular**.

\[
V = largo \times ancho \times espesor
\]

Donde:
- \(V\): volumen en m³  
- \(espesor\): espesor total de la losa

---

### 🟩 2.2 Zapata cuadrada o rectangular

Las zapatas aisladas para columnas también se modelan como un prisma:

\[
V = largo \times ancho \times espesor
\]

Esta aproximación es suficiente para estimación de materiales.

---

### 🟧 2.3 Columna rectangular

Las columnas rectangulares son prismas rectangulares:

\[
V = lado_1 \times lado_2 \times altura
\]

---

### 🟨 2.4 Columna circular

Modelada como un cilindro:

\[
V = \pi r^{2} \times h
\]

Donde:
- \(r = \frac{diámetro}{2}\)

---

## 🧩 3. Modelado computacional

El proyecto se divide en tres archivos principales:

mi_modelado/
│
├── funciones.py → Funciones matemáticas y validación
├── interfaz.py → Interfaz gráfica (Tkinter)
└── main.py → Integración general

yaml
Copiar código

---

### ✔ 3.1 Análisis

El sistema valida que:

- Todas las entradas sean numéricas
- No existan valores negativos ni cero
- Los datos correspondan físicamente a un elemento real

---

### ✔ 3.2 Diseño del sistema

El código se estructura de manera **modular**, creando una función para cada tipo de elemento:

- `volumen_losa()`
- `volumen_zapata()`
- `volumen_columna_rect()`
- `volumen_columna_circ()`

Se programó una función `validar()` para garantizar que los datos no sean incorrectos.

---

### ✔ 3.3 Pruebas de verificación

El archivo `funciones.py` contiene pruebas automáticas:

```python
pruebas()
