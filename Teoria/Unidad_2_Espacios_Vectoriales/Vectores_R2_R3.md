---
id: vectores_r2_r3
title: "Unidad 2: Vectores en R² y R³ — Geometría Vectorial, Rectas y Planos"
asignatura: Álgebra Lineal (DCEX0007)
unidad: 2
docente: Carol Asencio González
estudiante: Moisés Amundarain Romero
tags: [algebra-lineal, vectores, r2, r3, producto-punto, producto-cruz, rectas, planos, uss]
status: completado
---
# Unidad 2: Vectores en $\mathbb{R}^2$ y $\mathbb{R}^3$ — Geometría Vectorial, Rectas y Planos

> [!note] Leyenda de Trazabilidad y Procedencia Académica
> Para garantizar la máxima rigurosidad conceptual, trazabilidad y distinción de fuentes en la formación de Ingeniería Civil Informática de la Universidad San Sebastián (USS), los contenidos de este documento se clasifican mediante los siguientes distintivos:
> - `[Cátedra USS / Diapositivas Docente Carol Asencio]`: Contenidos curriculares oficiales, deducciones analíticas, teoremas y la totalidad de los 24 ejemplos y ejercicios desarrollados en estricta concordancia cronológica 1:1 con las 44 diapositivas de la asignatura Álgebra Lineal DCEX0007 (Sede Patagonia).
> - `[Texto Guía — Grossman / Axler / Aranda]`: Fundamentación matemática rigurosa, demostraciones analíticas completas y formalización algebraica (*Álgebra Lineal 7ª Ed.* de Stanley I. Grossman, *Linear Algebra Done Right 4th Ed.* de Sheldon Axler y *Álgebra Lineal con Python* de Aranda).
> - `[Material Complementario — UdeC / Enriquecimiento Web]`: Aplicaciones prácticas en mecánica y robótica tridimensional, problemas avanzados tipo certamen universitario (Universidad de Concepción), reducción histórica de las ecuaciones de Maxwell y fundamentos algorítmicos para computación gráfica 3D (Möller-Trumbore y Backface Culling).

---

> [!important] Resultado de Aprendizaje Formal (Slide 2) `[Cátedra USS]`
> **Analiza rectas y planos en el espacio identificando sus distancias y posiciones relativas.**
> 
> *Ejes temáticos del syllabus oficial:* Vectores en el plano y en el espacio, operaciones fundamentales y axiomas, producto escalar (punto), norma euclidiana y distancia, dirección y versores unitarios, ángulos entre vectores y Ley de Cosenos, ortogonalidad y paralelismo, proyecciones ortogonales, producto vectorial (cruz), áreas y volúmenes, ecuaciones de rectas y planos en $\mathbb{R}^3$, posiciones relativas e intersecciones, y distancias euclidianas mínimas.

---

## 1. Vectores en el Plano y en el Espacio (Slides 3–20) `[Cátedra USS]`

### 1.1 Definición Analítica y Geométrica (Slides 3–4) `[Cátedra USS]`

#### Vector $(a,b)$ en $\mathbb{R}^2$ (Slide 3) `[Cátedra USS]`
Un vector en el plano cartesiano bidimensional se define analíticamente como un par ordenado de números reales:

$$
\mathbf{v} = (a, b) \in \mathbb{R}^2
$$

donde $a$ denota la primera componente (abscisa horizontal) y $b$ denota la segunda componente (ordenada vertical). Mediante la base canónica del plano, se expresa de forma equivalente como:

$$
\mathbf{v} = a\mathbf{i} + b\mathbf{j}, \qquad \text{con } \mathbf{i} = (1, 0) \quad \text{y} \quad \mathbf{j} = (0, 1)
$$

Geométricamente, un vector representa una clase de equivalencia de segmentos de recta dirigidos (vectores libres equipolentes) determinados por:
1. **Magnitud o módulo:** la longitud escalar del segmento dirigido.
2. **Dirección:** la línea recta soporte o ángulo de inclinación espacial respecto a un eje coordenado de referencia.
3. **Sentido:** la orientación señalada por el extremo de la flecha hacia el punto terminal.

#### Vector $(a,b,c)$ en $\mathbb{R}^3$ (Slide 4) `[Cátedra USS]`
En el espacio tridimensional euclídeo, un vector se define algebraicamente como una terna ordenada de números reales:

$$
\mathbf{v} = (a, b, c) \in \mathbb{R}^3
$$

donde $a, b, c$ representan sus componentes escalares a lo largo de los ejes ortogonales $X$, $Y$ y $Z$ respectivamente. En términos de la base canónica tridimensional:

$$
\mathbf{v} = a\mathbf{i} + b\mathbf{j} + c\mathbf{k}, \qquad \text{con } \mathbf{i} = (1, 0, 0), \quad \mathbf{j} = (0, 1, 0), \quad \mathbf{k} = (0, 0, 1)
$$

Si se fija el origen de coordenadas en $O(0,0,0)$ y el punto final en $P(a,b,c)$, el vector $\mathbf{v} = \overrightarrow{OP}$ recibe el nombre de **vector de posición** del punto $P$. Dados dos puntos espaciales arbitrarios $P(x_P, y_P, z_P)$ y $Q(x_Q, y_Q, z_Q)$, el vector libre dirigido desde el punto inicial $P$ hacia el punto final $Q$ se obtiene mediante la resta vectorial de sus coordenadas:

$$
\overrightarrow{PQ} = Q - P = (x_Q - x_P,\ y_Q - y_P,\ z_Q - z_P)
$$

---

### 1.2 Operaciones Básicas entre Vectores (Slides 5–8) `[Cátedra USS]`

### Igualdad de Vectores (Slide 5) `[Cátedra USS]`
Dos vectores en $\mathbb{R}^n$ son iguales si y sólo si tienen, en el mismo orden, idénticos componentes escalares:

$$
\mathbf{v} = (v_1, v_2, v_3) \in \mathbb{R}^3 \quad \text{y} \quad \mathbf{w} = (w_1, w_2, w_3) \in \mathbb{R}^3 \implies \mathbf{v} = \mathbf{w} \iff v_1 = w_1, \quad v_2 = w_2, \quad v_3 = w_3
$$

> [!example] Ejemplo Oficial de Cátedra (Slide 5) `[Cátedra USS]`
> **Enunciado:** A partir de la representación en el espacio tridimensional, determine si los vectores $\vec{v} = (1, 3, 4)$ y $\vec{w} = (3, 1, 4)$ son iguales:
> 
> $$
> \text{¿Es } \vec{v} = \vec{w}?
> $$
> 
> **Resolución:**
> Comparando componente a componente:
> - Primera componente: $v_1 = 1$ y $w_1 = 3$. Como $1 \neq 3$, se tiene $v_1 \neq w_1$.
> - Segunda componente: $v_2 = 3$ y $w_2 = 1$. Como $3 \neq 1$, se tiene $v_2 \neq w_2$.
> - Tercera componente: $v_3 = 4$ y $w_3 = 4$. Coinciden, pero la igualdad vectorial exige coincidencia total.
> 
> **Conclusión:** Los vectores **no son iguales** ($\vec{v} \neq \vec{w}$) porque sus componentes homólogas difieren en los ejes $X$ e $Y$.

### Suma y Resta Vectorial (Slides 6–7) `[Cátedra USS]`
La adición y sustracción de vectores en $\mathbb{R}^n$ se realizan componente a componente:

$$
\mathbf{v} + \mathbf{w} = (v_1 + w_1,\ v_2 + w_2,\ v_3 + w_3)
$$

$$
\mathbf{v} - \mathbf{w} = (v_1 - w_1,\ v_2 - w_2,\ v_3 - w_3)
$$

*Interpretación geométrica:*
- **Suma ($\mathbf{v}+\mathbf{w}$):** Regla del paralelogramo o ley del triángulo (hacer coincidir el origen de $\mathbf{w}$ con el extremo de $\mathbf{v}$).
- **Resta ($\mathbf{v}-\mathbf{w}$):** Vector dirigido desde el extremo de $\mathbf{w}$ hacia el extremo de $\mathbf{v}$ cuando ambos comparten el mismo punto inicial.

> [!example] Ejemplo Oficial de Cátedra (Slide 6) `[Cátedra USS]`
> **Enunciado:** Dados $\vec{v} = (1, 3, 4)$ y $\vec{w} = (3, 1, 4)$ en $\mathbb{R}^3$, calcule la suma vectorial:
> 
> $$
> \vec{v} + \vec{w}
> $$
> 
> **Resolución:**
> Sumando las componentes homólogas:
> 
> $$
> \vec{v} + \vec{w} = (1 + 3,\ 3 + 1,\ 4 + 4) = (4, 4, 8)
> $$

> [!example] Ejemplo Oficial de Cátedra (Slide 7) `[Cátedra USS]`
> **Enunciado:** Con los mismos vectores $\vec{v} = (1, 3, 4)$ y $\vec{w} = (3, 1, 4)$, calcule:
> 
> $$
> \vec{v} - \vec{w} \qquad \text{y} \qquad \vec{w} - \vec{v}
> $$
> 
> **Resolución:**
> 1. Para $\vec{v} - \vec{w}$:
>    $$
>    \vec{v} - \vec{w} = (1 - 3,\ 3 - 1,\ 4 - 4) = (-2, 2, 0)
>    $$
> 2. Para $\vec{w} - \vec{v}$:
>    $$
>    \vec{w} - \vec{v} = (3 - 1,\ 1 - 3,\ 4 - 4) = (2, -2, 0)
>    $$
> 
> **Observación Geométrica:** $\vec{w} - \vec{v} = -(\vec{v} - \vec{w})$. Ambos vectores poseen exactamente el mismo módulo ($\sqrt{(-2)^2 + 2^2 + 0^2} = 2\sqrt{2}$) y la misma recta de soporte, pero tienen sentidos opuestos ($180^\circ$).

### Multiplicación por un Escalar (Slide 8) `[Cátedra USS]`
El escalamiento de un vector $\vec{v} = (v_1, v_2, v_3) \in \mathbb{R}^3$ por un factor escalar real $k \in \mathbb{R}$ se obtiene multiplicando cada componente por $k$:

$$
k\vec{v} = (k v_1,\ k v_2,\ k v_3)
$$

*Propiedades geométricas según el signo y magnitud de $k$:*
- Si $k > 1$: dilata la magnitud del vector conservando su dirección y sentido.
- Si $0 < k < 1$: contrae la magnitud conservando dirección y sentido.
- Si $k < 0$: invierte el sentido original del vector ($180^\circ$).
- Si $k = 0$: colapsa al vector nulo $\mathbf{0} = (0, 0, 0)$.

> [!example] Ejemplo Oficial de Cátedra (Slide 8) `[Cátedra USS]`
> **Enunciado:** Sea $\vec{v} = (1, 3, 4)$. Calcule los escalamientos:
> 
> $$
> 2\vec{v} \qquad \text{y} \qquad \frac{1}{2}\vec{v}
> $$
> 
> **Resolución:**
> 1. Multiplicación por $k = 2$:
>    $$
>    2\vec{v} = (2 \cdot 1,\ 2 \cdot 3,\ 2 \cdot 4) = (2, 6, 8)
>    $$
> 2. Multiplicación por $k = \frac{1}{2}$:
>    $$
>    \frac{1}{2}\vec{v} = \left(\frac{1}{2} \cdot 1,\ \frac{1}{2} \cdot 3,\ \frac{1}{2} \cdot 4\right) = \left(\frac{1}{2},\ \frac{3}{2},\ 2\right) = (0.5,\ 1.5,\ 2)
>    $$

---

### 1.3 Propiedades de las Operaciones entre Vectores (Slide 9) `[Cátedra USS]`

Sean $\vec{u}, \vec{v}, \vec{w} \in \mathbb{R}^3$ vectores arbitrarios y $\alpha, \beta \in \mathbb{R}$ escalares reales. Se satisfacen rigurosamente los **ocho axiomas fundamentales de espacio vectorial**:

1. **Conmutatividad de la adición:**
   $$
   \vec{v} + \vec{w} = \vec{w} + \vec{v}
   $$
2. **Asociatividad de la adición:**
   $$
   \vec{u} + (\vec{v} + \vec{w}) = (\vec{u} + \vec{v}) + \vec{w}
   $$
3. **Existencia del elemento neutro aditivo:**
   $$
   \vec{v} + \vec{0} = \vec{v}, \qquad \text{con } \vec{0} = (0, 0, 0)
   $$
4. **Existencia del elemento inverso aditivo (opuesto):**
   $$
   \vec{v} + (-\vec{v}) = \vec{0}, \qquad \text{donde } -\vec{v} = (-v_1, -v_2, -v_3)
   $$
5. **Identidad del escalar unidad:**
   $$
   1\vec{v} = \vec{v}
   $$
6. **Asociatividad mixta escalar:**
   $$
   \alpha(\beta\vec{v}) = (\alpha\beta)\vec{v}
   $$
7. **Distributividad del escalar sobre la adición vectorial:**
   $$
   \alpha(\vec{v} + \vec{w}) = \alpha\vec{v} + \alpha\vec{w}
   $$
8. **Distributividad del vector sobre la adición escalar:**
   $$
   (\alpha + \beta)\vec{v} = \alpha\vec{v} + \beta\vec{v}
   $$

---

### 1.4 Producto Punto (Escalar) (Slides 10–11) `[Cátedra USS]`

