---
title: "Suite de Simuladores 3D y Cuadernos Interactivos de Álgebra Lineal"
proyecto: "Álgebra Lineal (DCEX0007)"
carrera: "Ingeniería Civil Informática"
institución: "Universidad San Sebastián — Sede De la Patagonia"
autor: "Moisés Amundarain Romero"
docente: "Carol Asencio González"
status: "activo"
---

<div align="center">

# Suite de Simuladores 3D, Álgebra Simbólica y Cuadernos Interactivos
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

## Trazabilidad y Demarcación de Fuentes (Source Provenance Standard)

En cumplimiento de los estándares de rigurosidad académica y delimitación de fuentes, cada módulo, demostración y algoritmo implementado cuenta con la siguiente demarcación explícita:

* **[Cátedra USS / Diapositivas Docente]**: Operaciones Elementales por Fila (OEF), Forma Escalonada Reducida por Filas (RREF), Teorema de Rouché-Frobenius, discusión analítica de sistemas con parámetros, matriz de cofactores y adjunta, álgebra vectorial en $\mathbb{R}^2/\mathbb{R}^3$, producto cruz, ecuaciones vectoriales, paramétricas y simétricas de la recta y el plano en el espacio euclidiano.
* **[Texto Guía — Grossman / Poole / Axler]**: Interpretación geométrica tridimensional de sistemas $3 \times 3$, geometría de prismas triangulares y planos paralelos disjuntos (casos de inconsistencia), identidades vectoriales formales (Lagrange, Cauchy-Schwarz, Jacobi), distancias ortogonales entre rectas alabeadas y volúmenes de paralelepípedos mediante el producto mixto.
* **[Computación Científica y Simulación Física]**: Aritmética simbólica racional exacta con SymPy, modelado numérico con NumPy/SciPy, renderizado volumétrico y poligonal 3D con Matplotlib (`Poly3DCollection`, superficies paramétricas con transparencia controlada), simulación cinemática y estática de equilibrio de cuerpo rígido $6 \times 6$, y controles interactivos en tiempo real mediante `ipywidgets`.

---

## Paleta Institucional USS y Estándar de Visibilidad Tridimensional

Todos los gráficos generados por los scripts `.py` y cuadernos `.ipynb` implementan estrictamente la identidad cromática institucional de la Universidad San Sebastián y un estándar visual de ingeniería diseñado para máxima claridad perceptiva:

### Tabla de Colores Institucionales USS

| Color | Código HEX | Rol Gráfico / Significado Matemático |
| :--- | :---: | :--- |
| **USS Blue Principal** | `#00205B` | Ejes coordenados principales, vectores base $\mathbf{u}$, títulos, matrices canónicas, estructuras portantes. |
| **USS Gold** | `#D4AF37` | Soluciones únicas, rectas de intersección $\Pi_1 \cap \Pi_2$, vectores resultantes $\mathbf{u} \times \mathbf{v}$, torques $\boldsymbol{\tau}$, resaltes analíticos. |
| **Deep Blue / Secondary** | `#1B365D` | Planos primarios $\Pi_1$, vectores secundarios $\mathbf{v}$, contornos estructurales. |
| **Light Blue Accent** | `#4A90E2` | Planos secundarios $\Pi_2$, proyecciones ortogonales $\mathrm{proy}_{\mathbf{v}}(\mathbf{u})$, componentes vectoriales. |
| **Alert / Inconsistencia** | `#C0392B` | Planos de inconsistencia (SI), puntos singulares críticos $k_{\text{crítico}}$, componentes ortogonales $\mathbf{u}_\perp$. |
| **Teal / Subespacios** | `#16A085` | Planos terciarios $\Pi_3$, cables tensores, áreas de sustentación. |
| **Dark Slate** | `#2C3E50` | Mallas espaciales de fondo, textos analíticos y marcos matriciales. |

