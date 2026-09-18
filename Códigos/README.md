---
title: "Suite de Simuladores 3D y Cuadernos Interactivos de Álgebra Lineal"
proyecto: "Álgebra Lineal (DCEX0007)"
carrera: "Ingeniería Civil Informática"
institución: "Universidad San Sebastián — Sede Patagonia"
autor: "Moisés Amundarain Romero"
docente: "Carol Asencio González"
status: "activo"
---

<div align="center">

# 📐 Suite de Simuladores 3D, Álgebra Simbólica y Cuadernos Interactivos
### Álgebra Lineal (DCEX0007) — Universidad San Sebastián

![Python](https://img.shields.io/badge/Python-3.10%2B-00205B?style=for-the-badge&logo=python&logoColor=D4AF37)
![SymPy](https://img.shields.io/badge/SymPy-Symbolic--Math-00205B?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Linear--Algebra-00205B?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3D--Visualizations-00205B?style=for-the-badge&logo=python&logoColor=D4AF37)
![Jupyter](https://img.shields.io/badge/Jupyter-Interactive--Notebooks-00205B?style=for-the-badge&logo=jupyter&logoColor=white)
![Widgets](https://img.shields.io/badge/ipywidgets-8.0%2B-D4AF37?style=for-the-badge&logo=jupyter&logoColor=00205B)

<br/>

**Repositorio de Simulación Computacional, Álgebra Simbólica Exacta y Geometría Tridimensional**  
Diseñado y desarrollado por **Moisés Amundarain Romero**  
Ingeniería Civil Informática — Sede De la Patagonia, Puerto Montt  
Docente de Cátedra: **Carol Asencio González**

</div>

---

## 🧭 Trazabilidad y Demarcación de Fuentes (Source Provenance Standard)

En cumplimiento de los estándares de rigurosidad académica y propiedad intelectual, cada módulo, demostración y algoritmo implementado cuenta con la siguiente demarcación explícita:

* 🎓 **`[Cátedra USS / Diapositivas Docente]`**: Operaciones Elementales por Fila (OEF), Forma Escalonada Reducida por Filas (RREF), Teorema de Rouché-Frobenius, discusión de sistemas con parámetros, matriz de cofactores y adjunta, álgebra vectorial en $\mathbb{R}^2/\mathbb{R}^3$, producto cruz, ecuaciones vectoriales, paramétricas y simétricas de la recta y el plano.
* 📖 **`[Texto Guía — Grossman / Poole / Axler]`**: Interpretación geométrica tridimensional de sistemas $3 \times 3$, geometría de prismas triangulares y planos paralelos disjuntos (casos de inconsistencia), identidades vectoriales formales (Lagrange, Cauchy-Schwarz, Jacobi), distancias entre rectas alabeadas y volúmenes de paralelepípedos y tetraedros.
* 🌐 **`[Computación Científica y Simulación Física]`**: Aritmética simbólica racional exacta con SymPy, modelado numérico con NumPy/SciPy, renderizado volumétrico y poligonal 3D con Matplotlib (`Poly3DCollection`, superficies malladas), simulación cinemática/estática de torque $6 \times 6$ y controles interactivos en tiempo real con `ipywidgets`.

---

## 🎨 Paleta Institucional USS y Estándar Visual

Todos los gráficos generados por los scripts `.py` y cuadernos `.ipynb` implementan estrictamente la identidad cromática institucional de la Universidad San Sebastián:

| Color | Código HEX | Rol Gráfico / Significado Matemático |
| :--- | :---: | :--- |
| **USS Blue Principal** | `#00205B` | Ejes coordenados principales, vectores base $\mathbf{u}$, títulos, matrices canónicas. |
| **USS Gold** | `#D4AF37` | Soluciones únicas, rectas de intersección $\Pi_1 \cap \Pi_2$, vectores resultantes $\mathbf{u} \times \mathbf{v}$, torques $\boldsymbol{\tau}$. |
| **Deep Blue / Secondary** | `#1B365D` | Planos $\Pi_1$, vectores secundarios $\mathbf{v}$, contornos estructurales. |
| **Light Blue Accent** | `#4A90E2` | Planos $\Pi_2$, proyecciones ortogonales $\operatorname{proy}_{\mathbf{v}}(\mathbf{u})$, componentes vectoriales. |
| **Alert / Inconsistencia** | `#C0392B` | Planos de inconsistencia (SI), puntos singulares $k_{\text{crítico}}$, componentes ortogonales $\mathbf{u}_\perp$. |
| **Teal / Subespacios** | `#16A085` | Planos $\Pi_3$, cables tensores, áreas sustentadas. |
| **Dark Slate** | `#2C3E50` | Mallas de fondo, textos analíticos y marcos matriciales. |

---

## 🗂️ Arquitectura Modular del Directorio `Códigos/`

```text
Códigos/
├── README.md                                               # Este documento de presentación técnica
│
├── 01_Sistemas_Lineales_y_Matrices/                         # Unidad 1: Álgebra Matricial y Sistemas
│   ├── 01_gauss_jordan_y_rouche_frobenius_3d.py            # CLI: Eliminación Gauss-Jordan y Rouché-Frobenius 3D
│   ├── 01_gauss_jordan_y_rouche_frobenius_3d.ipynb         # Notebook interactivo con sliders y cámara 3D
│   ├── 01_gauss_rouche_scd.png                             # Render: Sistema Compatible Determinado (Punto único)
│   ├── 01_gauss_rouche_sci.png                             # Render: Sistema Compatible Indeterminado (Recta común)
│   ├── 01_gauss_rouche_si.png                              # Render: Sistema Incompatible (Prisma triangular)
│   ├── 02_sistemas_parametrizados_k.py                     # CLI: Discusión analítica con parámetro real k
│   ├── 02_sistemas_parametrizados_k.ipynb                  # Notebook con slider continuo de k y análisis de raíces
│   ├── 02_sistema_parametrico_k_3d.png                     # Render: Geometría de los planos según k
│   ├── 02_sistema_parametrico_k_analisis.png               # Gráfico: Determinante det(A(k)) vs k y singularidades
│   ├── 03_matrices_cofactores_e_inversa.py                 # CLI: Menores, cofactores, adjunta e inversa formal
│   ├── 03_matrices_cofactores_e_inversa.ipynb              # Notebook interactivo con mapas de calor de matrices
│   └── 03_matrices_cofactores_inversa_diagrama.png         # Render: Mapas de calor de A, Cof(A), Adj(A) y A^(-1)
│
├── 02_Geometria_Vectorial_R2_R3/                           # Unidad 2: Geometría del Espacio Euclidiano
│   ├── 04_vectores_fundamentos_y_proyecciones.py           # CLI: Producto punto, cosenos directores y proyecciones
│   ├── 04_vectores_fundamentos_y_proyecciones.ipynb        # Notebook interactivo 2D y 3D con descomposición ortogonal
│   ├── 04_vectores_fundamentos_y_proyecciones.png          # Render: Triángulo de proyección y verificación de Pitágoras
│   ├── 05_producto_cruz_y_paralelepipedos_3d.py            # CLI: Producto vectorial, áreas y producto mixto
│   ├── 05_producto_cruz_y_paralelepipedos_3d.ipynb         # Notebook interactivo con volumen de paralelepípedo
│   ├── 05_producto_cruz_y_paralelepipedos_3d.png          # Render 3D: Paralelepípedo volumétrico (Poly3DCollection)
│   ├── 06_rectas_en_r3_y_rectas_alabeadas.py               # CLI: Clasificación de rectas y distancia mínima
│   ├── 06_rectas_en_r3_y_rectas_alabeadas.ipynb            # Notebook interactivo de rectas alabeadas y segmento ortogonal
│   ├── 06_rectas_en_r3_y_rectas_alabeadas.png              # Render 3D: Rectas alabeadas y vector de mínima separación
│   ├── 07_planos_en_r3_e_intersecciones.py                 # CLI: Ecuaciones del plano, ángulo diedro y recta intersección
│   ├── 07_planos_en_r3_e_intersecciones.ipynb              # Notebook interactivo de intersección de planos
│   └── 07_planos_en_r3_e_intersecciones.png                # Render 3D: Planos secantes y vector director común
│
└── 03_Aplicaciones_Fisicas_y_Simulaciones/                  # Modelado Físico y Sistemas Estáticos
    ├── 08_simulacion_torque_y_equilibrio_3d.py             # CLI: Simulación de torque y equilibrio de cuerpo rígido
    ├── 08_simulacion_torque_y_equilibrio_3d.ipynb          # Notebook interactivo con control de cargas y ángulos
    ├── 08_simulacion_torque_y_equilibrio_3d.png            # Render 3D: Pluma mecánica, tensores espaciales y reacciones
    └── figura_simulacion_torque_equilibrio_3d.png          # Esquema técnico complementario de equilibrio
```

---

## 📊 Matriz Comparativa de los 8 Simuladores

| # | Módulo | Concepto Central | Script CLI (`.py`) | Cuaderno Interactivo (`.ipynb`) | Modelado Matemático Clave | Salida Visual |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | **Gauss-Jordan & Rouché-Frobenius** | Rango matricial, OEF y consistencia 3D | `01_gauss_jordan_y_rouche_frobenius_3d.py` | `01_gauss_jordan_y_rouche_frobenius_3d.ipynb` | $\operatorname{rg}(A)$ vs $\operatorname{rg}(A\|B)$<br/>SCD, SCI, SI | 3 planos en $\mathbb{R}^3$, punto de corte, haz de planos o prisma. |
| **02** | **Sistemas Parametrizados $k$** | Determinantes y discusión de bifurcaciones | `02_sistemas_parametrizados_k.py` | `02_sistemas_parametrizados_k.ipynb` | $\det(A(k)) = 0$<br/>Raíces críticas $k_i$ | Gráfico $\det(A(k))$ vs $k$ y configuración 3D instantánea. |
| **03** | **Cofactores e Inversa Matricial** | Expansión de Laplace e inversión analítica | `03_matrices_cofactores_e_inversa.py` | `03_matrices_cofactores_e_inversa.ipynb` | $A^{-1} = \frac{1}{\det(A)} \operatorname{Adj}(A)$<br/>$A \cdot A^{-1} = I_n$ | Mapas de calor matriciales con anotaciones numéricas y colores USS. |
| **04** | **Vectores & Proyecciones $\mathbb{R}^2/\mathbb{R}^3$** | Cosenos directores y descomposición ortogonal | `04_vectores_fundamentos_y_proyecciones.py` | `04_vectores_fundamentos_y_proyecciones.ipynb` | $\mathbf{u} = \operatorname{proy}_{\mathbf{v}}(\mathbf{u}) + \mathbf{u}_\perp$<br/>Cauchy-Schwarz | Triángulo vectorial 2D/3D con ángulo $\theta$ y cosenos directores. |
| **05** | **Producto Cruz & Paralelepípedos** | Ortogonalidad vectorial y volúmenes 3D | `05_producto_cruz_y_paralelepipedos_3d.py` | `05_producto_cruz_y_paralelepipedos_3d.ipynb` | $V = \|\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})\|$<br/>Identidad de Lagrange | Paralelepípedo sólido 3D con 6 caras poligonales semitransparentes. |
| **06** | **Rectas en $\mathbb{R}^3$ & Alabeadas** | Posiciones relativas y mínima distancia | `06_rectas_en_r3_y_rectas_alabeadas.py` | `06_rectas_en_r3_y_rectas_alabeadas.ipynb` | $d = \frac{\|(\mathbf{P}_2 - \mathbf{P}_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2)\|}{\|\mathbf{d}_1 \times \mathbf{d}_2\|}$ | Trayectorias de rectas en el espacio y segmento ortogonal de mínima separación. |
| **07** | **Planos en $\mathbb{R}^3$ & Ángulo Diedro** | Ecuación general e intersección de planos | `07_planos_en_r3_e_intersecciones.py` | `07_planos_en_r3_e_intersecciones.ipynb` | $\mathbf{d} = \mathbf{n}_1 \times \mathbf{n}_2$<br/>$\cos\theta = \frac{\|\mathbf{n}_1 \cdot \mathbf{n}_2\|}{\|\mathbf{n}_1\|\|\mathbf{n}_2\|}$ | Superficies de planos secantes y recta de intersección dorada. |
| **08** | **Torque 3D & Equilibrio Estático** | Estática de cuerpo rígido y tensores espaciales | `08_simulacion_torque_y_equilibrio_3d.py` | `08_simulacion_torque_y_equilibrio_3d.ipynb` | Sistema lineal $6 \times 6$:<br/>$\sum \mathbf{F} = \mathbf{0}$, $\sum \boldsymbol{\tau}_O = \mathbf{0}$ | Brazo mecánico en 3D, cables tensores, cargas y vector de torque. |

---

## 🔬 Descripción Técnica Detallada por Módulo

### Módulo 01: Sistemas de Ecuaciones Lineales y Rouché-Frobenius 3D
* **Archivo CLI:** `01_Sistemas_Lineales_y_Matrices/01_gauss_jordan_y_rouche_frobenius_3d.py`
* **Cuaderno:** `01_Sistemas_Lineales_y_Matrices/01_gauss_jordan_y_rouche_frobenius_3d.ipynb`
* **Fundamento Matemático:**
  Dado el sistema lineal $A\mathbf{x} = \mathbf{b}$ con $A \in \mathcal{M}_{m \times n}(\mathbb{R})$ y matriz aumentada $(A|\mathbf{b})$:
  $$ \operatorname{RREF}(A|\mathbf{b}) \implies \begin{cases}
  \operatorname{rg}(A) < \operatorname{rg}(A|\mathbf{b}) & \implies \text{Sistema Incompatible (SI, } \emptyset\text{)} \\
  \operatorname{rg}(A) = \operatorname{rg}(A|\mathbf{b}) = n & \implies \text{Sistema Compatible Determinado (SCD, solución única)} \\
  \operatorname{rg}(A) = \operatorname{rg}(A|\mathbf{b}) < n & \implies \text{Sistema Compatible Indeterminado (SCI, } \infty\text{ soluciones)}
  \end{cases} $$
* **Interactividad en Jupyter:** Deslizadores de coeficientes independientes, menú desplegable para alternar instantáneamente entre casos SCD, SCI y SI, y rotación de azimut/elevación en la cámara 3D.

---

### Módulo 02: Discusión de Sistemas Parametrizados con Parámetro $k$
* **Archivo CLI:** `01_Sistemas_Lineales_y_Matrices/02_sistemas_parametrizados_k.py`
* **Cuaderno:** `01_Sistemas_Lineales_y_Matrices/02_sistemas_parametrizados_k.ipynb`
* **Fundamento Matemático:**
  Sea $A(k)$ una matriz cuadrada con coeficientes dependientes de $k \in \mathbb{R}$. La invertibilidad depende de las raíces del polinomio característico del determinante:
  $$ \det(A(k)) = 0 \implies k \in \{k_1, k_2, \dots, k_p\} $$
  Para todo $k \notin \{k_1, \dots, k_p\}$, $\operatorname{rg}(A(k)) = n \implies \text{SCD}$. Para cada valor crítico $k_i$, se sustituye formalmente en $(A(k_i)|\mathbf{b}(k_i))$ y se computa la forma escalonada para discernir entre SCI y SI.
* **Interactividad en Jupyter:** Slider continuo `FloatSlider` para $k \in [-5, 5]$ que calcula en tiempo real $\det(A(k))$, evalúa rangos simbólicos en SymPy y actualiza dinámicamente la vista 3D de los tres planos.

---

### Módulo 03: Menores, Cofactores, Matriz Adjunta e Inversa
* **Archivo CLI:** `01_Sistemas_Lineales_y_Matrices/03_matrices_cofactores_e_inversa.py`
* **Cuaderno:** `01_Sistemas_Lineales_y_Matrices/03_matrices_cofactores_e_inversa.ipynb`
* **Fundamento Matemático:**
  Dada $A \in \mathcal{M}_{n \times n}(\mathbb{R})$:
  $$ C_{ij} = (-1)^{i+j} M_{ij}, \quad \operatorname{Cof}(A) = [C_{ij}], \quad \operatorname{Adj}(A) = [\operatorname{Cof}(A)]^T $$
  $$ A \cdot \operatorname{Adj}(A) = \det(A) I_n \implies A^{-1} = \frac{1}{\det(A)} \operatorname{Adj}(A) \quad (\text{si } \det(A) \neq 0) $$
* **Interactividad en Jupyter:** Matrices editables interactivas con cálculo instantáneo de determinantes por expansión de Laplace, visualización de matrices de paso y mapas de calor con gradiente institucional USS.

---

### Módulo 04: Vectores en $\mathbb{R}^2/\mathbb{R}^3$, Cosenos Directores y Proyecciones
* **Archivo CLI:** `02_Geometria_Vectorial_R2_R3/04_vectores_fundamentos_y_proyecciones.py`
* **Cuaderno:** `02_Geometria_Vectorial_R2_R3/04_vectores_fundamentos_y_proyecciones.ipynb`
* **Fundamento Matemático:**
  Para $\mathbf{u}, \mathbf{v} \in \mathbb{R}^3$:
  $$ \mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta, \quad \cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|} $$
  $$ \operatorname{proy}_{\mathbf{v}}(\mathbf{u}) = \left(\frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{v}\|^2}\right)\mathbf{v}, \quad \mathbf{u}_\perp = \mathbf{u} - \operatorname{proy}_{\mathbf{v}}(\mathbf{u}) $$
  Verificación formal: $\mathbf{u}_\perp \cdot \mathbf{v} = 0$, y teorema de Pitágoras vectorial $\|\mathbf{u}\|^2 = \|\operatorname{proy}_{\mathbf{v}}(\mathbf{u})\|^2 + \|\mathbf{u}_\perp\|^2$.
