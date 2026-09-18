#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modulo 08: Simulacion de Torque y Equilibrio Estatico en R3
Asignatura: Algebra Lineal (DCEX0007 / ICI) — Universidad San Sebastian (USS)

Este modulo modela, analiza y simula numerica y simbolicamente el equilibrio
estatico tridimensional de un cuerpo rigido (brazo mecanico / pluma de grua en
voladizo) sometido a cargas gravitacionales y sostenido por una rotula en el
origen y dos cables tensores espaciales.

Fundamentacion Mecanica y Matematica:
1. Definicion Vectorial del Torque:
   Para una fuerza F aplicada en un punto con vector de posicion r relativo a un
   centro de momentos O:
       tau_O = r x F = det([i, j, k; r_x, r_y, r_z; F_x, F_y, F_z])
   Magnitud:
       ||tau_O|| = ||r|| * ||F|| * sin(phi) = r_perp * ||F||
   donde r_perp es el brazo de palanca perpendicular a la linea de accion de F.

2. Leyes de Equilibrio Estatico de Newton-Euler (Cuerpo Rigido en R3):
   (I)  Equilibrio Traslacional:   sum F_i = 0   (3 ecuaciones escalares)
   (II) Equilibrio Rotacional:      sum tau_Oi = 0 (3 ecuaciones escalares)

3. Formulacion Matricial 6x6 (Sistema Lineal Isostatico):
   El sistema fisico se modela como un brazo rigido O-A de longitud L soportado
   en O(0,0,0) por una rotula con restriccion torsional axial y dos cables tensores
   anclados en C1(0, -d, h) y C2(0, d, h) con tensiones T1 y T2.
   Se plantea el sistema matricial exacto A * x = b, donde:
       x = [R_Ox, R_Oy, R_Oz, M_Ox, T1, T2]^T en R^6

Paleta de Colores Institucional USS:
- USS_BLUE         = '#00205B' (Azul institucional principal)
- USS_GOLD         = '#D4AF37' (Dorado institucional)
- USS_ACCENT_BLUE  = '#1E88E5' (Azul acento claro / reacciones)
- USS_ACCENT_GREEN = '#27AE60' (Verde acento / peso propio)
- USS_ACCENT_RED   = '#C0392B' (Rojo carga critica)
- USS_DARK_GRAY    = '#2C3E50' (Gris oscuro estructural)
- USS_LIGHT_GRAY   = '#F8F9FA' (Fondo claro / paneles)
- USS_BG_WHITE     = '#FFFFFF' (Fondo blanco)

