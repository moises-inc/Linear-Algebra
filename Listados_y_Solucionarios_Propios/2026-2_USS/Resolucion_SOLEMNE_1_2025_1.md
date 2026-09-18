---
id: resolucion-solemne-1-2025-1
title: "Resolución Oficial Pauta Docente — Solemne 1 (2025-1)"
asignatura: "Álgebra Lineal (DCEX 0007)"
docente: "Carol Asencio G."
institucion: "Universidad San Sebastián"
fecha: "2025-09-02"
tags:
  - algebra-lineal
  - solemne-1
  - uss
  - matrices
  - determinantes
  - cofactores
  - ecuacion-matricial
status: completado
---

# 📝 Resolución Oficial Pauta Docente — Solemne 1 (2025-1)
**Asignatura:** Álgebra Lineal (DCEX 0007)  
**Docente:** Carol Asencio G.  
**Universidad San Sebastián — Facultad de Ingeniería, Arquitectura y Diseño**  
**Fecha:** 02 de septiembre | **Tiempo:** 80 minutos | **Puntaje Total:** 100 puntos  

---

## 📌 Leyenda de Trazabilidad de Fuentes
- 🎓 `[Cátedra USS / Pauta Oficial Docente]`: Desarrollo algebraico oficial alineado con el criterio de corrección de la pauta institucional.
- 📖 `[Texto Guía / Demostración Formal]`: Justificaciones matemáticas rigurosas basadas en propiedades estándar del álgebra matricial.
- 🌐 `[Enriquecimiento Computacional SymPy]`: Verificación simbólica automatizada mediante script Python (`verificar_solemne1_2025.py`).

---

## 🗺️ Mapa de Respuestas (Resumen Ejecutivo)

| Sección | Pregunta | Resultado / Opción Correcta | Puntos | Resumen Justificativo |
| :--- | :---: | :---: | :---: | :--- |
| **Parte I** | **1** | **Falso (F)** | 8 pts | $D = C^2 + AB = \begin{pmatrix}15 & -14 \\ -4 & 15\end{pmatrix} \neq \begin{pmatrix}15 & -14 \\ 4 & -15\end{pmatrix}$. |
| | **2** | **Verdadero (V)** | 8 pts | $B^T = -B$, cumple exactamente la definición de matriz antisimétrica. |
| | **3** | **Falso (F)** | 8 pts | $\det A = 0$ (Fila 4 es m.e. de Fila 2), por tanto $A$ es singular (no regular). |
| **Parte II** | **2.1** | **Opción b** | 8 pts | $\left\|\begin{pmatrix}a & b \\ 7c & 7d\end{pmatrix}\right\| = 7\|A\| = 7(-13) = -91$. |
| | **2.2** | **Opción c** | 8 pts | $A_{32} = 6$, $A_{12} = -4 \implies A_{32} - 3A_{12} = 6 - 3(-4) = 18$. |
| | **2.3** | **Opción d** | 8 pts | $\det M = 20 - 2a \neq 0 \iff a \neq 10 \implies \forall a \in \mathbb{R} - \{10\}$. |
| **Parte III** | **Prob 1.a** | $X = \frac{1}{2}(I + A)$ | 20 pts | Despeje simbólico usando simetría $X^T=X, A^T=A$ y prop. de inversas. |
| | **Prob 1.b** | $X = \begin{pmatrix}2 & 1 \\ 1 & 0\end{pmatrix}$ | 6 pts | Evaluación numérica para $A = \begin{pmatrix}3 & 2 \\ 2 & -1\end{pmatrix}$. |
| | **Prob 2.a** | $\det A = 4$ | 6 pts | Regla de Sarrus: $\det A = 36 - 32 = 4 \neq 0$. |
| | **Prob 2.b** | $\text{adj}(A) = \begin{pmatrix}-6 & 10 & -6 \\ -11 & 19 & -9 \\ 2 & -2 & 2\end{pmatrix}$ | 15 pts | Matriz transpuesta de cofactores $(A_{ij})^T$. |
| | **Prob 2.c** | $A^{-1} = \begin{pmatrix}-3/2 & 5/2 & -3/2 \\ -11/4 & 19/4 & -9/4 \\ 1/2 & -1/2 & 1/2\end{pmatrix}$ | 5 pts | $A^{-1} = \frac{1}{\det A}\text{adj}(A)$. |

