---
id: resolucion_repaso_solemne_1
title: "Resolución Completa y Verificada: Guía de Repaso Solemne 1"
asignatura: "Álgebra Lineal (USS Patagónica)"
fecha: 2026-09-08
tags:
  - algebra_lineal
  - solemne_1
  - resolucion
  - uss
  - matrices
  - determinantes
  - sistemas_ecuaciones
  - gauss
status: completado
---

# 📖 Resolución Completa: Guía de Repaso Solemne 1
**Carrera:** Ingeniería Civil Informática  
**Institución:** Universidad San Sebastián (USS — Sede Patagonia)  
**Asignatura:** Álgebra Lineal  
**Docente:** Carol Asencio González  
**Estudiante:** Moisés Amundarain Romero  

---

## 📌 Tabla Resumen de Respuestas

| Ejercicio | Tipo | Tema Principal | Respuesta / Solución | Opción Correcta |
| :---: | :---: | :--- | :--- | :---: |
| **1** | Selección Múltiple | Igualdad de Determinantes | $x = 4 \lor x = -1$ | **Opción d** |
| **2** | Selección Múltiple | Análisis de Consistencia (Gauss) | Si $k \neq 10$ el sistema es Incompatible | **Opción d** |
| **3** | Selección Múltiple | Ecuación Matricial | $X = A - 2B^{-1}$ | **Opción D** |
| **4** | Selección Múltiple | Singularidad de Matriz $2 \times 2$ | $t = 2 \lor t = -2$ | **Opción B** |
| **5** | Selección Múltiple | Ecuaciones y Trasposición | $X = \frac{1}{3}(B^{-1} + A)$ | **Opción d** |
| **6.a** | Desarrollo | Regularidad de Matriz | $A$ es regular $\iff m \neq 3$ | $(\det A = 3-m)$ |
| **6.b** | Desarrollo | Parámetro No Solución Única | $m = 3$ | $(\det A = 0)$ |
| **6.c** | Desarrollo | Conjunto Solución ($m=3$) | $S = \{ (1 - \frac{1}{3}t, \, -\frac{8}{3}t, \, t) : t \in \mathbb{R} \}$ | Infinitas Sol. |
| **6.d** | Desarrollo | Inversa por Adjunta ($m=-1$) | $A^{-1} = \frac{1}{4} \begin{bmatrix} 1 & 1 & -1 \\\\ -4 & 0 & -8 \\\\ 1 & 1 & 3 \end{bmatrix}$ | Inversa Exacta |

---

## ✏️ Desarrollo Detallado Ejercicio por Ejercicio

### 🔹 Ejercicio 1: Ecuación con Determinantes

> [!important] **Enunciado:**
> Los valores de $x \in \mathbb{R}$, tales que:
> $$\begin{vmatrix} x & -1 \\ x & 2 \end{vmatrix} = \begin{vmatrix} 1 & 0 & 5 \\ 0 & x-2 & 6 \\ 0 & 0 & x+2 \end{vmatrix}$$

#### **Paso 1: Cálculo del determinante del lado izquierdo ($2 \times 2$)**
$$\begin{vmatrix} x & -1 \\ x & 2 \end{vmatrix} = (x)(2) - (-1)(x) = 2x + x = 3x$$

#### **Paso 2: Cálculo del determinante del lado derecho ($3 \times 3$)**
La matriz del lado derecho es **triangular superior**, por lo que su determinante es el producto de los elementos de su diagonal principal:
$$\begin{vmatrix} 1 & 0 & 5 \\ 0 & x-2 & 6 \\ 0 & 0 & x+2 \end{vmatrix} = (1) \cdot (x-2) \cdot (x+2) = x^2 - 4$$

#### **Paso 3: Igualación y resolución de la ecuación cuadrática**
$$3x = x^2 - 4 \implies x^2 - 3x - 4 = 0$$