### Criterios de Optimización Visual 3D
1. **Transparencia Controlada ($\alpha \in [0.20, 0.25]$):** Las superficies de los planos en $\mathbb{R}^3$ y las facetas de los paralelepípedos implementan un factor de opacidad calibrado entre $0.20$ y $0.25$. Esto erradica el problema de planos opacos que ocultan las trazas, ejes coordenados, rectas de intersección o vectores interiores.
2. **Orientación de Cámara Canónica ($\text{elev} = 25^\circ, \text{azim} = -50^\circ$):** La perspectiva tridimensional se encuentra calibrada para evitar ángulos degenerados donde los planos colapsen visualmente en líneas simples o los ejes se superpongan, proporcionando una percepción espacial inequívoca de la profundidad euclidiana.
3. **Arquitectura de Figuras Atómicas Individuales:** Se eliminaron las composiciones comprimidas en subplots múltiples abarrotados. Cada simulación exporta figuras independientes de alta resolución a $300\text{ DPI}$ (`bbox_inches='tight'`) con fondo blanco puro (`facecolor='white'`), garantizando nitidez tanto en pantalla como en reportes técnicos impresos.

---

## Arquitectura Modular del Directorio Códigos/

La suite se compone de 8 módulos computacionales divididos en 3 áreas temáticas, totalizando 19 figuras individuales de alta resolución:

```text
Códigos/
├── README.md                                               # Presentación técnica del directorio
│
├── 01_Sistemas_Lineales_y_Matrices/                         # Unidad 1: Sistemas Lineales, Rouché-Frobenius e Inversas
│   ├── 01_gauss_jordan_y_rouche_frobenius_3d.py            # CLI: Reducción Gauss-Jordan y clasificación Rouché-Frobenius
│   ├── 01_gauss_jordan_y_rouche_frobenius_3d.ipynb         # Cuaderno interactivo con sliders y perspectiva 3D dinámica
│   ├── 01_gauss_rouche_scd.png                             # Render 3D: Sistema Compatible Determinado (Solución única puntual)
│   ├── 01_gauss_rouche_sci.png                             # Render 3D: Sistema Compatible Indeterminado (Recta de infinitas soluciones)
│   ├── 01_gauss_rouche_si.png                              # Render 3D: Sistema Incompatible (Prisma triangular / planos paralelos)
│   ├── 02_sistemas_parametrizados_k.py                     # CLI: Discusión analítica con parámetro real k y determinantes
│   ├── 02_sistemas_parametrizados_k.ipynb                  # Cuaderno interactivo con slider continuo de k y cálculo de rango
│   ├── 02_det_k_curva_analisis.png                         # Gráfico 2D: det(A(k)) vs k con singularidades críticas resaltadas
│   ├── 02_sistema_k_scd.png                                # Render 3D: Configuración espacial para k = 2 (Caso SCD)
│   ├── 02_sistema_k_sci.png                                # Render 3D: Configuración espacial para k = 1 (Caso SCI)
│   ├── 02_sistema_k_si.png                                 # Render 3D: Configuración espacial para k = -2 (Caso SI)
│   ├── 03_matrices_cofactores_e_inversa.py                 # CLI: Menores, cofactores, matriz adjunta e inversa formal
│   ├── 03_matrices_cofactores_e_inversa.ipynb              # Cuaderno interactivo con mapas de calor matriciales
│   └── 03_matrices_cofactores_inversa_diagrama.png         # Diagrama 2D: Mapas de calor analíticos de A, Cof(A), Adj(A) y A^(-1)
│
├── 02_Geometria_Vectorial_R2_R3/                           # Unidad 2: Geometría del Espacio Euclidiano
│   ├── 04_vectores_fundamentos_y_proyecciones.py           # CLI: Producto punto, cosenos directores y proyecciones
│   ├── 04_vectores_fundamentos_y_proyecciones.ipynb        # Cuaderno interactivo con descomposición ortogonal en R2 y R3
│   ├── 04_vectores_operaciones_2d.png                      # Gráfico 2D: Suma, resta, combinación lineal y triángulo vectorial
│   ├── 04_vectores_proyeccion_ortogonal_3d.png             # Render 3D: Proyección ortogonal proy_v(u) y componente normal u_perp
│   ├── 05_producto_cruz_y_paralelepipedos_3d.py            # CLI: Producto vectorial, áreas y producto mixto volumétrico
│   ├── 05_producto_cruz_y_paralelepipedos_3d.ipynb         # Cuaderno interactivo con sólido paralelepípedo 3D
│   ├── 05_paralelepipedo_y_volumen_3d.png                  # Render 3D: Paralelepípedo volumétrico (Poly3DCollection)
│   ├── 05_producto_cruz_y_ortogonalidad_3d.png             # Render 3D: Producto cruz u x v, ortogonalidad y área paralelogramo
│   ├── 06_rectas_en_r3_y_rectas_alabeadas.py               # CLI: Clasificación de rectas en el espacio y distancia mínima
│   ├── 06_rectas_en_r3_y_rectas_alabeadas.ipynb            # Cuaderno interactivo de rectas alabeadas y segmento perpendicular
│   ├── 06_rectas_en_r3_y_rectas_alabeadas.png              # Render 3D: Rectas alabeadas en R3 y vector de mínima separación
│   ├── 07_planos_en_r3_e_intersecciones.py                 # CLI: Ecuaciones del plano, ángulo diedro y recta intersección
│   ├── 07_planos_en_r3_e_intersecciones.ipynb              # Cuaderno interactivo con planos secantes y distancia punto-plano
│   ├── 07_distancia_punto_plano_3d.png                     # Render 3D: Distancia perpendicular de punto P0 a plano Pi y normal n
│   └── 07_planos_secantes_e_interseccion_3d.png            # Render 3D: Planos secantes Pi1, Pi2 y recta de corte dorada
│
└── 03_Aplicaciones_Fisicas_y_Simulaciones/                  # Modelado Físico y Sistemas Estáticos
    ├── 08_simulacion_torque_y_equilibrio_3d.py             # CLI: Simulación de torque y equilibrio de cuerpo rígido 6x6
    ├── 08_simulacion_torque_y_equilibrio_3d.ipynb          # Cuaderno interactivo con control de cargas, ángulos y tensores
    ├── 08_estructura_grua_3d.png                           # Render 3D: Geometría estructural de pluma mecánica y cables
    ├── 08_diagrama_cuerpo_libre_3d.png                     # DCL 3D: Vectores de fuerza concurrentes, reacciones y cargas
    ├── 08_espacio_torques_equilibrio_3d.png                # Render 3D: Espacio vectorial de momentos y verificación sum tau = 0
    └── 08_analisis_sensibilidad_tensiones_2d.png           # Gráfico 2D: Curvas de tensión de cables y compresión axial vs ángulo
```