---

## Parte I: Verdadero o Falso (8 puntos c/u)

> [!important]
> **Criterio de Corrección:** Cada afirmación debe ser catalogada como Verdadera (V) o Falsa (F), acompañada de su demostración o contraejemplo algebraico completo para obtener el puntaje total.

---

### Pregunta 1
**Enunciado:**  
Sean las matrices:
$$A = \begin{pmatrix}10 & -2 & 4 \\ 2 & 8 & -6\end{pmatrix}, \quad B = \begin{pmatrix}1 & -1 \\ 0 & 2 \\ 1 & 0\end{pmatrix}, \quad C = \begin{pmatrix}-1 & 3 \\ 0 & 1\end{pmatrix}$$
Si $D = C^2 + AB$, entonces $D = \begin{pmatrix}15 & -14 \\ 4 & -15\end{pmatrix}$.

**Respuesta:** **FALSO (F)** 🎓

#### Justificación Algebraica Detallada:
1. **Cálculo de $C^2$:**
   $$C^2 = C \cdot C = \begin{pmatrix}-1 & 3 \\ 0 & 1\end{pmatrix}\begin{pmatrix}-1 & 3 \\ 0 & 1\end{pmatrix} = \begin{pmatrix}(-1)(-1) + 3(0) & (-1)(3) + 3(1) \\ 0(-1) + 1(0) & 0(3) + 1(1)\end{pmatrix} = \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix} = I_2$$

2. **Cálculo del producto $AB$:**
   $$AB = \begin{pmatrix}10 & -2 & 4 \\ 2 & 8 & -6\end{pmatrix}\begin{pmatrix}1 & -1 \\ 0 & 2 \\ 1 & 0\end{pmatrix} = \begin{pmatrix}10(1) + (-2)(0) + 4(1) & 10(-1) + (-2)(2) + 4(0) \\ 2(1) + 8(0) + (-6)(1) & 2(-1) + 8(2) + (-6)(0)\end{pmatrix}$$
   $$AB = \begin{pmatrix}10 + 0 + 4 & -10 - 4 + 0 \\ 2 + 0 - 6 & -2 + 16 + 0\end{pmatrix} = \begin{pmatrix}14 & -14 \\ -4 & 14\end{pmatrix}$$

3. **Cálculo de la suma $D = C^2 + AB$:**
   $$D = \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix} + \begin{pmatrix}14 & -14 \\ -4 & 14\end{pmatrix} = \begin{pmatrix}1 + 14 & 0 - 14 \\ 0 - 4 & 1 + 14\end{pmatrix} = \begin{pmatrix}15 & -14 \\ -4 & 15\end{pmatrix}$$

4. **Comparación con la propuesta:**
   La matriz obtenida es $D = \begin{pmatrix}15 & -14 \\ -4 & 15\end{pmatrix}$, mientras que la propuesta del enunciado afirma que $D = \begin{pmatrix}15 & -14 \\ 4 & -15\end{pmatrix}$. Se observan diferencias de signo en los elementos $d_{21}$ y $d_{22}$. Por ende, la proposición es **Falsa**.

---

### Pregunta 2
**Enunciado:**  
La matriz $B = \begin{pmatrix}0 & 2 & 1 \\ -2 & 0 & 5 \\ -1 & -5 & 0\end{pmatrix}$ es una matriz antisimétrica.

**Respuesta:** **VERDADERO (V)** 🎓

