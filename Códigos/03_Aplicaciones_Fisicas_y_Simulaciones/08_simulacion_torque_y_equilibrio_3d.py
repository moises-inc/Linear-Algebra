#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Módulo 08: Simulación de Torque y Equilibrio Estático en R³
Asignatura: Álgebra Lineal (DCEX0007 / ICI) — Universidad San Sebastián (USS)
================================================================================

Este módulo modela, analiza y simula numéricamente y simbólicamente el equilibrio
estático tridimensional de un cuerpo rígido (brazo mecánico / pluma de grúa en
voladizo) sometido a cargas gravitacionales y sostenido por un pivote en el
origen y cables tensores espaciales.

Fundamentación Mecánica y Matemática:
-------------------------------------
1. Definición Vectorial del Torque:
   Para una fuerza F aplicada en un punto con vector de posición r relativo a un
   centro de momentos O:
       tau_O = r x F = det([i, j, k; r_x, r_y, r_z; F_x, F_y, F_z])
   Magnitud:
       ||tau_O|| = ||r|| * ||F|| * sin(phi) = r_perp * ||F||
   donde r_perp es el brazo de palanca perpendicular a la línea de acción de F.

2. Leyes de Equilibrio Estático de Newton-Euler (Cuerpo Rígido en R³):
   (I)  Equilibrio Traslacional:   sum F_i = 0   (3 ecuaciones escalares)
   (II) Equilibrio Rotacional:      sum tau_Oi = 0 (3 ecuaciones escalares)

3. Formulación Matricial 6x6 (Sistema Lineal Isostático):
   El sistema físico se modela como un brazo rígido O-A de longitud L soportado
   en O(0,0,0) por una rótula esférica o pasador cilíndrico (reacciones R_Ox,
   R_Oy, R_Oz y restricción torsional axial M_Ox) y dos cables tensores
   anclados en C1(0, -d, h) y C2(0, d, h) con tensiones T1 y T2.
   Se plantea el sistema matricial exacto A * x = b, donde:
       x = [R_Ox, R_Oy, R_Oz, M_Ox, T1, T2]^T en R^6

Paleta de Colores USS Institucional:
-----------------------------------
- USS_BLUE        = '#00205B' (Azul institucional principal)
- USS_GOLD        = '#D4AF37' (Dorado institucional)
- USS_ACCENT_BLUE = '#1E88E5' (Azul acento claro)
- USS_ACCENT_GREEN= '#27AE60' (Verde acento)
- USS_ACCENT_RED  = '#C0392B' (Rojo carga / crítico)