---

## Matriz Comparativa de los 8 Simuladores

| # | Módulo | Concepto Central | Script CLI (`.py`) | Cuaderno Interactivo (`.ipynb`) | Modelado Matemático Clave | Salida Visual |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | **Gauss-Jordan & Rouché-Frobenius** | Rango matricial, OEF y consistencia 3D | `01_gauss_jordan_y_rouche_frobenius_3d.py` | `01_gauss_jordan_y_rouche_frobenius_3d.ipynb` | $\mathrm{rg}(A)$ vs $\mathrm{rg}(A\|B)$<br/>SCD, SCI, SI | 3 planos en $\mathbb{R}^3$, punto de corte, haz de planos o prisma triangular. |
| **02** | **Sistemas Parametrizados $k$** | Determinantes y bifurcaciones espaciales | `02_sistemas_parametrizados_k.py` | `02_sistemas_parametrizados_k.ipynb` | $\det(A(k)) = 0$<br/>Raíces críticas $k_i$ | Gráfico $\det(A(k))$ vs $k$ y configuración 3D instantánea por caso. |
| **03** | **Cofactores e Inversa Matricial** | Expansión de Laplace e inversión formal | `03_matrices_cofactores_e_inversa.py` | `03_matrices_cofactores_e_inversa.ipynb` | $A^{-1} = \frac{1}{\det(A)} \mathrm{Adj}(A)$<br/>$A \cdot A^{-1} = I_n$ | Mapas de calor matriciales con anotaciones numéricas y colores USS. |
| **04** | **Vectores & Proyecciones $\mathbb{R}^2/\mathbb{R}^3$** | Cosenos directores y descomposición ortogonal | `04_vectores_fundamentos_y_proyecciones.py` | `04_vectores_fundamentos_y_proyecciones.ipynb` | $\mathbf{u} = \mathrm{proy}_{\mathbf{v}}(\mathbf{u}) + \mathbf{u}_\perp$<br/>Cauchy-Schwarz | Triángulo vectorial 2D y descomposición ortogonal tridimensional en $\mathbb{R}^3$. |
| **05** | **Producto Cruz & Paralelepípedos** | Ortogonalidad vectorial y volúmenes 3D | `05_producto_cruz_y_paralelepipedos_3d.py` | `05_producto_cruz_y_paralelepipedos_3d.ipynb` | $V = \|\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})\|$<br/>Identidad de Lagrange | Paralelepípedo sólido 3D con caras semitransparentes y producto cruz normal. |
| **06** | **Rectas en $\mathbb{R}^3$ & Alabeadas** | Posiciones relativas y mínima separación | `06_rectas_en_r3_y_rectas_alabeadas.py` | `06_rectas_en_r3_y_rectas_alabeadas.ipynb` | $d = \frac{\|(\mathbf{P}_2 - \mathbf{P}_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2)\|}{\|\mathbf{d}_1 \times \mathbf{d}_2\|}$ | Trayectorias de rectas en el espacio y segmento perpendicular de mínima separación. |
| **07** | **Planos en $\mathbb{R}^3$ & Ángulo Diedro** | Ecuación general, distancia e intersección | `07_planos_en_r3_e_intersecciones.py` | `07_planos_en_r3_e_intersecciones.ipynb` | $\mathbf{d} = \mathbf{n}_1 \times \mathbf{n}_2$<br/>$d(P_0, \Pi) = \frac{\|A x_0 + B y_0 + C z_0 + D\|}{\sqrt{A^2 + B^2 + C^2}}$ | Planos secantes con recta de intersección y distancia ortogonal punto-plano. |
| **08** | **Torque 3D & Equilibrio Estático** | Estática de cuerpo rígido y tensores espaciales | `08_simulacion_torque_y_equilibrio_3d.py` | `08_simulacion_torque_y_equilibrio_3d.ipynb` | Sistema matricial $6 \times 6$:<br/>$\sum \mathbf{F} = \mathbf{0}$, $\sum \boldsymbol{\tau}_O = \mathbf{0}$ | Modelo estructural de grúa 3D, DCL espacial, espacio de momentos y curvas 2D. |

