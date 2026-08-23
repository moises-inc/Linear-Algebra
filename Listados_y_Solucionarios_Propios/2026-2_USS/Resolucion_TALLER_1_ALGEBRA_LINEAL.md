---
title: "Resolución Completa Taller 1 — Matrices, Determinantes e Inversas"
tags: [university, algebra_lineal, matrices, determinantes, inversa, taller]
---

# Resolución Completa Taller 1 — Matrices, Determinantes e Inversas

> [!abstract] Taller 1 · Álgebra Lineal · USS
> **Profesora:** Carol Asencio G. — **Estudiante:** Moisés Amundarain Romero
> **Contenido:** Operaciones con matrices (1.1–1.6), determinantes (2.1–2.7) y matriz inversa (3.1–3.9).
> **Método:** paso a paso con Operaciones Elementales por Filas (OEF) explícitas, verificación numérica con **SymPy** (`01_Sistemas_Lineales/verificar_taller1.py`) e ilustraciones generadas con Matplotlib (paleta USS `#00205B` / `#D4AF37`).

---
## 🗺️ Mapa de respuestas (resultados finales)

| # | Resultado clave | Ver dónde |
|:---|:---|:---|
| 1.1 | $A$: 0 diagonal, $+1$ sobre ella, $-1$ bajo ella | [1.1 Matrices por fórmula](#11-matrices-por-fórmula) |
| 1.2 | $(AB)^T = B^T A^T$ y $(A+B)^T = A^T + B^T$ verificadas | [1.2 Suma, producto y traspuestas](#12-suma-producto-y-traspuestas) |
| 1.3 | $AB = \begin{pmatrix}1&6\\6&13\end{pmatrix}$; $b), k), l)$ **imposibles** | [1.3 Cálculo matricial combinado](#13-cálculo-matricial-combinado) |
| 1.4 | $X_{ii} = \begin{pmatrix}-1/2&0\\-1&0\end{pmatrix}$; $X_{iii} = \begin{pmatrix}3/4&1/2\\3/4&1/4\end{pmatrix}$ | [1.4 Ecuaciones matriciales](#14-ecuaciones-matriciales) |
| 1.5 | $X^3 - X^2 - 5X + 5I_3 = \theta_3$ ✓ | [1.5 Polinomio de X](#15-polinomio-de-x) |
| 1.6 | $(x,y,z,w) = (-9/10, -3/5, 3/10, -3/10)$ | [1.6 Igualdad con incógnitas](#16-igualdad-con-incógnitas) |
| 2.1 | $\det\begin{pmatrix}3&4\\2&5\end{pmatrix} = 7$; $d)=0$ | [2.1 Determinantes 2x2](#21-determinantes-2x2) |
| 2.2 | $\det B_3 = -57$; k) $=-969$ | [2.2 Propiedades de determinantes](#22-propiedades-de-determinantes) |
| 2.3 | a) $113$; b) $-145$; c) $\ln(9e^6) = 6 + \ln 9$ | [2.3 Evaluación de determinantes](#23-evaluación-de-determinantes) |
| 2.4 | $\det(kA) = 2k^2$ | [2.4 Potencias y escala](#24-potencias-y-escala) |
| 2.5 | $\det = (b-a)(c-a)(c-b)$ (Vandermonde) | [2.5 Determinante de Vandermonde](#25-determinante-de-vandermonde) |
| 2.6 | Raíz real $\lambda = 1$ (además $\pm i$) | [2.6 Valores propios](#26-valores-propios) |
| 2.7 | a) $-5$; b) $300$; c) $5$; d) $-10$ | [2.7 Determinantes con datos](#27-determinantes-con-datos) |
| 3.1 | $X = \frac{1}{3}(BA + 3AB)$ | [3.1 Ecuación con traspuestas](#31-ecuación-con-traspuestas) |
| 3.2 | d) **no tiene solución** (E singular) | [3.2 Ecuaciones con inversas](#32-ecuaciones-con-inversas) |
| 3.3 | a) $X = \begin{pmatrix}1&1\\0&0\end{pmatrix}$; b) **imposible** | [3.3 Ecuaciones simples](#33-ecuaciones-simples) |
| 3.4 | $A^{-1} = \frac{1}{14}\begin{pmatrix}4&2\\1&4\end{pmatrix}$; $B$ no invertible | [3.4 Menores, cofactores y adjunta](#34-menores-cofactores-y-adjunta) |
| 3.5 | $X_3 = \begin{pmatrix}5&3/2\\-27/2&-17/4\end{pmatrix}$ | [3.5 Inversas y ecuaciones](#35-inversas-y-ecuaciones) |
| 3.6 | $X = \begin{pmatrix}6&9&12\\9&9&12\\12&12&12\end{pmatrix}$ | [3.6 Ecuación con A^T A](#36-ecuación-con-at-a) |
| 3.7 | a) $\lambda=5$; b) $\lambda=3/4$; c) $\lambda\in\{-2,-4/3\}$ | [3.7 Parámetro λ](#37-parámetro-λ) |
| 3.8 | a) $k = \frac{5\pm\sqrt{17}}{2}$; b) $k = 1\pm\sqrt{3}$ | [3.8 Matrices singulares](#38-matrices-singulares) |
| 3.9 | invertible $\iff a \neq \frac{1}{23}$ | [3.9 Invertibilidad 4x4](#39-invertibilidad-4x4) |

---

# 1. Operaciones con matrices

## 1.1 Matrices por fórmula

> [!example] Definiciones
> Con $i,j \in \{1,2,3,4\}$:
> $$a_{ij} = \begin{cases} 1 & i<j \\ -1 & i>j \\ 0 & i=j \end{cases} \qquad b_{ij} = (-1)^{i+j}(i+j) \qquad c_{ij} = (-1)^{i-j}(i\cdot j)$$

**Matriz $A$ (patrón "triangular de signos"):** sobre la diagonal todo $1$, bajo la diagonal todo $-1$, diagonal $0$:

$$
A = \begin{pmatrix}
0 & 1 & 1 & 1 \\
-1 & 0 & 1 & 1 \\
-1 & -1 & 0 & 1 \\
-1 & -1 & -1 & 0
\end{pmatrix}
$$

**Matriz $B$:** el signo $(-1)^{i+j}$ alterna como un tablero de ajedrez ($+$ cuando $i+j$ es par). Ejemplo: $b_{14} = (-1)^5\cdot 5 = -5$:

$$
B = \begin{pmatrix}
2 & -3 & 4 & -5 \\
-3 & 4 & -5 & 6 \\
4 & -5 & 6 & -7 \\
-5 & 6 & -7 & 8
\end{pmatrix}
$$

**Matriz $C$:** $i-j$ es par cuando $i$ y $j$ tienen la misma paridad (signo $+$), impar si no (signo $-$):

$$
C = \begin{pmatrix}
1 & -2 & 3 & -4 \\
-2 & 4 & -6 & 8 \\
3 & -6 & 9 & -12 \\
-4 & 8 & -12 & 16
\end{pmatrix}
$$

> [!tip] Truco de memoria (TDAH)
> En $C$, la fila $i$ es $i \times$ (fila 1 con signos alternados $+,-,+,-$). La columna $j$ es $j \times$ (columna 1 con signos alternados $+,-,+,-$).

---

## 1.2 Suma, producto y traspuestas

$$
A = \begin{pmatrix} 3 & 1 & 0 \\ 4 & 0 & 2 \\ -1 & 5 & 1 \end{pmatrix}
\qquad
B = \begin{pmatrix} 2 & 4 & -1 \\ 3 & 5 & 2 \\ -2 & 4 & -1 \end{pmatrix}
$$

**a) $A+B$** (componente a componente):

$$
A + B = \begin{pmatrix} 3+2 & 1+4 & 0+(-1) \\ 4+3 & 0+5 & 2+2 \\ -1+(-2) & 5+4 & 1+(-1) \end{pmatrix}
= \begin{pmatrix} 5 & 5 & -1 \\ 7 & 5 & 4 \\ -3 & 9 & 0 \end{pmatrix}
$$

**b) $AB$** (producto fila $\times$ columna; ver Figura 1). Ejemplo del elemento $(1,2)$: $3\cdot 4 + 1\cdot 5 + 0\cdot 4 = 17$:

$$
AB = \begin{pmatrix}
9 & 17 & -1 \\
4 & 24 & -6 \\
11 & 25 & 10
\end{pmatrix}
$$

**c) $BA$** — note que $AB \neq BA$:

$$
BA = \begin{pmatrix}
23 & -3 & 7 \\
27 & 13 & 12 \\
11 & -7 & 7
\end{pmatrix}
$$

> [!warning] ¡Ojo!
> $AB \neq BA$. El producto de matrices **no es conmutativo** (basta este ejemplo: $AB = \dots \neq BA$). Por eso en g) y h) los resultados difieren.

**d) $(AB)^T$** (traspuesta de b):

$$
(AB)^T = \begin{pmatrix} 9 & 4 & 11 \\ 17 & 24 & 25 \\ -1 & -6 & 10 \end{pmatrix}
$$

**e) $A^T$ y f) $B^T$:**

$$
A^T = \begin{pmatrix} 3 & 4 & -1 \\ 1 & 0 & 5 \\ 0 & 2 & 1 \end{pmatrix}
\qquad
B^T = \begin{pmatrix} 2 & 3 & -2 \\ 4 & 5 & 4 \\ -1 & 2 & -1 \end{pmatrix}
$$

**g) $A^T B^T$ y h) $B^T A^T$:**

$$
A^T B^T = \begin{pmatrix} 23 & 27 & 11 \\ -3 & 13 & -7 \\ 7 & 12 & 7 \end{pmatrix}
\qquad
B^T A^T = \begin{pmatrix} 9 & 4 & 11 \\ 17 & 24 & 25 \\ -1 & -6 & 10 \end{pmatrix}
$$

**i) $(A+B)^T$ y j) $A^T + B^T$:**

$$
(A+B)^T = \begin{pmatrix} 5 & 7 & -3 \\ 5 & 5 & 9 \\ -1 & 4 & 0 \end{pmatrix}
\qquad
A^T + B^T = \begin{pmatrix} 5 & 7 & -3 \\ 5 & 5 & 9 \\ -1 & 4 & 0 \end{pmatrix}
$$

**k) y l) Comprobaciones:**

> [!important] Resultado Clave — Propiedades de la traspuesta
> $$(AB)^T = B^T A^T \qquad \text{y} \qquad (A+B)^T = A^T + B^T$$
> Comparando d) con h): $(AB)^T = B^T A^T = \begin{pmatrix}9&4&11\\17&24&25\\-1&-6&10\end{pmatrix}$ ✓
> Comparando i) con j): son idénticas ✓ (verificado numéricamente con SymPy, `True` para ambas).

![Figura1_producto_matrices](../../05_Simulaciones_y_Visualizaciones/Figura1_producto_matrices.png)

---

## 1.3 Cálculo matricial combinado

$$
A = \begin{pmatrix}-1&2\\2&3\end{pmatrix}\quad
B = \begin{pmatrix}1&0\\0&1\end{pmatrix}\quad
C = \begin{pmatrix}1&0&-1\\2&1&3\end{pmatrix}\quad
D = \begin{pmatrix}2&0\\1&2\\1&3\end{pmatrix}\quad
E = \begin{pmatrix}1&1\\-1&1\end{pmatrix}
$$

> [!warning] Ojo con las Dimensiones
> Aquí $C$ es de orden $2\times 3$ y $D$ de orden $3\times 2$ (¡verificado leyendo el PDF por coordenadas!). Eso hace **imposibles** los ítems **b), k) y l)**, pero **posibles** c), f) y p).

