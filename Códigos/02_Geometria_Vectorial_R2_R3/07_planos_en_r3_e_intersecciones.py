#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
MÓDULO 07: PLANOS EN R³, POSICIONES RELATIVAS, ÁNGULO DIEDRO E INTERSECCIONES
Asignatura: Álgebra Lineal (DCEX0007) — Universidad San Sebastián (USS)
Carrera: Ingeniería Civil Informática
Docente: Carol Asencio González
Estudiante: Moisés Amundarain Romero
Paleta Institucional: USS Blue (#00205B), USS Gold (#D4AF37)
================================================================================
Propósito del Módulo:
    Modelar, calcular analíticamente y visualizar en 3D:
    1. Ecuaciones del plano en R³:
       - Ecuación vectorial y punto-normal: n · (r - P0) = 0.
       - Ecuación cartesiana o general: Ax + By + Cz + D = 0.
       - Plano determinado por 3 puntos no colineales: n = (P2 - P1) x (P3 - P1).
    2. Posiciones relativas entre dos planos Pi1 y Pi2:
       - Coincidentes.
       - Paralelos no coincidentes (con cálculo de distancia entre planos).
       - Secantes (intersección en una recta común).
    3. Ángulo diedro entre planos:
       cos(theta) = |n1 · n2| / (||n1|| * ||n2||),  theta en [0, pi/2].
    4. Cálculo analítico exacto de la recta de intersección L = Pi1 ∩ Pi2:
       - Vector director: d = n1 x n2.
       - Punto de paso particular P_int mediante pivoteo numérico de máxima estabilidad.
    5. Distancia de un punto Q(x0, y0, z0) a un plano Pi:
       d(Q, Pi) = |Ax0 + By0 + Cz0 + D| / sqrt(A² + B² + C²).
    6. Renderizado 3D de alta fidelidad con Matplotlib:
       - Superficies translúcidas de ambos planos con la paleta USS.
       - Vectores normales n1 y n2 erigidos desde sus planos.
       - Recta de intersección destacada con trazo dorado/rojo.
       - Panel lateral con desglose analítico riguroso.
================================================================================
"""

import os
import sys
import numpy as np
import sympy as sp
import matplotlib
if os.environ.get('DISPLAY', '') == '' or os.environ.get('HEADLESS', '') == '1':
    matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ==============================================================================
# 🎨 PALETA DE COLORES INSTITUCIONAL USS
# ==============================================================================
USS_BLUE = '#00205B'          # Primario institucional (Plano Pi1)
USS_GOLD = '#D4AF37'          # Secundario dorado (Plano Pi2 / Recta Intersección)
USS_ACCENT_BLUE = '#1E88E5'   # Azul de realce (Normal n1)
USS_ACCENT_GREEN = '#27AE60'  # Verde de realce (Normal n2)
USS_ACCENT_RED = '#C0392B'    # Rojo de realce (Recta y punto de intersección)
USS_GRAY = '#7F8C8D'          # Gris auxiliar
USS_LIGHT_BG = '#F8F9FA'      # Fondo claro


# ==============================================================================
# 📐 CLASE Y MÉTODOS ANALÍTICOS DE PLANO EN R³
# ==============================================================================

class PlanoR3:
    """
    Representa un plano en el espacio tridimensional R³:
    Ax + By + Cz + D = 0  <=>  n · (r - P0) = 0
    donde n = (A, B, C) es el vector normal no nulo.
    """
    def __init__(self, A: float, B: float, C: float, D: float, nombre: str = "Pi"):
        self.A = float(A)
        self.B = float(B)
        self.C = float(C)
        self.D = float(D)
        self.nombre = nombre
        self.n = np.array([self.A, self.B, self.C], dtype=float)
        
        self.norma_n = float(np.linalg.norm(self.n))
        if np.isclose(self.norma_n, 0.0):
            raise ValueError(f"Los coeficientes normales (A, B, C) del plano {nombre} no pueden ser todos nulos.")

    @classmethod
    def desde_punto_y_normal(cls, p0: np.ndarray, normal: np.ndarray, nombre: str = "Pi"):
        """Construye un plano a partir de un punto P0 y un vector normal n."""
        p0 = np.array(p0, dtype=float)
        n = np.array(normal, dtype=float)
        A, B, C = n
        D = -float(np.dot(n, p0))
        return cls(A, B, C, D, nombre=nombre)

    @classmethod
    def desde_tres_puntos(cls, p1: np.ndarray, p2: np.ndarray, p3: np.ndarray, nombre: str = "Pi"):
        """
        Construye un plano que pasa por 3 puntos no colineales:
        n = (p2 - p1) x (p3 - p1).
        """
        v1 = np.array(p2, dtype=float) - np.array(p1, dtype=float)
        v2 = np.array(p3, dtype=float) - np.array(p1, dtype=float)
        normal = np.cross(v1, v2)
        if np.isclose(np.linalg.norm(normal), 0.0):
            raise ValueError("Los tres puntos seleccionados son colineales; no determinan un plano único.")
        return cls.desde_punto_y_normal(p1, normal, nombre=nombre)

    def punto_arbitrario(self) -> np.ndarray:
        """Encuentra un punto garantizado que pertenezca al plano."""
        idx_max = np.argmax(np.abs(self.n))
        p = np.zeros(3)
        p[idx_max] = -self.D / self.n[idx_max]
        return p

    def ecuacion_general(self) -> str:
        """Retorna la ecuación cartesiana general en formato LaTeX/texto."""
        parts = []
        coefs = [self.A, self.B, self.C]
        vars_name = ['x', 'y', 'z']
        for c, v in zip(coefs, vars_name):
            if not np.isclose(c, 0.0):
                if not parts:
                    parts.append(f"{c:g}{v}" if c != 1 else v)
                else:
                    sign = "+" if c > 0 else "-"
                    abs_c = abs(c)
                    coef_str = f"{abs_c:g}" if abs_c != 1 else ""
                    parts.append(f"{sign} {coef_str}{v}")
        
        eq_lhs = " ".join(parts) if parts else "0"
        sign_d = f"+ {self.D:g}" if self.D > 0 else (f"- {abs(self.D):g}" if self.D < 0 else "")
        return f"{self.nombre}: {eq_lhs} {sign_d} = 0"

    def evaluar_punto(self, punto: np.ndarray) -> float:
        """Evalúa Ax + By + Cz + D."""
        return float(np.dot(self.n, punto) + self.D)

    def distancia_punto(self, punto: np.ndarray) -> float:
        """
        Calcula la distancia euclidiana de un punto al plano:
        d(Q, Pi) = |Ax0 + By0 + Cz0 + D| / ||n||
        """
        return abs(self.evaluar_punto(punto)) / self.norma_n


# ==============================================================================
# 🔍 ANÁLISIS DE POSICIONES RELATIVAS E INTERSECCIÓN
# ==============================================================================

def angulo_diedro(p1: PlanoR3, p2: PlanoR3) -> tuple[float, float]:
    """
    Calcula el ángulo diedro agudo theta entre dos planos:
    cos(theta) = |n1 · n2| / (||n1|| * ||n2||)
    Retorna: (theta_rad, theta_deg)
    """
    cos_theta = abs(np.dot(p1.n, p2.n)) / (p1.norma_n * p2.norma_n)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    theta_rad = float(np.arccos(cos_theta))
    theta_deg = float(np.degrees(theta_rad))
    return theta_rad, theta_deg


def clasificar_e_intersecar_planos(p1: PlanoR3, p2: PlanoR3) -> dict:
    """
    Clasifica la posición relativa de p1 y p2 e interactúa calculando la recta común:
    1. Si n1 x n2 == 0:
       - Si D1 y D2 son múltiplos idénticos -> COINCIDENTES (distancia = 0).
       - Si no -> PARALELOS NO COINCIDENTES (distancia d = |D1 - k*D2| / ||n1||).
    2. Si n1 x n2 != 0:
       - SECANTES:
         * Vector director de la recta: d = n1 x n2.
         * Punto de paso particular P_int hallado por eliminación gaussiana con pivoteo.
    """
    cross_n = np.cross(p1.n, p2.n)
    norm_cross_n = float(np.linalg.norm(cross_n))
    theta_rad, theta_deg = angulo_diedro(p1, p2)
    
    # 1. Caso de planos paralelos
    if np.isclose(norm_cross_n, 0.0):
        # Encontrar factor de escala k tal que n2 = k * n1
        k = p2.norma_n / p1.norma_n
        # Ajustar signo del producto punto
        if np.dot(p1.n, p2.n) < 0:
            k = -k
        
        # Evaluar coincidencia
        d_proporcional = p2.D - k * p1.D
        if np.isclose(d_proporcional, 0.0):
            return {
                'tipo': 'COINCIDENTES',
                'descripcion': 'Los planos son coincidentes (representan el mismo plano en R³).',
                'angulo_deg': 0.0,
                'distancia': 0.0,
                'recta_interseccion': None
            }
        else:
            # Distancia entre planos paralelos: evaluar punto arbitrario de p2 en p1
            pt_arb = p2.punto_arbitrario()
            dist = p1.distancia_punto(pt_arb)
            return {
                'tipo': 'PARALELOS',
                'descripcion': 'Los planos son estrictamente paralelos no coincidentes.',
                'angulo_deg': 0.0,
                'distancia': float(dist),
                'recta_interseccion': None
            }
    
    # 2. Caso de planos secantes
    d_recta = cross_n
    
    # Hallar un punto particular P_int en la recta de intersección:
    # Fijar la variable que corresponda a la componente de mayor magnitud en d_recta
    # para garantizar un determinante no nulo y máxima estabilidad numérica (sin división por cero).
    idx_fijo = int(np.argmax(np.abs(d_recta)))
    
    # Submatriz 2x2 eliminando la columna fijada
    cols_libres = [i for i in range(3) if i != idx_fijo]
    M_sub = np.array([
        [p1.n[cols_libres[0]], p1.n[cols_libres[1]]],
        [p2.n[cols_libres[0]], p2.n[cols_libres[1]]]
    ], dtype=float)
    
    b_sub = np.array([-p1.D, -p2.D], dtype=float)
    sol_sub = np.linalg.solve(M_sub, b_sub)
    
    p_int = np.zeros(3)
    p_int[cols_libres[0]] = sol_sub[0]
    p_int[cols_libres[1]] = sol_sub[1]
    p_int[idx_fijo] = 0.0  # Variable fijada en cero
    
    # Comprobación estricta de pertenencia a ambos planos
    err1 = abs(p1.evaluar_punto(p_int))
    err2 = abs(p2.evaluar_punto(p_int))
    
    return {
        'tipo': 'SECANTES',
        'descripcion': 'Los planos son secantes y se intersectan en una recta infinita.',
        'angulo_deg': theta_deg,
        'angulo_rad': theta_rad,
        'vector_director': d_recta,
        'punto_paso': p_int,
        'error_pertenencia_p1': err1,
        'error_pertenencia_p2': err2,
        'recta_interseccion': {
            'punto': p_int,
            'director': d_recta
        }
    }


# ==============================================================================
# 📊 VISUALIZACIÓN GRÁFICA 3D CIENTÍFICA
# ==============================================================================

def visualizar_interseccion_planos_3d(p1: PlanoR3, p2: PlanoR3,
                                      guardar_ruta: str = "07_planos_en_r3_e_intersecciones.png") -> plt.Figure:
    """
    Renderiza un gráfico 3D científico de alta precisión con Matplotlib:
    1. Superficies translúcidas de ambos planos Pi1 y Pi2 con paleta USS.
    2. Vectores normales n1 (USS Accent Blue) y n2 (USS Accent Green).
    3. Recta de intersección destacada con trazo dorado/rojo continuo.
    4. Punto de paso particular P_int.
    5. Panel lateral con desglose analítico formal y ángulo diedro.
    """
    res = clasificar_e_intersecar_planos(p1, p2)
    
    fig = plt.figure(figsize=(16, 7), facecolor='white')
    
    # --------------------------------------------------------------------------
    # SUBPLOT 1: Renderizado 3D de Planos e Intersección
    # --------------------------------------------------------------------------
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1.set_facecolor('white')
    ax1.set_title("1. Planos en R³ y Recta de Intersección\n" +
                  r"$\mathbf{d} = \mathbf{n}_1 \times \mathbf{n}_2 \quad \text{y} \quad \theta_{\text{diedro}} = \arccos\left(\frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{||\mathbf{n}_1|| ||\mathbf{n}_2||}\right)$",
                  fontsize=12, fontweight='bold', color=USS_BLUE, pad=15)
    
    # Generar cuadrícula XY de referencia centrada
    centro = res['punto_paso'] if res['tipo'] == 'SECANTES' else p1.punto_arbitrario()
    x_range = np.linspace(centro[0] - 3.5, centro[0] + 3.5, 20)
    y_range = np.linspace(centro[1] - 3.5, centro[1] + 3.5, 20)
    X, Y = np.meshgrid(x_range, y_range)
    
    # Función para evaluar z en un plano, o parametrizar según componente dominante
    def graficar_malla_plano(plano, color_surf, label_name):
        # Si C no es cero, despejar Z
        if not np.isclose(plano.C, 0.0):
            Z = (-plano.A * X - plano.B * Y - plano.D) / plano.C
            surf = ax1.plot_surface(X, Y, Z, color=color_surf, alpha=0.35, edgecolor='none')
        elif not np.isclose(plano.B, 0.0):
            # Si C es 0 pero B no, despejar Y a partir de X y Z
            z_r = np.linspace(centro[2] - 3.5, centro[2] + 3.5, 20)
            X_m, Z_m = np.meshgrid(x_range, z_r)
            Y_m = (-plano.A * X_m - plano.D) / plano.B
            surf = ax1.plot_surface(X_m, Y_m, Z_m, color=color_surf, alpha=0.35, edgecolor='none')
        else:
            # Plano vertical x = constante
            y_r = np.linspace(centro[1] - 3.5, centro[1] + 3.5, 20)
            z_r = np.linspace(centro[2] - 3.5, centro[2] + 3.5, 20)
            Y_m, Z_m = np.meshgrid(y_r, z_r)
            X_m = np.full_like(Y_m, -plano.D / plano.A)
            surf = ax1.plot_surface(X_m, Y_m, Z_m, color=color_surf, alpha=0.35, edgecolor='none')
        return surf
    
    graficar_malla_plano(p1, USS_BLUE, p1.nombre)
    graficar_malla_plano(p2, USS_GOLD, p2.nombre)
    
    # Graficar rectas y normales si son secantes
    if res['tipo'] == 'SECANTES':
        p_int = res['punto_paso']
        d_dir = res['vector_director']
        
        # Recta de intersección
        t_span = np.linspace(-3.5, 3.5, 60)
        pts_linea = np.array([p_int + t * d_dir for t in t_span])
        ax1.plot(pts_linea[:, 0], pts_linea[:, 1], pts_linea[:, 2],
                 color=USS_ACCENT_RED, linewidth=4.0,
                 label=r"Recta Intersección $L = \Pi_1 \cap \Pi_2$")
        
        # Punto particular P_int
        ax1.scatter([p_int[0]], [p_int[1]], [p_int[2]],
                    color=USS_ACCENT_RED, s=70, edgecolors='black',
                    label=f"P0 {tuple(np.round(p_int, 2))}")
        
        # Vectores normales n1 y n2 erigidos desde P_int
        n1_unit = p1.n / p1.norma_n
        n2_unit = p2.n / p2.norma_n
        ax1.quiver(p_int[0], p_int[1], p_int[2], n1_unit[0]*1.8, n1_unit[1]*1.8, n1_unit[2]*1.8,
                   color=USS_ACCENT_BLUE, linewidth=3.0, arrow_length_ratio=0.15,
                   label=r"$\mathbf{n}_1$ (normal $\Pi_1$)")
        ax1.quiver(p_int[0], p_int[1], p_int[2], n2_unit[0]*1.8, n2_unit[1]*1.8, n2_unit[2]*1.8,
                   color=USS_ACCENT_GREEN, linewidth=3.0, arrow_length_ratio=0.15,
                   label=r"$\mathbf{n}_2$ (normal $\Pi_2$)")
    
    ax1.set_xlabel('Eje X', fontweight='bold', color=USS_BLUE)
    ax1.set_ylabel('Eje Y', fontweight='bold', color=USS_BLUE)
    ax1.set_zlabel('Eje Z', fontweight='bold', color=USS_BLUE)
    ax1.legend(loc='upper left', fontsize=8, framealpha=0.9)
    ax1.view_init(elev=22, azim=40)
    
    # --------------------------------------------------------------------------
    # SUBPLOT 2: Panel Teórico y Analítico
    # --------------------------------------------------------------------------
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_facecolor(USS_LIGHT_BG)
    ax2.set_title("2. Ecuaciones Cartesianas y Métricas de Intersección\n" +
                  f"Diagnóstico: {res['tipo']}",
                  fontsize=12, fontweight='bold', color=USS_BLUE, pad=15)
    
    info_analitica = (
        r"$\mathbf{ECUACIONES\ DE\ LOS\ PLANOS:}$" + "\n"
        f" • {p1.ecuacion_general()}\n"
        f"   Vector Normal n1 = {p1.n},  ||n1|| = {p1.norma_n:.4f}\n\n"
        f" • {p2.ecuacion_general()}\n"
        f"   Vector Normal n2 = {p2.n},  ||n2|| = {p2.norma_n:.4f}\n\n"
        r"$\mathbf{RELACIÓN\ GEOMÉTRICA:}$" + "\n"
        f" • Producto punto n1 · n2 = {np.dot(p1.n, p2.n):.4f}\n"
        f" • Ángulo Diedro theta = {res['angulo_deg']:.2f}°\n"
        f" • Diagnóstico: {res['descripcion']}\n\n"
    )
    
    if res['tipo'] == 'SECANTES':
        d_vec = res['vector_director']
        p_pt = res['punto_paso']
        info_analitica += (
            r"$\mathbf{RECTA\ DE\ INTERSECCIÓN\ } L = \Pi_1 \cap \Pi_2:$" + "\n"
            f" • Vector director d = n1 x n2 = {d_vec}\n"
            f" • Punto de paso P0 = ({p_pt[0]:.4f}, {p_pt[1]:.4f}, {p_pt[2]:.4f})\n"
            f" • Ecuación Vectorial: (x, y, z) = P0 + t * {d_vec}\n"
            f" • Ecuaciones Paramétricas:\n"
            f"     x(t) = {p_pt[0]:.2f} + ({d_vec[0]:g})t\n"
            f"     y(t) = {p_pt[1]:.2f} + ({d_vec[1]:g})t\n"
            f"     z(t) = {p_pt[2]:.2f} + ({d_vec[2]:g})t\n\n"
            r"$\mathbf{VERIFICACIÓN\ DE\ CONSISTENCIA:}$" + "\n"
            f" • Error en Plano Pi1: {res['error_pertenencia_p1']:.2e}\n"
            f" • Error en Plano Pi2: {res['error_pertenencia_p2']:.2e}\n"
            f" • d · n1 = {np.dot(d_vec, p1.n):.2e} (Ortogonal a n1)\n"
            f" • d · n2 = {np.dot(d_vec, p2.n):.2e} (Ortogonal a n2)"
        )
    elif res['tipo'] == 'PARALELOS':
        info_analitica += (
            r"$\mathbf{SEPARACIÓN\ ENTRE\ PLANOS:}$" + "\n"
            f" • Distancia entre planos d(Pi1, Pi2) = {res['distancia']:.4f} [u]\n"
        )
    
    ax2.text(0.04, 0.95, info_analitica, transform=ax2.transAxes,
             fontsize=9.5, verticalalignment='top', fontfamily='monospace',
             bbox=dict(boxstyle='round,pad=0.8', facecolor='white',
                       edgecolor=USS_BLUE, linewidth=2.0, alpha=0.95))
    
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig(guardar_ruta, dpi=300, bbox_inches='tight')
    print(f" [Gráfico Guardado]: {guardar_ruta}")
    
    if os.environ.get('DISPLAY', '') != '' and os.environ.get('HEADLESS', '') != '1':
        plt.show()
    
    return fig


# ==============================================================================
# 🚀 EJECUCIÓN DEMOSTRATIVA
# ==============================================================================

def ejecucion_demostrativa():
    print("=" * 80)
    print(" UNIVERSIDAD SAN SEBASTIÁN — DEPARTAMENTO DE CIENCIAS EXACTAS")
    print(" MÓDULO 07: PLANOS EN R³, POSICIONES RELATIVAS E INTERSECCIONES")
    print("=" * 80)
    
    # --------------------------------------------------------------------------
    # 1. Definición de dos planos secantes
    # Pi1: 2x - y + z - 4 = 0
    # Pi2: x + 2y - z + 1 = 0
    # --------------------------------------------------------------------------
    print("\n--- 1. DEFINICIÓN DE PLANOS Y ECUACIONES CARTESIANAS ---")
    p1 = PlanoR3(A=2.0, B=-1.0, C=1.0, D=-4.0, nombre="Pi1")
    p2 = PlanoR3(A=1.0, B=2.0, C=-1.0, D=1.0, nombre="Pi2")
    
    print(p1.ecuacion_general())
    print(p2.ecuacion_general())
    
    # --------------------------------------------------------------------------
    # 2. Análisis Analítico e Intersección
    # --------------------------------------------------------------------------
    print("\n--- 2. ANÁLISIS DE INTERSECCIÓN Y ÁNGULO DIEDRO ---")
    resultado = clasificar_e_intersecar_planos(p1, p2)
    print(f"Posición Relativa: {resultado['tipo']}")
    print(f"Descripción: {resultado['descripcion']}")
    print(f"Ángulo Diedro theta: {resultado['angulo_deg']:.2f}°")
    
    if resultado['tipo'] == 'SECANTES':
        d = resultado['vector_director']
        p0 = resultado['punto_paso']
        print(f"Vector Director de la recta: {d}")
        print(f"Punto de paso particular P0: {p0}")
        print(f"Verificación ortogonalidad d · n1: {np.dot(d, p1.n):.2e}")
        print(f"Verificación ortogonalidad d · n2: {np.dot(d, p2.n):.2e}")
        print(f"Evaluación P0 en Pi1: {p1.evaluar_punto(p0):.2e}")
        print(f"Evaluación P0 en Pi2: {p2.evaluar_punto(p0):.2e}")
    
    # --------------------------------------------------------------------------
    # 3. Plano por 3 puntos y Distancia Punto-Plano
    # --------------------------------------------------------------------------
    print("\n--- 3. PLANO POR 3 PUNTOS Y DISTANCIA PUNTO-PLANO ---")
    ptA = np.array([1.0, 0.0, 2.0])
    ptB = np.array([0.0, 3.0, 1.0])
    ptC = np.array([2.0, 1.0, 0.0])
    p3 = PlanoR3.desde_tres_puntos(ptA, ptB, ptC, nombre="Pi3")
    print(f"Plano generado por A, B, C => {p3.ecuacion_general()}")
    
    punto_q = np.array([4.0, -1.0, 5.0])
    dist_q = p3.distancia_punto(punto_q)
    print(f"Distancia de Q{tuple(punto_q)} al plano Pi3: {dist_q:.4f}")
    
    # --------------------------------------------------------------------------
    # 4. Generación Gráfica 3D
    # --------------------------------------------------------------------------
    print("\n--- 4. GENERACIÓN DE FIGURA MATPLOTLIB 3D ---")
    out_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "07_planos_en_r3_e_intersecciones.png")
    visualizar_interseccion_planos_3d(p1, p2, guardar_ruta=out_img)
    
    print("=" * 80)
    print(" MÓDULO 07 COMPLETADO CON ÉXITO")
    print("=" * 80)


if __name__ == '__main__':
    ejecucion_demostrativa()