---

## Galería Integral de Figuras y Visualizaciones 3D (19 Renders)

### Módulos 01 y 02: Álgebra Matricial y Sistemas Lineales

<div align="center">

| Rouché-Frobenius: SCD (Solución Única) | Rouché-Frobenius: SCI (Recta Común) | Rouché-Frobenius: SI (Incompatible) |
| :---: | :---: | :---: |
| <img src="01_Sistemas_Lineales_y_Matrices/01_gauss_rouche_scd.png" width="300"/> | <img src="01_Sistemas_Lineales_y_Matrices/01_gauss_rouche_sci.png" width="300"/> | <img src="01_Sistemas_Lineales_y_Matrices/01_gauss_rouche_si.png" width="300"/> |

| Parámetro $k$: Curva de Singularidad | Parámetro $k$: SCD ($k = 2$) | Parámetro $k$: SCI ($k = 1$) |
| :---: | :---: | :---: |
| <img src="01_Sistemas_Lineales_y_Matrices/02_det_k_curva_analisis.png" width="300"/> | <img src="01_Sistemas_Lineales_y_Matrices/02_sistema_k_scd.png" width="300"/> | <img src="01_Sistemas_Lineales_y_Matrices/02_sistema_k_sci.png" width="300"/> |

| Parámetro $k$: SI ($k = -2$) | Módulo 03: Diagrama de Mapas de Calor Matriciales |
| :---: | :---: |
| <img src="01_Sistemas_Lineales_y_Matrices/02_sistema_k_si.png" width="300"/> | <img src="01_Sistemas_Lineales_y_Matrices/03_matrices_cofactores_inversa_diagrama.png" width="460"/> |