| Ítem | Operación | Resultado |
|:---:|:---|:---|
| a) | $3A$ | $\begin{pmatrix}-3&6\\6&9\end{pmatrix}$ |
| **b)** | $A + C$ | ❌ **No definida**: $2\times2 + 2\times3$ |
| c) | $CD$ | $\begin{pmatrix}1&-3\\8&11\end{pmatrix}$ ($2\times3 \cdot 3\times2$) |
| d) | $A - B$ | $\begin{pmatrix}-2&2\\2&2\end{pmatrix}$ |
| e) | $3A + 4B$ | $\begin{pmatrix}-3&6\\6&9\end{pmatrix} + \begin{pmatrix}4&0\\0&4\end{pmatrix} = \begin{pmatrix}1&6\\6&13\end{pmatrix}$ |
| f) | $AB + CD$ | $\begin{pmatrix}-1&2\\2&3\end{pmatrix} + \begin{pmatrix}1&-3\\8&11\end{pmatrix} = \begin{pmatrix}0&-1\\10&14\end{pmatrix}$ |
| g) | $7A$ | $\begin{pmatrix}-7&14\\14&21\end{pmatrix}$ |
| h) | $kE$ | $\begin{pmatrix}k&k\\-k&k\end{pmatrix}$ |
| i) | $8A + E$ | $\begin{pmatrix}-7&17\\15&25\end{pmatrix}$ |
| j) | $AE$ | $\begin{pmatrix}-3&1\\-1&5\end{pmatrix}$ |
| **k)** | $A(B+C)$ | ❌ **No definida**: $B+C$ ( $2\times2+2\times3$ ) |
| **l)** | $AB + AC$ | ❌ **No definida**: $AC$ es $2\times2 \cdot 2\times3$ |
| m) | $A+B$ | $\begin{pmatrix}0&2\\2&4\end{pmatrix}$ |
| n) | $B+A$ | $\begin{pmatrix}0&2\\2&4\end{pmatrix}$ (igual a m), conmutatividad de la suma ✓) |
| ñ) | $AA = A^2$ | $\begin{pmatrix}1+4&-2+6\\-2+6&4+9\end{pmatrix} = \begin{pmatrix}5&4\\4&13\end{pmatrix}$ |
| o) | $EE$ | $\begin{pmatrix}1-1&1+1\\-1-1&-1+1\end{pmatrix} = \begin{pmatrix}0&2\\-2&0\end{pmatrix}$ |
| p) | $(AB)C$ | $AB = A$; luego $\begin{pmatrix}-1&2\\2&3\end{pmatrix}\begin{pmatrix}1&0&-1\\2&1&3\end{pmatrix} = \begin{pmatrix}3&2&7\\8&3&7\end{pmatrix}$ |

> [!example] Verificación Algebraica
> En ñ): $AA_{11} = (-1)(-1) + 2\cdot 2 = 5$; $AA_{12} = (-1)(2) + 2\cdot 3 = 4$; $AA_{22} = 2\cdot 2 + 3\cdot 3 = 13$. En o): $EE_{12} = 1\cdot 1 + 1\cdot 1 = 2$; $EE_{21} = (-1)(1) + 1(-1) = -2$.

---

## 1.4 Ecuaciones matriciales

$$
A = \begin{pmatrix}3&2\\1&0\end{pmatrix}\quad
B = \begin{pmatrix}2&1\\2&1\end{pmatrix}\quad
C = \begin{pmatrix}1&1\\0&1\end{pmatrix}\quad
D = \begin{pmatrix}1&1&3\\1&1&-2\end{pmatrix}
$$

**a) Cálculos directos:**

$$
AB = \begin{pmatrix}10&5\\2&1\end{pmatrix}
\qquad
BA = \begin{pmatrix}7&4\\7&4\end{pmatrix}
$$

$$
DD^T = \begin{pmatrix}1&1&3\\1&1&-2\end{pmatrix}
\begin{pmatrix}1&1\\1&1\\3&-2\end{pmatrix}
= \begin{pmatrix}1+1+9 & 1+1-6 \\ 1+1-6 & 1+1+4\end{pmatrix}
= \begin{pmatrix}11&-4\\-4&6\end{pmatrix}
$$

$$
DD^T - C = \begin{pmatrix}11&-4\\-4&6\end{pmatrix} - \begin{pmatrix}1&1\\0&1\end{pmatrix} = \begin{pmatrix}10&-5\\-4&5\end{pmatrix}
$$

$$
C^2 = \begin{pmatrix}1&1\\0&1\end{pmatrix}^2 = \begin{pmatrix}1&2\\0&1\end{pmatrix}
\Rightarrow
AC^2 - I = \begin{pmatrix}3&2\\1&0\end{pmatrix}\begin{pmatrix}1&2\\0&1\end{pmatrix} - \begin{pmatrix}1&0\\0&1\end{pmatrix}
= \begin{pmatrix}3&8\\1&2\end{pmatrix} - I = \begin{pmatrix}2&8\\1&1\end{pmatrix}
$$

**b) Solución de las ecuaciones:**

**i)** $-2X + C = B \Rightarrow X = \frac{C - B}{2} = \frac{1}{2}\begin{pmatrix}1-2&1-1\\0-2&1-1\end{pmatrix} = \begin{pmatrix}-1/2&0\\-1&0\end{pmatrix}$

**ii)** $\left(A - \frac{2}{3}X\right)^T = 2C$. Traspongo ambos lados (la traspuesta de la traspuesta es la matriz):

$$
A - \tfrac{2}{3}X = (2C)^T = 2C^T
\Rightarrow
X = \tfrac{3}{2}\left(A - 2C^T\right)
= \tfrac{3}{2}\left(\begin{pmatrix}3&2\\1&0\end{pmatrix} - \begin{pmatrix}2&0\\2&2\end{pmatrix}\right)
= \begin{pmatrix}3/2 & 3 \\ -3/2 & -3\end{pmatrix}
$$

**iii)** $3X + C^T = 2B - X \Rightarrow 4X = 2B - C^T$:

$$
X = \frac{1}{4}\left(\begin{pmatrix}4&2\\4&2\end{pmatrix} - \begin{pmatrix}1&0\\1&1\end{pmatrix}\right)
= \begin{pmatrix}3/4 & 1/2 \\ 3/4 & 1/4\end{pmatrix}
$$

> [!important] Resultado Clave
> Verificación automática (SymPy): ii) y iii) reproducen la ecuación original con `True`.

---

## 1.5 Polinomio de $X$

$$
X = \begin{pmatrix}1&2&0\\2&-1&0\\0&0&1\end{pmatrix}
$$

Cálculo de potencias (el bloque $2\times2$ es simétrico y su cuadrado es $5I_2$):

$$
X^2 = \begin{pmatrix}5&0&0\\0&5&0\\0&0&1\end{pmatrix},
\qquad
X^3 = X^2 X = \begin{pmatrix}5&10&0\\10&-5&0\\0&0&1\end{pmatrix}
$$

Ahora la combinación pedida:

$$
X^3 - X^2 - 5X + 5I_3 =
\begin{pmatrix}5&10&0\\10&-5&0\\0&0&1\end{pmatrix}
- \begin{pmatrix}5&0&0\\0&5&0\\0&0&1\end{pmatrix}
- \begin{pmatrix}5&10&0\\10&-5&0\\0&0&5\end{pmatrix}
+ \begin{pmatrix}5&0&0\\0&5&0\\0&0&5\end{pmatrix}
= \begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix} = \theta_3
$$

> [!important] Resultado Clave
> $X$ satisface su propia ecuación polinomial: $X^3 - X^2 - 5X + 5I_3 = \theta_3$ ✓ (SymPy confirma matriz nula).
> **Contexto:** este es el espíritu del **Teorema de Cayley–Hamilton**: toda matriz cuadrada anula a su polinomio característico (Cayley lo probó para $2\times2$ en 1858; Frobenius lo generalizó en 1878 — MacTutor, St Andrews).

---

## 1.6 Igualdad con incógnitas

$$
\begin{pmatrix}2&1\\-2&3\end{pmatrix}
\begin{pmatrix}x+y & y \\ z & z-w\end{pmatrix}
=
\begin{pmatrix}x & y \\ 3+x & z-w\end{pmatrix}
\begin{pmatrix}1&2\\3&-2\end{pmatrix}
$$

Desarrollo de cada lado (producto fila $\times$ columna):

$$
\text{LHS} = \begin{pmatrix}
2(x+y) + 1\cdot z & 2y + 1\cdot(z-w) \\
-2(x+y) + 3\cdot z & -2y + 3(z-w)
\end{pmatrix}
= \begin{pmatrix}
2x+2y+z & 2y+z-w \\
-2x-2y+3z & -2y+3z-3w
\end{pmatrix}
$$

$$
\text{RHS} = \begin{pmatrix}
x\cdot 1 + y\cdot 3 & x\cdot 2 + y\cdot(-2) \\
(3+x)\cdot 1 + (z-w)\cdot 3 & (3+x)\cdot 2 + (z-w)\cdot(-2)
\end{pmatrix}
= \begin{pmatrix}
x+3y & 2x-2y \\
3+x+3z-3w & 6+2x-2z+2w
\end{pmatrix}
$$

Igualando coeficiente a coeficiente ($\text{LHS}_{ij} = \text{RHS}_{ij}$) para las 4 posiciones:

1. **Posición (1,1):** $2x + 2y + z = x + 3y \implies x - y + z = 0$
2. **Posición (1,2):** $2y + z - w = 2x - 2y \implies 2x - 4y - z + w = 0$
3. **Posición (2,1):** $-2x - 2y + 3z = 3 + x + 3z - 3w \implies 3x + 2y - 3w = -3$
4. **Posición (2,2):** $-2y + 3z - 3w = 6 + 2x - 2z + 2w \implies 2x + 2y - 5z + 5w = -6$

Obtenemos el sistema lineal $4\times 4$:

$$
\begin{cases}
x - y + z = 0 \\
2x - 4y - z + w = 0 \\
3x + 2y - 3w = -3 \\
2x + 2y - 5z + 5w = -6
\end{cases}
$$

### 📋 Resolución Paso a Paso por Eliminación Gaussiana y Gauss-Jordan

Formamos la **matriz ampliada** del sistema $[A \mid \mathbf{b}]$:

$$
[A \mid \mathbf{b}] = \left[\begin{array}{cccc|c}
\mathbf{1} & -1 & 1 & 0 & 0 \\
2 & -4 & -1 & 1 & 0 \\
3 & 2 & 0 & -3 & -3 \\
2 & 2 & -5 & 5 & -6
\end{array}\right]
$$

#### Paso 1: Anulación de la Columna 1 bajo el primer pivote ($a_{11} = 1$)
Aplicamos las siguientes Operaciones Elementales por Filas (OEF):
- $F_2 \to F_2 - 2F_1$
- $F_3 \to F_3 - 3F_1$
- $F_4 \to F_4 - 2F_1$

$$
\xrightarrow{\substack{F_2 \to F_2 - 2F_1 \\ F_3 \to F_3 - 3F_1 \\ F_4 \to F_4 - 2F_1}}
\left[\begin{array}{cccc|c}
1 & -1 & 1 & 0 & 0 \\
0 & \mathbf{-2} & -3 & 1 & 0 \\
0 & 5 & -3 & -3 & -3 \\
0 & 4 & -7 & 5 & -6
\end{array}\right]
$$

#### Paso 2: Anulación de la Columna 2 bajo el segundo pivote ($a_{22} = -2$)
Para anular los elementos debajo de la fila 2:
- $F_3 \to F_3 + \frac{5}{2}F_2$
- $F_4 \to F_4 + 2F_2$

Cálculos detallados:
- En $F_3$: $-3 + \frac{5}{2}(-3) = -\frac{21}{2}$, $-3 + \frac{5}{2}(1) = -\frac{1}{2}$, $-3 + \frac{5}{2}(0) = -3$.
- En $F_4$: $-7 + 2(-3) = -13$, $5 + 2(1) = 7$, $-6 + 2(0) = -6$.

$$
\xrightarrow{\substack{F_3 \to F_3 + \frac{5}{2}F_2 \\ F_4 \to F_4 + 2F_2}}
\left[\begin{array}{cccc|c}
1 & -1 & 1 & 0 & 0 \\
0 & -2 & -3 & 1 & 0 \\
0 & 0 & \mathbf{-\frac{21}{2}} & -\frac{1}{2} & -3 \\
0 & 0 & -13 & 7 & -6
\end{array}\right]
$$

#### Paso 3: Anulación de la Columna 3 bajo el tercer pivote ($a_{33} = -\frac{21}{2}$)
Aplicamos la OEF:
- $F_4 \to F_4 - \frac{-13}{-21/2}F_3 = F_4 - \frac{26}{21}F_3$

Cálculos detallados:
- En Columna 4: $7 - \frac{26}{21}\left(-\frac{1}{2}\right) = 7 + \frac{13}{21} = \frac{147 + 13}{21} = \frac{160}{21}$.
- En Término Independiente: $-6 - \frac{26}{21}(-3) = -6 + \frac{78}{21} = -6 + \frac{26}{7} = \frac{-42 + 26}{7} = -\frac{16}{7} = -\frac{48}{21}$.

$$
\xrightarrow{F_4 \to F_4 - \frac{26}{21}F_3}
\left[\begin{array}{cccc|c}
1 & -1 & 1 & 0 & 0 \\
0 & -2 & -3 & 1 & 0 \\
0 & 0 & -\frac{21}{2} & -\frac{1}{2} & -3 \\
0 & 0 & 0 & \mathbf{\frac{160}{21}} & -\frac{16}{7}
\end{array}\right]
$$