* **Interactividad en Jupyter:** Sliders de coordenadas de $\mathbf{u}$ y $\mathbf{v}$, visualización dual 2D y 3D, y cálculo automático de cosenos directores $\cos\alpha, \cos\beta, \cos\gamma$.

---

### Módulo 05: Producto Cruz, Identidad de Lagrange y Paralelepípedos 3D
* **Archivo CLI:** `02_Geometria_Vectorial_R2_R3/05_producto_cruz_y_paralelepipedos_3d.py`
* **Cuaderno:** `02_Geometria_Vectorial_R2_R3/05_producto_cruz_y_paralelepipedos_3d.ipynb`
* **Fundamento Matemático:**
  $$ \mathbf{u} \times \mathbf{v} = \begin{vmatrix} \hat{\mathbf{i}} & \hat{\mathbf{j}} & \hat{\mathbf{k}} \\ u_x & u_y & u_z \\ v_x & v_y & v_z \end{vmatrix}, \quad \|\mathbf{u} \times \mathbf{v}\|^2 = \|\mathbf{u}\|^2\|\mathbf{v}\|^2 - (\mathbf{u}\cdot\mathbf{v})^2 \quad (\text{Lagrange}) $$
  $$ V_{\text{paralelepípedo}} = |[\mathbf{u}, \mathbf{v}, \mathbf{w}]| = |\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})| = |\det([\mathbf{u}, \mathbf{v}, \mathbf{w}])| $$