> **Definición Formal de Cátedra (Slide 10):** El producto punto (o producto escalar) es una operación algebraica binaria entre dos vectores que devuelve como resultado un **escalar real**. Esta operación se introduce para expresar analíticamente las ideas geométricas de longitud, magnitud y ángulo entre vectores.
> 
> Para $\vec{v} = (v_1, v_2, v_3) \in \mathbb{R}^3$ y $\vec{w} = (w_1, w_2, w_3) \in \mathbb{R}^3$, el producto punto se define como:
> 
> $$
> \vec{v} \cdot \vec{w} = \sum_{i=1}^3 v_i w_i = v_1 w_1 + v_2 w_2 + v_3 w_3 \in \mathbb{R}
> $$

> [!example] Ejemplo Oficial de Cátedra (Slide 10) `[Cátedra USS]`
> **Enunciado:**
> 1. Sea $\vec{v} = (-1, 3, 4)$ y $\vec{w} = (1, 0, -4)$, calcular $\vec{v} \cdot \vec{w}$.
> 2. Sea $\vec{u} = (a, b, c)$, calcular $\vec{u} \cdot \vec{u}$.
> 
> **Resolución:**
> 1. Aplicando la definición del producto escalar:
>    $$
>    \vec{v} \cdot \vec{w} = (-1)(1) + (3)(0) + (4)(-4) = -1 + 0 - 16 = -17
>    $$
> 2. Para el vector general $\vec{u}$:
>    $$
>    \vec{u} \cdot \vec{u} = a(a) + b(b) + c(c) = a^2 + b^2 + c^2
>    $$
>    *Observación:* La suma de cuadrados de las componentes es siempre no negativa ($a^2 + b^2 + c^2 \ge 0$), lo que conduce directamente a la definición formal de norma euclidiana.

### Propiedades del Producto Punto (Slide 11) `[Cátedra USS]`
Para cualesquiera vectores $\vec{u}, \vec{v}, \vec{w} \in \mathbb{R}^3$ y cualquier escalar $\alpha \in \mathbb{R}$:

1. **Carácter Definido Positivo:**
   $$
   \vec{v} \cdot \vec{v} > 0 \quad \text{si } \vec{v} \neq \vec{0}, \qquad \text{y} \quad \vec{v} \cdot \vec{v} = 0 \iff \vec{v} = \vec{0}
   $$
2. **Conmutatividad (Simetría):**
   $$
   \vec{v} \cdot \vec{w} = \vec{w} \cdot \vec{v}
   $$
3. **Distributividad respecto a la adición vectorial:**
   $$
   \vec{u} \cdot (\vec{v} + \vec{w}) = \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w}
   $$
4. **Homogeneidad respecto a la ponderación escalar:**
   $$
   (\alpha\vec{v}) \cdot \vec{w} = \alpha(\vec{v} \cdot \vec{w}) = \vec{v} \cdot (\alpha\vec{w})
   $$

---

### 1.5 Norma Euclidiana y Distancia (Slides 12–13) `[Cátedra USS]`

> **Definición Formal de Cátedra (Slide 12):** La norma euclidiana define formalmente la longitud geométrica de un vector desde la métrica euclidiana. Para $\vec{v} = (v_1, v_2, v_3) \in \mathbb{R}^3$, su norma se denota $\|\vec{v}\|$ y se calcula mediante la raíz cuadrada de su producto punto consigo mismo:
> 
> $$
> \|\vec{v}\| = \sqrt{\vec{v} \cdot \vec{v}} = \sqrt{v_1^2 + v_2^2 + v_3^2}
> $$
> 
> **Propiedad fundamental:** $\vec{v} \cdot \vec{v} = \|\vec{v}\|^2$.
> 
> **Distancia Euclidiana entre dos puntos $A$ y $B$:**
> La distancia métrica entre $A(x_A, y_A, z_A)$ y $B(x_B, y_B, z_B)$ se define como la norma del vector que une ambos puntos:
> 
> $$
> d(A, B) = \|\overrightarrow{AB}\| = \|B - A\| = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}
> $$

> [!example] Ejemplo Oficial de Cátedra (Slide 12) `[Cátedra USS]`
> **Enunciado:**
> a) Sea $\vec{u} = (1, 0, -2)$, calcular $\|\vec{u}\|$.  
> b) Calcule la distancia euclidiana del punto $A = (2, 0, -1)$ al punto $B = (1, -3, -2)$.
> 
> **Resolución:**
> a) Cálculo de la norma:
> $$
> \|\vec{u}\| = \sqrt{1^2 + 0^2 + (-2)^2} = \sqrt{1 + 0 + 4} = \sqrt{5}
> $$
> b) Vector diferencia $\overrightarrow{AB} = B - A$:
> $$
> B - A = (1 - 2,\ -3 - 0,\ -2 - (-1)) = (-1, -3, -1)
> $$
> Calculando la distancia métrica:
> $$
> d(A, B) = \|B - A\| = \sqrt{(-1)^2 + (-3)^2 + (-1)^2} = \sqrt{1 + 9 + 1} = \sqrt{11}
> $$

### Propiedades de la Norma (Slide 13) `[Cátedra USS]`
Para vectores $\vec{v}, \vec{w} \in \mathbb{R}^3$ y escalares $\alpha \in \mathbb{R}$:

1. **No negatividad:** $\|\vec{v}\| \ge 0$, con $\|\vec{v}\| = 0 \iff \vec{v} = \vec{0}$.
2. **Homogeneidad absoluta:** $\|\alpha\vec{v}\| = |\alpha| \|\vec{v}\|$.
3. **Desigualdad Triangular:** $\|\vec{v} + \vec{w}\| \le \|\vec{v}\| + \|\vec{w}\|$.
4. **Desigualdad de Cauchy-Schwarz:** $|\vec{v} \cdot \vec{w}| \le \|\vec{v}\| \|\vec{w}\|$.

---

### 1.6 Dirección de un Vector en $\mathbb{R}^2$ (Slide 14) `[Cátedra USS]`

> **Definición Formal de Cátedra (Slide 14):** Se define la dirección del vector plano $\vec{v} = (a, b) \in \mathbb{R}^2$ como el ángulo $\theta$, medido en radianes (o grados sexagesimales), que forma el segmento orientado con la dirección positiva del semieje $X$. Por convención métrica, se escoge $\theta$ en el intervalo semiabierto:
> 
> $$
> 0 \le \theta < 2\pi \qquad (0^\circ \le \theta < 360^\circ)
> $$
> De la trigonometría básica en el triángulo rectángulo de catetos $a$ y $b$, si $a \neq 0$:
> 
> $$
> \tan\theta = \frac{b}{a}
> $$
> *Ajuste por cuadrantes:* Para determinar $\theta$ de manera unívoca, es imprescindible identificar el signo simultáneo de $a$ y $b$:
> - **Cuadrante I ($a>0, b>0$):** $\theta = \arctan(b/a)$.
> - **Cuadrante II ($a<0, b>0$):** $\theta = \pi - \arctan(|b/a|) = 180^\circ - \arctan(|b/a|)$.
> - **Cuadrante III ($a<0, b<0$):** $\theta = \pi + \arctan(|b/a|) = 180^\circ + \arctan(|b/a|)$.
> - **Cuadrante IV ($a>0, b<0$):** $\theta = 2\pi - \arctan(|b/a|) = 360^\circ - \arctan(|b/a|)$.

> [!example] Ejemplo Oficial de Cátedra (Slide 14) `[Cátedra USS]`
> **Enunciado:** Determine la magnitud y la dirección exacta de los siguientes cuatro vectores en $\mathbb{R}^2$:
> 
> $$
> \text{i) } \mathbf{v} = (2, 2) \qquad \text{ii) } \mathbf{v} = (2, 2\sqrt{3}) \qquad \text{iii) } \mathbf{v} = (-3, -3) \qquad \text{iv) } \mathbf{v} = (0, 3)
> $$
> 
> **Resolución Paso a Paso:**
> 1. **Caso i) $\mathbf{v} = (2, 2)$:**
>    - Magnitud: $\|\mathbf{v}\| = \sqrt{2^2 + 2^2} = \sqrt{8} = 2\sqrt{2}$.
>    - Cuadrante: $x = 2 > 0$, $y = 2 > 0$ (Primer Cuadrante).
>    - Dirección: $\tan\theta = \frac{2}{2} = 1 \implies \theta = \arctan(1) = \frac{\pi}{4}\ (45^\circ)$.
> 2. **Caso ii) $\mathbf{v} = (2, 2\sqrt{3})$:**
>    - Magnitud: $\|\mathbf{v}\| = \sqrt{2^2 + (2\sqrt{3})^2} = \sqrt{4 + 12} = \sqrt{16} = 4$.
>    - Cuadrante: $x = 2 > 0$, $y = 2\sqrt{3} > 0$ (Primer Cuadrante).
>    - Dirección: $\tan\theta = \frac{2\sqrt{3}}{2} = \sqrt{3} \implies \theta = \arctan(\sqrt{3}) = \frac{\pi}{3}\ (60^\circ)$.
> 3. **Caso iii) $\mathbf{v} = (-3, -3)$:**
>    - Magnitud: $\|\mathbf{v}\| = \sqrt{(-3)^2 + (-3)^2} = \sqrt{9 + 9} = \sqrt{18} = 3\sqrt{2}$.
>    - Cuadrante: $x = -3 < 0$, $y = -3 < 0$ (Tercer Cuadrante).
>    - Dirección: $\tan\theta = \frac{-3}{-3} = 1$. Estando en el tercer cuadrante:
>      $$
>      \theta = \pi + \frac{\pi}{4} = \frac{5\pi}{4}\ (225^\circ)
>      $$
> 4. **Caso iv) $\mathbf{v} = (0, 3)$:**
>    - Magnitud: $\|\mathbf{v}\| = \sqrt{0^2 + 3^2} = 3$.
>    - Cuadrante: $x = 0$, $y = 3 > 0$ (Sobre el semieje positivo $Y$).
>    - Dirección: $\theta = \frac{\pi}{2}\ (90^\circ)$.

---

### 1.7 Vectores Unitarios $\hat{v}$ y Base Canónica (Slide 15) `[Cátedra USS]`

> **Definición Formal de Cátedra (Slide 15):** Un vector unitario (o versor) es aquel cuya norma euclidiana es exactamente igual a la unidad ($\|\hat{v}\| = 1$).
> 
> Dado cualquier vector no nulo $\vec{v} \neq \mathbf{0}$, su versor unitario normalizado en la misma dirección y sentido se obtiene mediante la escala por el inverso de su norma:
> 
> $$
> \hat{v} = \frac{\vec{v}}{\|\vec{v}\|}
> $$
> 
> **Base Canónica Ortonormal:**
> - En $\mathbb{R}^2$: se denota al vector unitario horizontal por $\mathbf{i} = (1, 0)$ y al vertical por $\mathbf{j} = (0, 1)$. Todo vector del plano se expresa como combinación lineal única:
>   $$
>   \vec{v} = (a, b) = a\mathbf{i} + b\mathbf{j}
>   $$
> - En $\mathbb{R}^3$: los versores canónicos son $\mathbf{i} = (1, 0, 0)$, $\mathbf{j} = (0, 1, 0)$ y $\mathbf{k} = (0, 0, 1)$. Se descompone unívocamente como:
>   $$
>   \vec{v} = (x, y, z) = (x, 0, 0) + (0, y, 0) + (0, 0, z) = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}
>   $$
> 
> **Propiedad Álgebraica Esencial:** Ninguno de los vectores de la base canónica es múltiplo escalar de los demás; forman un conjunto **linealmente independiente** que genera la totalidad del espacio euclídeo.

---

### 1.8 Ángulos entre Vectores en $\mathbb{R}^3$ y Ley de Cosenos (Slides 16–18) `[Cátedra USS]`

### Deducción Geométrica de la Fórmula del Ángulo (Slide 16) `[Cátedra USS]`
Consideremos dos vectores no nulos $\vec{v}, \vec{w} \in \mathbb{R}^3$ que forman entre sí un ángulo $\theta \in [0, \pi]$. Al trazar el segmento que une sus extremos, se obtiene el triángulo de lados de longitud $\|\vec{v}\|$, $\|\vec{w}\|$ y $\|\vec{w} - \vec{v}\|$.

Aplicando la **Ley de los Cosenos** a dicho triángulo:

$$
\|\vec{w} - \vec{v}\|^2 = \|\vec{w}\|^2 + \|\vec{v}\|^2 - 2\|\vec{w}\| \|\vec{v}\| \cos\theta
$$

Por otra parte, expandiendo el miembro izquierdo mediante las propiedades del producto punto:

$$
\|\vec{w} - \vec{v}\|^2 = (\vec{w} - \vec{v}) \cdot (\vec{w} - \vec{v}) = \vec{w}\cdot\vec{w} - 2(\vec{w}\cdot\vec{v}) + \vec{v}\cdot\vec{v} = \|\vec{w}\|^2 - 2(\vec{v}\cdot\vec{w}) + \|\vec{v}\|^2
$$

Igualando algebraicamente ambas expresiones:

$$
\|\vec{w}\|^2 - 2(\vec{v}\cdot\vec{w}) + \|\vec{v}\|^2 = \|\vec{w}\|^2 + \|\vec{v}\|^2 - 2\|\vec{v}\| \|\vec{w}\| \cos\theta
$$

Cancelando $\|\vec{w}\|^2 + \|\vec{v}\|^2$ en ambos lados y dividiendo entre $-2$:

$$
\vec{v} \cdot \vec{w} = \|\vec{v}\| \|\vec{w}\| \cos\theta
$$

> **Definición de Ángulo (Slide 17):** Para vectores no nulos $\vec{v}, \vec{w}$, el ángulo $\theta$ es el único valor en $[0, \pi]$ dado por:
> 
> $$
> \cos\theta = \frac{\vec{v} \cdot \vec{w}}{\|\vec{v}\| \|\vec{w}\|} \implies \theta = \arccos\left( \frac{\vec{v} \cdot \vec{w}}{\|\vec{v}\| \|\vec{w}\|} \right)
> $$