> [!important] Forma Escalonada por Filas (REF) y Clasificación
> La matriz de coeficientes tiene 4 pivotes no nulos ($1, -2, -\frac{21}{2}, \frac{160}{21}$):
> $$\operatorname{rango}(A) = \operatorname{rango}(A \mid \mathbf{b}) = 4 = n \text{ (número de incógnitas)}$$
> Según el **Teorema de Rouché-Frobenius**, el sistema es **Compatible Determinado** (solución única).

#### Paso 4: Sustitución Regresiva (Fase de Jordan hacia RREF)
1. **De la Fila 4:**
 $$\frac{160}{21}w = -\frac{16}{7} \implies w = \left(-\frac{16}{7}\right) \cdot \left(\frac{21}{160}\right) = -\frac{3}{10}$$

2. **De la Fila 3:**
 $$-\frac{21}{2}z - \frac{1}{2}w = -3 \implies -\frac{21}{2}z - \frac{1}{2}\left(-\frac{3}{10}\right) = -3$$
 $$-\frac{21}{2}z + \frac{3}{20} = -3 \implies -\frac{21}{2}z = -3 - \frac{3}{20} = -\frac{63}{20} \implies z = \left(-\frac{63}{20}\right)\left(-\frac{2}{21}\right) = \frac{3}{10}$$

3. **De la Fila 2:**
 $$-2y - 3z + w = 0 \implies -2y = 3z - w = 3\left(\frac{3}{10}\right) - \left(-\frac{3}{10}\right) = \frac{9}{10} + \frac{3}{10} = \frac{12}{10} = \frac{6}{5}$$
 $$y = \frac{6/5}{-2} = -\frac{3}{5}$$

4. **De la Fila 1:**
 $$x - y + z = 0 \implies x = y - z = -\frac{3}{5} - \frac{3}{10} = -\frac{6}{10} - \frac{3}{10} = -\frac{9}{10}$$

Matriz final en **Forma Escalonada Reducida por Filas (RREF)**:

$$
\left[\begin{array}{cccc|c}
1 & 0 & 0 & 0 & -\frac{9}{10} \\
0 & 1 & 0 & 0 & -\frac{3}{5} \\
0 & 0 & 1 & 0 & \frac{3}{10} \\
0 & 0 & 0 & 1 & -\frac{3}{10}
\end{array}\right]
$$

> [!important] Resultado Clave
> $$x = -\frac{9}{10}, \qquad y = -\frac{3}{5}, \qquad z = \frac{3}{10}, \qquad w = -\frac{3}{10}$$
> Verificación en matrices originales: ambos productos matriciales arrojan la matriz idéntica $\begin{pmatrix}-3/2&-6/5\\-3/10&-6/5\end{pmatrix}$ ✓.

---

# 2. Cálculo de Determinantes

> [!info] Propiedades que usaremos (Cauchy, 1812)
> $|\det(A^T) = \det(A)|$ · $|\det(kA) = k^n\det(A)|$ · $|\det(AB) = \det(A)\det(B)|$ · si una fila es múltiplo de otra, $\det = 0$ · el intercambio de dos filas cambia el signo · sumar un múltiplo de una fila a otra **no altera** el determinante.

## 2.1 Determinantes $2\times2$

Fórmula: $\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad - bc$.

| Ítem | Matriz | Cálculo | Resultado |
|:---:|:---|:---|:---:|
| a) | $\begin{pmatrix}3&4\\2&5\end{pmatrix}$ | $3\cdot 5 - 4\cdot 2 = 15 - 8$ | $\mathbf{7}$ |
| b) | $\begin{pmatrix}0&3\\-1&7\end{pmatrix}$ | $0\cdot 7 - 3(-1) = 0 + 3$ | $\mathbf{3}$ |
| c) | $\begin{pmatrix}5&7\\6&2\end{pmatrix}$ | $5\cdot 2 - 7\cdot 6 = 10 - 42$ | $\mathbf{-32}$ |
| d) | $\begin{pmatrix}a&b\\2a&2b\end{pmatrix}$ | $a\cdot 2b - b\cdot 2a = 2ab - 2ab$ | $\mathbf{0}$ |

> [!example] d) — por propiedad
> La fila 2 es $2\times$ la fila 1 ($F_2 = 2F_1$): **fila proporcional $\Rightarrow \det = 0$**. No hay que calcular nada.

---

## 2.2 Propiedades de determinantes

Considere las siguientes matrices cuadradas de orden $2\times 2$ y $3\times 3$:

$$
A_2 = \begin{pmatrix}4 & -2 \\ -1 & 4\end{pmatrix}, \qquad
A_3 = \begin{pmatrix}1 & -2 & 3 \\ -1 & 4 & 5 \\ -3 & 6 & -9\end{pmatrix}, \qquad
B_2 = \begin{pmatrix}1 & -2 \\ -1 & 4\end{pmatrix}
$$
$$
B_3 = \begin{pmatrix}1 & -2 & 5 \\ -1 & 4 & -2 \\ 4 & -1 & 2\end{pmatrix}, \qquad
C_2 = \begin{pmatrix}1 & -1 \\ 0 & 3\end{pmatrix}, \qquad
C_3 = \begin{pmatrix}1 & -1 & 3 \\ 0 & 3 & 2 \\ 0 & 0 & -1\end{pmatrix}
$$

### 📌 1. Cálculo de los Determinantes Base

Antes de aplicar las propiedades algebraicas, calculamos el determinante de cada una de las 6 matrices:

1. **Determinante de $A_2 \in \mathcal{M}_{2\times 2}(\mathbb{R})$:**
 $$\det(A_2) = (4)(4) - (-2)(-1) = 16 - 2 = \mathbf{14}$$

2. **Determinante de $A_3 \in \mathcal{M}_{3\times 3}(\mathbb{R})$:**
 Observamos que la Fila 3 es múltiplo escalar de la Fila 1 ($F_3 = -3F_1$):
 $$\det(A_3) = \begin{vmatrix} 1 & -2 & 3 \\ -1 & 4 & 5 \\ -3 & 6 & -9 \end{vmatrix} \xrightarrow{F_3 \to F_3 + 3F_1} \begin{vmatrix} 1 & -2 & 3 \\ -1 & 4 & 5 \\ 0 & 0 & 0 \end{vmatrix} = \mathbf{0}$$

3. **Determinante de $B_2 \in \mathcal{M}_{2\times 2}(\mathbb{R})$:**
 $$\det(B_2) = (1)(4) - (-2)(-1) = 4 - 2 = \mathbf{2}$$

4. **Determinante de $B_3 \in \mathcal{M}_{3\times 3}(\mathbb{R})$ (Regla de Sarrus / Cofactores):**
 $$\det(B_3) = (1)(4)(2) + (-2)(-2)(4) + (5)(-1)(-1) - (4)(4)(5) - (-1)(-2)(1) - (2)(-1)(-2)$$
 $$\det(B_3) = 8 + 16 + 5 - 80 - 2 - 4 = 29 - 86 = \mathbf{-57}$$

5. **Determinante de $C_2 \in \mathcal{M}_{2\times 2}(\mathbb{R})$ (Triangular superior):**
 $$\det(C_2) = (1)(3) - (-1)(0) = \mathbf{3}$$

6. **Determinante de $C_3 \in \mathcal{M}_{3\times 3}(\mathbb{R})$ (Triangular superior):**
 $$\det(C_3) = 1 \cdot 3 \cdot (-1) = \mathbf{-3}$$

---

### 📊 2. Tabla Resumen de Propiedades Aplicadas

| Ítem | Expresión | Propiedad Utilizada | Desarrollo / Justificación | Resultado Final |
|:---:|:---|:---|:---|:---:|
| **a)** | $\det(A_2^T)$ | $\det(M^T) = \det(M)$ | $\det(A_2^T) = \det(A_2) = 14$ | $\mathbf{14}$ |
| **b)** | $\det(-2B_3^T)$ | $\det(kM) = k^n \det(M)$ con $n=3$ | $(-2)^3 \det(B_3^T) = -8(-57)$ | $\mathbf{456}$ |
| **c)** | $\det(B_2^T A_2)$ | $\det(MN) = \det(M)\det(N)$ | $\det(B_2)\det(A_2) = 2 \cdot 14$ | $\mathbf{28}$ |
| **d)** | $\det(B_2)$ | Determinante directo | Directo de base | $\mathbf{2}$ |
| **e)** | $\det(C_3^T)$ | $\det(M^T) = \det(M)$ | $\det(C_3^T) = \det(C_3) = -3$ | $\mathbf{-3}$ |
| **f)** | $\det(B_2^T)$ | $\det(M^T) = \det(M)$ | $\det(B_2^T) = \det(B_2) = 2$ | $\mathbf{2}$ |
| **g)** | $\det(A_2 B_2)$ | $\det(MN) = \det(M)\det(N)$ | $\det(A_2)\det(B_2) = 14 \cdot 2$ | $\mathbf{28}$ |
| **h)** | $\det(A_3 B_3^T)$ | $\det(MN) = \det(M)\det(N)$ | $\det(A_3)\det(B_3) = 0 \cdot (-57)$ | $\mathbf{0}$ |
| **i)** | $\det(A_3 B_3)$ | $\det(MN) = \det(M)\det(N)$ | $\det(A_3)\det(B_3) = 0 \cdot (-57)$ | $\mathbf{0}$ |
| **j)** | $\det(B_2 C_2 A_2)$ | Multiplicatividad asociativa | $\det(B_2)\det(C_2)\det(A_2) = 2 \cdot 3 \cdot 14$ | $\mathbf{84}$ |
| **k)** | $\det(B_3^T (A_3 - C_3))$ | $\det(MN) = \det(M)\det(N)$ | $\det(B_3) \cdot \det(A_3 - C_3) = (-57)(17)$ | $\mathbf{-969}$ |

---

### 📝 3. Desarrollo Detallado y Explicación Paso a Paso de Cada Ítem

#### a) $\lvert A_2^T \rvert = \det(A_2^T)$
* **Propiedad:** El determinante de la transpuesta de una matriz es igual al determinante de la matriz original ($\det(M^T) = \det(M)$).
* **Cálculo:**
 $$\det(A_2^T) = \det(A_2) = \mathbf{14}$$

#### b) $\lvert -2B_3^T \rvert = \det(-2B_3^T)$
* **Propiedad:** Para toda matriz $M \in \mathcal{M}_{n\times n}(\mathbb{R})$ y escalar $k \in \mathbb{R}$, se cumple $\det(kM) = k^n \det(M)$. Aquí $B_3$ es de orden $n=3$, luego el factor escalar sale elevado al cubo ($k^3$).
* **Cálculo:**
 $$\det(-2B_3^T) = (-2)^3 \det(B_3^T) = -8 \det(B_3) = -8(-57) = \mathbf{456}$$
> [!warning] Error Frecuente
> Olvidar elevar la constante al orden $n$. Un error común es escribir $-2\det(B_3)$ en lugar de $(-2)^3\det(B_3) = -8\det(B_3)$.

#### c) $\lvert B_2^T \cdot A_2 \rvert = \det(B_2^T A_2)$
* **Propiedad (Teorema de Cauchy-Binet):** El determinante del producto de matrices cuadradas es el producto de sus determinantes ($\det(MN) = \det(M)\det(N)$).
* **Cálculo:**
 $$\det(B_2^T A_2) = \det(B_2^T) \cdot \det(A_2) = \det(B_2) \cdot \det(A_2) = 2 \cdot 14 = \mathbf{28}$$

#### d) $\lvert B_2 \rvert = \det(B_2)$
* **Cálculo:**
 $$\det(B_2) = \mathbf{2}$$

#### e) $\lvert C_3^T \rvert = \det(C_3^T)$
* **Propiedad:** Invarianza bajo transposición ($\det(C_3^T) = \det(C_3)$).
* **Cálculo:**
 $$\det(C_3^T) = \det(C_3) = \mathbf{-3}$$

#### f) $\lvert B_2^T \rvert = \det(B_2^T)$
* **Propiedad:** $\det(B_2^T) = \det(B_2)$.
* **Cálculo:**
 $$\det(B_2^T) = \mathbf{2}$$

#### g) $\lvert A_2 \cdot B_2 \rvert = \det(A_2 B_2)$
* **Propiedad:** $\det(A_2 B_2) = \det(A_2)\det(B_2)$.
* **Cálculo:**
 $$\det(A_2 B_2) = 14 \cdot 2 = \mathbf{28}$$