* **Interactividad en Jupyter:** Generación de sólidos 3D con `Poly3DCollection`, control de transparencia alfa de las caras, cálculo de áreas de paralelogramos y triángulos, y verificación de anticonmutatividad.

---

### Módulo 06: Rectas en $\mathbb{R}^3$, Posiciones Relativas y Distancia entre Rectas Alabeadas
* **Archivo CLI:** `02_Geometria_Vectorial_R2_R3/06_rectas_en_r3_y_rectas_alabeadas.py`
* **Cuaderno:** `02_Geometria_Vectorial_R2_R3/06_rectas_en_r3_y_rectas_alabeadas.ipynb`
* **Fundamento Matemático:**
  Dadas $L_1: \mathbf{r}_1(t) = \mathbf{P}_1 + t\mathbf{d}_1$ y $L_2: \mathbf{r}_2(s) = \mathbf{P}_2 + s\mathbf{d}_2$:
  $$ d(L_1, L_2) = \frac{|(\mathbf{P}_2 - \mathbf{P}_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2)|}{\|\mathbf{d}_1 \times \mathbf{d}_2\|} $$
  Los puntos más cercanos $Q_1 \in L_1$ y $Q_2 \in L_2$ se obtienen del sistema lineal exacto impuesto por la ortogonalidad simultánea:
  $$ \begin{cases} (Q_2 - Q_1) \cdot \mathbf{d}_1 = 0 \\ (Q_2 - Q_1) \cdot \mathbf{d}_2 = 0 \end{cases} $$