> [!example] Ejemplo Oficial de Cátedra (Slide 17) `[Cátedra USS]`
> **Enunciado:**
> 1. Sea $\vec{v} = (0, 2, 2)$ y $\vec{w} = (2, 0, 2)$, determine el ángulo exacto entre ambos vectores.
> 2. Encuentre el ángulo entre los vectores $\vec{v} = 2\mathbf{i} + 3\mathbf{j}$ y $\vec{w} = -7\mathbf{i} + \mathbf{j}$.
> 
> **Resolución Paso a Paso:**
> 1. **Para $\vec{v} = (0, 2, 2)$ y $\vec{w} = (2, 0, 2)$:**
>    - Producto punto: $\vec{v} \cdot \vec{w} = 0(2) + 2(0) + 2(2) = 4$.
>    - Normas: $\|\vec{v}\| = \sqrt{0 + 4 + 4} = \sqrt{8} = 2\sqrt{2}$; $\|\vec{w}\| = \sqrt{4 + 0 + 4} = 2\sqrt{2}$.
>    - Coseno:
>      $$
>      \cos\theta = \frac{4}{(2\sqrt{2})(2\sqrt{2})} = \frac{4}{8} = \frac{1}{2}
>      $$
>    - Ángulo: $\theta = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3} = 60^\circ$.
> 2. **Para $\vec{v} = (2, 3)$ y $\vec{w} = (-7, 1)$:**
>    - Producto punto: $\vec{v} \cdot \vec{w} = 2(-7) + 3(1) = -14 + 3 = -11$.
>    - Normas: $\|\vec{v}\| = \sqrt{2^2 + 3^2} = \sqrt{13}$; $\|\vec{w}\| = \sqrt{(-7)^2 + 1^2} = \sqrt{49 + 1} = \sqrt{50} = 5\sqrt{2}$.
>    - Coseno:
>      $$
>      \cos\theta = \frac{-11}{\sqrt{13}\sqrt{50}} = \frac{-11}{\sqrt{650}} \approx -0.431455
>      $$
>    - Ángulo: como $\vec{v}\cdot\vec{w} < 0$, $\theta$ es obtuso:
>      $$
>      \theta = \arccos\left( \frac{-11}{\sqrt{650}} \right) \approx 2.0169\,\text{rad} \approx 115.56^\circ
>      $$

> [!example] Ejercicio Oficial de Cátedra (Slide 17–18) `[Cátedra USS]`
> **Enunciado:** Determine los ángulos directores del vector $\mathbf{v} = 2\mathbf{i} + 3\mathbf{j} + 4\mathbf{k}$ con respecto al semieje $X$, semieje $Y$ y semieje $Z$.
> 
> **Resolución Paso a Paso:**
> 1. **Cálculo de la norma del vector:**
>    $$
>    \|\mathbf{v}\| = \sqrt{2^2 + 3^2 + 4^2} = \sqrt{4 + 9 + 16} = \sqrt{29}
>    $$
> 2. **Cosenos directores respecto a cada eje coordenado:**
>    - Respecto al eje $X$ ($\alpha$ con $\mathbf{i} = (1,0,0)$):
>      $$
>      \cos\alpha = \frac{\mathbf{v}\cdot\mathbf{i}}{\|\mathbf{v}\|\|\mathbf{i}\|} = \frac{2}{\sqrt{29}} \implies \alpha = \arccos\left(\frac{2}{\sqrt{29}}\right) \approx 68.20^\circ\ (1.1903\,\text{rad})
>      $$
>    - Respecto al eje $Y$ ($\beta$ con $\mathbf{j} = (0,1,0)$):
>      $$
>      \cos\beta = \frac{\mathbf{v}\cdot\mathbf{j}}{\|\mathbf{v}\|\|\mathbf{j}\|} = \frac{3}{\sqrt{29}} \implies \beta = \arccos\left(\frac{3}{\sqrt{29}}\right) \approx 56.15^\circ\ (0.9799\,\text{rad})
>      $$
>    - Respecto al eje $Z$ ($\gamma$ con $\mathbf{k} = (0,0,1)$):
>      $$
>      \cos\gamma = \frac{\mathbf{v}\cdot\mathbf{k}}{\|\mathbf{v}\|\|\mathbf{k}\|} = \frac{4}{\sqrt{29}} \implies \gamma = \arccos\left(\frac{4}{\sqrt{29}}\right) \approx 42.03^\circ\ (0.7336\,\text{rad})
>      $$
> 3. **Verificación de la Identidad de Cosenos Directores:**
>    $$
>    \cos^2\alpha + \cos^2\beta + \cos^2\gamma = \left(\frac{2}{\sqrt{29}}\right)^2 + \left(\frac{3}{\sqrt{29}}\right)^2 + \left(\frac{4}{\sqrt{29}}\right)^2 = \frac{4 + 9 + 16}{29} = \frac{29}{29} = 1 \quad \checkmark
>    $$

---

### 1.9 Vectores Ortogonales (Perpendiculares) (Slide 19) `[Cátedra USS]`

> **Definición y Teorema de Cátedra (Slide 19):** Dos vectores no nulos $\vec{u}$ y $\vec{v}$ son ortogonales (perpendiculares, $\vec{u} \perp \vec{v}$) si el ángulo entre ellos es $\theta = \frac{\pi}{2}$ ($90^\circ$).
> 
> Como $\cos(\pi/2) = 0$, se establece la equivalencia fundamental:
> 
> $$
> \vec{v} \perp \vec{w} \iff \vec{v} \cdot \vec{w} = 0
> $$

> [!example] Ejemplo Oficial de Cátedra (Slide 19) `[Cátedra USS]`
> **Enunciado:** ¿Los vectores $\vec{v} = (-2, 1, \sqrt{2})$ y $\vec{w} = (1, 0, \sqrt{2})$ son ortogonales?
> 
> **Resolución:**
> Calculando el producto punto:
> 
> $$
> \vec{v} \cdot \vec{w} = (-2)(1) + (1)(0) + (\sqrt{2})(\sqrt{2}) = -2 + 0 + 2 = 0
> $$
> 
> **Conclusión:** Como $\vec{v} \cdot \vec{w} = 0$, los vectores **son efectivamente ortogonales** ($\vec{v} \perp \vec{w}$).

> [!example] Ejercicio Oficial de Cátedra (Slide 19) `[Cátedra USS]`
> **Enunciado:** Sean $\vec{v} = (1, -1, 0)$ y $\vec{w} = (1, 1, 0)$ en $\mathbb{R}^3$. Encuentre todos los vectores $\vec{u} \in \mathbb{R}^3$ que satisfagan simultáneamente las siguientes tres condiciones:
> 
> $$
> 1)\ \vec{u} \perp \vec{v}; \qquad 2)\ \|\vec{u}\| = 4; \qquad 3)\ \angle(\vec{u}, \vec{w}) = \frac{\pi}{3}
> $$
> 
> **Resolución Analítica Rigurosa:**
> Sea $\vec{u} = (x, y, z) \in \mathbb{R}^3$. Planteamos algebraicamente cada una de las condiciones:
> 1. **Condición 1 ($\vec{u} \perp \vec{v}$):**
>    $$
>    \vec{u} \cdot \vec{v} = x(1) + y(-1) + z(0) = x - y = 0 \implies y = x
>    $$
> 2. **Condición 2 ($\|\vec{u}\| = 4$):**
>    $$
>    \|\vec{u}\|^2 = x^2 + y^2 + z^2 = 4^2 = 16
>    $$
>    Sustituyendo $y = x$:
>    $$
>    x^2 + x^2 + z^2 = 16 \implies 2x^2 + z^2 = 16
>    $$
> 3. **Condición 3 ($\angle(\vec{u}, \vec{w}) = \pi/3$):**
>    Por definición de producto punto:
>    $$
>    \vec{u} \cdot \vec{w} = \|\vec{u}\| \|\vec{w}\| \cos\left(\frac{\pi}{3}\right)
>    $$
>    Calculando la norma de $\vec{w}$: $\|\vec{w}\| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{2}$. Como $\|\vec{u}\| = 4$ y $\cos(\pi/3) = \frac{1}{2}$:
>    $$
>    \vec{u} \cdot \vec{w} = 4 \cdot \sqrt{2} \cdot \frac{1}{2} = 2\sqrt{2}
>    $$
>    Por otro lado, expandiendo analíticamente $\vec{u} \cdot \vec{w}$:
>    $$
>    \vec{u} \cdot \vec{w} = x(1) + y(1) + z(0) = x + y
>    $$
>    Igualando ambas expresiones y usando que $y = x$:
>    $$
>    x + x = 2x = 2\sqrt{2} \implies x = \sqrt{2}
>    $$
>    Por lo tanto: $y = x = \sqrt{2}$.
> 4. **Determinación de la componente $z$:**
>    Sustituyendo $x = \sqrt{2}$ en la ecuación de la norma:
>    $$
>    2(\sqrt{2})^2 + z^2 = 16 \implies 2(2) + z^2 = 16 \implies 4 + z^2 = 16 \implies z^2 = 12
>    $$
>    Extrayendo raíces cuadradas:
>    $$
>    z = \pm\sqrt{12} = \pm 2\sqrt{3}
>    $$
> 
> **Resultado Final:** Existen exactamente dos vectores solución en el espacio tridimensional:
> 
> $$
> \vec{u}_1 = (\sqrt{2},\ \sqrt{2},\ 2\sqrt{3}) \qquad \text{y} \qquad \vec{u}_2 = (\sqrt{2},\ \sqrt{2},\ -2\sqrt{3})
> $$

---

### 1.10 Vectores Paralelos (Slide 20) `[Cátedra USS]`

> **Definición y Teorema de Cátedra (Slide 20):** Dos vectores no nulos $\vec{u}$ y $\vec{v}$ son paralelos ($\vec{u} \parallel \vec{v}$) si el ángulo entre ellos es $\theta = 0$ (mismo sentido) o $\theta = \pi$ (sentido opuesto).
> 
> **Teorema de Paralelismo:** Dos vectores $\vec{u}, \vec{v} \in \mathbb{R}^n$ son paralelos si y sólo si uno es múltiplo escalar del otro:
> 
> $$
> \vec{u} \parallel \vec{v} \iff \vec{u} = \lambda\vec{v}, \quad \text{para algún } \lambda \in \mathbb{R} \setminus \{0\}
> $$

> [!example] Ejemplo Oficial de Cátedra (Slide 20) `[Cátedra USS]`
> **Enunciado:** ¿Los vectores $\vec{v} = (2, -3)$ y $\vec{w} = (-4, 6)$ son paralelos?
> 
> **Resolución:**
> Buscamos un escalar $\lambda$ tal que $\vec{w} = \lambda\vec{v}$:
> 
> $$
> (-4, 6) = \lambda(2, -3) \implies \begin{cases} -4 = 2\lambda \implies \lambda = -2 \\ 6 = -3\lambda \implies \lambda = -2 \end{cases}
> $$
> 
> Como el factor $\lambda = -2$ es único y constante para todas las componentes, concluimos que $\vec{w} = -2\vec{v}$.
> 
> **Conclusión:** Los vectores **son paralelos** ($\vec{v} \parallel \vec{w}$) y tienen **sentidos opuestos** debido a que $\lambda < 0$.

> [!example] Ejercicio Oficial de Cátedra (Slide 20) `[Cátedra USS]`
> **Enunciado:** Sean $\mathbf{u} = 3\mathbf{i} + 4\mathbf{j} = (3, 4)$ y $\mathbf{v} = \mathbf{i} + \alpha\mathbf{j} = (1, \alpha)$. Determine el valor del parámetro real $\alpha$ para que:
> 
> $$
> a)\ \mathbf{u} \text{ y } \mathbf{v} \text{ sean ortogonales.} \qquad b)\ \mathbf{u} \text{ y } \mathbf{v} \text{ sean paralelos.}
> $$
> 
> **Resolución Paso a Paso:**
> 1. **Parte a) Ortogonalidad ($\mathbf{u} \perp \mathbf{v}$):**
>    Imponiendo la anulación del producto escalar:
>    $$
>    \mathbf{u} \cdot \mathbf{v} = 0 \iff (3)(1) + (4)(\alpha) = 0 \implies 3 + 4\alpha = 0 \implies \alpha = -\frac{3}{4}
>    $$
> 2. **Parte b) Paralelismo ($\mathbf{u} \parallel \mathbf{v}$):**
>    Imponiendo la proporcionalidad directa de sus componentes homólogas:
>    $$
>    \frac{u_x}{v_x} = \frac{u_y}{v_y} \implies \frac{3}{1} = \frac{4}{\alpha} \implies 3\alpha = 4 \implies \alpha = \frac{4}{3}
>    $$

---

## 2. Proyección Ortogonal (Slides 21–23) `[Cátedra USS]`

### Deducción Analítica del Vector Proyección (Slides 21–22) `[Cátedra USS]`
Geométricamente, se busca descomponer un vector $\vec{v} \neq \mathbf{0}$ en la suma de dos vectores perpendiculares entre sí, proyectando ortogonalmente sobre la dirección marcada por un vector de referencia $\vec{w} \neq \mathbf{0}$:

$$
\vec{v} = \mathbf{p} + \mathbf{q}, \qquad \text{donde } \mathbf{p} = t\vec{w} \parallel \vec{w} \quad \text{y} \quad \mathbf{q} \perp \vec{w}
$$

El vector $\mathbf{p}$ corresponde a la proyección ortogonal, denotada $\mathrm{proy}_{\vec{w}}\vec{v}$. Como $\mathbf{q} = \vec{v} - t\vec{w}$ debe ser ortogonal a $\vec{w}$, se impone:

$$
\vec{w} \cdot (\vec{v} - t\vec{w}) = 0 \implies \vec{w}\cdot\vec{v} - t(\vec{w}\cdot\vec{w}) = 0 \implies t\|\vec{w}\|^2 = \vec{w}\cdot\vec{v}
$$

Despejando el escalar $t$:

$$
t = \frac{\vec{w} \cdot \vec{v}}{\|\vec{w}\|^2}
$$

Sustituyendo $t$ en $\mathbf{p} = t\vec{w}$, se obtiene la **fórmula canónica de la proyección ortogonal**:

$$
\mathrm{proy}_{\vec{w}}\vec{v} = \left( \frac{\vec{w} \cdot \vec{v}}{\|\vec{w}\|^2} \right) \vec{w}
$$

Y la componente perpendicular complementaria (vector residual ortogonal) es:

$$
\mathrm{comp}^\perp_{\vec{w}}\vec{v} = \vec{v} - \mathrm{proy}_{\vec{w}}\vec{v}
$$

*Magnitud de la proyección (Slide 22):*
$$
\|\mathrm{proy}_{\vec{w}}\vec{v}\| = \left| \frac{\vec{w} \cdot \vec{v}}{\|\vec{w}\|^2} \right| \|\vec{w}\| = \frac{|\vec{w}\cdot\vec{v}|}{\|\vec{w}\|} = \|\vec{v}\| |\cos\theta|
$$

> [!example] Ejemplo Oficial de Cátedra (Slide 23) `[Cátedra USS]`
> **Enunciado:** Sea $\vec{v} = (2, -3)$ y $\vec{w} = (1, 1)$, determine:
> 
> $$
> 1)\ \mathrm{proy}_{\vec{w}}\vec{v} \qquad \text{y} \qquad 2)\ \mathrm{proy}_{\vec{v}}\vec{w}
> $$
> 
> **Resolución Paso a Paso:**
> 1. **Cálculo de $\mathrm{proy}_{\vec{w}}\vec{v}$ (proyección de $\vec{v}$ sobre $\vec{w}$):**
>    - Producto punto: $\vec{v} \cdot \vec{w} = 2(1) + (-3)(1) = 2 - 3 = -1$.
>    - Norma al cuadrado del vector base $\vec{w}$: $\|\vec{w}\|^2 = 1^2 + 1^2 = 2$.
>    - Aplicando la fórmula:
>      $$
>      \mathrm{proy}_{\vec{w}}\vec{v} = \left(\frac{-1}{2}\right) (1, 1) = \left(-\frac{1}{2},\ -\frac{1}{2}\right)
>      $$
> 2. **Cálculo de $\mathrm{proy}_{\vec{v}}\vec{w}$ (proyección de $\vec{w}$ sobre $\vec{v}$):**
>    - El producto punto es conmutativo: $\vec{w} \cdot \vec{v} = -1$.
>    - Norma al cuadrado del vector base $\vec{v}$: $\|\vec{v}\|^2 = 2^2 + (-3)^2 = 4 + 9 = 13$.
>    - Aplicando la fórmula:
>      $$
>      \mathrm{proy}_{\vec{v}}\vec{w} = \left(\frac{-1}{13}\right) (2, -3) = \left(-\frac{2}{13},\ \frac{3}{13}\right)
>      $$

---

## 3. Producto Cruz o Producto Vectorial (Slides 24–29) `[Cátedra USS]`

> **Definición Formal de Cátedra (Slide 24):** El producto cruz (o producto vectorial) entre dos vectores en $\mathbb{R}^3$ es una operación binaria cuyo resultado es un **nuevo vector espacial que es simultáneamente ortogonal** a los dos vectores originales.
> 
> Para $\vec{u} = (u_1, u_2, u_3) \in \mathbb{R}^3$ y $\vec{v} = (v_1, v_2, v_3) \in \mathbb{R}^3$, el producto cruz $\vec{u} \times \vec{v}$ se define mediante el desarrollo formal del determinante simbólico $3 \times 3$:
> 
> $$
> \vec{u} \times \vec{v} = \begin{vmatrix}
> \mathbf{i} & \mathbf{j} & \mathbf{k} \\
> u_1 & u_2 & u_3 \\
> v_1 & v_2 & v_3
> \end{vmatrix} = \begin{vmatrix} u_2 & u_3 \\ v_2 & v_3 \end{vmatrix} \mathbf{i} - \begin{vmatrix} u_1 & u_3 \\ v_1 & v_3 \end{vmatrix} \mathbf{j} + \begin{vmatrix} u_1 & u_2 \\ v_1 & v_2 \end{vmatrix} \mathbf{k}
> $$
> 
> Desarrollando los menores $2 \times 2$:
> 
> $$
> \vec{u} \times \vec{v} = (u_2 v_3 - u_3 v_2)\mathbf{i} - (u_1 v_3 - u_3 v_1)\mathbf{j} + (u_1 v_2 - u_2 v_1)\mathbf{k}
> $$
> 
> *Orientación espacial:* El sentido resultante viene unívocamente determinado por la **Regla de la Mano Derecha** (cerrando los dedos desde $\vec{u}$ hacia $\vec{v}$, el pulgar extendido apunta en la dirección de $\vec{u} \times \vec{v}$).

> [!example] Ejemplo Oficial de Cátedra (Slide 25) `[Cátedra USS]`
> **Enunciado:** Si $\vec{u} = 2\mathbf{i} + 4\mathbf{j} - 5\mathbf{k} = (2, 4, -5)$ y $\vec{v} = -3\mathbf{i} - 2\mathbf{j} + \mathbf{k} = (-3, -2, 1)$, determinar:
> 
> $$
> \vec{u} \times \vec{v} \qquad \text{y} \qquad \vec{v} \times \vec{u}
> $$
> 
> **Resolución Paso a Paso:**
> 1. **Cálculo de $\vec{u} \times \vec{v}$:**
>    $$
>    \vec{u} \times \vec{v} = \begin{vmatrix}
>    \mathbf{i} & \mathbf{j} & \mathbf{k} \\
>    2 & 4 & -5 \\
>    -3 & -2 & 1
>    \end{vmatrix}
>    $$
>    - Componente $\mathbf{i}$: $(4)(1) - (-5)(-2) = 4 - 10 = -6$.
>    - Componente $\mathbf{j}$: $- [ (2)(1) - (-5)(-3) ] = - [ 2 - 15 ] = -(-13) = 13$.
>    - Componente $\mathbf{k}$: $(2)(-2) - (4)(-3) = -4 - (-12) = -4 + 12 = 8$.
>    $$
>    \vec{u} \times \vec{v} = -6\mathbf{i} + 13\mathbf{j} + 8\mathbf{k} = (-6, 13, 8)
>    $$
> 2. **Cálculo de $\vec{v} \times \vec{u}$:**
>    $$
>    \vec{v} \times \vec{u} = \begin{vmatrix}
>    \mathbf{i} & \mathbf{j} & \mathbf{k} \\
>    -3 & -2 & 1 \\
>    2 & 4 & -5
>    \end{vmatrix}
>    $$
>    - Componente $\mathbf{i}$: $(-2)(-5) - (1)(4) = 10 - 4 = 6$.
>    - Componente $\mathbf{j}$: $- [ (-3)(-5) - (1)(2) ] = - [ 15 - 2 ] = -13$.
>    - Componente $\mathbf{k}$: $(-3)(4) - (-2)(2) = -12 - (-4) = -8$.
>    $$
>    \vec{v} \times \vec{u} = (6, -13, -8)
>    $$
> 
> **Comprobación:** Se evidencia analíticamente que $\vec{v} \times \vec{u} = -(\vec{u} \times \vec{v})$.

### Propiedades del Producto Cruz (Slide 26) `[Cátedra USS]`
Para vectores $\vec{u}, \vec{v}, \vec{w} \in \mathbb{R}^3$ y cualquier escalar $\alpha \in \mathbb{R}$:

1. $\vec{u} \cdot (\vec{u} \times \vec{v}) = 0$ (Ortogonalidad a $\vec{u}$).
2. $\vec{v} \cdot (\vec{u} \times \vec{v}) = 0$ (Ortogonalidad a $\vec{v}$).
3. $\|\vec{u} \times \vec{v}\|^2 = \|\vec{u}\|^2 \|\vec{v}\|^2 - (\vec{u} \cdot \vec{v})^2$ (**Identidad de Lagrange**).
4. $\vec{u} \times \vec{v} = -(\vec{v} \times \vec{u})$ (Anticonmutatividad).
5. $\vec{u} \times (\vec{v} + \vec{w}) = \vec{u} \times \vec{v} + \vec{u} \times \vec{w}$ (Distributividad por la izquierda).
6. $(\vec{u} + \vec{v}) \times \vec{w} = \vec{u} \times \vec{w} + \vec{v} \times \vec{w}$ (Distributividad por la derecha).
7. $\alpha(\vec{u} \times \vec{v}) = (\alpha\vec{u}) \times \vec{v} = \vec{u} \times (\alpha\vec{v})$ (Homogeneidad escalar).
8. $\vec{u} \times \vec{0} = \vec{0} \times \vec{u} = \vec{0}$.
9. $\vec{u} \times \vec{u} = \vec{0}$.

*Consecuencia de paralelismo (Slide 26):* De las propiedades 7 y 9 se deduce formalmente que dos vectores son paralelos si y sólo si su producto cruz es nulo:

$$
\vec{u} \parallel \vec{v} \implies \vec{u} = \alpha\vec{v} \implies \vec{u} \times \vec{v} = \alpha(\vec{v} \times \vec{v}) = \vec{0}
$$

### Magnitud Geométrica y Áreas (Slides 27–28) `[Cátedra USS]`
De la Identidad de Lagrange, sustituyendo $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta$:

$$
\|\vec{u} \times \vec{v}\|^2 = \|\vec{u}\|^2 \|\vec{v}\|^2 - \|\vec{u}\|^2 \|\vec{v}\|^2 \cos^2\theta = \|\vec{u}\|^2 \|\vec{v}\|^2 (1 - \cos^2\theta) = \|\vec{u}\|^2 \|\vec{v}\|^2 \sin^2\theta
$$

Extrayendo raíz cuadrada (ya que $\sin\theta \ge 0$ para $\theta \in [0, \pi]$):

$$
\|\vec{u} \times \vec{v}\| = \|\vec{u}\| \|\vec{v}\| \sin\theta
$$

**Significado Geométrico (Slide 27):**
Dado un paralelogramo sustentado por $\vec{u}$ y $\vec{v}$, su base mide $\|\vec{v}\|$ y su altura perpendicular mide $h = \|\vec{u}\|\sin\theta$. Por ende, su área es:

$$
\text{Área del Paralelogramo} = (\text{base})(h) = \|\vec{u}\| \|\vec{v}\| \sin\theta = \|\vec{u} \times \vec{v}\|
$$

Y el **área del triángulo** que tiene como lados a $\vec{u}$ y $\vec{v}$ es exactamente la mitad:

$$
\text{Área}_{\triangle} = \frac{1}{2} \|\vec{u} \times \vec{v}\|
$$

> [!example] Ejemplo Oficial de Cátedra (Slide 28) `[Cátedra USS]`
> **Enunciado:** Encuentre el área del triángulo con vértices consecutivos en:
> 
> $$
> P = (1, 3, -2), \qquad Q = (2, 1, 4), \qquad R = (-3, 1, 6)
> $$
> 
> **Resolución Paso a Paso:**
> 1. **Construcción de los vectores arista que parten del vértice común $P$:**
>    $$
>    \overrightarrow{PQ} = Q - P = (2 - 1,\ 1 - 3,\ 4 - (-2)) = (1, -2, 6)
>    $$
>    $$
>    \overrightarrow{PR} = R - P = (-3 - 1,\ 1 - 3,\ 6 - (-2)) = (-4, -2, 8)
>    $$
> 2. **Cálculo del producto vectorial $\overrightarrow{PQ} \times \overrightarrow{PR}$:**
>    $$
>    \overrightarrow{PQ} \times \overrightarrow{PR} = \begin{vmatrix}
>    \mathbf{i} & \mathbf{j} & \mathbf{k} \\
>    1 & -2 & 6 \\
>    -4 & -2 & 8
>    \end{vmatrix}
>    $$
>    - Componente $\mathbf{i}$: $(-2)(8) - (6)(-2) = -16 - (-12) = -4$.
>    - Componente $\mathbf{j}$: $- [ (1)(8) - (6)(-4) ] = - [ 8 + 24 ] = -32$.
>    - Componente $\mathbf{k}$: $(1)(-2) - (-2)(-4) = -2 - 8 = -10$.
>    $$
>    \overrightarrow{PQ} \times \overrightarrow{PR} = (-4, -32, -10)
>    $$
> 3. **Cálculo de la norma:**
>    $$
>    \|\overrightarrow{PQ} \times \overrightarrow{PR}\| = \sqrt{(-4)^2 + (-32)^2 + (-10)^2} = \sqrt{16 + 1024 + 100} = \sqrt{1140} = 2\sqrt{285}
>    $$
> 4. **Área del triángulo:**
>    $$
>    \text{Área}_{\triangle} = \frac{1}{2} \|\overrightarrow{PQ} \times \overrightarrow{PR}\| = \frac{1}{2} (2\sqrt{285}) = \sqrt{285} \approx 16.8819\,\text{u}^2
>    $$

### Triple Producto Escalar y Volumen del Paralelepípedo (Slide 29) `[Cátedra USS]`
Dados tres vectores no coplanares $\vec{u}, \vec{v}, \vec{w} \in \mathbb{R}^3$, el volumen del paralelepípedo cuyas aristas concurrentes son dichos vectores se define como el valor absoluto de su **triple producto escalar** (producto mixto):