Factorizando el trinomio:
$$(x - 4)(x + 1) = 0 \implies x_1 = 4, \quad x_2 = -1$$

> [!tip] **Conclusión:**
> La solución es $x = 4 \lor x = -1$, lo cual corresponde exactamente a la **Opción d**.

---

### 🔹 Ejercicio 2: Análisis de Consistencia de un Sistema $3 \times 3$

> [!important] **Enunciado:**
> De acuerdo con el sistema de ecuaciones:
> $$\begin{cases} 2x + y - z = 1 \\ x - 2y + z = 3 \\ 5x - 5y + 2z = k \end{cases}$$
> Determine la afirmación verdadera respecto al parámetro $k$.

#### **Paso 1: Construcción de la Matriz Aumentada $[A|B]$**
$$[A|B] = \begin{bmatrix} 2 & 1 & -1 & \mid & 1 \\ 1 & -2 & 1 & \mid & 3 \\ 5 & -5 & 2 & \mid & k \end{bmatrix}$$

#### **Paso 2: Eliminación Gaussiana por Operaciones Elementales por Filas (OEF)**
 Intercambiamos $F_1 \leftrightarrow F_2$ para obtener pivote $1$:
$$[A|B] \xrightarrow{F_1 \leftrightarrow F_2} \begin{bmatrix} 1 & -2 & 1 & \mid & 3 \\ 2 & 1 & -1 & \mid & 1 \\ 5 & -5 & 2 & \mid & k \end{bmatrix}$$

 Eliminamos entradas debajo del pivote $a_{11} = 1$:
$$F_2 \leftarrow F_2 - 2F_1: \quad [2 - 2(1), \, 1 - 2(-2), \, -1 - 2(1) \mid 1 - 2(3)] = [0, \, 5, \, -3 \mid -5]$$
$$F_3 \leftarrow F_3 - 5F_1: \quad [5 - 5(1), \, -5 - 5(-2), \, 2 - 5(1) \mid k - 5(3)] = [0, \, 5, \, -3 \mid k - 15]$$

La matriz queda:
$$\begin{bmatrix} 1 & -2 & 1 & \mid & 3 \\ 0 & 5 & -3 & \mid & -5 \\ 0 & 5 & -3 & \mid & k - 15 \end{bmatrix}$$

 Eliminamos la variable $y$ en la tercera fila ($F_3 \leftarrow F_3 - F_2$):
$$F_3 \leftarrow F_3 - F_2: \quad [0 - 0, \, 5 - 5, \, -3 - (-3) \mid (k - 15) - (-5)] = [0, \, 0, \, 0 \mid k - 10]$$

Matriz escalonada resultante:
$$\begin{bmatrix} 1 & -2 & 1 & \mid & 3 \\ 0 & 5 & -3 & \mid & -5 \\ 0 & 0 & 0 & \mid & k - 10 \end{bmatrix}$$

#### **Paso 3: Análisis por Teorema de Rouché-Frobenius**
1. **Si $k = 10$:** La tercera fila se convierte en $[0, 0, 0 \mid 0]$.
   $$\text{rg}(A) = 2 = \text{rg}(A|B) < n=3 \implies \text{\textbf{Sistema Compatible Indeterminado (Infinitas Soluciones)}}$$
2. **Si $k \neq 10$:** La tercera fila representa la ecuación $0x + 0y + 0z = k - 10 \neq 0$.
   $$\text{rg}(A) = 2 \neq \text{rg}(A|B) = 3 \implies \text{\textbf{Sistema Incompatible (Sin Solución)}}$$

> [!tip] **Conclusión:**
> La afirmación verdadera es: **Si $k \neq 10$ el sistema es Incompatible**, que corresponde a la **Opción d**.

---

### 🔹 Ejercicio 3: Despeje de Ecuación Matricial

> [!important] **Enunciado:**
> Considere la ecuación matricial $XB = AB - 2I$. Asumiendo que $B$ es invertible, halle la expresión para $X$.