* **Interactividad en Jupyter:** Selección de puntos y vectores directores, clasificación instantánea (coincidentes, paralelas, secantes, alabeadas) y trazado del segmento de mínima distancia perpendicular.

---

### Módulo 07: Planos en $\mathbb{R}^3$, Ángulo Diedro e Intersección
* **Archivo CLI:** `02_Geometria_Vectorial_R2_R3/07_planos_en_r3_e_intersecciones.py`
* **Cuaderno:** `02_Geometria_Vectorial_R2_R3/07_planos_en_r3_e_intersecciones.ipynb`
* **Fundamento Matemático:**
  Planos $\Pi_1: A_1 x + B_1 y + C_1 z + D_1 = 0$ y $\Pi_2: A_2 x + B_2 y + C_2 z + D_2 = 0$.
  Vector director de la recta intersección $L = \Pi_1 \cap \Pi_2$:
  $$ \mathbf{d} = \mathbf{n}_1 \times \mathbf{n}_2 = \begin{vmatrix} \hat{\mathbf{i}} & \hat{\mathbf{j}} & \hat{\mathbf{k}} \\ A_1 & B_1 & C_1 \\ A_2 & B_2 & C_2 \end{vmatrix} $$
  Ángulo diedro: $\cos\theta = \frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{\|\mathbf{n}_1\| \|\mathbf{n}_2\|}$.