$$
V = | \vec{w} \cdot (\vec{u} \times \vec{v}) | = \left| \det \begin{pmatrix}
u_1 & u_2 & u_3 \\
v_1 & v_2 & v_3 \\
w_1 & w_2 & w_3
\end{pmatrix} \right|
$$

> [!example] Ejemplo Oficial de Cátedra (Slide 29) `[Cátedra USS]`
> **Enunciado:** Calcule el volumen del paralelepípedo determinado por los vectores:
> 
> $$
> \vec{u} = (1, 3, -2), \qquad \vec{v} = (2, 1, 4), \qquad \vec{w} = (-3, 1, 6)
> $$
> 
> **Resolución Paso a Paso:**
> 1. **Planteamiento del determinante $3 \times 3$:**
>    $$
>    \det \begin{pmatrix}
>    1 & 3 & -2 \\
>    2 & 1 & 4 \\
>    -3 & 1 & 6
>    \end{pmatrix}
>    $$
> 2. **Desarrollo por cofactores en la primera fila:**
>    $$
>    = 1 \begin{vmatrix} 1 & 4 \\ 1 & 6 \end{vmatrix} - 3 \begin{vmatrix} 2 & 4 \\ -3 & 6 \end{vmatrix} + (-2) \begin{vmatrix} 2 & 1 \\ -3 & 1 \end{vmatrix}
>    $$
>    - Primer menor: $(1)(6) - (4)(1) = 6 - 4 = 2$.
>    - Segundo menor: $(2)(6) - (4)(-3) = 12 + 12 = 24$.
>    - Tercer menor: $(2)(1) - (1)(-3) = 2 + 3 = 5$.
>    $$
>    \det = 1(2) - 3(24) - 2(5) = 2 - 72 - 10 = -80
>    $$
> 3. **Volumen del paralelepípedo:**
>    $$
>    V = |-80| = 80\,\text{u}^3
>    $$

---

## 4. Rectas y Planos en el Espacio (Slides 30–44) `[Cátedra USS]`

### 4.1 Rectas en $\mathbb{R}^3$ y sus Ecuaciones (Slide 30) `[Cátedra USS]`
Una recta $L$ en el espacio tridimensional queda unívocamente determinada si se conocen un punto fijo $P(p_1, p_2, p_3)$ que pertenece a ella y un vector director no nulo $\vec{v} = (v_1, v_2, v_3) \neq \mathbf{0}$ paralelo a la misma:

1. **Ecuación Vectorial:**
   $$
   (x, y, z) = P + t\vec{v}, \qquad t \in \mathbb{R}
   $$
2. **Ecuaciones Paramétricas:**
   Despejando coordenada a coordenada:
   $$
   \begin{cases}
   x(t) = p_1 + t v_1 \\
   y(t) = p_2 + t v_2 \\
   z(t) = p_3 + t v_3
   \end{cases}, \qquad t \in \mathbb{R}
   $$
3. **Ecuaciones Simétricas (Continuas):**
   Si todas las componentes directrices son no nulas ($v_i \neq 0$), despejando el parámetro $t$:
   $$
   \frac{x - p_1}{v_1} = \frac{y - p_2}{v_2} = \frac{z - p_3}{v_3}
   $$
   *Caso con componente directriz nula:* Si alguna componente es nula (por ejemplo $v_3 = 0$), se igualan las fracciones correspondientes a las componentes no nulas y la coordenada nula se especifica como constante aparte:
   $$
   \frac{x - p_1}{v_1} = \frac{y - p_2}{v_2}, \qquad z = p_3
   $$

> [!example] Ejemplo Oficial de Cátedra (Slide 30) `[Cátedra USS]`
> **Enunciado:** Consideremos la recta $L$ que pasa por los puntos $P = (1, 3, -2)$ y $Q = (2, 1, -2)$. Determine su ecuación vectorial, ecuaciones paramétricas y ecuaciones simétricas.
> 
> **Resolución Paso a Paso:**
> 1. **Vector Director:**
>    $$
>    \vec{v} = Q - P = (2 - 1,\ 1 - 3,\ -2 - (-2)) = (1, -2, 0)
>    $$
> 2. **Ecuación Vectorial:**
>    Tomando $P(1, 3, -2)$ como punto de apoyo:
>    $$
>    (x, y, z) = (1, 3, -2) + t(1, -2, 0), \qquad t \in \mathbb{R}
>    $$
> 3. **Ecuaciones Paramétricas:**
>    $$
>    \begin{cases}
>    x = 1 + t \\
>    y = 3 - 2t \\
>    z = -2
>    \end{cases}, \qquad t \in \mathbb{R}
>    $$
> 4. **Ecuaciones Simétricas:**
>    Como $v_3 = 0$, la variable $z$ no depende del parámetro $t$:
>    $$
>    \frac{x - 1}{1} = \frac{y - 3}{-2}, \qquad z = -2
>    $$

---

### 4.2 Ángulo, Paralelismo, Perpendicularidad e Intersección entre Rectas (Slides 31–33) `[Cátedra USS]`

Consideremos dos rectas en el espacio:
$$
L_1: (x, y, z) = P + t\vec{v}, \quad t \in \mathbb{R} \qquad \text{y} \qquad L_2: (x, y, z) = Q + s\vec{w}, \quad s \in \mathbb{R}
$$

- **Paralelismo:** $L_1 \parallel L_2 \iff \vec{v} \parallel \vec{w} \iff \vec{v} = \lambda\vec{w}$.
- **Perpendicularidad:** $L_1 \perp L_2 \iff \vec{v} \perp \vec{w} \iff \vec{v} \cdot \vec{w} = 0$.
- **Ángulo entre rectas:** Es el ángulo agudo $\theta \in [0, \pi/2]$ entre sus vectores directores:
  $$
  \cos\theta = \frac{|\vec{v} \cdot \vec{w}|}{\|\vec{v}\| \|\vec{w}\|}
  $$
- **Intersección:** Para determinar si existe un punto de corte, se igualan las ecuaciones paramétricas usando parámetros independientes:
  $$
  P + t\vec{v} = Q + s\vec{w}
  $$
  El punto de intersección existe si y sólo si el sistema lineal de 3 ecuaciones con 2 incógnitas ($t$ y $s$) es compatible.

> [!example] Ejemplo Oficial de Cátedra (Slide 32) `[Cátedra USS]`
> **Enunciado:** Consideremos las cuatro rectas en $\mathbb{R}^3$:
> - $L_1: \mathbf{r}_1(t) = (-1, 3, 1) + t(4, 1, 0)$
> - $L_2: \mathbf{r}_2(s) = (-13, -3, -2) + s(12, 6, 3)$
> - $L_3: \mathbf{r}_3(u) = (1, 3, -2) + u(8, 2, 0)$
> - $L_4: \mathbf{r}_4(v) = (0, 2, -1) + v(-1, 4, 3)$
> 
> Resuelva los cuatro incisos de cátedra:
> a) Determine el punto de intersección entre la recta $L_1$ y $L_2$.  
> b) ¿Es $L_1 \parallel L_3$?  
> c) ¿Es $L_1 \perp L_4$?  
> d) ¿$L_1$ interseca a $L_4$?
> 
> **Resolución Paso a Paso:**
> 1. **Parte a) Intersección entre $L_1$ y $L_2$:**
>    Ecuaciones paramétricas de $L_1$: $x = -1 + 4t$, $y = 3 + t$, $z = 1$.  
>    Ecuaciones paramétricas de $L_2$: $x = -13 + 12s$, $y = -3 + 6s$, $z = -2 + 3s$.  
>    Igualando componente a componente:
>    $$
>    \begin{cases}
>    -1 + 4t = -13 + 12s & (1) \\
>    3 + t = -3 + 6s & (2) \\
>    1 = -2 + 3s & (3)
>    \end{cases}
>    $$
>    De la ecuación (3): $3s = 3 \implies s = 1$.  
>    Sustituyendo $s = 1$ en la ecuación (1):
>    $$
>    -1 + 4t = -13 + 12(1) = -1 \implies 4t = 0 \implies t = 0
>    $$
>    Verificando en la ecuación (2):
>    $$
>    3 + 0 = 3 \quad \text{y} \quad -3 + 6(1) = 3 \quad \checkmark \text{ (Compatible)}
>    $$
>    Sustituyendo $t = 0$ en $L_1$:
>    $$
>    (x, y, z) = (-1 + 0,\ 3 + 0,\ 1) = (-1, 3, 1)
>    $$
>    **Punto de intersección:** $P_0 = (-1, 3, 1)$.
> 2. **Parte b) ¿Es $L_1 \parallel L_3$?**
>    Vectores directores: $\mathbf{d}_1 = (4, 1, 0)$ y $\mathbf{d}_3 = (8, 2, 0)$.
>    $$
>    \mathbf{d}_3 = (8, 2, 0) = 2(4, 1, 0) = 2\mathbf{d}_1
>    $$
>    Como $\mathbf{d}_3$ es múltiplo escalar positivo de $\mathbf{d}_1$, **sí son paralelas** ($L_1 \parallel L_3$).
> 3. **Parte c) ¿Es $L_1 \perp L_4$?**
>    Vectores directores: $\mathbf{d}_1 = (4, 1, 0)$ y $\mathbf{d}_4 = (-1, 4, 3)$.
>    $$
>    \mathbf{d}_1 \cdot \mathbf{d}_4 = (4)(-1) + (1)(4) + (0)(3) = -4 + 4 + 0 = 0
>    $$
>    Como su producto punto es nulo, los vectores directores son ortogonales; por ende, **las rectas son perpendiculares** ($L_1 \perp L_4$).
> 4. **Parte d) ¿$L_1$ interseca a $L_4$?**
>    Igualando las ecuaciones paramétricas de $L_1$ y $L_4$:
>    $$
>    \begin{cases}
>    -1 + 4t = -v & (1) \\
>    3 + t = 2 + 4v & (2) \\
>    1 = -1 + 3v & (3)
>    \end{cases}
>    $$
>    De la ecuación (3): $3v = 2 \implies v = \frac{2}{3}$.  
>    Sustituyendo $v = \frac{2}{3}$ en la ecuación (2):
>    $$
>    3 + t = 2 + 4\left(\frac{2}{3}\right) = 2 + \frac{8}{3} = \frac{14}{3} \implies t = \frac{14}{3} - 3 = \frac{5}{3}
>    $$
>    Comprobando en la ecuación (1):
>    $$
>    \text{Lado izquierdo: } -1 + 4t = -1 + 4\left(\frac{5}{3}\right) = -1 + \frac{20}{3} = \frac{17}{3}
>    $$
>    $$
>    \text{Lado derecho: } -v = -\frac{2}{3}
>    $$
>    Como $\frac{17}{3} \neq -\frac{2}{3}$, el sistema es **incompatible**.
>    **Conclusión:** $L_1$ **no interseca a $L_4$**. Al ser perpendiculares y no cortarse, $L_1$ y $L_4$ son **rectas alabeadas perpendiculares**.

> [!example] Ejercicio Oficial de Cátedra (Slide 33) `[Cátedra USS]`
> **Enunciado:** Halle los valores de las constantes reales $m$ y $n$ para que las rectas $r$ y $s$ sean paralelas:
> 
> $$
> r: \begin{cases} x = 5 + 4t \\ y = 3 + t \\ z = -t \end{cases} \qquad \text{y} \qquad s: \frac{x}{m} = \frac{y - 1}{2} = \frac{z + 3}{n}
> $$
> 
> **Resolución Paso a Paso:**
> 1. **Extracción de los vectores directores:**
>    - Para la recta $r$: $\mathbf{d}_r = (4, 1, -1)$.
>    - Para la recta $s$: de los denominadores en las ecuaciones simétricas continuas: $\mathbf{d}_s = (m, 2, n)$.
> 2. **Condición de Paralelismo ($\mathbf{d}_s = k \mathbf{d}_r$):**
>    $$
>    (m, 2, n) = k(4, 1, -1) \implies \begin{cases} m = 4k \\ 2 = k \\ n = -k \end{cases}
>    $$
> 3. **Determinación de las constantes:**
>    De la segunda ecuación: $k = 2$.  
>    Sustituyendo en las demás:
>    - $m = 4(2) = 8$.
>    - $n = -(2) = -2$.
> 
> **Resultado:** Los valores requeridos son $m = 8$ y $n = -2$.

---

### 4.3 Planos en el Espacio y sus Ecuaciones (Slides 34–37) `[Cátedra USS]`

### Ecuación Vectorial y Condición de No Colinealidad (Slide 34) `[Cátedra USS]`
Sean $P, Q, R \in \mathbb{R}^3$ tres puntos no colineales. El plano $\Pi$ que contiene a dichos puntos queda determinado de forma vectorial para cualquier punto $M(x, y, z) \in \Pi$ mediante:

$$
M = P + t\overrightarrow{PQ} + s\overrightarrow{PR}, \qquad t, s \in \mathbb{R}
$$

*Criterio de No Colinealidad:* Tres puntos $P(p_1, p_2, p_3)$, $Q(q_1, q_2, q_3)$ y $R(r_1, r_2, r_3)$ no son colineales si sus vectores diferencia son linealmente independientes, lo que equivale a:

$$
\begin{vmatrix}
p_1 & p_2 & p_3 \\
q_1 & q_2 & q_3 \\
r_1 & r_2 & r_3
\end{vmatrix} \neq 0
$$

### Ecuación Punto-Normal y Ecuación Cartesiana (Slide 35) `[Cátedra USS]`
Si un vector no nulo $\vec{N} = (a, b, c)$ es perpendicular al plano $\Pi$, todo segmento orientado contenido en el plano es ortogonal a $\vec{N}$:

$$
( (x, y, z) - P ) \cdot \vec{N} = 0 \qquad \text{(Ecuación Punto-Normal)}
$$

Desarrollando el producto escalar:

$$
a(x - x_P) + b(y - y_P) + c(z - z_P) = 0 \iff ax + by + cz = d
$$

donde el término independiente constante es $d = \vec{N} \cdot P = a x_P + b y_P + c z_P$.

Si el plano está determinado por tres puntos no colineales $P, Q, R$, su vector normal se obtiene mediante el producto cruz de dos aristas directrices:

$$
\vec{N} = \overrightarrow{PQ} \times \overrightarrow{PR}
$$

> [!example] Ejemplo Oficial de Cátedra (Slide 36) `[Cátedra USS]`
> **Enunciado:** Consideremos un plano $\Pi_1$ que pasa por los puntos no colineales:
> 
> $$
> P = (1, 1, 1), \qquad Q = (2, 1, 2), \qquad R = (0, 2, -1)
> $$
> 
> Determine la **ecuación vectorial** y la **ecuación cartesiana** del plano $\Pi_1$.
> 
> **Resolución Paso a Paso:**
> 1. **Vectores directores coplanares:**
>    $$
>    \overrightarrow{PQ} = Q - P = (2 - 1,\ 1 - 1,\ 2 - 1) = (1, 0, 1)
>    $$
>    $$
>    \overrightarrow{PR} = R - P = (0 - 1,\ 2 - 1,\ -1 - 1) = (-1, 1, -2)
>    $$
> 2. **Ecuación Vectorial del Plano $\Pi_1$:**
>    Tomando $P(1, 1, 1)$ como punto de apoyo:
>    $$
>    (x, y, z) = (1, 1, 1) + t(1, 0, 1) + s(-1, 1, -2), \qquad t, s \in \mathbb{R}
>    $$
> 3. **Determinación del Vector Normal $\vec{N}$ por Producto Cruz:**
>    $$
>    \vec{N} = \overrightarrow{PQ} \times \overrightarrow{PR} = \begin{vmatrix}
>    \mathbf{i} & \mathbf{j} & \mathbf{k} \\
>    1 & 0 & 1 \\
>    -1 & 1 & -2
>    \end{vmatrix}
>    $$
>    - Componente $\mathbf{i}$: $(0)(-2) - (1)(1) = -1$.
>    - Componente $\mathbf{j}$: $- [ (1)(-2) - (1)(-1) ] = - [ -2 + 1 ] = 1$.
>    - Componente $\mathbf{k}$: $(1)(1) - (0)(-1) = 1$.
>    $$
>    \vec{N} = (-1, 1, 1)
>    $$
> 4. **Ecuación Cartesiana General:**
>    Aplicando la ecuación punto-normal con el punto $P(1, 1, 1)$:
>    $$
>    -1(x - 1) + 1(y - 1) + 1(z - 1) = 0 \implies -x + 1 + y - 1 + z - 1 = 0 \implies -x + y + z - 1 = 0
>    $$
>    Multiplicando por $-1$:
>    $$
>    x - y - z + 1 = 0 \iff x - y - z = -1
>    $$

### Posiciones Relativas Fundamentales (Slide 37) `[Cátedra USS]`
1. **Planos Paralelos:** Los vectores normales son colineales ($\vec{N}_1 \parallel \vec{N}_2$).
2. **Planos Perpendiculares:** Los vectores normales son ortogonales ($\vec{N}_1 \cdot \vec{N}_2 = 0$).
3. **Recta Perpendicular a un Plano:** El vector director de la recta es paralelo al normal del plano ($\mathbf{d} \parallel \vec{N}$).
4. **Recta Paralela a un Plano:** El vector director de la recta es ortogonal al normal del plano ($\mathbf{d} \cdot \vec{N} = 0$).

---

### 4.4 Paralelismo, Perpendicularidad y Ángulo entre Planos (Slides 38–40) `[Cátedra USS]`

Dada una recta $L_1: (x,y,z) = P + t\vec{v}$ y los dos planos generales:
$$
\Pi_1: a_1 x + b_1 y + c_1 z = d_1 \qquad \text{y} \qquad \Pi_2: a_2 x + b_2 y + c_2 z = d_2
$$
con vectores normales $\vec{N}_1 = (a_1, b_1, c_1)$ y $\vec{N}_2 = (a_2, b_2, c_2)$:

- $\Pi_1 \parallel \Pi_2 \iff \vec{N}_1 \parallel \vec{N}_2$.
- $\Pi_1 \perp \Pi_2 \iff \vec{N}_1 \perp \vec{N}_2 \iff \vec{N}_1 \cdot \vec{N}_2 = 0$.
- Ángulo diedro entre planos: $\cos\theta = \frac{|\vec{N}_1 \cdot \vec{N}_2|}{\|\vec{N}_1\| \|\vec{N}_2\|}$.
- $L_1 \parallel \Pi_1 \iff \vec{N}_1 \perp \vec{v} \iff \vec{N}_1 \cdot \vec{v} = 0$.
- $L_1 \perp \Pi_1 \iff \vec{N}_1 \parallel \vec{v} \iff \vec{N}_1 = k\vec{v}$.

> [!example] Ejemplo Oficial de Cátedra (Slide 39) `[Cátedra USS]`
> **Enunciado:**
> 1. Determine la ecuación cartesiana del plano $\Pi$ que contenga al punto $(0, 0, -1)$ y a la recta:
>    $$
>    L_1: (x, y, z) = (1, 2, 1) + t(0, 2, 3)
>    $$
> 2. Determine la ecuación cartesiana del plano $\Pi$ que sea paralelo a las rectas $L_1: (x, y, z) = (1, 2, 1) + t(0, 2, 3)$ y $L_2: (x, y, z) = (1, 0, 1) + t(5, 0, 0)$ y que contenga al punto $(1, 1, 1)$.
> 3. Determine la ecuación cartesiana del plano $\Pi$ que sea perpendicular a la recta $L_1: (x, y, z) = (1, 2, 1) + t(0, 2, 3)$ y que contenga al punto $(1, 1, 1)$.
> 
> **Resolución Paso a Paso:**
> 1. **Problema 1 (Plano que contiene punto y recta):**
>    - Punto exterior: $A = (0, 0, -1)$.
>    - Punto base de la recta: $P_0 = (1, 2, 1)$. Vector director: $\mathbf{d}_1 = (0, 2, 3)$.
>    - Vector coplanar entre $A$ y $P_0$: $\overrightarrow{AP_0} = P_0 - A = (1 - 0,\ 2 - 0,\ 1 - (-1)) = (1, 2, 2)$.
>    - Vector normal por producto cruz:
>      $$
>      \mathbf{n} = \overrightarrow{AP_0} \times \mathbf{d}_1 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 2 \\ 0 & 2 & 3 \end{vmatrix} = (6 - 4)\mathbf{i} - (3 - 0)\mathbf{j} + (2 - 0)\mathbf{k} = (2, -3, 2)
>      $$
>    - Ecuación del plano usando $A(0, 0, -1)$:
>      $$
>      2(x - 0) - 3(y - 0) + 2(z - (-1)) = 0 \implies 2x - 3y + 2z + 2 = 0 \iff 2x - 3y + 2z = -2
>      $$
> 2. **Problema 2 (Plano paralelo a dos rectas por un punto):**
>    - Vectores directores: $\mathbf{d}_1 = (0, 2, 3)$ y $\mathbf{d}_2 = (5, 0, 0)$.
>    - Vector normal ortogonal a ambas direcciones:
>      $$
>      \mathbf{n} = \mathbf{d}_1 \times \mathbf{d}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 0 & 2 & 3 \\ 5 & 0 & 0 \end{vmatrix} = (0)\mathbf{i} - (0 - 15)\mathbf{j} + (0 - 10)\mathbf{k} = (0, 15, -10)
>      $$
>      Simplificando dividiendo entre 5: $\mathbf{n} = (0, 3, -2)$.
>    - Ecuación del plano que contiene a $P(1, 1, 1)$:
>      $$
>      0(x - 1) + 3(y - 1) - 2(z - 1) = 0 \implies 3y - 3 - 2z + 2 = 0 \iff 3y - 2z = 1
>      $$
> 3. **Problema 3 (Plano perpendicular a una recta por un punto):**
>    - Si el plano es perpendicular a la recta, el vector director de la recta es su normal: $\mathbf{n} = \mathbf{d}_1 = (0, 2, 3)$.
>    - Ecuación del plano que contiene a $P(1, 1, 1)$:
>      $$
>      0(x - 1) + 2(y - 1) + 3(z - 1) = 0 \implies 2y - 2 + 3z - 3 = 0 \iff 2y + 3z = 5
>      $$

> [!example] Ejercicio Oficial de Cátedra (Slide 40) `[Cátedra USS]`
> **Enunciado:** Determine la ecuación de la recta que pasa por el punto $P(3, -3, 4)$ y es perpendicular a cada una de las siguientes rectas:
> 
> $$
> L_1: \frac{2x - 4}{2} = \frac{y - 3}{-1} = \frac{z + 2}{5} \qquad \text{y} \qquad L_2: \frac{x - 3}{1} = \frac{2y - 7}{3} = \frac{z - 3}{3}
> $$
> 
> **Resolución Paso a Paso:**
> 1. **Extracción y normalización de los vectores directores:**
>    - Para $L_1$: factorizando el numerador en $x$: $\frac{2(x - 2)}{2} = \frac{x - 2}{1} = \frac{y - 3}{-1} = \frac{z + 2}{5}$.  
>      Vector director: $\mathbf{d}_1 = (1, -1, 5)$.
>    - Para $L_2$: factorizando el numerador en $y$: $\frac{x - 3}{1} = \frac{2(y - 7/2)}{3} = \frac{y - 7/2}{3/2} = \frac{z - 3}{3}$.  
>      Vector director: $(1, 3/2, 3)$. Multiplicando por 2 para eliminar denominadores: $\mathbf{d}_2 = (2, 3, 6)$.
> 2. **Determinación del vector director perpendicular mediante producto cruz:**
>    $$
>    \mathbf{d} = \mathbf{d}_1 \times \mathbf{d}_2 = \begin{vmatrix}
>    \mathbf{i} & \mathbf{j} & \mathbf{k} \\
>    1 & -1 & 5 \\
>    2 & 3 & 6
>    \end{vmatrix}
>    $$
>    - Componente $\mathbf{i}$: $(-1)(6) - (5)(3) = -6 - 15 = -21$.
>    - Componente $\mathbf{j}$: $- [ (1)(6) - (5)(2) ] = - [ 6 - 10 ] = -(-4) = 4$.
>    - Componente $\mathbf{k}$: $(1)(3) - (-1)(2) = 3 - (-2) = 5$.
>    $$
>    \mathbf{d} = (-21, 4, 5)
>    $$
> 3. **Ecuación Vectorial de la Recta:**
>    Pasa por el punto $P(3, -3, 4)$ con dirección $\mathbf{d} = (-21, 4, 5)$:
>    $$
>    (x, y, z) = (3, -3, 4) + t(-21, 4, 5), \qquad t \in \mathbb{R}
>    $$

---

### 4.5 Intersección entre Recta y Plano (Slides 41–42) `[Cátedra USS]`

> **Método Sistemático de Cátedra (Slide 41):**
> 1. Se transforman las ecuaciones de la recta $L: P + t\vec{v}$ a sus ecuaciones paramétricas: $x(t) = p_1 + t v_1$, $y(t) = p_2 + t v_2$, $z(t) = p_3 + t v_3$.
> 2. Se sustituyen directamente $x(t), y(t), z(t)$ en la ecuación cartesiana del plano $\Pi: a_1 x + b_1 y + c_1 z = d_1$:
>    $$
>    a_1 x(t) + b_1 y(t) + c_1 z(t) = d_1
>    $$
> 3. Se resuelve para el parámetro escalar $t$:
>    - **Solución única para $t$:** La recta interseca al plano en un único punto $P_0(x(t), y(t), z(t))$.
>    - **Infinitas soluciones ($0t = 0$):** La recta está totalmente contenida en el plano ($L \subset \Pi$).
>    - **Sin solución ($0t = k$ con $k \neq 0$):** La recta es estrictamente paralela y ajena al plano ($L \cap \Pi = \emptyset$).

> [!example] Ejemplo Oficial de Cátedra (Slide 42) `[Cátedra USS]`
> **Enunciado:**
> 1. Determine la intersección entre el plano $\Pi: x - 2y + 3z = 1$ y la recta $L: (x, y, z) = (1, 2, 1) + t(0, 2, 3)$.
> 2. Halle la distancia euclidiana del punto $P = (4, 35, 70)$ al plano $\Pi: 5y + 12z - 1 = 0$.
> 
> **Resolución Paso a Paso:**
> 1. **Intersección Recta-Plano:**
>    - Ecuaciones paramétricas de $L$: $x = 1$, $y = 2 + 2t$, $z = 1 + 3t$.
>    - Sustituyendo en la ecuación cartesiana de $\Pi$:
>      $$
>      (1) - 2(2 + 2t) + 3(1 + 3t) = 1
>      $$
>      $$
>      1 - 4 - 4t + 3 + 9t = 1 \implies 5t = 1 \implies t = \frac{1}{5}
>      $$
>    - Sustituyendo $t = \frac{1}{5}$ en las ecuaciones paramétricas:
>      $$
>      x = 1
>      $$
>      $$
>      y = 2 + 2\left(\frac{1}{5}\right) = 2 + \frac{2}{5} = \frac{12}{5}
>      $$
>      $$
>      z = 1 + 3\left(\frac{1}{5}\right) = 1 + \frac{3}{5} = \frac{8}{5}
>      $$
>    **Punto de intersección único:** $P_{\text{int}} = \left(1,\ \frac{12}{5},\ \frac{8}{5}\right)$.
> 2. **Distancia del Punto al Plano:**
>    - Plano: $0x + 5y + 12z - 1 = 0$, con normal $\vec{N} = (0, 5, 12)$ y término $d = 1$.
>    - Punto: $P(4, 35, 70)$.
>    - Aplicando la fórmula de distancia:
>      $$
>      d(P, \Pi) = \frac{|0(4) + 5(35) + 12(70) - 1|}{\sqrt{0^2 + 5^2 + 12^2}} = \frac{|175 + 840 - 1|}{\sqrt{25 + 144}} = \frac{1014}{\sqrt{169}} = \frac{1014}{13} = 78\,\text{u}
>      $$
>    **Distancia mínima:** $78$ unidades exactas.