> [!tip] Observación de Conmutatividad
> Nótese que aunque en general $A_2 B_2 \neq B_2 A_2$, sus determinantes **siempre coinciden**: $\det(A_2 B_2) = \det(B_2 A_2) = 28$.

#### h) $\lvert A_3 B_3^T \rvert = \det(A_3 B_3^T)$
* **Propiedad:** $\det(A_3 B_3^T) = \det(A_3)\det(B_3^T)$.
* **Cálculo:** Como $A_3$ es singular ($\det A_3 = 0$):
 $$\det(A_3 B_3^T) = 0 \cdot (-57) = \mathbf{0}$$

#### i) $\lvert A_3 B_3 \rvert = \det(A_3 B_3)$
* **Propiedad:** $\det(A_3 B_3) = \det(A_3)\det(B_3)$.
* **Cálculo:**
 $$\det(A_3 B_3) = 0 \cdot (-57) = \mathbf{0}$$

#### j) $\lvert B_2 \cdot C_2 \cdot A_2 \rvert = \det(B_2 C_2 A_2)$
* **Propiedad:** Multiplicatividad extendida a $k$ matrices cuadradas del mismo orden.
* **Cálculo:**
 $$\det(B_2 C_2 A_2) = \det(B_2) \cdot \det(C_2) \cdot \det(A_2) = 2 \cdot 3 \cdot 14 = \mathbf{84}$$

#### k) $\lvert B_3^T (A_3 - C_3) \rvert = \det(B_3^T (A_3 - C_3))$
* **Propiedad:** Por multiplicatividad:
 $$\det(B_3^T (A_3 - C_3)) = \det(B_3^T) \cdot \det(A_3 - C_3) = \det(B_3) \cdot \det(A_3 - C_3)$$
* **Paso 1: Cálculo de la matriz diferencia $(A_3 - C_3)$:**
 $$A_3 - C_3 = \begin{pmatrix}1 & -2 & 3 \\ -1 & 4 & 5 \\ -3 & 6 & -9\end{pmatrix} - \begin{pmatrix}1 & -1 & 3 \\ 0 & 3 & 2 \\ 0 & 0 & -1\end{pmatrix} = \begin{pmatrix}0 & -1 & 0 \\ -1 & 1 & 3 \\ -3 & 6 & -8\end{pmatrix}$$
* **Paso 2: Determinante de $(A_3 - C_3)$ por expansión en la Fila 1:**
 $$\det(A_3 - C_3) = 0 \cdot C_{11} - (-1)\cdot \begin{vmatrix}-1 & 3 \\ -3 & -8\end{vmatrix} + 0 \cdot C_{13} = 1 \cdot \big((-1)(-8) - (3)(-3)\big) = 1 \cdot (8 + 9) = \mathbf{17}$$
* **Paso 3: Producto final:**
 $$\det(B_3^T (A_3 - C_3)) = (-57) \cdot 17 = \mathbf{-969}$$

> [!important] Verificación Numérica
> Todos los resultados anteriores fueron verificados de forma exacta mediante SymPy (`verificar_taller1.py`), confirmando 100% de consistencia algebraica.

![Figura2_sarrus_cofactores](../../05_Simulaciones_y_Visualizaciones/Figura2_sarrus_cofactores.png)

---

## 2.3 Evaluación de determinantes

**a)** $\begin{vmatrix}-3&-6&-1\\-4&-3&-2\\5&-4&-4\end{vmatrix}$. Desarrollo por la fila 1 ($\det = a_{11}M_{11} - a_{12}M_{12} + a_{13}M_{13}$):

$$
M_{11} = \begin{vmatrix}-3&-2\\-4&-4\end{vmatrix} = 12 - 8 = 4
\quad
M_{12} = \begin{vmatrix}-4&-2\\5&-4\end{vmatrix} = 16 + 10 = 26
\quad
M_{13} = \begin{vmatrix}-4&-3\\5&-4\end{vmatrix} = 16 + 15 = 31
$$

$$
\det = (-3)(4) - (-6)(26) + (-1)(31) = -12 + 156 - 31 = \mathbf{113}
$$

**b)** $\begin{vmatrix}1&-1&1&2\\3&-2&4&3\\5&4&1&2\\-3&0&3&1\end{vmatrix}$. Presentamos dos métodos rigurosos para comparar su eficiencia y desarrollo:

#### 🔹 Método 1: Desarrollo por Cofactores de Laplace (Columna 1)
Expandiendo por la columna 1 ($C_{i1} = (-1)^{i+1}M_{i1}$, alternando $+,-,+,-$):

$$
\det = 1\cdot\begin{vmatrix}-2&4&3\\4&1&2\\0&3&1\end{vmatrix}
- 3\cdot\begin{vmatrix}-1&1&2\\4&1&2\\0&3&1\end{vmatrix}
+ 5\cdot\begin{vmatrix}-1&1&2\\-2&4&3\\0&3&1\end{vmatrix}
- (-3)\cdot\begin{vmatrix}-1&1&2\\-2&4&3\\4&1&2\end{vmatrix}
$$

Calculando los menores $3\times 3$ por Sarrus:
- $M_{11} = (-2)(1)(1) + (4)(2)(0) + (3)(4)(3) - (0)(1)(3) - (3)(2)(-2) - (1)(4)(4) = -2 + 0 + 36 - 0 + 12 - 16 = 30$.
- $M_{21} = (-1)(1)(1) + (1)(2)(0) + (2)(4)(3) - (0)(1)(2) - (3)(2)(-1) - (1)(4)(1) = -1 + 0 + 24 - 0 + 6 - 4 = 25$.
- $M_{31} = (-1)(4)(1) + (1)(3)(0) + (2)(-2)(3) - (0)(4)(2) - (3)(3)(-1) - (1)(-2)(1) = -4 + 0 - 12 - 0 + 9 + 2 = -5$.
- $M_{41} = (-1)(4)(2) + (1)(3)(4) + (2)(-2)(1) - (4)(4)(2) - (1)(3)(-1) - (2)(-2)(1) = -8 + 12 - 4 - 32 + 3 + 4 = -25$.

$$
\det = 1(30) - 3(25) + 5(-5) + 3(-25) = 30 - 75 - 25 - 75 = \mathbf{-145}
$$

#### 🔹 Método 2: Reducción Gaussiana a Matriz Triangular Superior (OEF)
> [!tip] Propiedad Invariante de OEF en Determinantes
> La operación de sumar a una fila un múltiplo escalar de otra ($F_i \to F_i + cF_j$) **no altera el valor del determinante** ($\det(A') = \det(A)$).

**Paso 1:** Con el pivote $a_{11} = 1$, anulamos la columna 1:
- $F_2 \to F_2 - 3F_1$
- $F_3 \to F_3 - 5F_1$
- $F_4 \to F_4 + 3F_1$

$$
\det = \begin{vmatrix}1&-1&1&2\\3&-2&4&3\\5&4&1&2\\-3&0&3&1\end{vmatrix}
= \begin{vmatrix}
\mathbf{1} & -1 & 1 & 2 \\
0 & \mathbf{1} & 1 & -3 \\
0 & 9 & -4 & -8 \\
0 & -3 & 6 & 7
\end{vmatrix}
$$

**Paso 2:** Con el segundo pivote $a_{22} = 1$, anulamos la columna 2 bajo la fila 2:
- $F_3 \to F_3 - 9F_2$
- $F_4 \to F_4 + 3F_2$

$$
= \begin{vmatrix}
1 & -1 & 1 & 2 \\
0 & 1 & 1 & -3 \\
0 & 0 & \mathbf{-13} & 19 \\
0 & 0 & 9 & -2
\end{vmatrix}
$$

**Paso 3:** Con el tercer pivote $a_{33} = -13$, anulamos la posición (4,3):
- $F_4 \to F_4 + \frac{9}{13}F_3$

Cálculo en la posición (4,4): $-2 + \frac{9}{13}(19) = -\frac{26}{13} + \frac{171}{13} = \frac{145}{13}$.

$$
= \begin{vmatrix}
\mathbf{1} & -1 & 1 & 2 \\
0 & \mathbf{1} & 1 & -3 \\
0 & 0 & \mathbf{-13} & 19 \\
0 & 0 & 0 & \mathbf{\frac{145}{13}}
\end{vmatrix}
$$

**Paso 4:** La matriz ha quedado en **Forma Triangular Superior**. El determinante es simplemente el producto de su diagonal principal:

$$
\det = (1) \cdot (1) \cdot (-13) \cdot \left(\frac{145}{13}\right) = -13 \cdot \frac{145}{13} = \mathbf{-145}
$$

> [!important] Comparación Didáctica (TDAH / TEA)
> La reducción gaussiana reduce la complejidad de cálculo de $O(n!)$ (Laplace) a $O(n^3)$ operaciones elementales, evitando tener que calcular 4 determinantes $3\times 3$ separados. Ambos métodos convergen exactamente en $\mathbf{-145}$ ✓.

**c)** $\ln\left|\det\begin{pmatrix}e^2 & -5e^2 \\ e^4 & 4e^4\end{pmatrix}\right|$:

$$
\det = e^2\cdot 4e^4 - (-5e^2)(e^4) = 4e^6 + 5e^6 = 9e^6 > 0
$$

$$
\ln(9e^6) = \ln 9 + \ln e^6 = \mathbf{6 + \ln 9} \;\; (= 6 + 2\ln 3)
$$

> [!example] Truco con exponenciales
> $\ln$ y $e$ son funciones inversas: $\ln(e^6) = 6$. El factor $9$ "baja" como $\ln 9$.

---

## 2.4 Potencias y escala

$A \in \mathcal{M}_{2\times2}(\mathbb{R})$ con $\det(A) = 2$. Por el teorema de multiplicación de Cauchy, $\det(A^m) = (\det A)^m$, y por la propiedad de escala $\det(kA) = k^2\det(A)$ (orden $n=2$):

| Ítem | Expresión | Resultado |
|:---:|:---|:---:|
| a) | $\det(A^2)$ | $2^2 = \mathbf{4}$ |
| b) | $\det(A^3)$ | $2^3 = \mathbf{8}$ |
| c) | $\det(A^{100})$, $n\in\mathbb{N}$ | $\mathbf{2^n}$ (en general $\det(A^n) = 2^n$) |
| d) | $\det(2A)$ | $2^2\cdot 2 = \mathbf{8}$ |
| e) | $\det(3A)$ | $3^2\cdot 2 = \mathbf{18}$ |
| f) | $\det(kA)$, $k\in\mathbb{R}$ | $\mathbf{2k^2}$ |

> [!warning] ¡Ojo!
> $\det(kA) = k^{\mathbf{n}}\det(A)$ con $n$ = orden. Para $2\times2$ es $k^2$; para $3\times3$ sería $k^3$. Verificado: SymPy confirma $\det(A^2) = \det(A)^2$ en un ejemplo genérico.

---

## 2.5 Determinante de Vandermonde

$$
A = \begin{pmatrix}1&a&a^2\\1&b&b^2\\1&c&c^2\end{pmatrix}
\qquad \text{Probar: } \det(A) = (b-a)(c-a)(c-b)
$$

**Prueba por OEF.** Aplicamos $F_2 \to F_2 - F_1$ y $F_3 \to F_3 - F_1$ (sumar múltiplos de una fila **no cambia** el determinante):

$$
\det(A) = \begin{vmatrix}1&a&a^2\\0&b-a&b^2-a^2\\0&c-a&c^2-a^2\end{vmatrix}
= \begin{vmatrix}b-a&(b-a)(b+a)\\c-a&(c-a)(c+a)\end{vmatrix}
$$

Sacando factores $(b-a)$ de la fila 2 y $(c-a)$ de la fila 3 (propiedad de escala):

$$
\det(A) = (b-a)(c-a)\begin{vmatrix}1&b+a\\1&c+a\end{vmatrix}
= (b-a)(c-a)\big[(c+a) - (b+a)\big]
= (b-a)(c-a)(c-b)
$$

> [!important] Resultado Clave
> $$\det(A) = (b-a)(c-a)(c-b) \quad \blacksquare$$
> **Contexto:** esta matriz lleva el nombre de **Alexandre-Théophile Vandermonde** (1735–1796), quien en 1771 publicó métodos para calcular determinantes. El determinante de Vandermonde $\prod_{i<j}(x_j - x_i)$ es la base de la interpolación polinomial y aparece en el código corrector Reed–Solomon (discos duros, QR codes).

---

## 2.6 Valores propios

$$
A = \begin{pmatrix}0&1&2\\-1&0&1\\0&0&1\end{pmatrix}
$$