#### **Paso 1: Multiplicación por la derecha por $B^{-1}$**
Como $B$ es invertible, multiplicamos toda la ecuación por la derecha por $B^{-1}$:
$$(XB)B^{-1} = (AB - 2I)B^{-1}$$

#### **Paso 2: Aplicación de la propiedad asociativa y distributiva**
$$X(BB^{-1}) = (AB)B^{-1} - (2I)B^{-1}$$
$$X \cdot I = A(BB^{-1}) - 2(IB^{-1})$$
$$X = A \cdot I - 2 B^{-1}$$
$$X = A - 2B^{-1}$$

> [!tip] **Conclusión:**
> La solución algebraica exacta es $X = A - 2B^{-1}$, correspondiente a la **Opción D**.

---

### 🔹 Ejercicio 4: Matriz Singular ($2 \times 2$)

> [!important] **Enunciado:**
> Sea la matriz $A = \begin{bmatrix} t & 3 \\ 4 & 3t \end{bmatrix}$. Halle los valores reales de $t$ donde $\det(A) = 0$.

#### **Paso 1: Cálculo del determinante**
$$\det(A) = (t)(3t) - (3)(4) = 3t^2 - 12$$

#### **Paso 2: Resolución de la ecuación $\det(A) = 0$**
$$3t^2 - 12 = 0 \implies 3t^2 = 12 \implies t^2 = 4 \implies t = \pm 2$$

> [!tip] **Conclusión:**
> Los valores reales son $t = 2 \lor t = -2$, lo que corresponde a la **Opción B**.

---

### 🔹 Ejercicio 5: Despeje Matricial con Propiedad de Simetría

> [!important] **Enunciado:**
> Considere las matrices $A, B, X \in M_{2\times 2}(\mathbb{R})$, donde $B$ es una matriz **simétrica** ($B^T = B$) e **invertible** ($B^{-1}$ existe).
> Resolver algebraicamente la ecuación:
> $$2(X^T B)^T + BX - BA = I$$

#### **Paso 1: Trasposición de productos y uso de simetría**
Utilizando la propiedad de trasposición $(PQ)^T = Q^T P^T$:
$$(X^T B)^T = B^T (X^T)^T = B^T X$$

Como $B$ es simétrica ($B^T = B$), sustituimos $B^T$ por $B$:
$$(X^T B)^T = BX$$

#### **Paso 2: Sustitución y reducción de términos semejantes**
$$2(BX) + BX - BA = I$$
$$3BX - BA = I$$

#### **Paso 3: Factorización matricial por la izquierda**
$$B(3X - A) = I$$

#### **Paso 4: Despeje de $X$ mediante multiplicación por $B^{-1}$ por la izquierda**
$$B^{-1} B(3X - A) = B^{-1} I$$
$$I(3X - A) = B^{-1}$$
$$3X - A = B^{-1}$$
$$3X = B^{-1} + A \implies X = \frac{1}{3}(B^{-1} + A)$$

> [!tip] **Conclusión:**
> La expresión resulta en $X = \frac{1}{3}(B^{-1} + A)$, correspondiente a la **Opción d**.

---

### 🔹 Ejercicio 6: Desarrollo Completo de Sistema Paramétrico

> [!important] **Enunciado:**
> Dado el siguiente sistema de ecuaciones lineales en las variables $x, y, z$:
> $$\begin{cases} 2x - y - 2z = 2 \\ x + y + 3z = 1 \\ mx + z = 3 \end{cases}$$

#### **a) Valor de $m$ para que la matriz de coeficientes $A$ sea regular (invertible)**
Matriz de coeficientes $A$:
$$A = \begin{bmatrix} 2 & -1 & -2 \\ 1 & 1 & 3 \\ m & 0 & 1 \end{bmatrix}$$