</div>

### Módulos 04, 05, 06 y 07: Geometría Vectorial en $\mathbb{R}^2$ y $\mathbb{R}^3$

<div align="center">

| Operaciones Vectoriales 2D | Proyección Ortogonal 3D ($\mathbf{u}_\parallel, \mathbf{u}_\perp$) | Producto Cruz y Ortogonalidad 3D |
| :---: | :---: | :---: |
| <img src="02_Geometria_Vectorial_R2_R3/04_vectores_operaciones_2d.png" width="300"/> | <img src="02_Geometria_Vectorial_R2_R3/04_vectores_proyeccion_ortogonal_3d.png" width="300"/> | <img src="02_Geometria_Vectorial_R2_R3/05_producto_cruz_y_ortogonalidad_3d.png" width="300"/> |

| Paralelepípedo Volumétrico 3D | Rectas Alabeadas y Distancia Mínima | Distancia Punto-Plano 3D |
| :---: | :---: | :---: |
| <img src="02_Geometria_Vectorial_R2_R3/05_paralelepipedo_y_volumen_3d.png" width="300"/> | <img src="02_Geometria_Vectorial_R2_R3/06_rectas_en_r3_y_rectas_alabeadas.png" width="300"/> | <img src="02_Geometria_Vectorial_R2_R3/07_distancia_punto_plano_3d.png" width="300"/> |

| Planos Secantes y Recta de Intersección |
| :---: |
| <img src="02_Geometria_Vectorial_R2_R3/07_planos_secantes_e_interseccion_3d.png" width="460"/> |

</div>

### Módulo 08: Aplicaciones Físicas y Equilibrio Estático de Cuerpo Rígido

<div align="center">

| Estructura Mecánica 3D | Diagrama de Cuerpo Libre (DCL 3D) |
| :---: | :---: |
| <img src="03_Aplicaciones_Fisicas_y_Simulaciones/08_estructura_grua_3d.png" width="420"/> | <img src="03_Aplicaciones_Fisicas_y_Simulaciones/08_diagrama_cuerpo_libre_3d.png" width="420"/> |

| Espacio de Momentos y Torques 3D | Análisis de Sensibilidad y Tensiones 2D |
| :---: | :---: |
| <img src="03_Aplicaciones_Fisicas_y_Simulaciones/08_espacio_torques_equilibrio_3d.png" width="420"/> | <img src="03_Aplicaciones_Fisicas_y_Simulaciones/08_analisis_sensibilidad_tensiones_2d.png" width="420"/> |

</div>

---

## Descripción Técnica Detallada por Módulo

### Módulo 01: Sistemas de Ecuaciones Lineales y Rouché-Frobenius 3D
* **Archivo CLI:** `01_Sistemas_Lineales_y_Matrices/01_gauss_jordan_y_rouche_frobenius_3d.py`
* **Cuaderno:** `01_Sistemas_Lineales_y_Matrices/01_gauss_jordan_y_rouche_frobenius_3d.ipynb`
* **Fundamento Matemático:**
  Dado el sistema lineal $A\mathbf{x} = \mathbf{b}$ con $A \in \mathcal{M}_{m \times n}(\mathbb{R})$ y matriz aumentada $(A|\mathbf{b})$:
  $$ \mathrm{RREF}(A|\mathbf{b}) \implies \begin{cases}
  \mathrm{rg}(A) < \mathrm{rg}(A|\mathbf{b}) & \implies \text{Sistema Incompatible (SI, } \emptyset\text{)} \\
  \mathrm{rg}(A) = \mathrm{rg}(A|\mathbf{b}) = n & \implies \text{Sistema Compatible Determinado (SCD, solución única)} \\
  \mathrm{rg}(A) = \mathrm{rg}(A|\mathbf{b}) < n & \implies \text{Sistema Compatible Indeterminado (SCI, } \infty\text{ soluciones)}
  \end{cases} $$