Formamos $A - \lambda I$ y anulamos su determinante (la condición para que el sistema $(A-\lambda I)\mathbf{v} = \mathbf{0}$ tenga soluciones no triviales, o equivalentemente, para que la matriz sea singular):

$$
A - \lambda I = \begin{pmatrix}-\lambda&1&2\\-1&-\lambda&1\\0&0&1-\lambda\end{pmatrix}
$$

Expandiendo por la fila 3 (dos ceros):

$$
\det(A-\lambda I) = (1-\lambda)\begin{vmatrix}-\lambda&1\\-1&-\lambda\end{vmatrix}
= (1-\lambda)(\lambda^2 + 1)
$$

$$
(1-\lambda)(\lambda^2 + 1) = 0
\quad\Rightarrow\quad
\lambda = 1 \quad \text{o} \quad \lambda^2 = -1 \;\Rightarrow\; \lambda = \pm i
$$

> [!important] Resultado Clave
> $$p(\lambda) = (1-\lambda)(\lambda^2+1) \quad\Rightarrow\quad \lambda \in \{1,\, i,\, -i\}$$
> En $\mathbb{R}$ (como pide el enunciado: $\lambda\in\mathbb{R}$), la única solución es $\mathbf{\lambda = 1}$.
> **Contexto:** el polinomio $\det(A-\lambda I)$ se llama **polinomio característico**; sus raíces son los valores propios. Cauchy (1826) los estudió al diagonalizar formas cuadráticas, y D'Alembert (1747) los usó antes, en el movimiento de cuerdas con masas (MacTutor).

![Figura3_valores_propios](../../05_Simulaciones_y_Visualizaciones/Figura3_valores_propios.png)

---

## 2.7 Determinantes con datos

Sea $A = \begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix}$ con $|A| = 5$.

> [!warning] Errata detectada en el PDF (ítem a)
> En la página 3 del enunciado, la fila 2 del determinante a) aparece como $(d,\;e,\;i)$, lo que es una **errata tipográfica** (repite la $i$). La fila debe ser $(d,\;e,\;f)$, como exige el ejercicio (con $f$ el resultado es determinable a partir de $|A|=5$; con $i$ sería indeterminado). Resolvemos la versión correcta $(d,e,f)$.

**a)** $\begin{vmatrix}g&h&i\\d&e&f\\a&b&c\end{vmatrix}$: la fila 1 del nuevo determinante era la fila 3 de $A$, y la fila 3 era la fila 1: se **intercambiaron dos filas** (una transposición, permutación impar):

$$
\det = -\det(A) = \mathbf{-5}
$$

**b)** $\begin{vmatrix}-5g&-5h&-5i\\3d&3e&3f\\4a&4b&4c\end{vmatrix}$: filas escaladas por $-5$, $3$ y $4$, y reordenadas según la permutación $(3,2,1)$ (una transposición → signo $-$):

$$
\det = (-5)(3)(4)\cdot(-1)\cdot\det(A) = (-60)(-1)(5) = \mathbf{300}
$$

**c)** $\begin{vmatrix}a-b&b&c\\d-e&e&f\\g-h&h&i\end{vmatrix}$: aplicar la OEF $C_1 \to C_1 + C_2$ (o equivalentemente ver la primera columna como "columna 1 − columna 2"; sumar un múltiplo de una columna a otra **no cambia** el determinante):

$$
\det = \begin{vmatrix}a&b&c\\d&e&f\\g&h&i\end{vmatrix} = \mathbf{5}
$$

**d)** $\begin{vmatrix}2a-2d&2b-2e&2c-2f\\g&h&i\\d&e&f\end{vmatrix}$: la fila 1 es $2\cdot(F_1 - F_2)$ de $A$ (la fila 1 del original menos su fila 2), con las filas permutadas a $(1,3,2)$ (una transposición):

$$
\det = 2\cdot\left[\begin{vmatrix}a&b&c\\g&h&i\\d&e&f\end{vmatrix} - \underbrace{\begin{vmatrix}d&e&f\\g&h&i\\d&e&f\end{vmatrix}}_{=0\ \text{(filas iguales)}}\right]
= 2\cdot(-5) = \mathbf{-10}
$$

> [!example] Verificación simbólica
> SymPy confirma: a) $-5$, b) $60\cdot\det(A) = 300$, c) $5$, d) $-2\det(A) = -10$, sustituyendo $\det A = 5$.

---

# 3. Matriz inversa y Determinantes

> [!info] Teorema de invertibilidad
> $A$ es invertible $\iff \det(A) \neq 0$. Si lo es, $A^{-1} = \dfrac{1}{\det(A)}\,\mathrm{adj}(A)$, con $\mathrm{adj}(A) = [\mathrm{Cof}(A)]^T$ (Cayley, 1858). Las ecuaciones $AX = B$, $XA = B$ y $AXC = B$ se resuelven premultiplicando / postmultiplicando por las inversas correspondientes (cuando existen).

## 3.1 Ecuación con traspuestas

$$
2X^t - (3AB)^t = A^t B^t - X^t
$$

con $A = \begin{pmatrix}2&1&5\\0&-2&1\\0&0&3\end{pmatrix}$ y $B = \begin{pmatrix}3&4&7\\4&2&-1\\7&-1&2\end{pmatrix}$.

Usamos las propiedades $(AB)^T = B^T A^T$, $(kM)^T = kM^T$ y $(M^T)^T = M$:

$$
2X^T - 3B^T A^T = A^T B^T - X^T
\;\Rightarrow\;
3X^T = A^T B^T + 3B^T A^T
\;\Rightarrow\;
X = \frac{BA + 3AB}{3}
$$

> [!warning] ¡Ojo con las Dimensiones!
> Al traspasar el producto $AB$ el orden se invierte: $(AB)^T = B^T A^T$. Un clásico de error: escribir $(AB)^T = A^T B^T$.

Cálculo de los productos (SymPy verifica la ecuación completa):

$$
AB = \begin{pmatrix}45&5&23\\-1&-5&4\\21&-3&6\end{pmatrix}
\qquad
BA = \begin{pmatrix}6&-5&40\\8&0&19\\14&9&40\end{pmatrix}
$$

$$
X = \frac{1}{3}\left(\begin{pmatrix}6&-5&40\\8&0&19\\14&9&40\end{pmatrix} + 3\begin{pmatrix}45&5&23\\-1&-5&4\\21&-3&6\end{pmatrix}\right)
= \frac{1}{3}\begin{pmatrix}141&10&109\\5&-15&31\\77&0&58\end{pmatrix}
$$

> [!important] Resultado Clave
> $$X = \begin{pmatrix}47&10/3&109/3\\5/3&-5&31/3\\77/3&0&58/3\end{pmatrix}$$
> Verificación: $2X^T - 3(AB)^T - (A^TB^T - X^T) = \theta_3$ → `True`.

---

## 3.2 Ecuaciones con inversas

Matrices (de ejercicios anteriores):

$$
A = \begin{pmatrix}4&-2\\-1&4\end{pmatrix},\quad
B = \begin{pmatrix}1&-2&3\\-1&4&5\\-3&6&-9\end{pmatrix},\quad
C = \begin{pmatrix}1&-2\\-1&4\end{pmatrix},
$$
$$
D = \begin{pmatrix}1&-2&5\\-1&4&-2\\4&-1&2\end{pmatrix},\quad
E = \begin{pmatrix}1&-1&2\\0&3&-4\\1&-1&2\end{pmatrix},\quad
F = \begin{pmatrix}1&-1&3\\0&3&2\\0&0&-1\end{pmatrix}
$$

**a) $A\cdot X = C$.**
Como $\det(A) = 16 - 2 = 14 \neq 0$, la matriz es invertible. Resolvemos directamente mediante **Eliminación de Gauss-Jordan** sobre la matriz ampliada $[A \mid C]$:

$$
[A \mid C] = \left[\begin{array}{cc|cc}
4 & -2 & 1 & -2 \\
-1 & 4 & -1 & 4
\end{array}\right]
$$

- **Paso 1 (Intercambio de filas para pivote unitario):** $F_1 \leftrightarrow F_2$
 $$
 \xrightarrow{F_1 \leftrightarrow F_2}
 \left[\begin{array}{cc|cc}
 -1 & 4 & -1 & 4 \\
 4 & -2 & 1 & -2
 \end{array}\right]
 \xrightarrow{F_1 \to -F_1}
 \left[\begin{array}{cc|cc}
 \mathbf{1} & -4 & 1 & -4 \\
 4 & -2 & 1 & -2
 \end{array}\right]
 $$
- **Paso 2 (Anular bajo el pivote 1):** $F_2 \to F_2 - 4F_1$
 $$
 \xrightarrow{F_2 \to F_2 - 4F_1}
 \left[\begin{array}{cc|cc}
 1 & -4 & 1 & -4 \\
 0 & \mathbf{14} & -3 & 14
 \end{array}\right]
 $$
- **Paso 3 (Normalizar pivote 2 y anular hacia arriba):** $F_2 \to \frac{1}{14}F_2$, luego $F_1 \to F_1 + 4F_2$
 $$
 \xrightarrow{F_2 \to \frac{1}{14}F_2}
 \left[\begin{array}{cc|cc}
 1 & -4 & 1 & -4 \\
 0 & 1 & -3/14 & 1
 \end{array}\right]
 \xrightarrow{F_1 \to F_1 + 4F_2}
 \left[\begin{array}{cc|cc}
 1 & 0 & 1/7 & 0 \\
 0 & 1 & -3/14 & 1
 \end{array}\right]
 $$

> [!important] Resultado Clave
> $$X = \begin{pmatrix}1/7 & 0 \\ -3/14 & 1\end{pmatrix}$$

---

**b) $(B+D)\cdot X = F^T \cdot E$.** Primeramente calculamos los bloques:

$$
B+D = \begin{pmatrix}1&-2&3\\-1&4&5\\-3&6&-9\end{pmatrix} + \begin{pmatrix}1&-2&5\\-1&4&-2\\4&-1&2\end{pmatrix}
= \begin{pmatrix}2&-4&8\\-2&8&3\\1&5&-7\end{pmatrix}
$$

$$
F^T E = \begin{pmatrix}1&0&0\\-1&3&0\\3&2&-1\end{pmatrix}\begin{pmatrix}1&-1&2\\0&3&-4\\1&-1&2\end{pmatrix}
= \begin{pmatrix}1&-1&2\\-1&10&-14\\2&4&-4\end{pmatrix}
$$

Como $\det(B+D) = -242 \neq 0$, resolvemos la ecuación matricial mediante **Gauss-Jordan** sobre $[(B+D) \mid F^T E]$:

$$
\left[\begin{array}{ccc|ccc}
2 & -4 & 8 & 1 & -1 & 2 \\
-2 & 8 & 3 & -1 & 10 & -14 \\
1 & 5 & -7 & 2 & 4 & -4
\end{array}\right]
$$

- **Paso 1 (Pivote superior):** $F_1 \leftrightarrow F_3$ para tener pivote $1$:
 $$
 \xrightarrow{F_1 \leftrightarrow F_3}
 \left[\begin{array}{ccc|ccc}
 \mathbf{1} & 5 & -7 & 2 & 4 & -4 \\
 -2 & 8 & 3 & -1 & 10 & -14 \\
 2 & -4 & 8 & 1 & -1 & 2
 \end{array}\right]
 $$
- **Paso 2 (Anulación Columna 1):** $F_2 \to F_2 + 2F_1$, $F_3 \to F_3 - 2F_1$
 $$
 \xrightarrow{\substack{F_2 \to F_2 + 2F_1 \\ F_3 \to F_3 - 2F_1}}
 \left[\begin{array}{ccc|ccc}
 1 & 5 & -7 & 2 & 4 & -4 \\
 0 & \mathbf{18} & -11 & 3 & 18 & -22 \\
 0 & -14 & 22 & -3 & -9 & 10
 \end{array}\right]
 $$
- **Paso 3 (Anulación Columna 2):** $F_3 \to F_3 + \frac{7}{9}F_2$
 $$
 \xrightarrow{F_3 \to F_3 + \frac{7}{9}F_2}
 \left[\begin{array}{ccc|ccc}
 1 & 5 & -7 & 2 & 4 & -4 \\
 0 & 18 & -11 & 3 & 18 & -22 \\
 0 & 0 & \mathbf{\frac{121}{9}} & -\frac{6}{9} & \frac{45}{9} & -\frac{64}{9}
 \end{array}\right]
 $$
 *(Matriz en Forma Escalonada por Filas - REF)*