* **Interactividad en Jupyter:** Manipulación de normales y términos independientes, cálculo analítico de la recta de corte y visualización tridimensional de las superficies con normales unitarias.

---

### Módulo 08: Torque Vectorial 3D y Equilibrio Estático de Cuerpo Rígido
* **Archivo CLI:** `03_Aplicaciones_Fisicas_y_Simulaciones/08_simulacion_torque_y_equilibrio_3d.py`
* **Cuaderno:** `03_Aplicaciones_Fisicas_y_Simulaciones/08_simulacion_torque_y_equilibrio_3d.ipynb`
* **Fundamento Matemático y Mecánico:**
  Brazo estructural / pluma de grúa en $\mathbb{R}^3$ sometida a cargas externas y sostenida por un pivote esférico tridimensional en el origen y cables tensores anclados en puntos espaciales.
  Leyes de Newton-Euler para cuerpo rígido:
  $$ \sum \mathbf{F}_i = \mathbf{R}_O + \mathbf{T}_1 + \mathbf{T}_2 + \mathbf{W}_{\text{beam}} + \mathbf{W}_{\text{load}} = \mathbf{0} \quad (3 \text{ ecuaciones escalares}) $$
  $$ \sum \boldsymbol{\tau}_{O, i} = \mathbf{r}_{T_1} \times \mathbf{T}_1 + \mathbf{r}_{T_2} \times \mathbf{T}_2 + \mathbf{r}_{G} \times \mathbf{W}_{\text{beam}} + \mathbf{r}_{\text{tip}} \times \mathbf{W}_{\text{load}} = \mathbf{0} \quad (3 \text{ ecuaciones escalares}) $$
  Formulación en sistema matricial $6 \times 6$:
  $$ \begin{pmatrix} I_3 & \hat{\mathbf{u}}_{T_1} & \hat{\mathbf{u}}_{T_2} \\ 0_{3 \times 3} & [\mathbf{r}_{T_1}]_\times \hat{\mathbf{u}}_{T_1} & [\mathbf{r}_{T_2}]_\times \hat{\mathbf{u}}_{T_2} \end{pmatrix} \begin{pmatrix} \mathbf{R}_O \\ T_1 \\ T_2 \end{pmatrix} = \begin{pmatrix} -\mathbf{W}_{\text{total}} \\ -\boldsymbol{\tau}_{O, \text{cargas}} \end{pmatrix} $$