* **Interactividad en Jupyter:** Deslizadores de coeficientes independientes, selector desplegable de casos canónicos (SCD, SCI, SI) y rotación dinámica de perspectiva 3D.

---

### Módulo 02: Discusión de Sistemas Parametrizados con Parámetro $k$
* **Archivo CLI:** `01_Sistemas_Lineales_y_Matrices/02_sistemas_parametrizados_k.py`
* **Cuaderno:** `01_Sistemas_Lineales_y_Matrices/02_sistemas_parametrizados_k.ipynb`
* **Fundamento Matemático:**
  Sea $A(k)$ una matriz cuadrada dependiente de $k \in \mathbb{R}$. La invertibilidad depende de las raíces del polinomio característico del determinante:
  $$ \det(A(k)) = 0 \implies k \in \{k_1, k_2, \dots, k_p\} $$
  Para todo $k \notin \{k_1, \dots, k_p\}$, $\mathrm{rg}(A(k)) = n \implies \text{SCD}$. Para cada valor crítico $k_i$, se sustituye formalmente en $(A(k_i)|\mathbf{b}(k_i))$ y se computa la forma escalonada reducida por filas para discernir entre SCI y SI.
* **Interactividad en Jupyter:** Slider continuo `FloatSlider` para $k \in [-5, 5]$ que calcula en tiempo real $\det(A(k))$, evalúa rangos simbólicos en SymPy y actualiza instantáneamente los tres planos tridimensionales.

---

### Módulo 03: Menores, Cofactores, Matriz Adjunta e Inversa
* **Archivo CLI:** `01_Sistemas_Lineales_y_Matrices/03_matrices_cofactores_e_inversa.py`
* **Cuaderno:** `01_Sistemas_Lineales_y_Matrices/03_matrices_cofactores_e_inversa.ipynb`
* **Fundamento Matemático:**
  Dada $A \in \mathcal{M}_{n \times n}(\mathbb{R})$:
  $$ C_{ij} = (-1)^{i+j} M_{ij}, \quad \mathrm{Cof}(A) = [C_{ij}], \quad \mathrm{Adj}(A) = [\mathrm{Cof}(A)]^T $$
  $$ A \cdot \mathrm{Adj}(A) = \det(A) I_n \implies A^{-1} = \frac{1}{\det(A)} \mathrm{Adj}(A) \quad (\text{si } \det(A) \neq 0) $$
* **Interactividad en Jupyter:** Entradas interactivas para modificar matrices, cálculo instantáneo de determinantes por expansión de Laplace y visualización de mapas de calor anotados.

---

### Módulo 04: Vectores en $\mathbb{R}^2/\mathbb{R}^3$, Cosenos Directores y Proyecciones
* **Archivo CLI:** `02_Geometria_Vectorial_R2_R3/04_vectores_fundamentos_y_proyecciones.py`
* **Cuaderno:** `02_Geometria_Vectorial_R2_R3/04_vectores_fundamentos_y_proyecciones.ipynb`
* **Fundamento Matemático:**
  Para $\mathbf{u}, \mathbf{v} \in \mathbb{R}^3$:
  $$ \mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta, \quad \cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|} $$
  $$ \mathrm{proy}_{\mathbf{v}}(\mathbf{u}) = \left(\frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{v}\|^2}\right)\mathbf{v}, \quad \mathbf{u}_\perp = \mathbf{u} - \mathrm{proy}_{\mathbf{v}}(\mathbf{u}) $$
  Verificación de ortogonalidad formal: $\mathbf{u}_\perp \cdot \mathbf{v} = 0$, e identidad de Pitágoras vectorial: $\|\mathbf{u}\|^2 = \|\mathrm{proy}_{\mathbf{v}}(\mathbf{u})\|^2 + \|\mathbf{u}_\perp\|^2$.