- **Paso 4 (Normalizar Fila 3 y eliminación hacia arriba):** $F_3 \to \frac{9}{121}F_3$
 $$
 \xrightarrow{F_3 \to \frac{9}{121}F_3}
 \left[\begin{array}{ccc|ccc}
 1 & 5 & -7 & 2 & 4 & -4 \\
 0 & 18 & -11 & 3 & 18 & -22 \\
 0 & 0 & 1 & -\frac{6}{121} & \frac{45}{121} & -\frac{64}{121}
 \end{array}\right]
 $$
- **Paso 5 (Anular Columna 3 arriba):** $F_2 \to F_2 + 11F_3$, $F_1 \to F_1 + 7F_3$, luego $F_2 \to \frac{1}{18}F_2$ y $F_1 \to F_1 - 5F_2$:
 $$
 \xrightarrow{\text{Gauss-Jordan}}
 \left[\begin{array}{ccc|ccc}
 1 & 0 & 0 & \frac{235}{242} & \frac{113}{242} & \frac{3}{121} \\
 0 & 1 & 0 & \frac{3}{22} & \frac{27}{22} & -\frac{17}{11} \\
 0 & 0 & 1 & -\frac{6}{121} & \frac{45}{121} & -\frac{64}{121}
 \end{array}\right]
 $$

> [!important] Resultado Clave
> $$X = \begin{pmatrix}235/242 & 113/242 & 3/121 \\ 3/22 & 27/22 & -17/11 \\ -6/121 & 45/121 & -64/121\end{pmatrix}$$
> Verificación SymPy: $(B+D)X = F^TE$ → `True`.

---

**c) $C\cdot X\cdot A^T = A\cdot C$.** Premultiplicamos por $C^{-1}$ y postmultiplicamos por $(A^T)^{-1}$:

$$
X = C^{-1} A C (A^T)^{-1}
$$

$C^{-1} = \frac{1}{2}\begin{pmatrix}4&2\\1&1\end{pmatrix}$, $(A^T)^{-1} = (A^{-1})^T = \frac{1}{14}\begin{pmatrix}4&1\\2&4\end{pmatrix}$:

$$
X = \frac{1}{2}\begin{pmatrix}4&2\\1&1\end{pmatrix}\begin{pmatrix}4&-2\\-1&4\end{pmatrix}\begin{pmatrix}1&-2\\-1&4\end{pmatrix}\frac{1}{14}\begin{pmatrix}4&1\\2&4\end{pmatrix}
= \begin{pmatrix}0&-7/2\\2/7&9/28\end{pmatrix}
$$

---

**d) $E^T \cdot X \cdot F = B - D$.**

> [!warning] Restricción Crítica — ¡$E$ es singular!
> Como $F_3 = F_1$ en $E$, $\det(E) = 0$ y $\det(E^T) = 0$. No existe inversa para despejar algebraicamente.

#### 🔍 Demostración por Reducción Escalonada y Teorema de Rouché-Frobenius
Aplicamos OEF a la matriz de coeficientes $E^T$:

$$
E^T = \begin{pmatrix} 1 & 0 & 1 \\ -1 & 3 & -1 \\ 2 & -4 & 2 \end{pmatrix}
\xrightarrow{\substack{F_2 \to F_2 + F_1 \\ F_3 \to F_3 - 2F_1}}
\begin{pmatrix} 1 & 0 & 1 \\ 0 & 3 & 0 \\ 0 & -4 & 0 \end{pmatrix}
\xrightarrow{F_3 \to F_3 + \frac{4}{3}F_2}
\begin{pmatrix} \mathbf{1} & 0 & 1 \\ 0 & \mathbf{3} & 0 \\ 0 & 0 & \mathbf{0} \end{pmatrix}
$$

La matriz $E^T$ tiene solo **2 pivotes no nulos** $\implies \operatorname{rango}(E^T) = 2 < 3$.

Para que la ecuación matricial $E^T Y = B - D$ (donde $Y = XF$) sea compatible, cada columna de $B - D$ debe pertenecer al espacio columna de $E^T$.
Calculamos $B - D$:

$$
B - D = \begin{pmatrix}1&-2&3\\-1&4&5\\-3&6&-9\end{pmatrix} - \begin{pmatrix}1&-2&5\\-1&4&-2\\4&-1&2\end{pmatrix}
= \begin{pmatrix}0 & 0 & -2 \\ 0 & 0 & 7 \\ \mathbf{-7} & 7 & -11\end{pmatrix}
$$

Tomando la primera columna $\mathbf{b}_1 = \begin{pmatrix}0\\0\\-7\end{pmatrix}$ y reduciendo la matriz ampliada $[E^T \mid \mathbf{b}_1]$:

$$
\left[\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
-1 & 3 & -1 & 0 \\
2 & -4 & 2 & -7
\end{array}\right]
\xrightarrow{\substack{F_2 \to F_2 + F_1 \\ F_3 \to F_3 - 2F_1}}
\left[\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
0 & 3 & 0 & 0 \\
0 & -4 & 0 & -7
\end{array}\right]
\xrightarrow{F_3 \to F_3 + \frac{4}{3}F_2}
\left[\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
0 & 3 & 0 & 0 \\
\mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{-7}
\end{array}\right]
$$

La tercera fila representa la ecuación $0y_1 + 0y_2 + 0y_3 = -7$ ($0 = -7$, absurdo).
Por el **Teorema de Rouché-Frobenius**:
$$\operatorname{rango}(E^T) = 2 < \operatorname{rango}(E^T \mid \mathbf{b}_1) = 3 \implies \textbf{Sistema Incompatible}$$

> [!important] Conclusión
> **No existe solución** $X \in \mathcal{M}_3(\mathbb{R})$ (conjunto vacío $\emptyset$, validado con SymPy: `EmptySet`).

---

## 3.3 Ecuaciones simples

**a)** $\begin{pmatrix}1&3\\1&2\end{pmatrix} X = \begin{pmatrix}1&1\\1&1\end{pmatrix}$.
Como $\det = 2 - 3 = -1 \neq 0$, la matriz de coeficientes es invertible. Resolvemos paso a paso mediante **Eliminación de Gauss-Jordan** sobre la matriz ampliada:

$$
\left[\begin{array}{cc|cc}
\mathbf{1} & 3 & 1 & 1 \\
1 & 2 & 1 & 1
\end{array}\right]
\xrightarrow{F_2 \to F_2 - F_1}
\left[\begin{array}{cc|cc}
1 & 3 & 1 & 1 \\
0 & \mathbf{-1} & 0 & 0
\end{array}\right]
\xrightarrow{F_2 \to -F_2}
\left[\begin{array}{cc|cc}
1 & 3 & 1 & 1 \\
0 & \mathbf{1} & 0 & 0
\end{array}\right]
$$

$$
\xrightarrow{F_1 \to F_1 - 3F_2}
\left[\begin{array}{cc|cc}
\mathbf{1} & 0 & 1 & 1 \\
0 & \mathbf{1} & 0 & 0
\end{array}\right]
\quad\Rightarrow\quad
X = \begin{pmatrix}1&1\\0&0\end{pmatrix}
$$

---

**b)** $X\begin{pmatrix}2&-1\\4&-2\end{pmatrix} = \begin{pmatrix}1&3\\6&2\end{pmatrix}$.

Sea $M = \begin{pmatrix}2&-1\\4&-2\end{pmatrix}$ y $R = \begin{pmatrix}1&3\\6&2\end{pmatrix}$. Aplicando la transposición a ambos lados:

$$
(X M)^T = R^T \iff M^T X^T = R^T \iff \begin{pmatrix}2&4\\-1&-2\end{pmatrix} X^T = \begin{pmatrix}1&6\\3&2\end{pmatrix}
$$

#### 🔍 Análisis por Eliminación Gaussiana y Teorema de Rouché-Frobenius
Formamos la matriz ampliada del sistema $[M^T \mid R^T]$:

$$
[M^T \mid R^T] = \left[\begin{array}{cc|cc}
\mathbf{2} & 4 & 1 & 6 \\
-1 & -2 & 3 & 2
\end{array}\right]
$$

Aplicamos la OEF $F_2 \to F_2 + \frac{1}{2}F_1$:

$$
\xrightarrow{F_2 \to F_2 + \frac{1}{2}F_1}
\left[\begin{array}{cc|cc}
\mathbf{2} & 4 & 1 & 6 \\
\mathbf{0} & \mathbf{0} & \mathbf{\frac{7}{2}} & \mathbf{5}
\end{array}\right]
$$

> [!warning] Inconsistencia Absoluta (Rouché-Frobenius)
> La fila 2 tiene ceros en los coeficientes pero valores no nulos en los términos independientes:
> - Para la columna 1: $0x_{11} + 0x_{12} = \frac{7}{2} \implies 0 = \frac{7}{2}$ (absurdo).
> - Para la columna 2: $0x_{21} + 0x_{22} = 5 \implies 0 = 5$ (absurdo).
>
> Por el **Teorema de Rouché-Frobenius**:
> $$\operatorname{rango}(M^T) = 1 < \operatorname{rango}(M^T \mid R^T) = 2 \implies \textbf{Sistema Incompatible}$$
> Por lo tanto, **la ecuación no tiene solución** (validado con SymPy: `EmptySet`).

---

**c)** $\begin{pmatrix}3&1\\2&1\end{pmatrix} X \begin{pmatrix}1&3\\1&2\end{pmatrix} = \begin{pmatrix}3&3\\2&2\end{pmatrix}$.

Sean $P = \begin{pmatrix}3&1\\2&1\end{pmatrix}$ (con $\det P = 3-2 = 1 \neq 0$) y $Q = \begin{pmatrix}1&3\\1&2\end{pmatrix}$ (con $\det Q = 2-3 = -1 \neq 0$).
Como ambas matrices son invertibles, despejamos:

$$
X = P^{-1} R \, Q^{-1}
$$

Calculamos las inversas $2\times 2$ por la fórmula directa / Gauss-Jordan:
- $P^{-1} = \frac{1}{1}\begin{pmatrix}1&-1\\-2&3\end{pmatrix} = \begin{pmatrix}1&-1\\-2&3\end{pmatrix}$
- $Q^{-1} = \frac{1}{-1}\begin{pmatrix}2&-3\\-1&1\end{pmatrix} = \begin{pmatrix}-2&3\\1&-1\end{pmatrix}$

Efectuamos el producto por etapas:

$$
P^{-1} R = \begin{pmatrix}1&-1\\-2&3\end{pmatrix}\begin{pmatrix}3&3\\2&2\end{pmatrix} = \begin{pmatrix}3-2 & 3-2 \\ -6+6 & -6+6\end{pmatrix} = \begin{pmatrix}1&1\\0&0\end{pmatrix}
$$

$$
X = (P^{-1} R) Q^{-1} = \begin{pmatrix}1&1\\0&0\end{pmatrix}\begin{pmatrix}-2&3\\1&-1\end{pmatrix} = \begin{pmatrix}-2+1 & 3-1 \\ 0 & 0\end{pmatrix} = \begin{pmatrix}-1&2\\0&0\end{pmatrix}
$$

> [!example] Verificación
> $P X Q = \begin{pmatrix}3&1\\2&1\end{pmatrix}\begin{pmatrix}-1&2\\0&0\end{pmatrix}\begin{pmatrix}1&3\\1&2\end{pmatrix} = \begin{pmatrix}-3&6\\-2&4\end{pmatrix}\begin{pmatrix}1&3\\1&2\end{pmatrix} = \begin{pmatrix}3&3\\2&2\end{pmatrix}$ ✓

---

## 3.4 Menores, cofactores y adjunta

Para cada matriz cuadrada $M$:
1. **Menor complementario $M_{ij}$:** determinante de la submatriz eliminando la fila $i$ y columna $j$.
2. **Cofactor $C_{ij}$:** $(-1)^{i+j}M_{ij}$.
3. **Matriz Adjunta $\operatorname{adj}(M)$:** traspuesta de la matriz de cofactores $[\operatorname{Cof}(M)]^T$.
4. **Matriz Inversa $M^{-1}$:** $\frac{1}{\det M}\operatorname{adj}(M)$ (si $\det M \neq 0$).

---

### 🔹 Matriz $A = \begin{pmatrix}4&-2\\-1&4\end{pmatrix}$