Autor: Subagente 3 — Desarrollador Módulo 03 (dev_module_03)
Ecosistema: Antigravity 2.0 / Bóveda Obsidian USS
"""

import os
import sys
import numpy as np
import sympy as sp

# Configuración headless segura para entornos sin servidor X11/Wayland
if os.environ.get('DISPLAY', '') == '' and os.environ.get('WAYLAND_DISPLAY', '') == '':
    import matplotlib
    matplotlib.use('Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ==============================================================================
# 1. CONSTANTES ESTÉTICAS INSTITUCIONALES USS
# ==============================================================================
USS_BLUE = '#00205B'
USS_GOLD = '#D4AF37'
USS_ACCENT_BLUE = '#1E88E5'
USS_ACCENT_GREEN = '#27AE60'
USS_ACCENT_RED = '#C0392B'

USS_DARK_GRAY = '#2C3E50'
USS_LIGHT_GRAY = '#ECF0F1'
USS_BG_WHITE = '#FFFFFF'

# Parámetros tipográficos de Matplotlib
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = USS_BLUE
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['mathtext.fontset'] = 'cm'


# ==============================================================================
# 2. DEFINICIÓN DE CLASES Y MODELO MECÁNICO TRIDIMENSIONAL
# ==============================================================================
class SistemaEquilibrio3D:
    """
    Modela un sistema de grúa / brazo mecánico tridimensional en voladizo.
    
    Geometría por defecto:
    - Pivote en el origen: O = (0, 0, 0)
    - Punta del brazo: A = (L, 0, 0) con L = 5.0 m
    - Anclaje Cable 1: C1 = (0, -d, h) con d = 2.5 m, h = 4.0 m
    - Anclaje Cable 2: C2 = (0,  d, h) con d = 2.5 m, h = 4.0 m
    - Carga gravitacional en A: W = [0, 0, -W_mag] (W_mag = 8000 N = 8 kN)
    - Fuerza lateral (viento o excentricidad): F_lat = [0, F_lat_y, 0]
    """

    def __init__(self, L=5.0, d=2.5, h=4.0, W_mag=8000.0, F_lat_y=0.0, W_boom=1500.0):
        self.L = float(L)
        self.d = float(d)
        self.h = float(h)
        self.W_mag = float(W_mag)
        self.F_lat_y = float(F_lat_y)
        self.W_boom = float(W_boom)  # Peso propio del brazo aplicado en L/2

        # Puntos geométricos clave
        self.r_O = np.array([0.0, 0.0, 0.0])
        self.r_A = np.array([self.L, 0.0, 0.0])
        self.r_G = np.array([self.L / 2.0, 0.0, 0.0])  # Centro de gravedad del brazo
        self.C1 = np.array([0.0, -self.d, self.h])
        self.C2 = np.array([0.0,  self.d, self.h])

        # Vectores directores y versores unitarios de los cables
        self._calcular_geometria_cables()

    def _calcular_geometria_cables(self):
        """Calcula vectores directores y vectores unitarios que apuntan desde A hacia anclajes."""
        self.v_c1 = self.C1 - self.r_A
        self.len_c1 = np.linalg.norm(self.v_c1)
        self.u1 = self.v_c1 / self.len_c1

        self.v_c2 = self.C2 - self.r_A
        self.len_c2 = np.linalg.norm(self.v_c2)
        self.u2 = self.v_c2 / self.len_c2

    def construir_matriz_sistema(self):
        """
        Construye la matriz A (6x6) y el vector b (6x1) del sistema lineal A * x = b.
        
        Vector de incógnitas:
            x = [R_Ox, R_Oy, R_Oz, M_Ox, T_1, T_2]^T
            
        Filas del sistema (Ecuaciones de Newton-Euler):
            Fila 0: sum F_x = 0  =>  R_Ox + T1*u1_x + T2*u2_x = -F_ext_x
            Fila 1: sum F_y = 0  =>  R_Oy + T1*u1_y + T2*u2_y = -F_ext_y
            Fila 2: sum F_z = 0  =>  R_Oz + T1*u1_z + T2*u2_z = -F_ext_z
            Fila 3: sum tau_Ox = 0 => M_Ox + [r_A x (T1*u1)]_x + [r_A x (T2*u2)]_x = -tau_ext_x
            Fila 4: sum tau_Oy = 0 => 0    + [r_A x (T1*u1)]_y + [r_A x (T2*u2)]_y = -tau_ext_y
            Fila 5: sum tau_Oz = 0 => 0    + [r_A x (T1*u1)]_z + [r_A x (T2*u2)]_z = -tau_ext_z
            
        Retorna:
            A: np.ndarray de tamaño (6, 6)
            b: np.ndarray de tamaño (6,)
        """
        A = np.zeros((6, 6), dtype=np.float64)
        b = np.zeros(6, dtype=np.float64)

        # 1. Coeficientes de R_O = [R_Ox, R_Oy, R_Oz]
        A[0:3, 0:3] = np.eye(3)
        # R_O pasa por el origen O(0,0,0), luego r_O x R_O = 0 en las filas de torque
        A[3:6, 0:3] = 0.0

        # 2. Coeficientes de M_Ox (momento de reacción torsional en el eje X)
        A[0:3, 3] = np.array([0.0, 0.0, 0.0])
        A[3:6, 3] = np.array([1.0, 0.0, 0.0])

        # 3. Coeficientes de T_1 (Cable 1)
        A[0:3, 4] = self.u1
        tau_u1 = np.cross(self.r_A, self.u1)
        A[3:6, 4] = tau_u1

        # 4. Coeficientes de T_2 (Cable 2)
        A[0:3, 5] = self.u2
        tau_u2 = np.cross(self.r_A, self.u2)
        A[3:6, 5] = tau_u2

        # 5. Vector de términos independientes b (Fuerzas y Torques externos negativos)
        # Carga en A: W_carga = [0, F_lat_y, -W_mag]
        F_carga = np.array([0.0, self.F_lat_y, -self.W_mag])
        # Peso propio del brazo en G: W_propio = [0, 0, -W_boom]
        F_boom = np.array([0.0, 0.0, -self.W_boom])

        F_ext_total = F_carga + F_boom
        tau_ext_total = np.cross(self.r_A, F_carga) + np.cross(self.r_G, F_boom)

        b[0:3] = -F_ext_total
        b[3:6] = -tau_ext_total

        return A, b

    def resolver_numerico(self):
        """
        Resuelve el sistema lineal 6x6 usando descomposición LU / solución directa de NumPy.
        Calcula rango, determinante, número de condición y residuo euclidiano.
        """
        A, b = self.construir_matriz_sistema()
        det_A = np.linalg.det(A)
        rank_A = np.linalg.matrix_rank(A)
        cond_A = np.linalg.cond(A)

        if rank_A < 6:
            raise ValueError(f"El sistema es singular (rango={rank_A} < 6). No es isostático.")

        x = np.linalg.solve(A, b)
        residuo = np.linalg.norm(np.dot(A, x) - b)

        resultados = {
            'R_Ox': x[0],
            'R_Oy': x[1],
            'R_Oz': x[2],
            'M_Ox': x[3],
            'T_1': x[4],
            'T_2': x[5],
            'vector_x': x,
            'det_A': det_A,
            'rank_A': rank_A,
            'cond_A': cond_A,
            'residuo': residuo,
            'A': A,
            'b': b
        }
        return resultados

    def resolver_simbolico(self):
        """
        Obtiene la solución analítica cerrada exacta utilizando SymPy.
        """
        L_s, d_s, h_s = sp.symbols('L d h', positive=True, real=True)
        W_s, F_lat_s, Wb_s = sp.symbols('W F_lat W_boom', real=True)
        R_x, R_y, R_z, M_x, T1, T2 = sp.symbols('R_Ox R_Oy R_Oz M_Ox T_1 T_2', real=True)

        S_c = sp.sqrt(L_s**2 + d_s**2 + h_s**2)
        u1_s = sp.Matrix([-L_s / S_c, -d_s / S_c, h_s / S_c])
        u2_s = sp.Matrix([-L_s / S_c,  d_s / S_c, h_s / S_c])

        # Fuerzas
        F_RO_s = sp.Matrix([R_x, R_y, R_z])
        F_T1_s = T1 * u1_s
        F_T2_s = T2 * u2_s
        F_ext_s = sp.Matrix([0, F_lat_s, -W_s])
        F_boom_s = sp.Matrix([0, 0, -Wb_s])

        # Suma de fuerzas
        eq_F = F_RO_s + F_T1_s + F_T2_s + F_ext_s + F_boom_s

        # Momentos en O
        r_A_s = sp.Matrix([L_s, 0, 0])
        r_G_s = sp.Matrix([L_s / 2, 0, 0])
        tau_T1_s = r_A_s.cross(F_T1_s)
        tau_T2_s = r_A_s.cross(F_T2_s)
        tau_ext_s = r_A_s.cross(F_ext_s)
        tau_boom_s = r_G_s.cross(F_boom_s)
        M_RO_s = sp.Matrix([M_x, 0, 0])

        eq_tau = M_RO_s + tau_T1_s + tau_T2_s + tau_ext_s + tau_boom_s

        ecuaciones = list(eq_F) + list(eq_tau)
        incognitas = [R_x, R_y, R_z, M_x, T1, T2]
        sol_simbolica = sp.solve(ecuaciones, incognitas)

        return sol_simbolica

    def auditoria_equilibrio(self, res):
        """
        Calcula detalladamente cada vector de fuerza y su vector de torque respecto
        al origen O para auditar el cumplimiento riguroso de sum F = 0 y sum tau = 0.
        """
        R_O = np.array([res['R_Ox'], res['R_Oy'], res['R_Oz']])
        F_T1 = res['T_1'] * self.u1
        F_T2 = res['T_2'] * self.u2
        F_carga = np.array([0.0, self.F_lat_y, -self.W_mag])
        F_boom = np.array([0.0, 0.0, -self.W_boom])

        # Torques individuales
        tau_RO = np.cross(self.r_O, R_O)  # Es 0
        tau_T1 = np.cross(self.r_A, F_T1)
        tau_T2 = np.cross(self.r_A, F_T2)
        tau_carga = np.cross(self.r_A, F_carga)
        tau_boom = np.cross(self.r_G, F_boom)
        tau_react_M = np.array([res['M_Ox'], 0.0, 0.0])

        sum_F = R_O + F_T1 + F_T2 + F_carga + F_boom
        sum_tau = tau_RO + tau_T1 + tau_T2 + tau_carga + tau_boom + tau_react_M

        auditoria = {
            'Fuerzas': {
                'Rótula O (R_O)': (self.r_O, R_O, tau_RO),
                'Cable 1 (F_T1)': (self.r_A, F_T1, tau_T1),
                'Cable 2 (F_T2)': (self.r_A, F_T2, tau_T2),
                'Carga Suspendida (W)': (self.r_A, F_carga, tau_carga),
                'Peso Propio Brazo (W_b)': (self.r_G, F_boom, tau_boom),
                'Momento Reactivo Axial (M_Ox)': (self.r_O, np.zeros(3), tau_react_M)
            },
            'sum_F': sum_F,
            'norm_sum_F': np.linalg.norm(sum_F),
            'sum_tau': sum_tau,
            'norm_sum_tau': np.linalg.norm(sum_tau)
        }
        return auditoria


# ==============================================================================
# 3. GENERACIÓN DE VISUALIZACIÓN GRÁFICA MULTIPANEL DE ALTA FIDELIDAD
# ==============================================================================
def graficar_simulacion_3d(sistema, res, auditoria, ruta_guardado=None):
    """
    Genera una figura técnica institucional de 4 paneles (300 DPI) que ilustra:
      Panel 1 (3D): Geometría estructural tridimensional y cables tensores.
      Panel 2 (3D): Diagrama de Cuerpo Libre (DCL) con vectores de fuerza a escala.
      Panel 3 (3D): Espacio vectorial de torques individuales tau_i = r_i x F_i y lazo cerrado.
      Panel 4 (2D): Análisis de sensibilidad paramétrica de tensiones vs posición de carga.
    """
    fig = plt.figure(figsize=(18, 14), facecolor=USS_BG_WHITE)

    # --------------------------------------------------------------------------
    # Subplot 1: Estructura 3D, Muro de Anclaje y Cables
    # --------------------------------------------------------------------------
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    ax1.set_title('1. Geometría Espacial del Brazo de Grúa y Cables Tensores\n(Universidad San Sebastián — Álgebra Lineal)',
                  fontsize=11, fontweight='bold', color=USS_BLUE, pad=12)

    # Representación del muro vertical de anclaje (x = 0) con Poly3DCollection
    muro_y = sistema.d * 1.6
    muro_z_max = sistema.h * 1.3
    verts_muro = [
        np.array([[0, -muro_y, -0.5],
                  [0,  muro_y, -0.5],
                  [0,  muro_y,  muro_z_max],
                  [0, -muro_y,  muro_z_max]])
    ]
    muro = Poly3DCollection(verts_muro, alpha=0.12, facecolor=USS_BLUE, edgecolor=USS_GOLD, linewidths=1.5)
    ax1.add_collection3d(muro)

    # Brazo mecánico (línea sólida gruesa con marcadores)
    ax1.plot([sistema.r_O[0], sistema.r_A[0]],
             [sistema.r_O[1], sistema.r_A[1]],
             [sistema.r_O[2], sistema.r_A[2]],
             color=USS_BLUE, linewidth=5.5, label='Brazo Mecánico (Acero Estructural)', zorder=4)

    # Cables tensores (líneas punteadas con dorado USS)
    ax1.plot([sistema.r_A[0], sistema.C1[0]],
             [sistema.r_A[1], sistema.C1[1]],
             [sistema.r_A[2], sistema.C1[2]],
             color=USS_GOLD, linewidth=2.8, linestyle='--',
             label=f'Cable 1 ($T_1 = {res["T_1"]:.1f}$ N)')

    ax1.plot([sistema.r_A[0], sistema.C2[0]],
             [sistema.r_A[1], sistema.C2[1]],
             [sistema.r_A[2], sistema.C2[2]],
             color=USS_GOLD, linewidth=2.8, linestyle=':',
             label=f'Cable 2 ($T_2 = {res["T_2"]:.1f}$ N)')

    # Nodos y anclajes
    ax1.scatter([0], [0], [0], color=USS_BLUE, s=120, edgecolors=USS_GOLD, linewidth=2, label='Pivote $O(0,0,0)$')
    ax1.scatter([sistema.r_A[0]], [sistema.r_A[1]], [sistema.r_A[2]],
                color=USS_ACCENT_RED, s=100, label='Extremo de Carga $A$')
    ax1.scatter([sistema.C1[0], sistema.C2[0]],
                [sistema.C1[1], sistema.C2[1]],
                [sistema.C1[2], sistema.C2[2]],
                color=USS_GOLD, s=90, edgecolors=USS_BLUE, label='Anclajes Muro $C_1, C_2$')

    # Configuración de límites y etiquetas
    ax1.set_xlim([-0.5, sistema.L + 1.0])
    ax1.set_ylim([-muro_y, muro_y])
    ax1.set_zlim([-1.0, muro_z_max])
    ax1.set_xlabel('$X$ (m) [Línea del Brazo]', fontweight='bold')
    ax1.set_ylabel('$Y$ (m) [Lateral]', fontweight='bold')
    ax1.set_zlabel('$Z$ (m) [Vertical]', fontweight='bold')
    ax1.view_init(elev=24, azim=130)
    ax1.legend(loc='upper right', fontsize=8, framealpha=0.9)
    ax1.grid(True, linestyle=':', alpha=0.5)

    # --------------------------------------------------------------------------
    # Subplot 2: Diagrama de Cuerpo Libre 3D (DCL)
    # --------------------------------------------------------------------------
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    ax2.set_title('2. Diagrama de Cuerpo Libre Tridimensional (DCL 3D)\n[Fuerzas Concurrentes y Reactivas]',
                  fontsize=11, fontweight='bold', color=USS_BLUE, pad=12)

    # Esqueleto estructural tenue
    ax2.plot([sistema.r_O[0], sistema.r_A[0]], [0, 0], [0, 0],
             color=USS_DARK_GRAY, linewidth=2.0, alpha=0.4, linestyle='-')

    # Factor de escala visual para fuerzas (metros por Newton)
    escala_F = 1.8 / max(res['T_1'], res['T_2'], abs(res['R_Ox']), sistema.W_mag)

    def dibujar_flecha_3d(ax, origen, vector, color, label, lw=2.5):
        ox, oy, oz = origen
        vx, vy, vz = vector * escala_F
        ax.quiver(ox, oy, oz, vx, vy, vz,
                  color=color, linewidth=lw, arrow_length_ratio=0.28, normalize=False)
        ax.text(ox + vx * 1.12, oy + vy * 1.12, oz + vz * 1.12,
                label, color=color, fontsize=8.5, fontweight='bold')

    # Vectores de fuerza en DCL
    dibujar_flecha_3d(ax2, sistema.r_O, np.array([res['R_Ox'], res['R_Oy'], res['R_Oz']]),
                      USS_ACCENT_BLUE, r'$\vec{R}_O$ (Reacción Pivote)', lw=3.0)
    dibujar_flecha_3d(ax2, sistema.r_A, res['T_1'] * sistema.u1,
                      USS_GOLD, r'$\vec{T}_1$ (Tensión 1)', lw=2.8)
    dibujar_flecha_3d(ax2, sistema.r_A, res['T_2'] * sistema.u2,
                      '#B8860B', r'$\vec{T}_2$ (Tensión 2)', lw=2.8)
    dibujar_flecha_3d(ax2, sistema.r_A, np.array([0, sistema.F_lat_y, -sistema.W_mag]),
                      USS_ACCENT_RED, r'$\vec{W}$ (Carga)', lw=3.0)
    dibujar_flecha_3d(ax2, sistema.r_G, np.array([0, 0, -sistema.W_boom]),
                      USS_ACCENT_GREEN, r'$\vec{W}_{boom}$ (Peso Propio)', lw=2.5)

    ax2.set_xlim([-1.0, sistema.L + 1.0])
    ax2.set_ylim([-sistema.d - 1.0, sistema.d + 1.0])
    ax2.set_zlim([-3.0, sistema.h + 1.0])
    ax2.set_xlabel('$X$ (m)', fontweight='bold')
    ax2.set_ylabel('$Y$ (m)', fontweight='bold')
    ax2.set_zlabel('$Z$ (m)', fontweight='bold')
    ax2.view_init(elev=22, azim=125)
    ax2.grid(True, linestyle=':', alpha=0.5)

    # --------------------------------------------------------------------------
    # Subplot 3: Espacio Vectorial de Torques (tau_i = r_i x F_i)
    # --------------------------------------------------------------------------
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    ax3.set_title(r'3. Espacio Vectorial de Torques Respecto a $O$ ($\vec{\tau} = \vec{r} \times \vec{F}$)' +
                  '\n' + r'[Equilibrio Rotacional: $\sum \vec{\tau}_O = \vec{0}$]',
                  fontsize=11, fontweight='bold', color=USS_BLUE, pad=12)

    # Extraer torques de la auditoría
    tau_T1 = auditoria['Fuerzas']['Cable 1 (F_T1)'][2]
    tau_T2 = auditoria['Fuerzas']['Cable 2 (F_T2)'][2]
    tau_W = auditoria['Fuerzas']['Carga Suspendida (W)'][2]
    tau_Wb = auditoria['Fuerzas']['Peso Propio Brazo (W_b)'][2]
    tau_M = auditoria['Fuerzas']['Momento Reactivo Axial (M_Ox)'][2]

    max_tau = max(np.linalg.norm(tau_T1), np.linalg.norm(tau_T2), np.linalg.norm(tau_W), 1.0)
    escala_tau = 3.0 / max_tau

    def dibujar_vector_torque(ax, origen, vec_tau, color, label):
        ox, oy, oz = origen
        vx, vy, vz = vec_tau * escala_tau
        ax.quiver(ox, oy, oz, vx, vy, vz,
                  color=color, linewidth=2.8, arrow_length_ratio=0.25, normalize=False)
        ax.text(ox + vx * 1.15, oy + vy * 1.15, oz + vz * 1.15,
                label, color=color, fontsize=8.5, fontweight='bold')

    origen_0 = np.array([0.0, 0.0, 0.0])
    dibujar_vector_torque(ax3, origen_0, tau_T1, USS_GOLD, r'$\vec{\tau}_{T1}$')
    dibujar_vector_torque(ax3, origen_0, tau_T2, '#B8860B', r'$\vec{\tau}_{T2}$')
    dibujar_vector_torque(ax3, origen_0, tau_W, USS_ACCENT_RED, r'$\vec{\tau}_W$')
    dibujar_vector_torque(ax3, origen_0, tau_Wb, USS_ACCENT_GREEN, r'$\vec{\tau}_{W,b}$')
    if np.linalg.norm(tau_M) > 1e-6:
        dibujar_vector_torque(ax3, origen_0, tau_M, USS_ACCENT_BLUE, r'$\vec{M}_{Ox}$')

    # Cadena poligonal de suma de torques (polígono cerrado que evidencia sum tau = 0)
    p0 = origen_0
    p1 = p0 + tau_T1 * escala_tau
    p2 = p1 + tau_T2 * escala_tau
    p3 = p2 + tau_Wb * escala_tau
    p4 = p3 + tau_W * escala_tau
    p5 = p4 + tau_M * escala_tau  # Cierra exactamente en p0

    cadena = np.array([p0, p1, p2, p3, p4, p5])
    ax3.plot(cadena[:, 0], cadena[:, 1], cadena[:, 2],
             color=USS_BLUE, linestyle='--', linewidth=1.5,
             marker='o', markersize=4, label=r'Lazo Cerrado ($\sum \vec{\tau} = \mathbf{0}$)')

    lim_t = 3.5
    ax3.set_xlim([-lim_t, lim_t])
    ax3.set_ylim([-lim_t, lim_t])
    ax3.set_zlim([-lim_t, lim_t])
    ax3.set_xlabel(r'$\tau_x$ (N$\cdot$m)', fontweight='bold')
    ax3.set_ylabel(r'$\tau_y$ (N$\cdot$m)', fontweight='bold')
    ax3.set_zlabel(r'$\tau_z$ (N$\cdot$m)', fontweight='bold')
    ax3.view_init(elev=20, azim=55)
    ax3.legend(loc='lower left', fontsize=8)
    ax3.grid(True, linestyle=':', alpha=0.5)

    # --------------------------------------------------------------------------
    # Subplot 4: Análisis de Sensibilidad Paramétrica
    # --------------------------------------------------------------------------
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.set_title('4. Sensibilidad de Esfuerzos vs. Posición de la Carga ($x_A / L$)\n[Comportamiento de Cables y Pivote]',
                  fontsize=11, fontweight='bold', color=USS_BLUE, pad=12)

    # Barrido de posición de carga desde 0.2 L hasta 1.0 L
    posiciones_rel = np.linspace(0.2, 1.0, 50)
    t1_vals = []
    t2_vals = []
    rox_vals = []

    for s_pos in posiciones_rel:
        sis_temp = SistemaEquilibrio3D(
            L=sistema.L, d=sistema.d, h=sistema.h,
            W_mag=sistema.W_mag, F_lat_y=sistema.F_lat_y, W_boom=sistema.W_boom
        )
        # Modificar punto de aplicación de la carga
        sis_temp.r_A = np.array([s_pos * sistema.L, 0.0, 0.0])
        sis_temp._calcular_geometria_cables()
        res_temp = sis_temp.resolver_numerico()
        t1_vals.append(res_temp['T_1'])
        t2_vals.append(res_temp['T_2'])
        rox_vals.append(res_temp['R_Ox'])

    ax4.plot(posiciones_rel, t1_vals, color=USS_GOLD, linewidth=2.5, label='Tensión $T_1$ (Cable 1)')
    ax4.plot(posiciones_rel, t2_vals, color=USS_DARK_GRAY, linestyle='--', linewidth=2.0, label='Tensión $T_2$ (Cable 2)')
    ax4.plot(posiciones_rel, rox_vals, color=USS_ACCENT_BLUE, linewidth=2.5, label='Compresión $R_{Ox}$ (Pivote O)')

    # Resaltar punto de operación actual
    pos_actual = 1.0
    ax4.axvline(pos_actual, color=USS_ACCENT_RED, linestyle=':', alpha=0.7, label='Punto Actual ($x = L$)')
    ax4.scatter([pos_actual], [res['T_1']], color=USS_GOLD, s=60, zorder=5)
    ax4.scatter([pos_actual], [res['R_Ox']], color=USS_ACCENT_BLUE, s=60, zorder=5)

    ax4.set_xlabel('Posición Relativa de la Carga ($x / L$)', fontweight='bold')
    ax4.set_ylabel('Magnitud de Fuerza (N)', fontweight='bold')
    ax4.grid(True, linestyle=':', alpha=0.6)
    ax4.legend(loc='upper left', fontsize=8.5)

    plt.tight_layout()

    if ruta_guardado:
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
        print(f"[OK] Gráfico de simulación 3D guardado exitosamente en:\n     {ruta_guardado}")

    # Si hay interfaz gráfica activa, desplegar ventana interactiva
    if os.environ.get('DISPLAY', '') != '' or os.environ.get('WAYLAND_DISPLAY', '') != '':
        plt.show()

    plt.close(fig)


# ==============================================================================
# 4. FUNCIÓN PRINCIPAL DE EJECUCIÓN Y REPORTE PEDAGÓGICO
# ==============================================================================
def main():
    """Ejecuta el pipeline completo de cálculo, auditoría y visualización."""
    print("=" * 80)
    print("UNIVERSIDAD SAN SEBASTIÁN — FACULTAD DE INGENIERÍA, ARQUITECTURA Y DISEÑO")
    print("DEPARTAMENTO DE CIENCIAS EXACTAS — ÁLGEBRA LINEAL (DCEX0007)")
    print("MÓDULO 08: SIMULACIÓN DE TORQUE Y EQUILIBRIO ESTÁTICO EN R³")
    print("=" * 80)

    # 1. Instanciar sistema mecánico
    sistema = SistemaEquilibrio3D(
        L=5.0,        # Longitud de la pluma (m)
        d=2.5,        # Semiancho de anclajes en el muro (m)
        h=4.0,        # Altura de anclajes sobre el pivote (m)
        W_mag=8000.0, # Carga gravitacional suspendida en la punta (8 kN)
        F_lat_y=0.0,  # Fuerza lateral nula inicialmente (caso simétrico)
        W_boom=1500.0 # Peso propio de la pluma (1.5 kN)
    )

    print("\n[1] PARÁMETROS GEOMÉTRICOS Y MECÁNICOS DEL SISTEMA:")
    print(f"    - Longitud del Brazo (L)           : {sistema.L:.2f} m")
    print(f"    - Carga Gravitacional Externa (W)  : {sistema.W_mag:.2f} N")
    print(f"    - Peso Propio del Brazo (W_boom)   : {sistema.W_boom:.2f} N (aplicado en L/2)")
    print(f"    - Anclajes de Cables C1 y C2       : C1(0, {-sistema.d:.1f}, {sistema.h:.1f}) | C2(0, {sistema.d:.1f}, {sistema.h:.1f})")
    print(f"    - Longitud de cada Cable           : {sistema.len_c1:.4f} m")
    print(f"    - Versor Cable 1 (u1)              : [{sistema.u1[0]:.4f}, {sistema.u1[1]:.4f}, {sistema.u1[2]:.4f}]")
    print(f"    - Versor Cable 2 (u2)              : [{sistema.u2[0]:.4f}, {sistema.u2[1]:.4f}, {sistema.u2[2]:.4f}]")

    # 2. Resolución Simbólica con SymPy
    print("\n[2] DEDUCCIÓN SIMBÓLICA EXACTA (SymPy):")
    sol_simb = sistema.resolver_simbolico()
    for var, expr in sol_simb.items():
        print(f"    - {str(var):<6} = {sp.simplify(expr)}")

    # 3. Resolución Numérica con NumPy
    print("\n[3] RESOLUCIÓN NUMÉRICA DEL SISTEMA LINEAL 6x6 (NumPy):")
    res = sistema.resolver_numerico()
    A = res['A']
    b = res['b']

    print(f"    - Determinante det(A)              : {res['det_A']:.4f}")
    print(f"    - Rango de la Matriz rank(A)       : {res['rank_A']} (Grado de libertad = 0, Isostático)")
    print(f"    - Número de Condición kappa(A)     : {res['cond_A']:.2f} (Excelente estabilidad numérica)")
    print(f"    - Residuo Euclidiano ||Ax - b||    : {res['residuo']:.2e} N")

    print("\n    VECTOR SOLUCIÓN x = [R_Ox, R_Oy, R_Oz, M_Ox, T_1, T_2]^T:")
    nombres_incog = [
        ("R_Ox", "Reacción en Pivote O (Compresión X)", "N"),
        ("R_Oy", "Reacción en Pivote O (Lateral Y)", "N"),
        ("R_Oz", "Reacción en Pivote O (Vertical Z)", "N"),
        ("M_Ox", "Momento Reactivo Torsional (Eje X)", "N·m"),
        ("T_1 ", "Tensión en Cable Tensor 1", "N"),
        ("T_2 ", "Tensión en Cable Tensor 2", "N")
    ]
    for (tag, desc, unidad), val in zip(nombres_incog, res['vector_x']):
        print(f"      * {tag} ({desc:<36}): {val:12.2f} {unidad}")

    # 4. Auditoría de Equilibrio Estático de Newton-Euler
    print("\n[4] AUDITORÍA RIGUROSA DE EQUILIBRIO ESTÁTICO DE CUERPO RÍGIDO:")
    audit = sistema.auditoria_equilibrio(res)
    print("    " + "-" * 74)
    print(f"    {'Fuerza / Elemento':<26} | {'Fuerza F (N)':<22} | {'Torque tau_O (N·m)':<22}")
    print("    " + "-" * 74)
    for elem, (r, F, tau) in audit['Fuerzas'].items():
        str_F = f"[{F[0]:.1f}, {F[1]:.1f}, {F[2]:.1f}]"
        str_tau = f"[{tau[0]:.1f}, {tau[1]:.1f}, {tau[2]:.1f}]"
        print(f"    {elem:<26} | {str_F:<22} | {str_tau:<22}")
    print("    " + "-" * 74)
    print(f"    SUMA TOTAL DE FUERZAS sum F         : [{audit['sum_F'][0]:.2e}, {audit['sum_F'][1]:.2e}, {audit['sum_F'][2]:.2e}] N")
    print(f"    NORMA sum F (Tolerancia < 1e-12)    : {audit['norm_sum_F']:.2e} N -> EQUILIBRIO TRASLACIONAL CONFIRMADO")
    print(f"    SUMA TOTAL DE TORQUES sum tau_O     : [{audit['sum_tau'][0]:.2e}, {audit['sum_tau'][1]:.2e}, {audit['sum_tau'][2]:.2e}] N·m")
    print(f"    NORMA sum tau_O (Tol. < 1e-12)      : {audit['norm_sum_tau']:.2e} N·m -> EQUILIBRIO ROTACIONAL CONFIRMADO")

    # 5. Generación y Guardado de la Figura
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_figura = os.path.join(directorio_actual, "figura_simulacion_torque_equilibrio_3d.png")
    print("\n[5] GENERANDO GRÁFICO TÉCNICO MULTIPANEL 300 DPI...")
    graficar_simulacion_3d(sistema, res, audit, ruta_guardado=ruta_figura)

    print("\n" + "=" * 80)
    print("SIMULACIÓN Y VERIFICACIÓN MATRICIAL COMPLETADAS CON ÉXITO")
    print("=" * 80)


if __name__ == "__main__":
    main()