#### Justificación Algebraica Detallada:
1. **Definición de Matriz Antisimétrica:**  
   Una matriz cuadrada $B \in \mathcal{M}_n(\mathbb{R})$ es antisimétrica si y solo si su transpuesta es igual a su opuesta aditiva:
   $$B^T = -B$$

2. **Cálculo de $B^T$ (Intercambio de filas por columnas):**
   $$B^T = \begin{pmatrix}0 & -2 & -1 \\ 2 & 0 & -5 \\ 1 & 5 & 0\end{pmatrix}$$

3. **Cálculo de $-B$ (Multiplicación por el escalar $-1$):**
   $$-B = -1 \cdot \begin{pmatrix}0 & 2 & 1 \\ -2 & 0 & 5 \\ -1 & -5 & 0\end{pmatrix} = \begin{pmatrix}0 & -2 & -1 \\ 2 & 0 & -5 \\ 1 & 5 & 0\end{pmatrix}$$

4. **Conclusión:**  
   Como $B^T = -B$ y todos los elementos de la diagonal principal son cero ($b_{ii} = 0$), se verifica rigurosamente la definición de matriz antisimétrica. Por tanto, la afirmación es **Verdadera**.

---

### Pregunta 3
**Enunciado:**  
Dadas las siguientes matrices $A$, $B$ y $C$:
$$A = \begin{pmatrix}0 & 0 & 0 & 1 \\ -1 & -2 & 2 & 1 \\ 0 & 5 & -1 & 0 \\ -3 & -6 & 6 & 3\end{pmatrix}, \quad B = \begin{pmatrix}0 & 0 & 1 \\ 1 & -1 & 0 \\ -1 & 0 & -1\end{pmatrix}, \quad C = \begin{pmatrix}0 & 1 \\ -2 & 1\end{pmatrix}$$
Las matrices A, B y C son regulares.

**Respuesta:** **FALSO (F)** 🎓

#### Justificación Algebraica Detallada:
1. **Criterio de Regularidad:**  
   Una matriz cuadrada es regular (invertible) si y solo si su determinante es no nulo ($\det \neq 0$).

2. **Análisis de la Matriz $A$:**  
   Observamos las filas de la matriz $A \in \mathcal{M}_4(\mathbb{R})$:
   - Fila 2: $R_2 = (-1, -2, 2, 1)$
   - Fila 4: $R_4 = (-3, -6, 6, 3)$
   
   Nótese que $R_4 = 3 \cdot R_2$. Al ser la cuarta fila un múltiplo escalar exacto de la segunda fila, las filas de $A$ son linealmente dependientes. Por las propiedades fundamentales de los determinantes:
   $$\det A = 0$$
   Por consiguiente, la matriz $A$ es **singular** (no es regular).

3. **Determinantes de $B$ y $C$:**
   $$\det B = 0(1 - 0) - 0(-1 - 0) + 1(0 - 1) = -1 \neq 0 \quad (\text{Regular})$$
   $$\det C = (0)(1) - (1)(-2) = 2 \neq 0 \quad (\text{Regular})$$

4. **Conclusión:**  
   Dado que $A$ no es una matriz regular, el enunciado afirmativo conjunto "A, B y C son regulares" es **Falso**.

---

## Parte II: Selección Múltiple (8 puntos c/u)

> [!tip]
> **Estrategia Táctica:** Justificar formalmente la opción seleccionada analizando las propiedades de los determinantes, cofactores y sistemas de ecuaciones lineales.

---

### Pregunta 2.1
**Enunciado:**  
Sea $A = \begin{pmatrix}a & b \\ c & d\end{pmatrix}$ y $|A| = -13$. ¿Cuál de las siguientes afirmaciones es verdadera?

a) $\begin{vmatrix}c & d \\ a & b\end{vmatrix} = -13$  
b) $\begin{vmatrix}a & b \\ 7c & 7d\end{vmatrix} = -91$  
c) $|3A| = -39$  
d) $|-A^{-1}| = \frac{1}{13}$

**Opción Correcta:** **b** 🎓