- $\det A = 16 - 2 = 14 \neq 0$ (invertible).
- **Menores:** $M_{11} = 4$, $M_{12} = -1$, $M_{21} = -2$, $M_{22} = 4 \implies \operatorname{Men}(A) = \begin{pmatrix}4&-1\\-2&4\end{pmatrix}$.
- **Cofactores:** $C_{11} = 4$, $C_{12} = 1$, $C_{21} = 2$, $C_{22} = 4 \implies \operatorname{Cof}(A) = \begin{pmatrix}4&1\\2&4\end{pmatrix}$.
- **Adjunta:** $\operatorname{adj}(A) = [\operatorname{Cof}(A)]^T = \begin{pmatrix}4&2\\1&4\end{pmatrix}$.
- **Inversa (Método de la Adjunta):**
 $$A^{-1} = \frac{1}{14}\begin{pmatrix}4&2\\1&4\end{pmatrix} = \begin{pmatrix}2/7&1/7\\1/14&2/7\end{pmatrix}$$

#### 🔄 Comparación Didáctica: Inversa de $A$ por Método de Gauss-Jordan $[A \mid I_2]$
$$
\left[\begin{array}{cc|cc}
4 & -2 & 1 & 0 \\
-1 & 4 & 0 & 1
\end{array}\right]
\xrightarrow{F_1 \leftrightarrow F_2}
\left[\begin{array}{cc|cc}
-1 & 4 & 0 & 1 \\
4 & -2 & 1 & 0
\end{array}\right]
\xrightarrow{F_1 \to -F_1}
\left[\begin{array}{cc|cc}
\mathbf{1} & -4 & 0 & -1 \\
4 & -2 & 1 & 0
\end{array}\right]
$$
$$
\xrightarrow{F_2 \to F_2 - 4F_1}
\left[\begin{array}{cc|cc}
1 & -4 & 0 & -1 \\
0 & \mathbf{14} & 1 & 4
\end{array}\right]
\xrightarrow{F_2 \to \frac{1}{14}F_2}
\left[\begin{array}{cc|cc}
1 & -4 & 0 & -1 \\
0 & \mathbf{1} & 1/14 & 2/7
\end{array}\right]
\xrightarrow{F_1 \to F_1 + 4F_2}
\left[\begin{array}{cc|cc}
\mathbf{1} & 0 & \mathbf{2/7} & \mathbf{1/7} \\
0 & \mathbf{1} & \mathbf{1/14} & \mathbf{2/7}
\end{array}\right]
$$
Ambos métodos coinciden con exactitud matemática ✓.

---

### 🔹 Matriz $B = \begin{pmatrix}1&-2&3\\-1&4&5\\-3&6&-9\end{pmatrix}$

- $\det B = 0$ debido a que $F_3 = -3F_1$ (filas linealmente dependientes).
- **Menores:**
 - Fila 1: $M_{11} = \begin{vmatrix}4&5\\6&-9\end{vmatrix} = -66$, $M_{12} = \begin{vmatrix}-1&5\\-3&-9\end{vmatrix} = 24$, $M_{13} = \begin{vmatrix}-1&4\\-3&6\end{vmatrix} = 6$.
 - Fila 2: $M_{21} = \begin{vmatrix}-2&3\\6&-9\end{vmatrix} = 0$, $M_{22} = \begin{vmatrix}1&3\\-3&-9\end{vmatrix} = 0$, $M_{23} = \begin{vmatrix}1&-2\\-3&6\end{vmatrix} = 0$.
 - Fila 3: $M_{31} = \begin{vmatrix}-2&3\\4&5\end{vmatrix} = -22$, $M_{32} = \begin{vmatrix}1&3\\-1&5\end{vmatrix} = 8$, $M_{33} = \begin{vmatrix}1&-2\\-1&4\end{vmatrix} = 2$.
 $$\operatorname{Men}(B) = \begin{pmatrix}-66&24&6\\0&0&0\\-22&8&2\end{pmatrix}$$
- **Cofactores:** $\operatorname{Cof}(B) = \begin{pmatrix}-66&-24&6\\0&0&0\\-22&-8&2\end{pmatrix}$.
- **Adjunta:** $\operatorname{adj}(B) = [\operatorname{Cof}(B)]^T = \begin{pmatrix}-66&0&-22\\-24&0&-8\\6&0&2\end{pmatrix}$.

#### 🔍 Intento de Inversión por Gauss-Jordan $[B \mid I_3]$
$$
\left[\begin{array}{ccc|ccc}
\mathbf{1} & -2 & 3 & 1 & 0 & 0 \\
-1 & 4 & 5 & 0 & 1 & 0 \\
-3 & 6 & -9 & 0 & 0 & 1
\end{array}\right]
\xrightarrow{\substack{F_2 \to F_2 + F_1 \\ F_3 \to F_3 + 3F_1}}
\left[\begin{array}{ccc|ccc}
1 & -2 & 3 & 1 & 0 & 0 \\
0 & \mathbf{2} & 8 & 1 & 1 & 0 \\
\mathbf{0} & \mathbf{0} & \mathbf{0} & 3 & 0 & 1
\end{array}\right]
$$

> [!warning] Fila Nula en el Bloque Izquierdo
> La Fila 3 del bloque de coeficientes es idénticamente nula ($[0\quad 0\quad 0]$), lo que demuestra que $\operatorname{rango}(B) = 2 < 3$. Es algebraicamente imposible obtener la matriz identidad $I_3$ a la izquierda.
> **Conclusión:** **$B^{-1}$ no existe** (matriz singular).

---

### 🔹 Matriz $C = \begin{pmatrix}1&-2\\-1&4\end{pmatrix}$

- $\det C = 4 - 2 = 2 \neq 0$ (invertible).
- **Menores:** $\operatorname{Men}(C) = \begin{pmatrix}4&-1\\-2&1\end{pmatrix}$.
- **Cofactores:** $\operatorname{Cof}(C) = \begin{pmatrix}4&1\\2&1\end{pmatrix}$.
- **Adjunta:** $\operatorname{adj}(C) = [\operatorname{Cof}(C)]^T = \begin{pmatrix}4&2\\1&1\end{pmatrix}$.
- **Inversa (Método de la Adjunta):**
 $$C^{-1} = \frac{1}{2}\begin{pmatrix}4&2\\1&1\end{pmatrix} = \begin{pmatrix}2&1\\1/2&1/2\end{pmatrix}$$

#### 🔄 Comparación Didáctica: Inversa de $C$ por Método de Gauss-Jordan $[C \mid I_2]$
$$
\left[\begin{array}{cc|cc}
\mathbf{1} & -2 & 1 & 0 \\
-1 & 4 & 0 & 1
\end{array}\right]
\xrightarrow{F_2 \to F_2 + F_1}
\left[\begin{array}{cc|cc}
1 & -2 & 1 & 0 \\
0 & \mathbf{2} & 1 & 1
\end{array}\right]
\xrightarrow{F_2 \to \frac{1}{2}F_2}
\left[\begin{array}{cc|cc}
1 & -2 & 1 & 0 \\
0 & \mathbf{1} & 1/2 & 1/2
\end{array}\right]
$$
$$
\xrightarrow{F_1 \to F_1 + 2F_2}
\left[\begin{array}{cc|cc}
\mathbf{1} & 0 & \mathbf{2} & \mathbf{1} \\
0 & \mathbf{1} & \mathbf{1/2} & \mathbf{1/2}
\end{array}\right]
\quad\Rightarrow\quad
C^{-1} = \begin{pmatrix}2&1\\1/2&1/2\end{pmatrix}
$$

> [!example] Verificación de $CC^{-1} = I_2$
> $\begin{pmatrix}1&-2\\-1&4\end{pmatrix}\begin{pmatrix}2&1\\1/2&1/2\end{pmatrix} = \begin{pmatrix}2-1 & 1-1 \\ -2+2 & -1+2\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2$ ✓.

## 3.5 Inversas y ecuaciones

$$
A = \begin{pmatrix}1&-2\\3&4\end{pmatrix},\qquad
B = \begin{pmatrix}0&1\\5&-6\end{pmatrix},\qquad
C = \begin{pmatrix}-2&0\\5&2\end{pmatrix}
$$

**a) Existencia de inversas** (teorema: invertible $\iff \det \neq 0$):

$$
\det A = 4 + 6 = 10 \neq 0 \Rightarrow A^{-1} = \frac{1}{10}\begin{pmatrix}4&2\\-3&1\end{pmatrix} = \begin{pmatrix}2/5&1/5\\-3/10&1/10\end{pmatrix}
$$

$$
\det B = 0 - 5 = -5 \neq 0 \Rightarrow B^{-1} = -\frac{1}{5}\begin{pmatrix}-6&-1\\-5&0\end{pmatrix} = \begin{pmatrix}6/5&1/5\\1&0\end{pmatrix}
$$

$$
\det C = -4 \neq 0 \Rightarrow C^{-1} = -\frac{1}{4}\begin{pmatrix}2&0\\-5&-2\end{pmatrix} = \begin{pmatrix}-1/2&0\\5/4&1/2\end{pmatrix}
$$

**b) Despejes generales** (para $A,B,C$ invertibles):

$$
AX = B - C \Rightarrow X = A^{-1}(B-C)
\qquad
AXB = BC \Rightarrow X = A^{-1}BC\,B^{-1}
\qquad
XA + C = XB \Rightarrow X(A-B) = -C \Rightarrow X = -C(A-B)^{-1}
$$

**c) Matrices solución:**

**1)** $X = A^{-1}(B-C)$ con $B-C = \begin{pmatrix}0&1\\5&-6\end{pmatrix} - \begin{pmatrix}-2&0\\5&2\end{pmatrix} = \begin{pmatrix}2&1\\0&-8\end{pmatrix}$:

$$
X = \begin{pmatrix}2/5&1/5\\-3/10&1/10\end{pmatrix}\begin{pmatrix}2&1\\0&-8\end{pmatrix}
= \begin{pmatrix}4/5 & 2/5 - 8/5 \\ -3/5 & -3/10 - 8/10\end{pmatrix}
= \begin{pmatrix}4/5&-6/5\\-3/5&-11/10\end{pmatrix}
$$

**2)** $X = A^{-1}(BC)B^{-1}$; con $BC = \begin{pmatrix}5&2\\-40&-12\end{pmatrix}$:

$$
A^{-1}BC = \begin{pmatrix}-6&-8/5\\-11/2&-9/5\end{pmatrix}
\quad\Rightarrow\quad
X = \begin{pmatrix}-6&-8/5\\-11/2&-9/5\end{pmatrix}\begin{pmatrix}6/5&1/5\\1&0\end{pmatrix}
= \begin{pmatrix}-44/5&-6/5\\-42/5&-11/10\end{pmatrix}
$$

**3)** $X = -C(A-B)^{-1}$; con $A-B = \begin{pmatrix}1&-3\\-2&10\end{pmatrix}$, $\det = 4$, $(A-B)^{-1} = \frac14\begin{pmatrix}10&3\\2&1\end{pmatrix}$:

$$
X = -\begin{pmatrix}-2&0\\5&2\end{pmatrix}\cdot\frac14\begin{pmatrix}10&3\\2&1\end{pmatrix}
= -\frac14\begin{pmatrix}-20&-6\\54&17\end{pmatrix}
= \begin{pmatrix}5&3/2\\-27/2&-17/4\end{pmatrix}
$$

> [!example] Verificación de 3)
> $X A + C = X B$ → SymPy: `True` para cada una de las tres soluciones.

---

## 3.6 Ecuación con $A^T A$

$A = \begin{pmatrix}0&1&1\\0&0&1\end{pmatrix}$ (de orden $2\times3$) y $B = (b_{ij})$ con $b_{ij} = i+j$:

$$
B = \begin{pmatrix}2&3&4\\3&4&5\\4&5&6\end{pmatrix}
$$

La ecuación es $B - \frac{1}{3}X = A^T A$. Despejamos $X = 3(B - A^TA)$:

$$
A^T A = \begin{pmatrix}0&0\\1&0\\1&1\end{pmatrix}\begin{pmatrix}0&1&1\\0&0&1\end{pmatrix}
= \begin{pmatrix}0&0&0\\0&1&1\\0&1&2\end{pmatrix}
$$

$$
X = 3\left(\begin{pmatrix}2&3&4\\3&4&5\\4&5&6\end{pmatrix} - \begin{pmatrix}0&0&0\\0&1&1\\0&1&2\end{pmatrix}\right)
= 3\begin{pmatrix}2&3&4\\3&3&4\\4&4&4\end{pmatrix}
= \begin{pmatrix}6&9&12\\9&9&12\\12&12&12\end{pmatrix}
$$

> [!example] Verificación
> $B - \frac13 X = \begin{pmatrix}0&0&0\\0&1&1\\0&1&2\end{pmatrix} = A^TA$ ✓

---

## 3.7 Parámetro $\lambda$