* **Interactividad en Jupyter:** Deslizadores de componentes vectoriales, visualización dual 2D/3D y cálculo de cosenos directores $\cos\alpha, \cos\beta, \cos\gamma$.

---

### Módulo 05: Producto Cruz, Identidad de Lagrange y Paralelepípedos 3D
* **Archivo CLI:** `02_Geometria_Vectorial_R2_R3/05_producto_cruz_y_paralelepipedos_3d.py`
* **Cuaderno:** `02_Geometria_Vectorial_R2_R3/05_producto_cruz_y_paralelepipedos_3d.ipynb`
* **Fundamento Matemático:**
  $$ \mathbf{u} \times \mathbf{v} = \begin{vmatrix} \hat{\mathbf{i}} & \hat{\mathbf{j}} & \hat{\mathbf{k}} \\ u_x & u_y & u_z \\ v_x & v_y & v_z \end{vmatrix}, \quad \|\mathbf{u} \times \mathbf{v}\|^2 = \|\mathbf{u}\|^2\|\mathbf{v}\|^2 - (\mathbf{u}\cdot\mathbf{v})^2 \quad (\text{Lagrange}) $$
  $$ V_{\text{paralelepípedo}} = |[\mathbf{u}, \mathbf{v}, \mathbf{w}]| = |\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})| = |\det([\mathbf{u}, \mathbf{v}, \mathbf{w}])| $$
* **Interactividad en Jupyter:** Creación de sólidos 3D con `Poly3DCollection`, control de factor de transparencia $\alpha$, cálculo de áreas y volúmenes, y demostración de anticonmutatividad.

---

### Módulo 06: Rectas en $\mathbb{R}^3$, Posiciones Relativas y Distancia entre Rectas Alabeadas
* **Archivo CLI:** `02_Geometria_Vectorial_R2_R3/06_rectas_en_r3_y_rectas_alabeadas.py`
* **Cuaderno:** `02_Geometria_Vectorial_R2_R3/06_rectas_en_r3_y_rectas_alabeadas.ipynb`
* **Fundamento Matemático:**
  Dadas las rectas $L_1: \mathbf{r}_1(t) = \mathbf{P}_1 + t\mathbf{d}_1$ y $L_2: \mathbf{r}_2(s) = \mathbf{P}_2 + s\mathbf{d}_2$:
  $$ d(L_1, L_2) = \frac{|(\mathbf{P}_2 - \mathbf{P}_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2)|}{\|\mathbf{d}_1 \times \mathbf{d}_2\|} $$
  Los puntos de máxima proximidad $Q_1 \in L_1$ y $Q_2 \in L_2$ se determinan resolviendo el sistema lineal inducido por la condición de ortogonalidad simultánea:
  $$ \begin{cases} (Q_2 - Q_1) \cdot \mathbf{d}_1 = 0 \\ (Q_2 - Q_1) \cdot \mathbf{d}_2 = 0 \end{cases} $$
* **Interactividad en Jupyter:** Configuración de puntos de paso y vectores directores, clasificación topológica y trazado del segmento ortogonal de mínima separación.

---

### Módulo 07: Planos en $\mathbb{R}^3$, Ángulo Diedro e Intersección
* **Archivo CLI:** `02_Geometria_Vectorial_R2_R3/07_planos_en_r3_e_intersecciones.py`
* **Cuaderno:** `02_Geometria_Vectorial_R2_R3/07_planos_en_r3_e_intersecciones.ipynb`
* **Fundamento Matemático:**
  Para los planos $\Pi_1: A_1 x + B_1 y + C_1 z + D_1 = 0$ y $\Pi_2: A_2 x + B_2 y + C_2 z + D_2 = 0$:
  $$ \mathbf{d} = \mathbf{n}_1 \times \mathbf{n}_2, \quad \cos\theta = \frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{\|\mathbf{n}_1\| \|\mathbf{n}_2\|} $$
  Distancia ortogonal de un punto $P_0(x_0, y_0, z_0)$ a un plano $\Pi$:
  $$ d(P_0, \Pi) = \frac{|A x_0 + B y_0 + C z_0 + D|}{\sqrt{A^2 + B^2 + C^2}} $$