#### Análisis Breve de cada Opción:
- **Opción a (Falsa):** Al intercambiar la Fila 1 y Fila 2, el determinante cambia de signo:  
  $$\begin{vmatrix}c & d \\ a & b\end{vmatrix} = -|A| = -(-13) = 13 \neq -13$$
- **Opción b (VERDADERA):** Al multiplicar la Fila 2 por el escalar $k = 7$, el determinante resulta multiplicado por $7$:  
  $$\begin{vmatrix}a & b \\ 7c & 7d\end{vmatrix} = 7 \cdot |A| = 7 \cdot (-13) = -91$$
- **Opción c (Falsa):** Para una matriz $A \in \mathcal{M}_2(\mathbb{R})$, $|kA| = k^2 |A|$:  
  $$|3A| = 3^2 \cdot |A| = 9 \cdot (-13) = -117 \neq -39$$
- **Opción d (Falsa):** Puesto que $|-A^{-1}| = (-1)^2 \cdot |A^{-1}| = \frac{1}{|A|}$:  
  $$|-A^{-1}| = \frac{1}{-13} = -\frac{1}{13} \neq \frac{1}{13}$$

---

### Pregunta 2.2
**Enunciado:**  
Dada la matriz $A = \begin{pmatrix}1 & 0 & 3 \\ 2 & -3 & 0 \\ 0 & 1 & 2\end{pmatrix}$.  
Sea $A_{ij}$ los cofactores de $A$. Entonces, el resultado de $A_{32} - 3A_{12}$ es:

a) $-6$  
b) $6$  
c) $18$  
d) $2$

**Opción Correcta:** **c** 🎓

#### Desarrollo y Cálculo de Cofactores:
1. **Cálculo del cofactor $A_{32}$:**  
   $$\text{Menor } M_{32} = \begin{vmatrix}1 & 3 \\ 2 & 0\end{vmatrix} = (1)(0) - (3)(2) = -6$$
   $$A_{32} = (-1)^{3+2} M_{32} = (-1)^5 (-6) = 6$$

2. **Cálculo del cofactor $A_{12}$:**  
   $$\text{Menor } M_{12} = \begin{vmatrix}2 & 0 \\ 0 & 2\end{vmatrix} = (2)(2) - (0)(0) = 4$$
   $$A_{12} = (-1)^{1+2} M_{12} = (-1)^3 (4) = -4$$

3. **Evaluación de la expresión $A_{32} - 3A_{12}$:**  
   $$A_{32} - 3A_{12} = 6 - 3(-4) = 6 + 12 = 18$$

---

### Pregunta 2.3
**Enunciado:**  
Obtenga el valor de $a$ para que el sistema sea compatible con solución determinada:
$$\begin{cases} x + y - z = 0 \\ x + 3y + z = 0 \\ 3x + ay + 4z = 0 \end{cases}$$

a) $\forall a \in \mathbb{R} - \{-10\}$  
b) $a = 10$  
c) $a = -10 \lor a = 10$  
d) $\forall a \in \mathbb{R} - \{10\}$

**Opción Correcta:** **d** 🎓

#### Desarrollo del Determinante de Coeficientes:
1. **Matriz de coeficientes $M$:**  
   $$M = \begin{pmatrix}1 & 1 & -1 \\ 1 & 3 & 1 \\ 3 & a & 4\end{pmatrix}$$

2. **Condición de Solución Única (Teorema de Rouché-Frobenius / Cramer):**  
   Por ser un sistema homogéneo ($MX = 0$), el sistema admite solución única (la solución trivial $x=y=z=0$) si y solo si la matriz de coeficientes es invertible, es decir, $\det M \neq 0$.