**a)** $A = \begin{pmatrix}\lambda&-2\\4&-1\end{pmatrix}$, $|A| = 3$:

$$
\det(A) = \lambda(-1) - (-2)(4) = -\lambda + 8 = 3 \;\Rightarrow\; \mathbf{\lambda = 5}
$$

**b)** $B = \begin{pmatrix}4&-2&0\\-1&\lambda&-1\\0&-1&4\end{pmatrix}$, $|B| = 0$. Desarrollamos por la columna 1 (dos ceros):

$$
\det(B) = 4\begin{vmatrix}\lambda&-1\\-1&4\end{vmatrix} - (-2)\begin{vmatrix}-1&-1\\0&4\end{vmatrix} = 4(4\lambda - 1) + 2(-4) = 16\lambda - 4 - 8 = 16\lambda - 12
$$

$$
16\lambda - 12 = 0 \;\Rightarrow\; \mathbf{\lambda = \frac{3}{4}}
$$

**c)** $C = \begin{pmatrix}\lambda&-2&1\\0&-3&5\\0&2&\lambda\end{pmatrix}$, $|C| = 8$. Triangular por bloques (ceros bajo $\lambda$ en la columna 1):

$$
\det(C) = \lambda\begin{vmatrix}-3&5\\2&\lambda\end{vmatrix} = \lambda(-3\lambda - 10) = -3\lambda^2 - 10\lambda = 8
$$

$$
3\lambda^2 + 10\lambda + 8 = 0 \;\Rightarrow\; \lambda = \frac{-10 \pm \sqrt{100 - 96}}{6} = \frac{-10 \pm 2}{6}
$$

> [!important] Resultado Clave
> $$\lambda = -2 \quad \text{o} \quad \lambda = -\frac{4}{3}$$

---

## 3.8 Matrices sin inversa

"No tener inversa" $\iff \det = 0$ (teorema de invertibilidad).

**a)** $A = \begin{pmatrix}k-3&-2\\-2&k-2\end{pmatrix}$:

$$
\det(A) = (k-3)(k-2) - 4 = k^2 - 5k + 6 - 4 = k^2 - 5k + 2 = 0
$$

$$
k = \frac{5 \pm \sqrt{25 - 8}}{2} \;\Rightarrow\; \mathbf{k = \frac{5 \pm \sqrt{17}}{2}}
$$

**b)** $A = \begin{pmatrix}2&0&0\\0&k+1&-1\\0&1&k-3\end{pmatrix}$ (triangular por bloques):

$$
\det(A) = 2\begin{vmatrix}k+1&-1\\1&k-3\end{vmatrix} = 2\big[(k+1)(k-3) + 1\big] = 2(k^2 - 2k - 2) = 0
$$

$$
k^2 - 2k - 2 = 0 \;\Rightarrow\; \mathbf{k = 1 \pm \sqrt{3}}
$$

---

## 3.9 Invertibilidad $4\times4$

$$
A = \begin{pmatrix}a&0&1&-1\\1&2&0&2\\0&-3&2&0\\1&a&3&a\end{pmatrix}
$$

Presentamos dos desarrollos matemáticos completos para determinar la condición de invertibilidad:

---

### 🔹 Método 1: Desarrollo por Cofactores de Laplace (Fila 1)

Desarrollamos $\det(A)$ por la fila 1 (el elemento $a_{12} = 0$ anula un término):

$$
\det(A) = a\cdot C_{11} + 0\cdot C_{12} + 1\cdot C_{13} + (-1)\cdot C_{14}
$$

Calculamos los menores y cofactores $3\times 3$:
- **Cofactor $C_{11} = +M_{11}$:**
 $$M_{11} = \begin{vmatrix}2&0&2\\-3&2&0\\a&3&a\end{vmatrix} = 2(2a - 0) - 0 + 2(-9 - 2a) = 4a - 18 - 4a = -18 \implies C_{11} = -18$$
- **Cofactor $C_{13} = +M_{13}$:**
 $$M_{13} = \begin{vmatrix}1&2&2\\0&-3&0\\1&a&a\end{vmatrix} = -3\begin{vmatrix}1&2\\1&a\end{vmatrix} = -3(a - 2) = 6 - 3a \implies C_{13} = 6 - 3a$$
- **Cofactor $C_{14} = -M_{14}$:**
 $$M_{14} = \begin{vmatrix}1&2&0\\0&-3&2\\1&a&3\end{vmatrix} = 1(-9 - 2a) - 2(0 - 2) + 0 = -9 - 2a + 4 = -5 - 2a \implies C_{14} = 5 + 2a$$

Sustituyendo en la expansión:

$$
\det(A) = a(-18) + 1(6 - 3a) - (5 + 2a) = -18a + 6 - 3a - 5 - 2a = 1 - 23a
$$

---

### 🔹 Método 2: Eliminación Gaussiana a Matriz Triangular Superior (OEF)

Llevamos la matriz $A$ a su **Forma Escalonada por Filas (REF)** para calcular el determinante como el producto de los pivotes:

**Paso 1 (Intercambio $F_1 \leftrightarrow F_2$ para tener pivote numérico 1):**
> [!info] Regla de OEF
> Intercambiar dos filas multiplica el determinante por $(-1)$.

$$
\det(A) = (-1) \cdot \begin{vmatrix}
\mathbf{1} & 2 & 0 & 2 \\
a & 0 & 1 & -1 \\
0 & -3 & 2 & 0 \\
1 & a & 3 & a
\end{vmatrix}
$$

**Paso 2 (Anular columna 1 bajo el pivote):** $F_2 \to F_2 - aF_1$, $F_4 \to F_4 - F_1$ (no cambian el $\det$):

$$
\det(A) = (-1) \cdot \begin{vmatrix}
\mathbf{1} & 2 & 0 & 2 \\
0 & -2a & 1 & -1 - 2a \\
0 & -3 & 2 & 0 \\
0 & a - 2 & 3 & a - 2
\end{vmatrix}
$$

**Paso 3 (Intercambio $F_2 \leftrightarrow F_3$ para fijar el pivote numérico $-3$):**
Nuevo cambio de signo: $(-1) \cdot (-1) = +1$:

$$
\det(A) = \begin{vmatrix}
\mathbf{1} & 2 & 0 & 2 \\
0 & \mathbf{-3} & 2 & 0 \\
0 & -2a & 1 & -1 - 2a \\
0 & a - 2 & 3 & a - 2
\end{vmatrix}
$$

**Paso 4 (Anular columna 2 bajo $-3$):** $F_3 \to F_3 - \frac{2a}{3}F_2$, $F_4 \to F_4 + \frac{a - 2}{3}F_2$:
- En $F_3$: $1 - \frac{2a}{3}(2) = \frac{3 - 4a}{3}$, elemento $(3,4) = -1 - 2a$.
- En $F_4$: $3 + \frac{a - 2}{3}(2) = \frac{9 + 2a - 4}{3} = \frac{2a + 5}{3}$, elemento $(4,4) = a - 2$.

$$
\det(A) = \begin{vmatrix}
\mathbf{1} & 2 & 0 & 2 \\
0 & \mathbf{-3} & 2 & 0 \\
0 & 0 & \mathbf{\frac{3 - 4a}{3}} & -1 - 2a \\
0 & 0 & \frac{2a + 5}{3} & a - 2
\end{vmatrix}
$$

**Paso 5 (Anular posición (4,3)):** $F_4 \to F_4 - \left(\frac{2a + 5}{3 - 4a}\right) F_3$:
Cálculo detallado del pivote en la posición $(4,4)$:
$$
(a - 2) - \left(\frac{2a + 5}{3 - 4a}\right)(-1 - 2a) = (a - 2) + \frac{(2a + 5)(2a + 1)}{3 - 4a}
$$
$$
= \frac{(a - 2)(3 - 4a) + (4a^2 + 12a + 5)}{3 - 4a} = \frac{(-4a^2 + 11a - 6) + (4a^2 + 12a + 5)}{3 - 4a} = \frac{23a - 1}{3 - 4a} = -\frac{1 - 23a}{3 - 4a}
$$

$$
\det(A) = \begin{vmatrix}
\mathbf{1} & 2 & 0 & 2 \\
0 & \mathbf{-3} & 2 & 0 \\
0 & 0 & \mathbf{\frac{3 - 4a}{3}} & -1 - 2a \\
0 & 0 & 0 & \mathbf{-\frac{1 - 23a}{3 - 4a}}
\end{vmatrix}
$$

**Paso 6 (Producto de la diagonal principal):**

$$
\det(A) = (1) \cdot (-3) \cdot \left(\frac{3 - 4a}{3}\right) \cdot \left(-\frac{1 - 23a}{3 - 4a}\right)
= (-1)(3 - 4a) \cdot \left(-\frac{1 - 23a}{3 - 4a}\right) = 1 - 23a
$$

---

### 🎯 Teorema de Invertibilidad y Condición Final

Una matriz cuadrada es invertible si y solo si tiene **rango completo** (4 pivotes no nulos en su forma escalonada), lo cual equivale a $\det(A) \neq 0$:

$$
1 - 23a \neq 0 \iff 23a \neq 1 \iff \mathbf{a \neq \frac{1}{23}}
$$

> [!important] Resultado Clave
> La matriz $A$ es **invertible** para todo $a \in \mathbb{R} \setminus \left\{\frac{1}{23}\right\}$.
> Si $a = \frac{1}{23}$, el cuarto pivote se anula, $\operatorname{rango}(A) = 3 < 4$ y la matriz se vuelve singular.

---

## 🧪 Verificación numérica (SymPy)

Todo el taller se validó con el script `01_Sistemas_Lineales/verificar_taller1.py` (SymPy), que reproduce:

- Las matrices de los ejercicios 1.1–1.6, 2.2, 2.6, 2.7 y 3.1–3.9.
- Cada producto, traspuesta, determinante, cofactor, adjunta, inversa y valor propio.
- Las verificaciones booleanas: $(AB)^T = B^TA^T$, $(A+B)^T = A^T + B^T$, $AX = B$, $X^3 - X^2 - 5X + 5I = \theta$, etc. → todas `True`.
- Los casos singulares: $X \cdot M = R$ (3.3b) y $E^TXF = B-D$ (3.2d) → `EmptySet` (sistemas incompatibles).

**Scripts y figuras generados:**

| Archivo | Ruta |
|:---|:---|
| Verificación SymPy | `01_Sistemas_Lineales/verificar_taller1.py` |
| Figuras Matplotlib | `05_Simulaciones_y_Visualizaciones/generar_figuras_taller1.py` |
| Figura 1 — producto de matrices | `05_Simulaciones_y_Visualizaciones/Figura1_producto_matrices.png` |
| Figura 2 — Sarrus y cofactores | `05_Simulaciones_y_Visualizaciones/Figura2_sarrus_cofactores.png` |
| Figura 3 — valores propios | `05_Simulaciones_y_Visualizaciones/Figura3_valores_propios.png` |

---

## 📚 Referencias y contexto histórico

> [!quote] Bibliografía
> - Kleiner, I. (2007). *A History of Abstract Algebra*. Birkhäuser. (Los determinantes preceden a las matrices; orígenes en China s. II a.C., Seki Kowa y Leibniz en 1683.)
> - MacTutor History of Mathematics — *Matrices and Determinants* (St Andrews): Cauchy 1812 (multiplicación de determinantes), Sylvester 1850 (término "matriz"), Cayley 1858 (*Memoir on the theory of matrices*: inversa vía determinante), Frobenius 1878 (teorema de Cayley–Hamilton general y noción de rango).
> - de la Puente, M.J. (UCM) — *Historia del Álgebra Lineal*: Vandermonde 1771, Laplace 1772, Jacobi 1841 (definición algorítmica del determinante), Weierstrass/Kronecker 1903 (definición axiomática).
> - Grossman, S. (2012). *Álgebra Lineal* (7ª ed.). McGraw-Hill. (Texto base del que provienen los ejercicios del taller.)
> - Apuntes del curso: [Apuntes — Matrices](../../Teoria/Unidad_1_Matrices_y_Sistemas/Matrices.md) (Unidad 1: Cramer, rango por menores, Rouché–Frobenius).

**Aplicaciones reales del material del taller:** la matriz adjunta en códigos correctores de errores y criptografía; el determinante como **área/volumen** (Lagrange, 1773) y criterio de invertibilidad en robótica (jacobianos de cinemática); los **valores propios** en análisis de vibraciones (D'Alembert), estabilidad de sistemas dinámicos y PageRank de Google; las **ecuaciones matriciales** en control automático (ecuaciones de Lyapunov $AX + XB = C$).