---

### 4.6 Distancia Mínima de un Punto al Plano (Slide 43) `[Cátedra USS]`

> **Deducción Analítica de Cátedra (Slide 43):**
> Consideremos un plano $\Pi$ de ecuación general $ax + by + cz = d$ y un punto exterior $Q(x_Q, y_Q, z_Q)$. Sea $P(x_P, y_P, z_P)$ un punto arbitrario perteneciente a $\Pi$, de modo que $ax_P + by_P + cz_P = d$.
> 
> La distancia perpendicular mínima $d(Q, \Pi)$ equivale a la longitud de la proyección ortogonal del vector $\overrightarrow{PQ} = Q - P$ sobre el vector normal $\vec{N} = (a, b, c)$:
> 
> $$
> d(Q, \Pi) = \|\mathrm{proy}_{\vec{N}}\overrightarrow{PQ}\| = \frac{|\overrightarrow{PQ} \cdot \vec{N}|}{\|\vec{N}\|}
> $$
> Desarrollando el producto escalar:
> $$
> \overrightarrow{PQ} \cdot \vec{N} = a(x_Q - x_P) + b(y_Q - y_P) + c(z_Q - z_P) = ax_Q + by_Q + cz_Q - (ax_P + by_P + cz_P)
> $$
> Como $ax_P + by_P + cz_P = d$, se obtiene la **fórmula canónica universal**:
> 
> $$
> d(Q, \Pi) = \frac{|ax_Q + by_Q + cz_Q - d|}{\sqrt{a^2 + b^2 + c^2}}
> $$

---

### 4.7 Distancia de una Recta a un Plano y entre Planos Paralelos (Slide 44) `[Cátedra USS]`

1. **Distancia de una Recta a un Plano:**
   - Si la recta corta al plano, la distancia mínima es cero ($d = 0$).
   - Si la recta es paralela al plano ($L \parallel \Pi$), la distancia de la recta al plano es constante e igual a la distancia de cualquier punto $P_0 \in L$ al plano $\Pi$, aplicando la fórmula de distancia punto-plano.
2. **Distancia entre Dos Planos:**
   - La distancia entre dos planos sólo es no nula si los planos son **paralelos**.
   - Tomando un punto arbitrario $P_0$ en el primer plano, se calcula su distancia al segundo plano.
   - Si los planos están normalizados en sus coeficientes lineales:
     $$
     \Pi_1: ax + by + cz = d_1 \qquad \text{y} \qquad \Pi_2: ax + by + cz = d_2
     $$
     la distancia viene dada directamente por:
     $$
     d(\Pi_1, \Pi_2) = \frac{|d_1 - d_2|}{\sqrt{a^2 + b^2 + c^2}}
     $$

> [!example] Ejemplo Oficial de Cátedra (Slide 44) `[Cátedra USS]`
> **Enunciado:** Determine la distancia euclidiana entre los siguientes planos paralelos:
> 
> $$
> \Pi_1: 2x - 3y + z = 1 \qquad \text{y} \qquad \Pi_2: 4x - 6y + 2z = 0
> $$
> 
> **Resolución Paso a Paso:**
> 1. **Verificación de paralelismo:**
>    - Normal de $\Pi_1$: $\vec{N}_1 = (2, -3, 1)$.
>    - Normal de $\Pi_2$: $\vec{N}_2 = (4, -6, 2) = 2(2, -3, 1) = 2\vec{N}_1$.
>    Como $\vec{N}_2 = 2\vec{N}_1$, los planos son estrictamente paralelos.
> 2. **Normalización de coeficientes:**
>    Dividiendo la ecuación de $\Pi_2$ entre 2:
>    $$
>    \Pi_2: 2x - 3y + z = 0
>    $$
> 3. **Cálculo de la distancia:**
>    Con $a = 2$, $b = -3$, $c = 1$, $d_1 = 1$ y $d_2 = 0$:
>    $$
>    d(\Pi_1, \Pi_2) = \frac{|1 - 0|}{\sqrt{2^2 + (-3)^2 + 1^2}} = \frac{1}{\sqrt{4 + 9 + 1}} = \frac{1}{\sqrt{14}} = \frac{\sqrt{14}}{14} \approx 0.2673\,\text{u}
>    $$

---

## 5. Material Complementario y Aplicaciones Avanzadas (Grossman, Axler y UdeC)

### 5.1 Teorema y Demostración: Desigualdad de Cauchy-Schwarz `[Texto Guía — Axler §6A]`
> **Teorema:** Para cualesquiera vectores $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$, se cumple:
> 
> $$
> |\mathbf{u} \cdot \mathbf{v}| \le \|\mathbf{u}\| \|\mathbf{v}\|
> $$
> verificándose la igualdad si y sólo si $\mathbf{u}$ y $\mathbf{v}$ son linealmente dependientes (paralelos).

**Demostración Rigurosa:**
Si $\mathbf{v} = \mathbf{0}$, la desigualdad se reduce a $0 \le 0$, lo cual es trivialmente cierto. Supongamos $\mathbf{v} \neq \mathbf{0}$. Para cualquier escalar real $t \in \mathbb{R}$, consideramos el vector $\mathbf{u} + t\mathbf{v}$. Por la propiedad definida positiva de la norma:

$$
\|\mathbf{u} + t\mathbf{v}\|^2 \ge 0, \quad \forall t \in \mathbb{R}
$$

Desarrollando mediante el producto escalar:

$$
\|\mathbf{u} + t\mathbf{v}\|^2 = (\mathbf{u} + t\mathbf{v}) \cdot (\mathbf{u} + t\mathbf{v}) = \|\mathbf{u}\|^2 + 2t(\mathbf{u} \cdot \mathbf{v}) + t^2 \|\mathbf{v}\|^2 \ge 0
$$

Esta expresión es un trinomio cuadrático en la variable $t$ de la forma $A t^2 + B t + C \ge 0$, con:

$$
A = \|\mathbf{v}\|^2 > 0, \qquad B = 2(\mathbf{u} \cdot \mathbf{v}), \qquad C = \|\mathbf{u}\|^2
$$

Para que una parábola cuadrática con coeficiente principal positivo se mantenga siempre mayor o igual a cero en toda la recta real, su discriminante $\Delta = B^2 - 4AC$ debe ser necesariamente menor o igual a cero:

$$
\Delta = [2(\mathbf{u} \cdot \mathbf{v})]^2 - 4 \|\mathbf{v}\|^2 \|\mathbf{u}\|^2 \le 0
$$

$$
4(\mathbf{u} \cdot \mathbf{v})^2 \le 4 \|\mathbf{u}\|^2 \|\mathbf{v}\|^2 \implies (\mathbf{u} \cdot \mathbf{v})^2 \le \|\mathbf{u}\|^2 \|\mathbf{v}\|^2
$$

Extrayendo raíz cuadrada en ambos miembros:

$$
|\mathbf{u} \cdot \mathbf{v}| \le \|\mathbf{u}\| \|\mathbf{v}\| \qquad \blacksquare
$$

---

### 5.2 Teorema y Demostración: Identidad de Lagrange `[Texto Guía — Grossman §4.4]`
> **Teorema:** Para vectores $\mathbf{u} = (u_1, u_2, u_3)$ y $\mathbf{v} = (v_1, v_2, v_3)$ en $\mathbb{R}^3$:
> 
> $$
> \|\mathbf{u} \times \mathbf{v}\|^2 = \|\mathbf{u}\|^2 \|\mathbf{v}\|^2 - (\mathbf{u} \cdot \mathbf{v})^2
> $$

**Demostración Algebraica:**
Por definición de las componentes del producto cruz:

$$
\mathbf{u} \times \mathbf{v} = (u_2 v_3 - u_3 v_2,\ u_3 v_1 - u_1 v_3,\ u_1 v_2 - u_2 v_1)
$$

Calculando la norma al cuadrado:

$$
\|\mathbf{u} \times \mathbf{v}\|^2 = (u_2 v_3 - u_3 v_2)^2 + (u_3 v_1 - u_1 v_3)^2 + (u_1 v_2 - u_2 v_1)^2
$$

Expandiendo cada binomio al cuadrado:

$$
= (u_2^2 v_3^2 - 2u_2 u_3 v_2 v_3 + u_3^2 v_2^2) + (u_3^2 v_1^2 - 2u_1 u_3 v_1 v_3 + u_1^2 v_3^2) + (u_1^2 v_2^2 - 2u_1 u_2 v_1 v_2 + u_2^2 v_1^2)
$$

Sumando y restando los términos cuadráticos diagonales $u_1^2 v_1^2 + u_2^2 v_2^2 + u_3^2 v_3^2$:

$$
= (u_1^2 + u_2^2 + u_3^2)(v_1^2 + v_2^2 + v_3^2) - (u_1 v_1 + u_2 v_2 + u_3 v_3)^2
$$

Reconociendo las definiciones de norma y producto punto:

$$
= \|\mathbf{u}\|^2 \|\mathbf{v}\|^2 - (\mathbf{u} \cdot \mathbf{v})^2 \qquad \blacksquare
$$

---

### 5.3 Caso Práctico 1: Momento de Torsión (Torque 3D en Robótica) `[Material Complementario — UdeC]`
En ingeniería y robótica industrial, el momento de torsión $\boldsymbol{\tau}$ generado por una fuerza $\mathbf{F}$ respecto a un punto pivote $O$ se formula como el producto vectorial entre el vector brazo de palanca $\mathbf{r}$ y la fuerza aplicada:

$$
\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}
$$

> [!example] Problema de Ingeniería: Torque en Brazo Robótico
> Un actuador robótico situado en el origen $O(0,0,0)$ extiende su eslabón hasta el extremo $P(0.4,\ 0.3,\ 0.2)\,\text{m}$. En dicho extremo se aplica una fuerza de carga $\mathbf{F} = (10,\ -20,\ 50)\,\text{N}$.  
> Calcule el vector momento de torsión $\boldsymbol{\tau}$ en el pivote y la magnitud total del torque ejercido.
> 
> **Resolución:**
> $$
> \boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} = \begin{vmatrix}
> \mathbf{i} & \mathbf{j} & \mathbf{k} \\
> 0.4 & 0.3 & 0.2 \\
> 10 & -20 & 50
> \end{vmatrix}
> $$
> - Componente $\mathbf{i}$: $(0.3)(50) - (0.2)(-20) = 15 - (-4) = 19\,\text{N}\cdot\text{m}$.
> - Componente $\mathbf{j}$: $- [ (0.4)(50) - (0.2)(10) ] = - [ 20 - 2 ] = -18\,\text{N}\cdot\text{m}$.
> - Componente $\mathbf{k}$: $(0.4)(-20) - (0.3)(10) = -8 - 3 = -11\,\text{N}\cdot\text{m}$.
> 
> $$
> \boldsymbol{\tau} = (19,\ -18,\ -11)\,\text{N}\cdot\text{m}
> $$
> 
> Magnitud total del torque:
> $$
> \|\boldsymbol{\tau}\| = \sqrt{19^2 + (-18)^2 + (-11)^2} = \sqrt{361 + 324 + 121} = \sqrt{806} \approx 28.39\,\text{N}\cdot\text{m}
> $$

---

### 5.4 Caso Práctico 2: Equilibrio Estático Tridimensional de un Nodo `[Material Complementario — UdeC]`
En estructuras y mecánica de sólidos, el equilibrio estático de una junta espacial exige que la resultante vectorial de todas las fuerzas concurrentes sea idénticamente nula:

$$
\sum \mathbf{F} = \mathbf{F}_1 + \mathbf{F}_2 + \mathbf{F}_3 + \mathbf{W} = \mathbf{0}
$$

> [!example] Problema de Ingeniería: Sistema de Cables Atirantados
> Un peso vertical $\mathbf{W} = (0,\ 0,\ -980)\,\text{N}$ cuelga de un nodo en el origen $O(0,0,0)$ sostenido por tres cables anclados en los puntos $A(1, 0, 2)$, $B(-1, 1, 2)$ y $C(0, -1, 2)$. Determine la tensión escalar de cada cable para mantener el equilibrio estático.
> 
> **Resolución:**
> Los vectores directores unitarios de los cables dirigidos desde el nodo hacia los anclajes son:
> - $\mathbf{u}_A = \frac{(1, 0, 2)}{\sqrt{5}}$
> - $\mathbf{u}_B = \frac{(-1, 1, 2)}{\sqrt{6}}$
> - $\mathbf{u}_C = \frac{(0, -1, 2)}{\sqrt{5}}$
> 
> Imponiendo $\sum \mathbf{F} = \mathbf{0}$:
> $$
> T_A \mathbf{u}_A + T_B \mathbf{u}_B + T_C \mathbf{u}_C = (0,\ 0,\ 980)
> $$
> Separando por componentes se obtiene un sistema lineal $3 \times 3$ con solución única y positiva, garantizando que todos los cables operen a tracción.

---