* **Interactividad en Jupyter:** Ajuste de coeficientes de planos, determinación analítica de la recta de intersección y renderizado con vectores normales unitarios.

---

### Módulo 08: Torque Vectorial 3D y Equilibrio Estático de Cuerpo Rígido
* **Archivo CLI:** `03_Aplicaciones_Fisicas_y_Simulaciones/08_simulacion_torque_y_equilibrio_3d.py`
* **Cuaderno:** `03_Aplicaciones_Fisicas_y_Simulaciones/08_simulacion_torque_y_equilibrio_3d.ipynb`
* **Fundamento Matemático y Mecánico:**
  Pluma mecánica articulada en el origen $O$ con rótula esférica y sustentada por cables tensores anclados en el espacio:
  $$ \sum \mathbf{F}_i = \mathbf{R}_O + \mathbf{T}_1 + \mathbf{T}_2 + \mathbf{W}_{\text{pluma}} + \mathbf{W}_{\text{carga}} = \mathbf{0} $$
  $$ \sum \boldsymbol{\tau}_{O, i} = \mathbf{r}_{T_1} \times \mathbf{T}_1 + \mathbf{r}_{T_2} \times \mathbf{T}_2 + \mathbf{r}_{G} \times \mathbf{W}_{\text{pluma}} + \mathbf{r}_{\text{extremo}} \times \mathbf{W}_{\text{carga}} = \mathbf{0} $$
  Formulación en sistema matricial $6 \times 6$:
  $$ \begin{pmatrix} I_3 & \hat{\mathbf{u}}_{T_1} & \hat{\mathbf{u}}_{T_2} \\ 0_{3 \times 3} & [\mathbf{r}_{T_1}]_\times \hat{\mathbf{u}}_{T_1} & [\mathbf{r}_{T_2}]_\times \hat{\mathbf{u}}_{T_2} \end{pmatrix} \begin{pmatrix} \mathbf{R}_O \\ T_1 \\ T_2 \end{pmatrix} = \begin{pmatrix} -\mathbf{W}_{\text{total}} \\ -\boldsymbol{\tau}_{O, \text{cargas}} \end{pmatrix} $$
* **Interactividad en Jupyter:** Modificación en tiempo real de masas de carga, ángulo de inclinación de la pluma y posiciones de anclaje, con cálculo dinámico de tensiones y reacciones.

---

## Instalación y Requisitos

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

## Guía de Ejecución

### 1. Ejecución de Scripts CLI (.py)
Los scripts detectan automáticamente la disponibilidad de display gráfico; en servidores sin interfaz visual (headless) utilizan de forma transparente el backend `Agg` de Matplotlib y exportan las figuras PNG a disco:

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
```bash
jupyter lab
# o
jupyter notebook
```
También pueden ejecutarse directamente en Visual Studio Code o Cursor con el kernel de `.venv` seleccionado.

---

## Estándar de Privacidad y Seguridad

> [!IMPORTANT]
> **Políticas de Cero Fugas y Código Limpio:**
> 1. Ningún script ni cuaderno contiene rutas locales privadas del sistema operativo host.
> 2. No se incluyen prompts de agentes, instrucciones internas de IA ni documentos privados de evaluación docente.
> 3. Todo el código es 100% de autoría propia de Moisés Amundarain Romero, destinado a fines pedagógicos, de investigación y computación científica.

---

<div align="center">
Desarrollado con rigor matemático y computacional por<br/>
<b>Moisés Amundarain Romero</b><br/>
Universidad San Sebastián — Sede De la Patagonia
</div>

---
## Conexiones
- [README Principal](../README.md)
- [Teoría y Notas de Álgebra Lineal](../Teoria/README.md)
- [Solucionarios de Talleres](../Listados_y_Solucionarios_Propios/2026-2_USS/Resolucion_TALLER_1_ALGEBRA_LINEAL.md)