Calculamos el determinante de $A$ mediante desarrollo por cofactores en la fila 3 ($F_3$):
$$\det(A) = m \cdot (-1)^{3+1} \begin{vmatrix} -1 & -2 \\ 1 & 3 \end{vmatrix} + 0 \cdot (-1)^{3+2} + 1 \cdot (-1)^{3+3} \begin{vmatrix} 2 & -1 \\ 1 & 1 \end{vmatrix}$$
$$\det(A) = m \cdot (1) \cdot (-3 - (-2)) + 1 \cdot (1) \cdot (2 - (-1))$$
$$\det(A) = m(-1) + 1(3) = 3 - m$$

Para que la matriz $A$ sea **regular** (no singular, invertible), su determinante debe ser no nulo:
$$\det(A) \neq 0 \iff 3 - m \neq 0 \iff \mathbf{m \neq 3}$$

---

#### **b) Valor(es) de $m$ para que el sistema NO tenga solución única**
Un sistema de ecuaciones lineales cuadradas $AX = B$ **no tiene solución única** si y solo si $\det(A) = 0$.
$$\det(A) = 0 \iff 3 - m = 0 \iff \mathbf{m = 3}$$

---

#### **c) Conjunto solución del sistema para $m = 3$**
Sustituimos $m = 3$ en la matriz aumentada $[A|B]$:

$$
[A|B] = \left[\begin{array}{ccc|c}
2 & -1 & -2 & 2 \\
1 & 1 & 3 & 1 \\
3 & 0 & 1 & 3
\end{array}\right]
$$

Aplicamos Eliminación Gaussiana (OEF):

1. Intercambiamos $F_1 \leftrightarrow F_2$:

$$
\left[\begin{array}{ccc|c}
1 & 1 & 3 & 1 \\
2 & -1 & -2 & 2 \\
3 & 0 & 1 & 3
\end{array}\right]
$$

2. $F_2 \leftarrow F_2 - 2F_1$ y $F_3 \leftarrow F_3 - 3F_1$:

$$F_2 \leftarrow [2-2, \, -1-2, \, -2-6 \mid 2-2] = [0, \, -3, \, -8 \mid 0]$$
$$F_3 \leftarrow [3-3, \, 0-3, \, 1-9 \mid 3-3] = [0, \, -3, \, -8 \mid 0]$$

La matriz queda:

$$
\left[\begin{array}{ccc|c}
1 & 1 & 3 & 1 \\
0 & -3 & -8 & 0 \\
0 & -3 & -8 & 0
\end{array}\right]
$$

3. $F_3 \leftarrow F_3 - F_2$:

$$
\left[\begin{array}{ccc|c}
1 & 1 & 3 & 1 \\
0 & -3 & -8 & 0 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

4. Escalamos $F_2 \leftarrow -\frac{1}{3}F_2$:

$$
\left[\begin{array}{ccc|c}
1 & 1 & 3 & 1 \\
0 & 1 & \frac{8}{3} & 0 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

5. $F_1 \leftarrow F_1 - F_2$:

$$F_1 \leftarrow \left[1-0, \, 1-1, \, 3 - \frac{8}{3} \;\middle|\; 1 - 0\right] = \left[1, \, 0, \, \frac{1}{3} \;\middle|\; 1\right]$$

Matriz en Forma Escalonada Reducida por Filas (RREF):

$$
\left[\begin{array}{ccc|c}
1 & 0 & \frac{1}{3} & 1 \\
0 & 1 & \frac{8}{3} & 0 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

Parametrización tomando la variable libre $z = t \in \mathbb{R}$:

$$
\begin{cases}
x + \frac{1}{3}t = 1 \implies x = 1 - \frac{1}{3}t \\
y + \frac{8}{3}t = 0 \implies y = -\frac{8}{3}t \\
z = t
\end{cases}
$$

> [!example] **Conjunto Solución Formal:**
> $$ \mathbf{S} = \left\{ \left( 1 - \frac{1}{3}t, \, -\frac{8}{3}t, \, t \right) : t \in \mathbb{R} \right\} $$

---

#### **d) Cálculo de la inversa $A^{-1}$ para $m = -1$ por el método de la Adjunta**
Para $m = -1$, la matriz $A$ es:
$$A = \begin{bmatrix} 2 & -1 & -2 \\ 1 & 1 & 3 \\ -1 & 0 & 1 \end{bmatrix}$$

##### **1. Determinante de $A$**
$$\det(A) = 3 - m = 3 - (-1) = 4 \neq 0$$

##### **2. Matriz de Cofactores $C = (C_{ij})$**
$$C_{11} = + \begin{vmatrix} 1 & 3 \\ 0 & 1 \end{vmatrix} = 1 - 0 = 1$$
$$C_{12} = - \begin{vmatrix} 1 & 3 \\ -1 & 1 \end{vmatrix} = -(1 - (-3)) = -4$$
$$C_{13} = + \begin{vmatrix} 1 & 1 \\ -1 & 0 \end{vmatrix} = 0 - (-1) = 1$$

$$C_{21} = - \begin{vmatrix} -1 & -2 \\ 0 & 1 \end{vmatrix} = -(-1 - 0) = 1$$
$$C_{22} = + \begin{vmatrix} 2 & -2 \\ -1 & 1 \end{vmatrix} = 2 - 2 = 0$$
$$C_{23} = - \begin{vmatrix} 2 & -1 \\ -1 & 0 \end{vmatrix} = -(0 - 1) = 1$$

$$C_{31} = + \begin{vmatrix} -1 & -2 \\ 1 & 3 \end{vmatrix} = -3 - (-2) = -1$$
$$C_{32} = - \begin{vmatrix} 2 & -2 \\ 1 & 3 \end{vmatrix} = -(6 - (-2)) = -8$$
$$C_{33} = + \begin{vmatrix} 2 & -1 \\ 1 & 1 \end{vmatrix} = 2 - (-1) = 3$$

Matriz de cofactores $C$:
$$C = \begin{bmatrix} 1 & -4 & 1 \\ 1 & 0 & 1 \\ -1 & -8 & 3 \end{bmatrix}$$

##### **3. Matriz Adjunta $\text{Adj}(A) = C^T$**
$$\text{Adj}(A) = \begin{bmatrix} 1 & 1 & -1 \\ -4 & 0 & -8 \\ 1 & 1 & 3 \end{bmatrix}$$

##### **4. Cálculo de la Inversa $A^{-1} = \frac{1}{\det(A)} \text{Adj}(A)$**
$$A^{-1} = \frac{1}{4} \begin{bmatrix} 1 & 1 & -1 \\ -4 & 0 & -8 \\ 1 & 1 & 3 \end{bmatrix} = \mathbf{\begin{bmatrix} \frac{1}{4} & \frac{1}{4} & -\frac{1}{4} \\[6pt] -1 & 0 & -2 \\[6pt] \frac{1}{4} & \frac{1}{4} & \frac{3}{4} \end{bmatrix}}$$

> [!important] **Verificación Computacional:**
> Validación simbólica formal realizada mediante **SymPy** (`verificar_repaso_solemne1.py`).

---
## 🔗 Conexiones
- [README Principal](../../README.md)
- [Dashboard de Álgebra Lineal](../../README.md)
- [Unidad 1: Matrices y Sistemas de Ecuaciones Lineales](../../Teoria/Unidad_1_Matrices_y_Sistemas/Matrices.md)
- [Resolución Taller 1 — Álgebra Lineal](Resolucion_TALLER_1_ALGEBRA_LINEAL.md)
- [Resolución Taller 2 — Álgebra Lineal](Resolucion_TALLER_2_ALGEBRA_LINEAL.md)
- [Resolución Solemne 1 2025-1](Resolucion_SOLEMNE_1_2025_1.md)