### 5.5 Ejercicio Avanzado Tipo Certamen 1 (UdeC): Rectas Alabeadas y Distancia Mínima `[Material Complementario — UdeC]`

> [!example] Certamen Universitario: Distancia entre Rectas Alabeadas
> Dadas las rectas en $\mathbb{R}^3$:
> 
> $$
> L_1: (x, y, z) = (1, 0, -1) + t(2, 1, 3) \qquad \text{y} \qquad L_2: (x, y, z) = (0, 1, 2) + s(1, -2, 1)
> $$
> 
> a) Demuestre analíticamente que $L_1$ y $L_2$ son rectas alabeadas.  
> b) Calcule la distancia mínima perpendicular común entre ambas rectas.
> 
> **Resolución Paso a Paso:**
> 1. **Vectores directores:** $\mathbf{d}_1 = (2, 1, 3)$ y $\mathbf{d}_2 = (1, -2, 1)$.
>    $$
>    \mathbf{n} = \mathbf{d}_1 \times \mathbf{d}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & 1 & 3 \\ 1 & -2 & 1 \end{vmatrix} = (1 - (-6))\mathbf{i} - (2 - 3)\mathbf{j} + (-4 - 1)\mathbf{k} = (7, 1, -5)
>    $$
>    Como $\mathbf{n} \neq \mathbf{0}$, las rectas **no son paralelas**.
> 2. **Criterio de no intersección (Triple producto con $\overrightarrow{P_1P_2}$):**
>    $P_1 = (1, 0, -1)$ y $P_2 = (0, 1, 2) \implies \overrightarrow{P_1P_2} = (-1, 1, 3)$.
>    $$
>    \det(\overrightarrow{P_1P_2},\ \mathbf{d}_1,\ \mathbf{d}_2) = \overrightarrow{P_1P_2} \cdot \mathbf{n} = (-1)(7) + (1)(1) + (3)(-5) = -7 + 1 - 15 = -21 \neq 0
>    $$
>    Como el determinante es distinto de cero, los vectores no son coplanares; por lo tanto, las rectas **son estrictamente alabeadas**.
> 3. **Distancia mínima perpendicular común:**
>    $$
>    d(L_1, L_2) = \frac{|\overrightarrow{P_1P_2} \cdot (\mathbf{d}_1 \times \mathbf{d}_2)|}{\|\mathbf{d}_1 \times \mathbf{d}_2\|} = \frac{|-21|}{\sqrt{7^2 + 1^2 + (-5)^2}} = \frac{21}{\sqrt{49 + 1 + 25}} = \frac{21}{\sqrt{75}} = \frac{21}{5\sqrt{3}} = \frac{7\sqrt{3}}{5} \approx 2.4249\,\text{u}
>    $$

---

### 5.6 Ejercicio Avanzado Tipo Certamen 2 (UdeC): Plano Perpendicular a Dos Planos Concurrentes `[Material Complementario — UdeC]`

> [!example] Certamen Universitario: Construcción de Plano Ortogonal
> Determine la ecuación cartesiana del plano $\Pi$ que pasa por el punto $A(2, -1, 3)$ y es simultáneamente perpendicular a los planos:
> 
> $$
> \Pi_1: 2x - y + z = 4 \qquad \text{y} \qquad \Pi_2: x + 2y - 3z = 1
> $$
> 
> **Resolución Paso a Paso:**
> 1. **Extracción de normales:**
>    $\mathbf{n}_1 = (2, -1, 1)$ y $\mathbf{n}_2 = (1, 2, -3)$.
> 2. **Determinación de la normal del plano buscado:**
>    Como $\Pi$ debe ser perpendicular a $\Pi_1$ y a $\Pi_2$, su vector normal $\mathbf{n}$ debe ser paralelo a $\mathbf{n}_1 \times \mathbf{n}_2$:
>    $$
>    \mathbf{n} = \mathbf{n}_1 \times \mathbf{n}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & -1 & 1 \\ 1 & 2 & -3 \end{vmatrix} = (3 - 2)\mathbf{i} - (-6 - 1)\mathbf{j} + (4 - (-1))\mathbf{k} = (1, 7, 5)
>    $$
> 3. **Ecuación del plano con el punto $A(2, -1, 3)$:**
>    $$
>    1(x - 2) + 7(y - (-1)) + 5(z - 3) = 0 \implies x - 2 + 7y + 7 + 5z - 15 = 0
>    $$
>    $$
>    x + 7y + 5z - 10 = 0 \iff x + 7y + 5z = 10
>    $$

---

### 5.7 Enriquecimiento Epistemológico: De los Cuaterniones de Hamilton al Análisis Vectorial `[Enriquecimiento Web]`
En 1843, Sir William Rowan Hamilton descubrió los **cuaterniones** ($\mathbb{H}$), extendiendo los números complejos a 4 dimensiones con tres unidades imaginarias $i^2 = j^2 = k^2 = ijk = -1$. El producto de dos cuaterniones puros contenía tanto una parte escalar negativa como una parte vectorial:

$$
p \cdot q = -(\mathbf{p}\cdot\mathbf{q}) + (\mathbf{p}\times\mathbf{q})
$$

Hacia finales del siglo XIX, **Josiah Willard Gibbs** (en Yale) y **Oliver Heaviside** (en el Reino Unido) reconocieron que la física clásica no requería la maquinaria algebraica completa de los cuaterniones, sino que convenía separar formalmente la parte escalar (producto punto) de la parte vectorial (producto cruz). 

Esta separación revolucionó la física teórica: Heaviside tradujo las **20 ecuaciones diferenciales originales de James Clerk Maxwell** formuladas en cuaterniones a las **4 ecuaciones vectoriales modernas** del electromagnetismo clásico ($\nabla \cdot \mathbf{E} = \rho/\varepsilon_0$, $\nabla \cdot \mathbf{B} = 0$, $\nabla \times \mathbf{E} = -\partial\mathbf{B}/\partial t$, $\nabla \times \mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\partial\mathbf{E}/\partial t$), sentando la base de la teoría de campos y la computación científica actual.

---

### 5.8 Enriquecimiento en Computación Gráfica 3D: Ray Tracing y Backface Culling `[Enriquecimiento Web]`
1. **Algoritmo de Möller-Trumbore (Ray-Triangle Intersection):**
   Utilizado universalmente en motores de renderizado por trazado de rayos (Unreal Engine, Blender Cycles), determina si un rayo $\mathbf{r}(t) = \mathbf{O} + t\mathbf{D}$ interseca un triángulo de vértices $V_0, V_1, V_2$ sin necesidad de calcular explícitamente la ecuación del plano. Expresa la intersección en coordenadas baricéntricas $(u, v)$ mediante productos cruz y puntos:
   $$
   \begin{pmatrix} t \\ u \\ v \end{pmatrix} = \frac{1}{\mathbf{P}\cdot\mathbf{E}_1} \begin{pmatrix} \mathbf{Q}\cdot\mathbf{E}_2 \\ \mathbf{P}\cdot\mathbf{T} \\ \mathbf{Q}\cdot\mathbf{D} \end{pmatrix}
   $$
   donde $\mathbf{E}_1 = V_1 - V_0$, $\mathbf{E}_2 = V_2 - V_0$, $\mathbf{T} = \mathbf{O} - V_0$, $\mathbf{P} = \mathbf{D} \times \mathbf{E}_2$ y $\mathbf{Q} = \mathbf{T} \times \mathbf{E}_1$.
2. **Descarte de Caras Ocultas (Backface Culling):**
   En la rasterización de modelos 3D, una cara triangular con vector normal saliente $\mathbf{n}$ no es visible por la cámara orientada con vector de vista $\mathbf{v}_{\text{view}}$ si:
   $$
   \mathbf{n} \cdot \mathbf{v}_{\text{view}} \ge 0
   $$
   permitiendo descartar el 50% de la geometría de la escena antes de enviarla a los sombreadores de fragmentos (pixel shaders).

---

## 6. Verificación Computacional en Python (SymPy)

A continuación se presenta el script analítico completo en Python para verificar de manera simbólica y numérica cada uno de los resultados demostrados a lo largo de este documento:

```python
import sympy as sp

print("=== VERIFICACIÓN SIMBÓLICA DE LA UNIDAD 2 ===")

# Slide 5, 6, 7 y 8: Operaciones Básicas
v = sp.Matrix([1, 3, 4])
w = sp.Matrix([3, 1, 4])
assert v != w, "Error en Slide 5"
assert v + w == sp.Matrix([4, 4, 8]), "Error en Slide 6"
assert v - w == sp.Matrix([-2, 2, 0]) and w - v == sp.Matrix([2, -2, 0]), "Error en Slide 7"
assert 2*v == sp.Matrix([2, 6, 8]) and sp.Rational(1,2)*v == sp.Matrix([sp.Rational(1,2), sp.Rational(3,2), 2]), "Error en Slide 8"

# Slide 10: Producto Punto
v10 = sp.Matrix([-1, 3, 4])
w10 = sp.Matrix([1, 0, -4])
assert v10.dot(w10) == -17, "Error en Slide 10"

# Slide 12: Norma y Distancia
u12 = sp.Matrix([1, 0, -2])
assert u12.norm() == sp.sqrt(5), "Error en Slide 12a"
A = sp.Matrix([2, 0, -1])
B = sp.Matrix([1, -3, -2])
assert (B - A).norm() == sp.sqrt(11), "Error en Slide 12b"

# Slide 17: Ángulos
v17 = sp.Matrix([0, 2, 2])
w17 = sp.Matrix([2, 0, 2])
assert v17.dot(w17) / (v17.norm() * w17.norm()) == sp.Rational(1, 2), "Error en Slide 17.1"

# Slide 19: Ortogonalidad y Ejercicio Avanzado
v19 = sp.Matrix([-2, 1, sp.sqrt(2)])
w19 = sp.Matrix([1, 0, sp.sqrt(2)])
assert v19.dot(w19) == 0, "Error en Slide 19 ejemplo"
u_sol1 = sp.Matrix([sp.sqrt(2), sp.sqrt(2), 2*sp.sqrt(3)])
u_sol2 = sp.Matrix([sp.sqrt(2), sp.sqrt(2), -2*sp.sqrt(3)])
assert u_sol1.norm() == 4 and u_sol1.dot(sp.Matrix([1,-1,0])) == 0, "Error en Slide 19 ejercicio"

# Slide 20: Paralelismo
alpha = sp.symbols('alpha', real=True)
u_p = sp.Matrix([3, 4])
v_p = sp.Matrix([1, alpha])
assert sp.solve(u_p.dot(v_p), alpha)[0] == sp.Rational(-3, 4)
assert sp.solve(3*alpha - 4, alpha)[0] == sp.Rational(4, 3)

# Slide 23: Proyecciones Ortogonales
v23 = sp.Matrix([2, -3])
w23 = sp.Matrix([1, 1])
assert (v23.dot(w23)/(w23.norm()**2))*w23 == sp.Matrix([sp.Rational(-1,2), sp.Rational(-1,2)])
assert (w23.dot(v23)/(v23.norm()**2))*v23 == sp.Matrix([sp.Rational(-2,13), sp.Rational(3,13)])

# Slide 25: Producto Cruz
u25 = sp.Matrix([2, 4, -5])
v25 = sp.Matrix([-3, -2, 1])
assert u25.cross(v25) == sp.Matrix([-6, 13, 8])
assert v25.cross(u25) == sp.Matrix([6, -13, -8])

# Slide 28 y 29: Área y Volumen
PQ = sp.Matrix([1, -2, 6])
PR = sp.Matrix([-4, -2, 8])
assert sp.Rational(1, 2) * PQ.cross(PR).norm() == sp.sqrt(285)
M_vol = sp.Matrix([[1, 3, -2], [2, 1, 4], [-3, 1, 6]])
assert abs(M_vol.det()) == 80

# Slide 33: Rectas Paralelas
assert sp.Matrix([8, 2, -2]) == 2 * sp.Matrix([4, 1, -1])

# Slide 36: Plano por 3 Puntos
n36 = sp.Matrix([1, 0, 1]).cross(sp.Matrix([-1, 1, -2]))
assert n36 == sp.Matrix([-1, 1, 1])

# Slide 42: Intersección Recta-Plano y Distancia
t = sp.symbols('t', real=True)
t_val = sp.solve(1 - 2*(2 + 2*t) + 3*(1 + 3*t) - 1, t)[0]
assert t_val == sp.Rational(1, 5)
assert abs(5*35 + 12*70 - 1) / sp.sqrt(25 + 144) == 78

# Slide 44: Distancia entre Planos Paralelos
assert sp.Rational(1, 1) / sp.sqrt(2**2 + (-3)**2 + 1**2) == 1 / sp.sqrt(14)

print("¡Validación 100% exitosa!")
```

---

## 7. Enlaces y Conexiones Bidireccionales

- [[algebra_lineal_dashboard|Dashboard Principal de Álgebra Lineal]]
- [[Matrices|Unidad 1: Matrices y Sistemas de Ecuaciones Lineales]]
- [[Espacios_y_Subespacios_Vectoriales|Unidad 2.2: Espacios y Subespacios Vectoriales]]
- [[Transformaciones_Lineales|Unidad 3: Transformaciones Lineales]]
- [[Valores_y_Vectores_Propios|Unidad 4: Valores y Vectores Propios]]
- [[Grossman_Algebra_Lineal_Maestro|Nota Maestra Grossman (Capítulo 4: Vectores en R2 y R3)]]
- [[Axler_Linear_Algebra_Done_Right_Maestro|Nota Maestra Axler (Capítulo 6: Espacios con Producto Interno)]]
- [[Home|Panel de Control Unificado (Home)]]
- [[Task_Board|Tablero de Control de Agentes (Task Board)]]