3. **Cálculo de $\det M$ por la Regla de Sarrus:**  
   $$\det M = \begin{vmatrix}1 & 1 & -1 \\ 1 & 3 & 1 \\ 3 & a & 4\end{vmatrix}$$
   - Productos diagonales principales: $(1)(3)(4) + (1)(1)(3) + (-1)(1)(a) = 12 + 3 - a = 15 - a$
   - Productos diagonales secundarias: $(3)(3)(-1) + (a)(1)(1) + (4)(1)(1) = -9 + a + 4 = a - 5$
   - Determinante:
     $$\det M = (15 - a) - (a - 5) = 15 - a - a + 5 = 20 - 2a$$

4. **Establecimiento de la condición de compatibilidad:**  
   $$\det M \neq 0 \iff 20 - 2a \neq 0 \iff 2a \neq 20 \iff a \neq 10$$
   Por tanto, el sistema es compatible determinado para todo $a \in \mathbb{R} - \{10\}$.

---

## Parte III: Problemas de Desarrollo (26 puntos c/u)

---

### Problema 1 (26 puntos)

Dada la ecuación matricial:
$$2(A^{-1}X)^T + X^T(A^{-1})^T - XB(AB)^{-1} = (A^{-1} + I)^T$$
donde $X, A, B$ son matrices de orden $n$, con $X$ y $A$ simétricas. Se pide:

#### a) Despejar la matriz $X$ (20 puntos) 🎓

> [!important]
> **Invariantes y Propiedades de Simetría Utilizadas:**
> - $X^T = X$ ($X$ es simétrica)
> - $A^T = A \implies (A^{-1})^T = (A^T)^{-1} = A^{-1}$ ($A$ y $A^{-1}$ son simétricas)
> - Transpuesta del producto: $(MN)^T = N^T M^T$
> - Inversa del producto: $(MN)^{-1} = N^{-1} M^{-1}$

**Desarrollo Paso a Paso:**

1. **Simplificación del primer término $2(A^{-1}X)^T$:**
   $$2(A^{-1}X)^T = 2 \cdot X^T (A^{-1})^T$$
   Aplicando las propiedades de simetría $X^T = X$ y $(A^{-1})^T = A^{-1}$:
   $$2(A^{-1}X)^T = 2 X A^{-1}$$

2. **Simplificación del segundo término $X^T(A^{-1})^T$:**
   $$X^T(A^{-1})^T = X A^{-1}$$

3. **Simplificación del tercer término $XB(AB)^{-1}$:**
   Aplicando la propiedad de la inversa de un producto $(AB)^{-1} = B^{-1} A^{-1}$:
   $$XB(AB)^{-1} = X B (B^{-1} A^{-1}) = X (B B^{-1}) A^{-1} = X I_n A^{-1} = X A^{-1}$$

4. **Simplificación del lado derecho $(A^{-1} + I)^T$:**
   Aplicando la transpuesta de una suma y $(A^{-1})^T = A^{-1}$:
   $$(A^{-1} + I)^T = (A^{-1})^T + I^T = A^{-1} + I$$

5. **Sustitución de todas las expresiones simplificadas en la ecuación original:**
   $$2 X A^{-1} + X A^{-1} - X A^{-1} = A^{-1} + I$$
   Agrupando términos semejantes en el lado izquierdo:
   $$(2 + 1 - 1) X A^{-1} = A^{-1} + I$$
   $$2 X A^{-1} = A^{-1} + I$$

6. **Aislamiento de la matriz $X$:**
   Multiplicando ambos miembros de la ecuación **por la derecha** por la matriz $A$:
   $$(2 X A^{-1}) A = (A^{-1} + I) A$$
   $$2 X (A^{-1} A) = A^{-1} A + I A$$
   Puesto que $A^{-1} A = I$ y $I A = A$:
   $$2 X I = I + A$$
   $$2 X = I + A$$
   Multiplicando por el escalar $\frac{1}{2}$:
   $$X = \frac{1}{2}(I + A)$$

---

#### b) Determinar la matriz $X$, considerando $A = \begin{pmatrix}3 & 2 \\ 2 & -1\end{pmatrix}$ matriz de orden dos (6 puntos) 🎓