* **Interactividad en Jupyter:** Control de masa de carga, inclinación del brazo, posición de anclaje de cables y evaluación inmediata de tensiones, reacciones y factor de seguridad estructural.

---

## 💻 Instalación y Requisitos

### Requisitos del Sistema
* Python 3.10 o superior.
* Gestor de paquetes `pip`.

### Instalación Rápida
```bash
# 1. Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate  # En Linux/macOS
# .venv\Scripts\activate   # En Windows

# 2. Instalar dependencias exactas
pip install -r requirements.txt
```

### Contenido de `requirements.txt`
```text
numpy>=1.24.0
sympy>=1.12
matplotlib>=3.7.0
ipywidgets>=8.0.0
nbformat>=5.9.0
scipy>=1.10.0
```

---

## ⚡ Guía de Ejecución

### 1. Ejecución de Scripts CLI (.py)
Los scripts están diseñados para ejecutarse tanto en entornos con servidor gráfico como en servidores headless (detectan automáticamente si hay display o usan el backend `Agg` guardando los renders PNG):

```bash
# Módulo 01: Gauss-Jordan y Rouché-Frobenius
python3 01_Sistemas_Lineales_y_Matrices/01_gauss_jordan_y_rouche_frobenius_3d.py

# Módulo 02: Discusión con parámetro k
python3 01_Sistemas_Lineales_y_Matrices/02_sistemas_parametrizados_k.py

# Módulo 03: Menores, cofactores e inversa
python3 01_Sistemas_Lineales_y_Matrices/03_matrices_cofactores_e_inversa.py

# Módulo 04: Vectores y proyecciones
python3 02_Geometria_Vectorial_R2_R3/04_vectores_fundamentos_y_proyecciones.py

# Módulo 05: Producto cruz y paralelepípedos
python3 02_Geometria_Vectorial_R2_R3/05_producto_cruz_y_paralelepipedos_3d.py

# Módulo 06: Rectas en R3 y alabeadas
python3 02_Geometria_Vectorial_R2_R3/06_rectas_en_r3_y_rectas_alabeadas.py

# Módulo 07: Planos en R3 e intersección
python3 02_Geometria_Vectorial_R2_R3/07_planos_en_r3_e_intersecciones.py

# Módulo 08: Simulación de torque 3D y equilibrio estático
python3 03_Aplicaciones_Fisicas_y_Simulaciones/08_simulacion_torque_y_equilibrio_3d.py
```

### 2. Ejecución de Cuadernos Interactivos (.ipynb)
Para aprovechar toda la interactividad de los sliders y controles con `ipywidgets`:

```bash
# Iniciar JupyterLab o Jupyter Notebook
jupyter lab
# o
jupyter notebook
```
Abre cualquiera de los cuadernos en el navegador, o ejecútalos directamente desde **VS Code** o **Cursor** con la extensión de Jupyter instalada.

---

## 🔒 Estándar de Privacidad y Seguridad

> [!IMPORTANT]
> **Políticas de Cero Fugas y Código Limpio:**
> 1. Ningún script ni cuaderno contiene rutas locales privadas del sistema operativo.
> 2. No se incluyen prompts de agentes, instrucciones internas de IA ni documentos privados de evaluación docente.
> 3. Todo el código es 100% de autoría propia de Moisés Amundarain Romero, destinado a fines pedagógicos, de investigación y computación científica.

---

---

<div align="center">
Desarrollado con rigor matemático y pasión por la ingeniería por<br/>
<b>Moisés Amundarain Romero</b><br/>
Universidad San Sebastián — Sede Patagonia
</div>

---

🔗 [Volver al repositorio principal](../README.md)

