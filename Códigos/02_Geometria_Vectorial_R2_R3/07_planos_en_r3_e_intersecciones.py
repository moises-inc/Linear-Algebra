#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modulo 07: Planos en R3, Posiciones Relativas, Angulo Diedro e Intersecciones
Asignatura: Algebra Lineal (DCEX0007) - Universidad San Sebastian (USS)
Carrera: Ingenieria Civil Informatica
Docente: Carol Asencio Gonzalez
Estudiante: Moises Amundarain Romero
Paleta Institucional: USS Blue (#00205B), USS Gold (#D4AF37)

Proposito:
    1. Ecuaciones punto-normal y cartesiana general del plano: Ax + By + Cz + D = 0.
    2. Determinacion de plano a partir de tres puntos no colineales.
    3. Posiciones relativas entre planos: coincidentes, paralelos y secantes.
    4. Angulo diedro agudo: cos(theta) = |n1 . n2| / (||n1|| * ||n2||).
    5. Calculo analitico de la recta de interseccion L = Pi1 cap Pi2 con pivoteo numerico.
    6. Distancia minima de un punto a un plano y proyeccion ortogonal.
    7. Generacion de figuras 3D cientificas individuales con alpha=0.25 y paleta USS.
"""

import os
import sys
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Paleta Institucional USS
USS_BLUE = '#00205B'
USS_GOLD = '#D4AF37'
USS_ACCENT_BLUE = '#1E88E5'
USS_ACCENT_GREEN = '#27AE60'
USS_ACCENT_RED = '#C0392B'
USS_GRAY = '#7F8C8D'
USS_LIGHT_BG = '#F8F9FA'


class PlanoR3:
    """
    Representa un plano en R3 mediante la ecuacion cartesiana general:
    Ax + By + Cz + D = 0
    con vector normal n = (A, B, C) no nulo.
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
            raise ValueError(f"El vector normal del plano {nombre} no puede ser nulo.")

    @classmethod
    def desde_punto_y_normal(cls, p0: np.ndarray, normal: np.ndarray, nombre: str = "Pi"):
        """Construye un plano a partir de un punto P0 y vector normal n."""
        p0 = np.array(p0, dtype=float)
        n = np.array(normal, dtype=float)
        A, B, C = n
        D = -float(np.dot(n, p0))
        return cls(A, B, C, D, nombre=nombre)

    @classmethod
    def desde_tres_puntos(cls, p1: np.ndarray, p2: np.ndarray, p3: np.ndarray, nombre: str = "Pi"):
        """Construye el plano determinado por 3 puntos no colineales: n = (p2-p1) x (p3-p1)."""
        v1 = np.array(p2, dtype=float) - np.array(p1, dtype=float)
        v2 = np.array(p3, dtype=float) - np.array(p1, dtype=float)
        normal = np.cross(v1, v2)
        if np.isclose(np.linalg.norm(normal), 0.0):
            raise ValueError("Los tres puntos son colineales; no determinan un plano unico.")
        return cls.desde_punto_y_normal(p1, normal, nombre=nombre)

    def punto_arbitrario(self) -> np.ndarray:
        """Determina un punto garantizado sobre el plano mediante componente dominante."""
        idx_max = int(np.argmax(np.abs(self.n)))
        p = np.zeros(3)
        p[idx_max] = -self.D / self.n[idx_max]
        return p

    def ecuacion_general(self) -> str:
        """Retorna la ecuacion cartesiana en formato texto."""
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
        """Evalua Ax + By + Cz + D."""
        return float(np.dot(self.n, punto) + self.D)

    def distancia_punto(self, punto: np.ndarray) -> float:
        """Calcula la distancia perpendicular d = |Ax0 + By0 + Cz0 + D| / ||n||."""
        return abs(self.evaluar_punto(punto)) / self.norma_n

    def proyeccion_punto(self, punto: np.ndarray) -> np.ndarray:
        """Calcula la proyeccion ortogonal del punto sobre el plano."""
        t = -self.evaluar_punto(punto) / (self.norma_n**2)
        return punto + t * self.n


def angulo_diedro(p1: PlanoR3, p2: PlanoR3) -> tuple[float, float]:
    """Calcula el angulo diedro agudo theta entre p1 y p2: cos(theta) = |n1 . n2| / (||n1|| * ||n2||)."""
    cos_theta = abs(float(np.dot(p1.n, p2.n))) / (p1.norma_n * p2.norma_n)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    theta_rad = float(np.arccos(cos_theta))
    theta_deg = float(np.degrees(theta_rad))
    return theta_rad, theta_deg


def clasificar_e_intersecar_planos(p1: PlanoR3, p2: PlanoR3) -> dict:
    """Clasifica la posicion de p1 y p2 y calcula la recta de interseccion si son secantes."""
    cross_n = np.cross(p1.n, p2.n)
    norm_cross_n = float(np.linalg.norm(cross_n))
    theta_rad, theta_deg = angulo_diedro(p1, p2)
    
    if np.isclose(norm_cross_n, 0.0):
        k = p2.norma_n / p1.norma_n
        if np.dot(p1.n, p2.n) < 0:
            k = -k
        d_prop = p2.D - k * p1.D
        if np.isclose(d_prop, 0.0):
            return {'tipo': 'COINCIDENTES', 'angulo_deg': 0.0, 'distancia': 0.0}
        else:
            pt_arb = p2.punto_arbitrario()
            return {'tipo': 'PARALELOS', 'angulo_deg': 0.0, 'distancia': float(p1.distancia_punto(pt_arb))}
    
    # Secantes: calcular director y punto de paso con pivoteo
    d_recta = cross_n
    idx_fijo = int(np.argmax(np.abs(d_recta)))
    cols = [i for i in range(3) if i != idx_fijo]
    
    M_sub = np.array([
        [p1.n[cols[0]], p1.n[cols[1]]],
        [p2.n[cols[0]], p2.n[cols[1]]]
    ], dtype=float)
    b_sub = np.array([-p1.D, -p2.D], dtype=float)
    sol_sub = np.linalg.solve(M_sub, b_sub)
    
    p_int = np.zeros(3)
    p_int[cols[0]] = sol_sub[0]
    p_int[cols[1]] = sol_sub[1]
    p_int[idx_fijo] = 0.0
    
    return {
        'tipo': 'SECANTES',
        'angulo_deg': theta_deg,
        'angulo_rad': theta_rad,
        'vector_director': d_recta,
        'punto_paso': p_int,
        'err_p1': abs(p1.evaluar_punto(p_int)),
        'err_p2': abs(p2.evaluar_punto(p_int))
    }


def generar_grafico_interseccion_planos_3d(p1: PlanoR3, p2: PlanoR3,
                                            guardar_ruta: str = "07_planos_secantes_e_interseccion_3d.png") -> plt.Figure:
    """
    Figura 3D individual:
    Dos planos secantes con alpha=0.25, vectores normales n1 y n2, y recta de interseccion L en USS_GOLD.
    """
    res = clasificar_e_intersecar_planos(p1, p2)
    fig = plt.figure(figsize=(9, 8), facecolor='white')
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_facecolor('white')
    
    ang_val = res.get('angulo_deg', 0.0)
    ax.set_title(f"Planos Secantes en R3: L = Pi1 cap Pi2 (Angulo Diedro = {ang_val:.1f} deg)",
                 fontsize=12.5, fontweight='bold', color=USS_BLUE, pad=16)
    
    centro = res['punto_paso'] if res['tipo'] == 'SECANTES' else p1.punto_arbitrario()
    
    # Cuadricula para planos
    xr = np.linspace(centro[0] - 3.2, centro[0] + 3.2, 16)
    yr = np.linspace(centro[1] - 3.2, centro[1] + 3.2, 16)
    X, Y = np.meshgrid(xr, yr)
    
    def graficar_plano_malla(plano, color_surf, alpha_val=0.25):
        if not np.isclose(plano.C, 0.0):
            Z = (-plano.A * X - plano.B * Y - plano.D) / plano.C
            return ax.plot_surface(X, Y, Z, color=color_surf, alpha=alpha_val, edgecolor='none')
        elif not np.isclose(plano.B, 0.0):
            zr = np.linspace(centro[2] - 3.2, centro[2] + 3.2, 16)
            Xm, Zm = np.meshgrid(xr, zr)
            Ym = (-plano.A * Xm - plano.D) / plano.B
            return ax.plot_surface(Xm, Ym, Zm, color=color_surf, alpha=alpha_val, edgecolor='none')
        else:
            yr_loc = np.linspace(centro[1] - 3.2, centro[1] + 3.2, 16)
            zr_loc = np.linspace(centro[2] - 3.2, centro[2] + 3.2, 16)
            Ym, Zm = np.meshgrid(yr_loc, zr_loc)
            Xm = np.full_like(Ym, -plano.D / plano.A)
            return ax.plot_surface(Xm, Ym, Zm, color=color_surf, alpha=alpha_val, edgecolor='none')
    
    # Superficies de planos con alpha=0.25
    graficar_plano_malla(p1, USS_BLUE, alpha_val=0.25)
    graficar_plano_malla(p2, USS_ACCENT_BLUE, alpha_val=0.25)
    
    if res['tipo'] == 'SECANTES':
        p0 = res['punto_paso']
        d = res['vector_director']
        
        # Recta de interseccion L en USS_GOLD
        t_span = np.linspace(-3.2, 3.2, 60)
        pts_linea = np.array([p0 + t * d for t in t_span])
        ax.plot(pts_linea[:, 0], pts_linea[:, 1], pts_linea[:, 2],
                color=USS_GOLD, linewidth=3.8, label="Recta de interseccion L (Pi1 cap Pi2)")
        
        # Punto de paso
        ax.scatter([p0[0]], [p0[1]], [p0[2]], color=USS_GOLD, s=70, edgecolors='black', label="P0 (en recta L)")
        
        # Vectores normales erigidos desde P0
        n1_u = p1.n / p1.norma_n
        n2_u = p2.n / p2.norma_n
        ax.quiver(p0[0], p0[1], p0[2], n1_u[0]*1.8, n1_u[1]*1.8, n1_u[2]*1.8,
                  color=USS_BLUE, linewidth=3.0, arrow_length_ratio=0.14, label="n1 (normal Pi1)")
        ax.quiver(p0[0], p0[1], p0[2], n2_u[0]*1.8, n2_u[1]*1.8, n2_u[2]*1.8,
                  color=USS_ACCENT_GREEN, linewidth=3.0, arrow_length_ratio=0.14, label="n2 (normal Pi2)")
    
    ax.set_xlabel("Eje X", fontweight='bold', color=USS_BLUE)
    ax.set_ylabel("Eje Y", fontweight='bold', color=USS_BLUE)
    ax.set_zlabel("Eje Z", fontweight='bold', color=USS_BLUE)
    ax.legend(loc='upper left', fontsize=8.5, framealpha=0.95)
    ax.view_init(elev=25, azim=-50)
    
    plt.tight_layout()
    plt.savefig(guardar_ruta, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return fig


def generar_grafico_distancia_punto_plano_3d(plano: PlanoR3, punto: np.ndarray,
                                              guardar_ruta: str = "07_distancia_punto_plano_3d.png") -> plt.Figure:
    """
    Figura 3D individual:
    Plano Pi con alpha=0.25, punto P en el espacio, proyeccion ortogonal P_proj
    y segmento de minima distancia resaltado en USS_GOLD.
    """
    fig = plt.figure(figsize=(9, 8), facecolor='white')
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_facecolor('white')
    
    p_proj = plano.proyeccion_punto(punto)
    dist_val = plano.distancia_punto(punto)
    
    ax.set_title(f"Distancia Minima de un Punto a un Plano en R3: d = {dist_val:.4f} [u]",
                 fontsize=12.5, fontweight='bold', color=USS_BLUE, pad=16)
    
    # Centro en la proyeccion
    xr = np.linspace(p_proj[0] - 3.5, p_proj[0] + 3.5, 16)
    yr = np.linspace(p_proj[1] - 3.5, p_proj[1] + 3.5, 16)
    X, Y = np.meshgrid(xr, yr)
    
    if not np.isclose(plano.C, 0.0):
        Z = (-plano.A * X - plano.B * Y - plano.D) / plano.C
        ax.plot_surface(X, Y, Z, color=USS_BLUE, alpha=0.25, edgecolor='none')
    elif not np.isclose(plano.B, 0.0):
        zr = np.linspace(p_proj[2] - 3.5, p_proj[2] + 3.5, 16)
        Xm, Zm = np.meshgrid(xr, zr)
        Ym = (-plano.A * Xm - plano.D) / plano.B
        ax.plot_surface(Xm, Ym, Zm, color=USS_BLUE, alpha=0.25, edgecolor='none')
    else:
        yr_loc = np.linspace(p_proj[1] - 3.5, p_proj[1] + 3.5, 16)
        zr_loc = np.linspace(p_proj[2] - 3.5, p_proj[2] + 3.5, 16)
        Ym, Zm = np.meshgrid(yr_loc, zr_loc)
        Xm = np.full_like(Ym, -plano.D / plano.A)
        ax.plot_surface(Xm, Ym, Zm, color=USS_BLUE, alpha=0.25, edgecolor='none')
    
    # Punto P en el espacio
    ax.scatter([punto[0]], [punto[1]], [punto[2]], color=USS_ACCENT_RED, s=80,
               edgecolors='black', linewidths=1.2, label=f"P ({punto[0]:g}, {punto[1]:g}, {punto[2]:g})")
    
    # Proyeccion ortogonal P_proj
    ax.scatter([p_proj[0]], [p_proj[1]], [p_proj[2]], color=USS_BLUE, s=80,
               edgecolors='black', linewidths=1.2, label=f"P_proj ({p_proj[0]:.2f}, {p_proj[1]:.2f}, {p_proj[2]:.2f})")
    
    # Segmento de minima distancia en USS_GOLD
    ax.plot([punto[0], p_proj[0]], [punto[1], p_proj[1]], [punto[2], p_proj[2]],
            color=USS_GOLD, linewidth=3.5, linestyle='--', label=f"Distancia minima d = {dist_val:.4f}")
    
    # Vector normal erigido desde P_proj
    n_unit = plano.n / plano.norma_n
    ax.quiver(p_proj[0], p_proj[1], p_proj[2], n_unit[0]*1.8, n_unit[1]*1.8, n_unit[2]*1.8,
              color=USS_ACCENT_GREEN, linewidth=2.8, arrow_length_ratio=0.15, label="Normal n al plano")
    
    ax.set_xlabel("Eje X", fontweight='bold', color=USS_BLUE)
    ax.set_ylabel("Eje Y", fontweight='bold', color=USS_BLUE)
    ax.set_zlabel("Eje Z", fontweight='bold', color=USS_BLUE)
    ax.legend(loc='upper left', fontsize=8.5, framealpha=0.95)
    ax.view_init(elev=25, azim=-50)
    
    plt.tight_layout()
    plt.savefig(guardar_ruta, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return fig


def ejecucion_demostrativa():
    print("Modulo 07: Planos en R3, Posiciones Relativas e Intersecciones")
    print("Universidad San Sebastian - Departamento de Ciencias Exactas")
    
    # 1. Definicion de dos planos secantes
    print("\n--- 1. ECUACIONES CARTESIANAS DE LOS PLANOS ---")
    p1 = PlanoR3(A=2.0, B=-1.0, C=1.0, D=-4.0, nombre="Pi1")
    p2 = PlanoR3(A=1.0, B=2.0, C=-1.0, D=1.0, nombre="Pi2")
    
    print(p1.ecuacion_general())
    print(p2.ecuacion_general())
    
    # 2. Analisis de interseccion y angulo diedro
    print("\n--- 2. ANALISIS DE INTERSECCION Y ANGULO DIEDRO ---")
    res = clasificar_e_intersecar_planos(p1, p2)
    print(f"Posicion Relativa: {res['tipo']}")
    print(f"Angulo Diedro theta: {res['angulo_deg']:.2f} deg ({res['angulo_rad']:.4f} rad)")
    
    if res['tipo'] == 'SECANTES':
        d = res['vector_director']
        p0 = res['punto_paso']
        print(f"Vector Director de la recta d = {d}")
        print(f"Punto de paso particular P0 = {p0}")
        print(f"Verificacion pertenencia P0 a Pi1: {res['err_p1']:.2e}")
        print(f"Verificacion pertenencia P0 a Pi2: {res['err_p2']:.2e}")
        print(f"Ortogonalidad d . n1: {np.dot(d, p1.n):.2e}")
        print(f"Ortogonalidad d . n2: {np.dot(d, p2.n):.2e}")
        assert res['err_p1'] < 1e-12 and res['err_p2'] < 1e-12, "Error en pertenencia de P0 a los planos."
    
    # 3. Plano por tres puntos y distancia punto-plano
    print("\n--- 3. PLANO POR TRES PUNTOS Y DISTANCIA PUNTO-PLANO ---")
    ptA = np.array([1.0, 0.0, 2.0])
    ptB = np.array([0.0, 3.0, 1.0])
    ptC = np.array([2.0, 1.0, 0.0])
    p3 = PlanoR3.desde_tres_puntos(ptA, ptB, ptC, nombre="Pi3")
    print(f"Plano generado por A, B, C => {p3.ecuacion_general()}")
    
    punto_q = np.array([4.0, -1.0, 5.0])
    dist_q = p3.distancia_punto(punto_q)
    proj_q = p3.proyeccion_punto(punto_q)
    print(f"Punto Q en el espacio: {punto_q}")
    print(f"Proyeccion ortogonal Q_proj: {proj_q}")
    print(f"Distancia minima d(Q, Pi3) = {dist_q:.4f} [u]")
    print(f"Verificacion pertenencia Q_proj a Pi3: {p3.evaluar_punto(proj_q):.2e}")
    
    # 4. Generacion de figuras 3D cientificas individuales
    print("\n--- 4. GENERACION DE FIGURAS CIENTIFICAS 3D INDIVIDUALES ---")
    dir_base = os.path.dirname(os.path.abspath(__file__))
    ruta_sec = os.path.join(dir_base, "07_planos_secantes_e_interseccion_3d.png")
    ruta_dist = os.path.join(dir_base, "07_distancia_punto_plano_3d.png")
    
    generar_grafico_interseccion_planos_3d(p1, p2, guardar_ruta=ruta_sec)
    print(f"Grafico 1 guardado: {ruta_sec}")
    
    generar_grafico_distancia_punto_plano_3d(p3, punto_q, guardar_ruta=ruta_dist)
    print(f"Grafico 2 guardado: {ruta_dist}")
    
    print("\nModulo 07 ejecutado con exito.")


if __name__ == '__main__':
    ejecucion_demostrativa()