Autor: Subagente 3 — Refactor Modulo 03 (refactor_module_03)
Ecosistema: Antigravity 2.0 / Boveda Obsidian USS
"""

import os
import sys
import numpy as np
import sympy as sp

# Configuracion headless segura para entornos sin servidor X11/Wayland
if os.environ.get('DISPLAY', '') == '' and os.environ.get('WAYLAND_DISPLAY', '') == '':
    import matplotlib
    matplotlib.use('Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Constantes Esteticas Institucionales USS
USS_BLUE = '#00205B'
USS_GOLD = '#D4AF37'
USS_ACCENT_BLUE = '#1E88E5'
USS_ACCENT_GREEN = '#27AE60'
USS_ACCENT_RED = '#C0392B'
USS_DARK_GRAY = '#2C3E50'
USS_LIGHT_GRAY = '#F8F9FA'
USS_BG_WHITE = '#FFFFFF'

# Parametros tipograficos de Matplotlib
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = USS_BLUE
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['mathtext.fontset'] = 'cm'


class SistemaEquilibrio3D:
    """
    Modela un sistema de grua / aguilon mecanico tridimensional en voladizo.

    Parametros geometricos y mecanicos:
    - Pivote en el origen: O = (0, 0, 0)
    - Punta del brazo: A = (L, 0, 0) con L = 5.0 m
    - Centro de gravedad del brazo: G = (L/2, 0, 0)
    - Anclaje Cable 1: C1 = (0, -d, h) con d = 2.5 m, h = 4.0 m
    - Anclaje Cable 2: C2 = (0,  d, h) con d = 2.5 m, h = 4.0 m
    - Carga gravitacional en A: W = [0, 0, -W_mag] (W_mag = 8000 N)
    - Fuerza lateral en A: F_lat = [0, F_lat_y, 0]
    - Peso propio del brazo en G: W_boom = [0, 0, -W_boom] (W_boom = 1500 N)
    """

    def __init__(self, L=5.0, d=2.5, h=4.0, W_mag=8000.0, F_lat_y=0.0, W_boom=1500.0):
        self.L = float(L)
        self.d = float(d)
        self.h = float(h)
        self.W_mag = float(W_mag)
        self.F_lat_y = float(F_lat_y)
        self.W_boom = float(W_boom)

        # Nodos geometricos clave
        self.r_O = np.array([0.0, 0.0, 0.0])
        self.r_A = np.array([self.L, 0.0, 0.0])
        self.r_G = np.array([self.L / 2.0, 0.0, 0.0])
        self.C1 = np.array([0.0, -self.d, self.h])
        self.C2 = np.array([0.0,  self.d, self.h])

        self._calcular_geometria_cables()

    def _calcular_geometria_cables(self):
        """Calcula vectores directores y versores unitarios desde A hacia los anclajes C1 y C2."""
        self.v_c1 = self.C1 - self.r_A
        self.len_c1 = np.linalg.norm(self.v_c1)
        self.u1 = self.v_c1 / self.len_c1

        self.v_c2 = self.C2 - self.r_A
        self.len_c2 = np.linalg.norm(self.v_c2)
        self.u2 = self.v_c2 / self.len_c2

    def construir_matriz_sistema(self, x_carga=None):
        """
        Construye la matriz A (6x6) y el vector b (6x1) del sistema lineal A * x = b.

        Vector de incognitas:
            x = [R_Ox, R_Oy, R_Oz, M_Ox, T_1, T_2]^T en R^6

        Filas del sistema (Ecuaciones de Newton-Euler):
            Fila 0: sum F_x = 0  =>  R_Ox + T1*u1_x + T2*u2_x = -F_ext_x
            Fila 1: sum F_y = 0  =>  R_Oy + T1*u1_y + T2*u2_y = -F_ext_y
            Fila 2: sum F_z = 0  =>  R_Oz + T1*u1_z + T2*u2_z = -F_ext_z
            Fila 3: sum tau_Ox = 0 => M_Ox + [r_A x (T1*u1)]_x + [r_A x (T2*u2)]_x = -tau_ext_x
            Fila 4: sum tau_Oy = 0 => 0    + [r_A x (T1*u1)]_y + [r_A x (T2*u2)]_y = -tau_ext_y
            Fila 5: sum tau_Oz = 0 => 0    + [r_A x (T1*u1)]_z + [r_A x (T2*u2)]_z = -tau_ext_z
        """
        A = np.zeros((6, 6), dtype=np.float64)
        b = np.zeros(6, dtype=np.float64)

        # 1. Coeficientes de R_O = [R_Ox, R_Oy, R_Oz]
        A[0:3, 0:3] = np.eye(3)
        A[3:6, 0:3] = 0.0

        # 2. Coeficientes de M_Ox (momento de reaccion torsional en el eje X)
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

        # 5. Vector de terminos independientes b
        pos_carga = self.r_A if x_carga is None else np.array([float(x_carga), 0.0, 0.0])
        F_carga = np.array([0.0, self.F_lat_y, -self.W_mag])
        F_boom = np.array([0.0, 0.0, -self.W_boom])

        F_ext_total = F_carga + F_boom
        tau_ext_total = np.cross(pos_carga, F_carga) + np.cross(self.r_G, F_boom)

        b[0:3] = -F_ext_total
        b[3:6] = -tau_ext_total

        return A, b

    def resolver_numerico(self, x_carga=None):
        """
        Resuelve el sistema lineal 6x6 usando descomposicion directa de NumPy.
        Calcula rango, determinante, numero de condicion y residuo euclidiano.
        """
        A, b = self.construir_matriz_sistema(x_carga=x_carga)
        det_A = np.linalg.det(A)
        rank_A = np.linalg.matrix_rank(A)
        cond_A = np.linalg.cond(A)

        if rank_A < 6:
            raise ValueError(f"El sistema es singular (rango={rank_A} < 6). Estructura no isostatica.")

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
            'b': b,
            'x_carga': self.L if x_carga is None else float(x_carga)
        }
        return resultados

    def resolver_simbolico(self):
        """
        Obtiene la solucion analitica cerrada exacta utilizando SymPy.
        """
        L_s, d_s, h_s = sp.symbols('L d h', positive=True, real=True)
        W_s, F_lat_s, Wb_s = sp.symbols('W F_lat W_boom', real=True)
        R_x, R_y, R_z, M_x, T1, T2 = sp.symbols('R_Ox R_Oy R_Oz M_Ox T_1 T_2', real=True)

        S_c = sp.sqrt(L_s**2 + d_s**2 + h_s**2)
        u1_s = sp.Matrix([-L_s / S_c, -d_s / S_c, h_s / S_c])
        u2_s = sp.Matrix([-L_s / S_c,  d_s / S_c, h_s / S_c])

        F_RO_s = sp.Matrix([R_x, R_y, R_z])
        F_T1_s = T1 * u1_s
        F_T2_s = T2 * u2_s
        F_ext_s = sp.Matrix([0, F_lat_s, -W_s])
        F_boom_s = sp.Matrix([0, 0, -Wb_s])

        eq_F = F_RO_s + F_T1_s + F_T2_s + F_ext_s + F_boom_s

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
        pos_carga = np.array([res['x_carga'], 0.0, 0.0])
        F_carga = np.array([0.0, self.F_lat_y, -self.W_mag])
        F_boom = np.array([0.0, 0.0, -self.W_boom])

        tau_RO = np.cross(self.r_O, R_O)
        tau_T1 = np.cross(self.r_A, F_T1)
        tau_T2 = np.cross(self.r_A, F_T2)
        tau_carga = np.cross(pos_carga, F_carga)
        tau_boom = np.cross(self.r_G, F_boom)
        tau_react_M = np.array([res['M_Ox'], 0.0, 0.0])

        sum_F = R_O + F_T1 + F_T2 + F_carga + F_boom
        sum_tau = tau_RO + tau_T1 + tau_T2 + tau_carga + tau_boom + tau_react_M

        auditoria = {
            'Fuerzas': {
                'Rotula O (R_O)': (self.r_O, R_O, tau_RO),
                'Cable 1 (F_T1)': (self.r_A, F_T1, tau_T1),
                'Cable 2 (F_T2)': (self.r_A, F_T2, tau_T2),
                'Carga Suspendida (W)': (pos_carga, F_carga, tau_carga),
                'Peso Propio Brazo (W_boom)': (self.r_G, F_boom, tau_boom),
                'Momento Reactivo Axial (M_Ox)': (self.r_O, np.zeros(3), tau_react_M)
            },
            'sum_F': sum_F,
            'norm_sum_F': np.linalg.norm(sum_F),
            'sum_tau': sum_tau,
            'norm_sum_tau': np.linalg.norm(sum_tau)
        }
        return auditoria


# ==============================================================================
# RUTINAS GRAFICAS INDIVIDUALES DE ALTA DEFINICION (300 DPI)
# ==============================================================================

def graficar_estructura_grua_3d(sistema, res, ruta_guardado=None):
    """
    Figura 1: Modelo Fisico 3D de la Grua Atirantada.
    Visualiza el aguilon rigido, la rotula en el origen, el muro vertical de anclaje,
    los cables tensores espaciales en USS_GOLD y la carga suspendida.
    """
    fig = plt.figure(figsize=(10, 8), facecolor=USS_BG_WHITE)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor(USS_BG_WHITE)

    # 1. Muro de anclaje vertical (x = 0) con Poly3DCollection (alpha entre 0.20 y 0.30)
    muro_y = sistema.d * 1.6
    muro_z_max = sistema.h * 1.3
    verts_muro = [
        np.array([[0, -muro_y, -0.6],
                  [0,  muro_y, -0.6],
                  [0,  muro_y,  muro_z_max],
                  [0, -muro_y,  muro_z_max]])
    ]
    muro = Poly3DCollection(verts_muro, alpha=0.25, facecolor=USS_BLUE, edgecolor=USS_GOLD, linewidths=1.5)
    ax.add_collection3d(muro)

    # Lineas de referencia en el muro
    ax.plot([0, 0], [-muro_y, muro_y], [sistema.h, sistema.h],
            color=USS_GOLD, linestyle=':', linewidth=1.0, alpha=0.7)

    # 2. Aguilon rigido (acero estructural)
    ax.plot([sistema.r_O[0], sistema.r_A[0]],
            [sistema.r_O[1], sistema.r_A[1]],
            [sistema.r_O[2], sistema.r_A[2]],
            color=USS_BLUE, linewidth=5.0, label='Aguilon Rigido (Acero USS)', zorder=5)

    # 3. Cables tensores espaciales
    ax.plot([sistema.r_A[0], sistema.C1[0]],
            [sistema.r_A[1], sistema.C1[1]],
            [sistema.r_A[2], sistema.C1[2]],
            color=USS_GOLD, linewidth=2.8, linestyle='--',
            label=f'Cable Tensor 1 ($T_1 = {res["T_1"]:.1f}$ N)', zorder=4)

    ax.plot([sistema.r_A[0], sistema.C2[0]],
            [sistema.r_A[1], sistema.C2[1]],
            [sistema.r_A[2], sistema.C2[2]],
            color=USS_GOLD, linewidth=2.8, linestyle=':',
            label=f'Cable Tensor 2 ($T_2 = {res["T_2"]:.1f}$ N)', zorder=4)

    # 4. Nodos y anclajes
    ax.scatter([0], [0], [0], color=USS_BLUE, s=140, edgecolors=USS_GOLD, linewidth=2.0,
               label='Rotula en Origen $O(0,0,0)$', zorder=6)
    ax.scatter([sistema.r_A[0]], [sistema.r_A[1]], [sistema.r_A[2]],
               color=USS_ACCENT_RED, s=120, edgecolors=USS_BLUE, linewidth=1.5,
               label=f'Extremo de Carga $A({sistema.L:.1f}, 0, 0)$', zorder=6)
    ax.scatter([sistema.C1[0], sistema.C2[0]],
               [sistema.C1[1], sistema.C2[1]],
               [sistema.C1[2], sistema.C2[2]],
               color=USS_GOLD, s=100, edgecolors=USS_BLUE, linewidth=1.5,
               label='Anclajes en Muro $C_1, C_2$', zorder=6)

    # 5. Carga suspendida y peso propio (vectores esquematicos)
    ax.quiver(sistema.r_A[0], sistema.r_A[1], sistema.r_A[2],
              0, 0, -1.2, color=USS_ACCENT_RED, linewidth=3.0, arrow_length_ratio=0.25)
    ax.text(sistema.r_A[0] + 0.15, 0.0, -1.35,
            f'Carga $W = {sistema.W_mag:.0f}$ N', color=USS_ACCENT_RED, fontsize=9.5, fontweight='bold')

    ax.scatter([sistema.r_G[0]], [sistema.r_G[1]], [sistema.r_G[2]],
               color=USS_ACCENT_GREEN, s=80, edgecolors=USS_BLUE, linewidth=1.5,
               label='Centro de Gravedad $G(L/2, 0, 0)$', zorder=6)
    ax.quiver(sistema.r_G[0], sistema.r_G[1], sistema.r_G[2],
              0, 0, -0.7, color=USS_ACCENT_GREEN, linewidth=2.2, arrow_length_ratio=0.3)
    ax.text(sistema.r_G[0] + 0.1, 0.0, -0.85,
            f'$W_{{boom}} = {sistema.W_boom:.0f}$ N', color=USS_ACCENT_GREEN, fontsize=8.5, fontweight='bold')

    # Configuracion de limites y etiquetas
    ax.set_xlim([-0.5, sistema.L + 1.0])
    ax.set_ylim([-muro_y, muro_y])
    ax.set_zlim([-1.6, muro_z_max])
    ax.set_xlabel('Eje X (m) [Aguilon]', fontweight='bold', labelpad=8)
    ax.set_ylabel('Eje Y (m) [Transversal]', fontweight='bold', labelpad=8)
    ax.set_zlabel('Eje Z (m) [Vertical]', fontweight='bold', labelpad=8)
    ax.set_title('Estructura Tridimensional del Brazo de Grua Atirantado\nUniversidad San Sebastian — DCEX0007',
                 fontsize=12, fontweight='bold', color=USS_BLUE, pad=15)
    ax.view_init(elev=24, azim=130)
    ax.legend(loc='upper right', fontsize=8.5, framealpha=0.92)
    ax.grid(True, linestyle=':', alpha=0.5)

    plt.tight_layout()
    if ruta_guardado:
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
    plt.close(fig)


def graficar_diagrama_cuerpo_libre_3d(sistema, res, ruta_guardado=None):
    """
    Figura 2: Diagrama de Cuerpo Libre Tridimensional (DCL 3D).
    Muestra los vectores de fuerza concurrentes en cada nodo: reacciones en el pivote
    (R_Ox, R_Oz en USS_ACCENT_BLUE), tensiones vectoriales T1 y T2 en USS_GOLD,
    y cargas gravitacionales W y W_boom.
    """
    fig = plt.figure(figsize=(10, 8), facecolor=USS_BG_WHITE)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor(USS_BG_WHITE)

    # Esqueleto estructural tenue de referencia
    ax.plot([sistema.r_O[0], sistema.r_A[0]], [0, 0], [0, 0],
            color=USS_DARK_GRAY, linewidth=2.0, alpha=0.35, linestyle='-')

    # Factor de escala fisica para los vectores de fuerza (metros por Newton)
    fuerza_max = max(res['T_1'], res['T_2'], abs(res['R_Ox']), sistema.W_mag)
    escala_F = 2.0 / fuerza_max

    def dibujar_vector_fuerza(ox, oy, oz, vx, vy, vz, color, label, lw=2.8):
        fx = vx * escala_F
        fy = vy * escala_F
        fz = vz * escala_F
        ax.quiver(ox, oy, oz, fx, fy, fz, color=color, linewidth=lw, arrow_length_ratio=0.22, normalize=False)
        ax.text(ox + fx * 1.12, oy + fy * 1.12, oz + fz * 1.12,
                label, color=color, fontsize=9.0, fontweight='bold')

    # 1. Reacciones en el pivote O(0,0,0)
    R_vec = np.array([res['R_Ox'], res['R_Oy'], res['R_Oz']])
    dibujar_vector_fuerza(0, 0, 0, R_vec[0], R_vec[1], R_vec[2],
                          USS_ACCENT_BLUE, r'$\vec{R}_O$ (Reaccion Resultante)', lw=3.2)
    # Componentes cartesianas de reaccion en O
    dibujar_vector_fuerza(0, 0, 0, res['R_Ox'], 0, 0,
                          USS_ACCENT_BLUE, f'$R_{{Ox}} = {res["R_Ox"]:.1f}$ N', lw=1.8)
    dibujar_vector_fuerza(0, 0, 0, 0, 0, res['R_Oz'],
                          USS_ACCENT_BLUE, f'$R_{{Oz}} = {res["R_Oz"]:.1f}$ N', lw=1.8)

    # 2. Tensiones de los cables en la punta A
    f_t1 = res['T_1'] * sistema.u1
    f_t2 = res['T_2'] * sistema.u2
    dibujar_vector_fuerza(sistema.r_A[0], sistema.r_A[1], sistema.r_A[2],
                          f_t1[0], f_t1[1], f_t1[2],
                          USS_GOLD, f'$\\vec{{T}}_1$ ({res["T_1"]:.1f} N)', lw=3.0)
    dibujar_vector_fuerza(sistema.r_A[0], sistema.r_A[1], sistema.r_A[2],
                          f_t2[0], f_t2[1], f_t2[2],
                          '#B8860B', f'$\\vec{{T}}_2$ ({res["T_2"]:.1f} N)', lw=3.0)

    # 3. Carga gravitacional suspendida en A
    dibujar_vector_fuerza(sistema.r_A[0], sistema.r_A[1], sistema.r_A[2],
                          0.0, sistema.F_lat_y, -sistema.W_mag,
                          USS_ACCENT_RED, f'$\\vec{{W}}$ ({sistema.W_mag:.0f} N)', lw=3.0)

    # 4. Peso propio del aguilon en G
    dibujar_vector_fuerza(sistema.r_G[0], sistema.r_G[1], sistema.r_G[2],
                          0.0, 0.0, -sistema.W_boom,
                          USS_ACCENT_GREEN, f'$\\vec{{W}}_{{boom}}$ ({sistema.W_boom:.0f} N)', lw=2.4)

    # Marcadores de nodos
    ax.scatter([0], [0], [0], color=USS_BLUE, s=120, edgecolors=USS_GOLD, linewidth=2.0)
    ax.scatter([sistema.r_A[0]], [0], [0], color=USS_ACCENT_RED, s=100)
    ax.scatter([sistema.r_G[0]], [0], [0], color=USS_ACCENT_GREEN, s=70)

    # Panel informativo de esfuerzos
    info_dcl = (
        "Equilibrio de Fuerzas:\n"
        f"  R_Ox  = {res['R_Ox']:10.1f} N (Compresion)\n"
        f"  R_Oz  = {res['R_Oz']:10.1f} N (Soporte Vertical)\n"
        f"  T_1   = {res['T_1']:10.1f} N (Traccion)\n"
        f"  T_2   = {res['T_2']:10.1f} N (Traccion)\n"
        f"  W     = {sistema.W_mag:10.1f} N (Carga)\n"
        f"  W_b   = {sistema.W_boom:10.1f} N (Peso Propio)"
    )
    ax.text2D(0.03, 0.82, info_dcl, transform=ax.transAxes,
              fontsize=8.5, fontfamily='monospace',
              bbox=dict(boxstyle='round,pad=0.5', facecolor=USS_LIGHT_GRAY, edgecolor=USS_BLUE, alpha=0.9))

    ax.set_xlim([-1.0, sistema.L + 1.0])
    ax.set_ylim([-sistema.d - 1.0, sistema.d + 1.0])
    ax.set_zlim([-2.5, sistema.h + 0.5])
    ax.set_xlabel('Eje X (m)', fontweight='bold', labelpad=8)
    ax.set_ylabel('Eje Y (m)', fontweight='bold', labelpad=8)
    ax.set_zlabel('Eje Z (m)', fontweight='bold', labelpad=8)
    ax.set_title('Diagrama de Cuerpo Libre Tridimensional (DCL 3D)\nEquilibrio de Fuerzas Concurrentes y Reactivas',
                 fontsize=12, fontweight='bold', color=USS_BLUE, pad=15)
    ax.view_init(elev=22, azim=125)
    ax.grid(True, linestyle=':', alpha=0.5)

    plt.tight_layout()
    if ruta_guardado:
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
    plt.close(fig)


def graficar_espacio_torques_3d(sistema, res, auditoria, ruta_guardado=None):
    """
    Figura 3: Espacio Vectorial de Torques y Poligonal Cerrada en R3.
    Grafica los momentos tau_i = r_i x F_i y la cadena poligonal cerrada demostrando
    visualmente que sum tau_O = 0 (equilibrio rotacional estricto).
    """
    fig = plt.figure(figsize=(10, 8), facecolor=USS_BG_WHITE)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor(USS_BG_WHITE)

    # Torques individuales respecto a O
    tau_T1 = auditoria['Fuerzas']['Cable 1 (F_T1)'][2]
    tau_T2 = auditoria['Fuerzas']['Cable 2 (F_T2)'][2]
    tau_W = auditoria['Fuerzas']['Carga Suspendida (W)'][2]
    tau_Wb = auditoria['Fuerzas']['Peso Propio Brazo (W_boom)'][2]
    tau_M = auditoria['Fuerzas']['Momento Reactivo Axial (M_Ox)'][2]

    max_tau = max(np.linalg.norm(tau_T1), np.linalg.norm(tau_T2), np.linalg.norm(tau_W), 1.0)
    escala_tau = 3.0 / max_tau

    def dibujar_vector_torque(origen, vec_tau, color, label):
        ox, oy, oz = origen
        vx, vy, vz = vec_tau * escala_tau
        ax.quiver(ox, oy, oz, vx, vy, vz,
                  color=color, linewidth=2.8, arrow_length_ratio=0.22, normalize=False)
        ax.text(ox + vx * 1.15, oy + vy * 1.15, oz + vz * 1.15,
                label, color=color, fontsize=9.0, fontweight='bold')

    origen_0 = np.array([0.0, 0.0, 0.0])
    dibujar_vector_torque(origen_0, tau_T1, USS_GOLD, r'$\vec{\tau}_{T1}$')
    dibujar_vector_torque(origen_0, tau_T2, '#B8860B', r'$\vec{\tau}_{T2}$')
    dibujar_vector_torque(origen_0, tau_W, USS_ACCENT_RED, r'$\vec{\tau}_W$')
    dibujar_vector_torque(origen_0, tau_Wb, USS_ACCENT_GREEN, r'$\vec{\tau}_{W,boom}$')
    if np.linalg.norm(tau_M) > 1e-6:
        dibujar_vector_torque(origen_0, tau_M, USS_ACCENT_BLUE, r'$\vec{M}_{Ox}$')

    # Cadena poligonal cerrada (cabeza a cola)
    p0 = origen_0
    p1 = p0 + tau_T1 * escala_tau
    p2 = p1 + tau_T2 * escala_tau
    p3 = p2 + tau_Wb * escala_tau
    p4 = p3 + tau_W * escala_tau
    p5 = p4 + tau_M * escala_tau

    cadena = np.array([p0, p1, p2, p3, p4, p5])
    ax.plot(cadena[:, 0], cadena[:, 1], cadena[:, 2],
            color=USS_BLUE, linestyle='--', linewidth=2.2,
            marker='o', markersize=6, markerfacecolor=USS_GOLD, markeredgecolor=USS_BLUE,
            label=r'Poligonal Cerrada: $\sum \vec{\tau}_O = \mathbf{0}$', zorder=5)

    # Panel informativo de auditoria de momentos
    info_tau = (
        "Auditoria de Momentos en O:\n"
        f"  ||tau_T1||    = {np.linalg.norm(tau_T1):8.1f} N*m\n"
        f"  ||tau_T2||    = {np.linalg.norm(tau_T2):8.1f} N*m\n"
        f"  ||tau_W||     = {np.linalg.norm(tau_W):8.1f} N*m\n"
        f"  ||tau_Wboom|| = {np.linalg.norm(tau_Wb):8.1f} N*m\n"
        f"  ||sum tau_O|| = {auditoria['norm_sum_tau']:.2e} N*m\n"
        "  Estado: Equilibrio Rotacional Confirmado"
    )
    ax.text2D(0.03, 0.82, info_tau, transform=ax.transAxes,
              fontsize=8.5, fontfamily='monospace',
              bbox=dict(boxstyle='round,pad=0.5', facecolor=USS_LIGHT_GRAY, edgecolor=USS_BLUE, alpha=0.9))

    lim_t = 3.2
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-lim_t, lim_t])
    ax.set_zlim([-2.0, 2.0])
    ax.set_xlabel(r'$\tau_x$ (N$\cdot$m)', fontweight='bold', labelpad=8)
    ax.set_ylabel(r'$\tau_y$ (N$\cdot$m)', fontweight='bold', labelpad=8)
    ax.set_zlabel(r'$\tau_z$ (N$\cdot$m)', fontweight='bold', labelpad=8)
    ax.set_title('Espacio Vectorial de Torques y Poligono Cerrado de Equilibrio\n' +
                 r'$\sum \vec{\tau}_O = \vec{\tau}_{T1} + \vec{\tau}_{T2} + \vec{\tau}_W + \vec{\tau}_{W,boom} = \mathbf{0}$',
                 fontsize=12, fontweight='bold', color=USS_BLUE, pad=15)
    ax.view_init(elev=20, azim=55)
    ax.legend(loc='lower left', fontsize=8.5, framealpha=0.92)
    ax.grid(True, linestyle=':', alpha=0.5)

    plt.tight_layout()
    if ruta_guardado:
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
    plt.close(fig)


def graficar_analisis_sensibilidad_2d(sistema, res, ruta_guardado=None):
    """
    Figura 4: Analisis de Sensibilidad 2D de Esfuerzos vs Posicion de la Carga.
    Muestra la variacion continua de las tensiones T1 y T2 y de la reaccion axial R_Ox
    frente a la posicion relativa x/L de la carga suspendida.
    """
    fig, ax = plt.subplots(figsize=(10, 6.5), facecolor=USS_BG_WHITE)
    ax.set_facecolor(USS_BG_WHITE)

    # Barrido de posicion de la carga desde 0.2 L hasta 1.0 L
    posiciones_x = np.linspace(0.2 * sistema.L, sistema.L, 80)
    posiciones_rel = posiciones_x / sistema.L

    t1_vals = []
    t2_vals = []
    rox_vals = []
    roz_vals = []

    for x_c in posiciones_x:
        res_temp = sistema.resolver_numerico(x_carga=x_c)
        t1_vals.append(res_temp['T_1'])
        t2_vals.append(res_temp['T_2'])
        rox_vals.append(res_temp['R_Ox'])
        roz_vals.append(res_temp['R_Oz'])

    t1_vals = np.array(t1_vals)
    t2_vals = np.array(t2_vals)
    rox_vals = np.array(rox_vals)
    roz_vals = np.array(roz_vals)

    # Curvas de esfuerzos
    ax.plot(posiciones_x, t1_vals, color=USS_GOLD, linewidth=2.8,
            label=r'Tension en Cables $T_1 = T_2$ (Traccion)')
    ax.plot(posiciones_x, rox_vals, color=USS_ACCENT_BLUE, linewidth=2.8,
            label=r'Compresion Axial en Aguilon $R_{Ox}$')
    ax.plot(posiciones_x, roz_vals, color=USS_ACCENT_GREEN, linewidth=2.0, linestyle='-.',
            label=r'Reaccion Vertical en Pivote $R_{Oz}$')

    # Punto nominal de operacion (x = L = 5.0 m)
    pos_nominal = sistema.L
    ax.axvline(pos_nominal, color=USS_ACCENT_RED, linestyle=':', alpha=0.75, linewidth=1.5,
               label=f'Punto Nominal ($x = L = {pos_nominal:.1f}$ m)')
    ax.scatter([pos_nominal], [res['T_1']], color=USS_GOLD, s=70, zorder=5, edgecolors=USS_BLUE)
    ax.scatter([pos_nominal], [res['R_Ox']], color=USS_ACCENT_BLUE, s=70, zorder=5, edgecolors=USS_BLUE)
    ax.scatter([pos_nominal], [res['R_Oz']], color=USS_ACCENT_GREEN, s=70, zorder=5, edgecolors=USS_BLUE)

    # Anotaciones numericas en el punto nominal
    ax.annotate(f'$T = {res["T_1"]:.1f}$ N', xy=(pos_nominal, res['T_1']),
                xytext=(pos_nominal - 0.7, res['T_1'] + 400),
                fontsize=8.5, fontweight='bold', color=USS_GOLD,
                arrowprops=dict(arrowstyle='->', color=USS_GOLD, lw=1.2))
    ax.annotate(f'$R_{{Ox}} = {res["R_Ox"]:.1f}$ N', xy=(pos_nominal, res['R_Ox']),
                xytext=(pos_nominal - 0.7, res['R_Ox'] - 600),
                fontsize=8.5, fontweight='bold', color=USS_ACCENT_BLUE,
                arrowprops=dict(arrowstyle='->', color=USS_ACCENT_BLUE, lw=1.2))

    # Panel con formulaciones analiticas
    info_formulas = (
        r"$\mathbf{Ecuaciones\ de\ Dependencia:}$" + "\n" +
        r"$T(x) = \frac{S_c}{2h} \left(\frac{x}{L} W + \frac{1}{2} W_{boom}\right)$" + "\n" +
        r"$R_{Ox}(x) = \frac{L}{h} \left(\frac{x}{L} W + \frac{1}{2} W_{boom}\right)$" + "\n" +
        r"$R_{Oz}(x) = \left(1 - \frac{x}{L}\right) W + \frac{1}{2} W_{boom}$"
    )
    ax.text(0.03, 0.95, info_formulas, transform=ax.transAxes, verticalalignment='top',
            fontsize=9.0, bbox=dict(boxstyle='round,pad=0.5', facecolor=USS_LIGHT_GRAY, edgecolor=USS_BLUE, alpha=0.9))

    ax.set_xlabel('Posicion de la Carga $x$ a lo Largo del Aguilon (m)', fontweight='bold')
    ax.set_ylabel('Magnitud de Fuerza (N)', fontweight='bold')
    ax.set_title('Analisis de Sensibilidad de Esfuerzos vs. Posicion de la Carga\n' +
                 'Universidad San Sebastian — Departamento de Ciencias Exactas',
                 fontsize=12, fontweight='bold', color=USS_BLUE, pad=12)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='center left', fontsize=8.5, framealpha=0.92)

    # Segundo eje superior con la posicion relativa x/L
    ax_top = ax.twiny()
    ax_top.set_xlim(ax.get_xlim())
    ticks_x = np.linspace(1.0, sistema.L, 5)
    ax_top.set_xticks(ticks_x)
    ax_top.set_xticklabels([f'{t / sistema.L:.1f} L' for t in ticks_x])
    ax_top.set_xlabel('Posicion Relativa de la Carga ($x / L$)', fontweight='bold', color=USS_DARK_GRAY, labelpad=8)

    plt.tight_layout()
    if ruta_guardado:
        plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
    plt.close(fig)


# ==============================================================================
# FUNCION PRINCIPAL DE EJECUCION Y REPORTE
# ==============================================================================

def main():
    """Ejecuta el pipeline completo de calculo, auditoria y generacion de figuras."""
    print("--- Sistema de Equilibrio Estático en R3: Grúa Atirantada ---")
    print("Dimensiones del sistema: L = 5.0 m, d = 2.5 m, h = 4.0 m")
    print("Cargas aplicadas: Carga suspendida W = 8000 N, Peso propio W_boom = 1500 N\n")

    # 1. Instanciar sistema mecanico
    sistema = SistemaEquilibrio3D(
        L=5.0,
        d=2.5,
        h=4.0,
        W_mag=8000.0,
        F_lat_y=0.0,
        W_boom=1500.0
    )

    print("Parámetros geométricos y mecánicos del sistema:")
    print(f"  Longitud del brazo (L)          : {sistema.L:.2f} m")
    print(f"  Carga suspendida (W)            : {sistema.W_mag:.2f} N")
    print(f"  Peso propio del brazo (W_boom)  : {sistema.W_boom:.2f} N (aplicado en L/2)")
    print(f"  Anclajes en muro C1 y C2        : C1(0, {-sistema.d:.1f}, {sistema.h:.1f}) m | C2(0, {sistema.d:.1f}, {sistema.h:.1f}) m")
    print(f"  Longitud de los cables          : {sistema.len_c1:.4f} m")
    print(f"  Versor Cable 1 (u1)             : [{sistema.u1[0]:.4f}, {sistema.u1[1]:.4f}, {sistema.u1[2]:.4f}]")
    print(f"  Versor Cable 2 (u2)             : [{sistema.u2[0]:.4f}, {sistema.u2[1]:.4f}, {sistema.u2[2]:.4f}]\n")

    # 2. Deduccion Simbolica con SymPy
    print("Deducción simbólica exacta (SymPy):")
    sol_simb = sistema.resolver_simbolico()
    for var, expr in sol_simb.items():
        print(f"  {str(var):<6} = {sp.simplify(expr)}")
    print()

    # 3. Resolucion Numerica con NumPy
    print("Resolución numérica del sistema lineal 6x6 (NumPy):")
    res = sistema.resolver_numerico()

    print(f"  Determinante det(A)             : {res['det_A']:.4f}")
    print(f"  Rango de la matriz rank(A)      : {res['rank_A']} (Sistema isostático, solución única)")
    print(f"  Número de condición kappa(A)    : {res['cond_A']:.2f} (Estabilidad numérica)")
    print(f"  Residuo euclidiano ||Ax - b||   : {res['residuo']:.2e} N\n")

    print("Vector de incógnitas solución x = [R_Ox, R_Oy, R_Oz, M_Ox, T_1, T_2]^T:")
    nombres_incog = [
        ("R_Ox", "Reacción en Pivote O (Compresión X)", "N"),
        ("R_Oy", "Reacción en Pivote O (Lateral Y)", "N"),
        ("R_Oz", "Reacción en Pivote O (Vertical Z)", "N"),
        ("M_Ox", "Momento Reactivo Torsional (Eje X)", "N·m"),
        ("T_1 ", "Tensión en Cable Tensor 1", "N"),
        ("T_2 ", "Tensión en Cable Tensor 2", "N")
    ]
    for (tag, desc, unidad), val in zip(nombres_incog, res['vector_x']):
        print(f"  {tag:<6} ({desc:<36}): {val:12.2f} {unidad}")
    print()

    # 4. Auditoria de Equilibrio Estatico de Newton-Euler
    print("Auditoría de equilibrio estático de Newton-Euler:")
    audit = sistema.auditoria_equilibrio(res)
    for elem, (r, F, tau) in audit['Fuerzas'].items():
        str_F = f"[{F[0]:8.1f}, {F[1]:8.1f}, {F[2]:8.1f}] N"
        str_tau = f"[{tau[0]:8.1f}, {tau[1]:8.1f}, {tau[2]:8.1f}] N·m"
        print(f"  {elem:<30} | F = {str_F} | tau_O = {str_tau}")
    print()
    print(f"Suma total de fuerzas sum F        : [{audit['sum_F'][0]:.2e}, {audit['sum_F'][1]:.2e}, {audit['sum_F'][2]:.2e}] N")
    print(f"Norma euclidiana ||sum F||         : {audit['norm_sum_F']:.2e} N (Equilibrio traslacional confirmado)")
    print(f"Suma total de momentos sum tau_O   : [{audit['sum_tau'][0]:.2e}, {audit['sum_tau'][1]:.2e}, {audit['sum_tau'][2]:.2e}] N·m")
    print(f"Norma euclidiana ||sum tau_O||     : {audit['norm_sum_tau']:.2e} N·m (Equilibrio rotacional confirmado)\n")

    # 5. Generacion y Guardado de las 4 Figuras Individuales
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    figuras = [
        ("08_estructura_grua_3d.png", graficar_estructura_grua_3d, (sistema, res)),
        ("08_diagrama_cuerpo_libre_3d.png", graficar_diagrama_cuerpo_libre_3d, (sistema, res)),
        ("08_espacio_torques_equilibrio_3d.png", graficar_espacio_torques_3d, (sistema, res, audit)),
        ("08_analisis_sensibilidad_tensiones_2d.png", graficar_analisis_sensibilidad_2d, (sistema, res))
    ]

    print("Generando figuras independientes de alta definición (300 DPI):")
    for nombre_archivo, func_grafico, args in figuras:
        ruta_salida = os.path.join(directorio_actual, nombre_archivo)
        func_grafico(*args, ruta_guardado=ruta_salida)
        tamano_kb = os.path.getsize(ruta_salida) / 1024
        print(f"  Guardado: {nombre_archivo} ({tamano_kb:.1f} KB)")
    print()
    print("Simulación y validación estructural completadas con éxito.")


if __name__ == "__main__":
    main()