1. **Definición de la Matriz Identidad $I_2$:**
   $$I_2 = \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$$

2. **Cálculo de la suma $I + A$:**
   $$I + A = \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix} + \begin{pmatrix}3 & 2 \\ 2 & -1\end{pmatrix} = \begin{pmatrix}1 + 3 & 0 + 2 \\ 0 + 2 & 1 + (-1)\end{pmatrix} = \begin{pmatrix}4 & 2 \\ 2 & 0\end{pmatrix}$$

3. **Cálculo final de $X = \frac{1}{2}(I + A)$:**
   $$X = \frac{1}{2} \begin{pmatrix}4 & 2 \\ 2 & 0\end{pmatrix} = \begin{pmatrix}\frac{4}{2} & \frac{2}{2} \\[1ex] \frac{2}{2} & \frac{0}{2}\end{pmatrix} = \begin{pmatrix}2 & 1 \\ 1 & 0\end{pmatrix}$$

---

### Problema 2 (26 puntos)

Para la matriz:
$$A = \begin{pmatrix}5 & -2 & 6 \\ 1 & 0 & 3 \\ -4 & 2 & -1\end{pmatrix}$$

Se pide:

#### a) Calcular el determinante de $A$ (6 puntos) 🎓

Aplicando la **Regla de Sarrus**:
$$\det A = \begin{vmatrix} 5 & -2 & 6 \\ 1 & 0 & 3 \\ -4 & 2 & -1 \end{vmatrix}$$

- **Suma de productos de las diagonales principales (de izquierda a derecha):**
  $$P_1 = (5)(0)(-1) + (-2)(3)(-4) + (6)(1)(2) = 0 + 24 + 12 = 36$$

- **Suma de productos de las diagonales secundarias (de derecha a izquierda):**
  $$P_2 = (-4)(0)(6) + (2)(3)(5) + (-1)(1)(-2) = 0 + 30 + 2 = 32$$

- **Valor del Determinante:**
  $$\det A = P_1 - P_2 = 36 - 32 = 4$$

---

#### b) La matriz $\text{adj}(A)$ (15 puntos) 🎓

La matriz adjunta es la transpuesta de la matriz de cofactores: $\text{adj}(A) = (A_{ij})^T$, donde $A_{ij} = (-1)^{i+j} M_{ij}$.

**Cálculo detallado de los 9 cofactores:**

1. **Fila 1:**
   $$A_{11} = (-1)^{1+1} \begin{vmatrix} 0 & 3 \\ 2 & -1 \end{vmatrix} = +1 \cdot [(0)(-1) - (3)(2)] = +1 \cdot (0 - 6) = -6$$
   $$A_{12} = (-1)^{1+2} \begin{vmatrix} 1 & 3 \\ -4 & -1 \end{vmatrix} = -1 \cdot [(1)(-1) - (3)(-4)] = -1 \cdot (-1 + 12) = -11$$
   $$A_{13} = (-1)^{1+3} \begin{vmatrix} 1 & 0 \\ -4 & 2 \end{vmatrix} = +1 \cdot [(1)(2) - (0)(-4)] = +1 \cdot (2 - 0) = 2$$

2. **Fila 2:**
   $$A_{21} = (-1)^{2+1} \begin{vmatrix} -2 & 6 \\ 2 & -1 \end{vmatrix} = -1 \cdot [(-2)(-1) - (6)(2)] = -1 \cdot (2 - 12) = 10$$
   $$A_{22} = (-1)^{2+2} \begin{vmatrix} 5 & 6 \\ -4 & -1 \end{vmatrix} = +1 \cdot [(5)(-1) - (6)(-4)] = +1 \cdot (-5 + 24) = 19$$
   $$A_{23} = (-1)^{2+3} \begin{vmatrix} 5 & -2 \\ -4 & 2 \end{vmatrix} = -1 \cdot [(5)(2) - (-2)(-4)] = -1 \cdot (10 - 8) = -2$$

3. **Fila 3:**
   $$A_{31} = (-1)^{3+1} \begin{vmatrix} -2 & 6 \\ 0 & 3 \end{vmatrix} = +1 \cdot [(-2)(3) - (6)(0)] = +1 \cdot (-6 - 0) = -6$$
   $$A_{32} = (-1)^{3+2} \begin{vmatrix} 5 & 6 \\ 1 & 3 \end{vmatrix} = -1 \cdot [(5)(3) - (6)(1)] = -1 \cdot (15 - 6) = -9$$
   $$A_{33} = (-1)^{3+3} \begin{vmatrix} 5 & -2 \\ 1 & 0 \end{vmatrix} = +1 \cdot [(5)(0) - (-2)(1)] = +1 \cdot (0 + 2) = 2$$

**Matriz de Cofactores $(A_{ij})$:**
$$C = (A_{ij}) = \begin{pmatrix}-6 & -11 & 2 \\ 10 & 19 & -2 \\ -6 & -9 & 2\end{pmatrix}$$

**Matriz Adjunta $\text{adj}(A) = C^T$:**
$$\text{adj}(A) = \begin{pmatrix}-6 & 10 & -6 \\ -11 & 19 & -9 \\ 2 & -2 & 2\end{pmatrix}$$

---

#### c) Si existe, la inversa de $A$ (5 puntos) 🎓

Dado que $\det A = 4 \neq 0$, la matriz $A$ es regular y su inversa $A^{-1}$ existe y está dada por:
$$A^{-1} = \frac{1}{\det A} \text{adj}(A)$$

Sustituyendo el valor del determinante $\det A = 4$ y la matriz $\text{adj}(A)$:
$$A^{-1} = \frac{1}{4} \begin{pmatrix}-6 & 10 & -6 \\ -11 & 19 & -9 \\ 2 & -2 & 2\end{pmatrix} = \begin{pmatrix}-\frac{6}{4} & \frac{10}{4} & -\frac{6}{4} \\[1.5ex] -\frac{11}{4} & \frac{19}{4} & -\frac{9}{4} \\[1.5ex] \frac{2}{4} & -\frac{2}{4} & \frac{2}{4}\end{pmatrix} = \begin{pmatrix}-\frac{3}{2} & \frac{5}{2} & -\frac{3}{2} \\[1.5ex] -\frac{11}{4} & \frac{19}{4} & -\frac{9}{4} \\[1.5ex] \frac{1}{2} & -\frac{1}{2} & \frac{1}{2}\end{pmatrix}$$

> [!example]
> **Verificación de Inversibilidad ($A \cdot A^{-1} = I_3$):**
> $$A \cdot A^{-1} = \begin{pmatrix}5 & -2 & 6 \\ 1 & 0 & 3 \\ -4 & 2 & -1\end{pmatrix} \begin{pmatrix}-\frac{3}{2} & \frac{5}{2} & -\frac{3}{2} \\[1.5ex] -\frac{11}{4} & \frac{19}{4} & -\frac{9}{4} \\[1.5ex] \frac{1}{2} & -\frac{1}{2} & \frac{1}{2}\end{pmatrix} = \begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}$$

---

## 🛠️ Verificación Automatizada (SymPy)

La resolución ha sido verificada analítica y computacionalmente mediante **SymPy** (`verificar_solemne1_2025.py`), validando cada determinante, matriz de cofactores, adjunta e inversa.

---
## 🔗 Conexiones
- [README Principal](../../README.md)
- [Dashboard de Álgebra Lineal](../../README.md)
- [Unidad 1: Matrices y Sistemas de Ecuaciones Lineales](../../Teoria/Unidad_1_Matrices_y_Sistemas/Matrices.md)
- [Resolución Taller 1 — Álgebra Lineal](Resolucion_TALLER_1_ALGEBRA_LINEAL.md)
- [Resolución Taller 2 — Álgebra Lineal](Resolucion_TALLER_2_ALGEBRA_LINEAL.md)
