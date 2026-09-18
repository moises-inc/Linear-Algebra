#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modulo 06: Rectas en R3, Posiciones Relativas y Rectas Alabeadas
Asignatura: Algebra Lineal (DCEX0007) - Universidad San Sebastian (USS)
Carrera: Ingenieria Civil Informatica
Docente: Carol Asencio Gonzalez
Estudiante: Moises Amundarain Romero
Paleta Institucional: USS Blue (#00205B), USS Gold (#D4AF37)

Proposito:
    1. Formas analiticas de la recta en R3: vectorial, parametrica y simetrica.
    2. Clasificacion de posiciones relativas: coincidentes, paralelas, secantes y alabeadas.
    3. Distancia minima entre rectas alabeadas: d = |(P2 - P1) . (d1 x d2)| / ||d1 x d2||.
    4. Determinacion exacta de los puntos Q1 en L1 y Q2 en L2 mediante sistema de Gram 2x2.
    5. Verificacion rigurosa de ortogonalidad del segmento perpendicular comun.
    6. Visualizacion 3D cientifica individual con planos paralelos contenedores (alpha=0.20).
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


class RectaR3:
    """Representa una recta en R3 definida por r(t) = P0 + t * d."""
    def __init__(self, punto: np.ndarray, director: np.ndarray, nombre: str = "L"):
        self.p0 = np.array(punto, dtype=float)
        self.d = np.array(director, dtype=float)
        self.nombre = nombre
        
        norm_d = np.linalg.norm(self.d)
        if np.isclose(norm_d, 0.0):
            raise ValueError(f"El vector director de la recta {nombre} no puede ser nulo.")
    
    def punto_en_parametro(self, t: float) -> np.ndarray:
        """Calcula r(t) = P0 + t * d."""
        return self.p0 + t * self.d

    def ecuacion_vectorial(self) -> str:
        """Retorna la ecuacion vectorial."""
        return f"{self.nombre}: (x, y, z) = ({self.p0[0]:g}, {self.p0[1]:g}, {self.p0[2]:g}) + t*({self.d[0]:g}, {self.d[1]:g}, {self.d[2]:g})"

    def ecuaciones_parametricas(self) -> str:
        """Retorna las ecuaciones parametricas escalares."""
        p, d = self.p0, self.d
        sx = f"+ {d[0]:g}t" if d[0] >= 0 else f"- {abs(d[0]):g}t"
        sy = f"+ {d[1]:g}t" if d[1] >= 0 else f"- {abs(d[1]):g}t"
        sz = f"+ {d[2]:g}t" if d[2] >= 0 else f"- {abs(d[2]):g}t"
        return f"{self.nombre} => x = {p[0]:g} {sx},  y = {p[1]:g} {sy},  z = {p[2]:g} {sz}"

    def ecuaciones_simetricas(self) -> str:
        """Retorna las ecuaciones simetricas."""
        p, d = self.p0, self.d
        partes = []
        nombres = ['x', 'y', 'z']
        fijas = []
        for i in range(3):
            if np.isclose(d[i], 0.0):
                fijas.append(f"{nombres[i]} = {p[i]:g}")
            else:
                p_str = f" - {p[i]:g}" if p[i] > 0 else (f" + {abs(p[i]):g}" if p[i] < 0 else "")
                partes.append(f"({nombres[i]}{p_str})/{d[i]:g}")
        sim_str = " = ".join(partes) if partes else ""
        if fijas:
            sim_str += (" ; " if sim_str else "") + ", ".join(fijas)
        return f"{self.nombre}: {sim_str}"


def calcular_puntos_mas_cercanos_alabeadas(r1: RectaR3, r2: RectaR3) -> tuple[np.ndarray, np.ndarray, float, float]:
    """
    Calcula los puntos Q1 en L1 y Q2 en L2 resolviendo el sistema lineal de Gram 2x2:
    (Q2 - Q1) . d1 = 0
    (Q2 - Q1) . d2 = 0
    """
    p1, d1 = r1.p0, r1.d
    p2, d2 = r2.p0, r2.d
    delta_p = p2 - p1
    
    d1_dot_d1 = float(np.dot(d1, d1))
    d2_dot_d2 = float(np.dot(d2, d2))
    d1_dot_d2 = float(np.dot(d1, d2))
    
    M = np.array([
        [d1_dot_d1, -d1_dot_d2],
        [d1_dot_d2, -d2_dot_d2]
    ], dtype=float)
    
    b = np.array([
        float(np.dot(delta_p, d1)),
        float(np.dot(delta_p, d2))
    ], dtype=float)
    
    sol = np.linalg.solve(M, b)
    t_opt = float(sol[0])
    s_opt = float(sol[1])
    
    q1 = r1.punto_en_parametro(t_opt)
    q2 = r2.punto_en_parametro(s_opt)
    return q1, q2, t_opt, s_opt


def clasificar_posicion_relativa(r1: RectaR3, r2: RectaR3) -> dict:
    """Clasifica la posicion relativa de dos rectas en R3."""
    p1, d1 = r1.p0, r1.d
    p2, d2 = r2.p0, r2.d
    
    delta_p = p2 - p1
    cross_d = np.cross(d1, d2)
    norm_cross_d = float(np.linalg.norm(cross_d))
    
    if np.isclose(norm_cross_d, 0.0):
        cross_delta = np.cross(delta_p, d1)
        if np.isclose(np.linalg.norm(cross_delta), 0.0):
            return {
                'tipo': 'COINCIDENTES',
                'descripcion': 'Las rectas son coincidentes.',
                'distancia': 0.0,
                'puntos_cercanos': (p1, p1)
            }
        else:
            dist = float(np.linalg.norm(cross_delta) / np.linalg.norm(d1))
            return {
                'tipo': 'PARALELAS',
                'descripcion': 'Las rectas son paralelas no coincidentes.',
                'distancia': dist,
                'puntos_cercanos': None
            }
    
    pm = float(np.dot(delta_p, cross_d))
    if np.isclose(pm, 0.0, atol=1e-9):
        A = np.column_stack([d1, -d2])
        sol, _, _, _ = np.linalg.lstsq(A, delta_p, rcond=None)
        q1 = r1.punto_en_parametro(float(sol[0]))
        return {
            'tipo': 'SECANTES',
            'descripcion': 'Las rectas son secantes e intersecan en un punto unico.',
            'distancia': 0.0,
            'punto_interseccion': q1,
            'puntos_cercanos': (q1, q1)
        }
    
    distancia = abs(pm) / norm_cross_d
    q1, q2, t_opt, s_opt = calcular_puntos_mas_cercanos_alabeadas(r1, r2)
    return {
        'tipo': 'ALABEADAS',
        'descripcion': 'Las rectas son alabeadas (no paralelas y no coplanares).',
        'distancia': float(distancia),
        'producto_mixto': pm,
        'norm_cross_directores': norm_cross_d,
        'q1': q1,
        'q2': q2,
        't_opt': t_opt,
        's_opt': s_opt
    }


def generar_grafico_rectas_alabeadas_3d(r1: RectaR3, r2: RectaR3,
                                         guardar_ruta: str = "06_rectas_en_r3_y_rectas_alabeadas.png") -> plt.Figure:
    """
    Genera una figura 3D individual cientifica:
    Rectas L1 (USS_BLUE), L2 (USS_ACCENT_BLUE), segmento perpendicular comun Q1-Q2
    resaltado en USS_GOLD con marcadores s=90, y planos paralelos con alpha=0.20.
    """
    res = clasificar_posicion_relativa(r1, r2)
    
    fig = plt.figure(figsize=(9, 8), facecolor='white')
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_facecolor('white')
    
    dist_val = res['distancia']
    ax.set_title(f"Rectas Alabeadas en R3: Distancia Minima d = {dist_val:.4f} [u]",
                 fontsize=12.5, fontweight='bold', color=USS_BLUE, pad=16)
    
    # Rango de visualizacion
    t_span = np.linspace(-3.0, 3.0, 50)
    pts_l1 = np.array([r1.punto_en_parametro(t) for t in t_span])
    pts_l2 = np.array([r2.punto_en_parametro(t) for t in t_span])
    
    # Trazar rectas
    ax.plot(pts_l1[:, 0], pts_l1[:, 1], pts_l1[:, 2],
            color=USS_BLUE, linewidth=3.0, label=f"Recta {r1.nombre}")
    ax.plot(pts_l2[:, 0], pts_l2[:, 1], pts_l2[:, 2],
            color=USS_ACCENT_BLUE, linewidth=3.0, label=f"Recta {r2.nombre}")
    
    # Puntos base
    ax.scatter([r1.p0[0]], [r1.p0[1]], [r1.p0[2]], color=USS_BLUE, s=50, edgecolors='black', label=f"P1 (base L1)")
    ax.scatter([r2.p0[0]], [r2.p0[1]], [r2.p0[2]], color=USS_ACCENT_BLUE, s=50, edgecolors='black', label=f"P2 (base L2)")
    
    if res['tipo'] == 'ALABEADAS':
        q1 = res['q1']
        q2 = res['q2']
        
        # Segmento perpendicular comun en USS_GOLD
        ax.plot([q1[0], q2[0]], [q1[1], q2[1]], [q1[2], q2[2]],
                color=USS_GOLD, linewidth=3.5, label=f"Segmento perpendicular comun (d = {dist_val:.4f})")
        
        # Marcadores en Q1 y Q2 en USS_GOLD con s=90
        ax.scatter([q1[0]], [q1[1]], [q1[2]], color=USS_GOLD, s=90, edgecolors='black',
                   linewidths=1.2, marker='o', label="Q1 en L1 (contacto)")
        ax.scatter([q2[0]], [q2[1]], [q2[2]], color=USS_GOLD, s=90, edgecolors='black',
                   linewidths=1.2, marker='s', label="Q2 en L2 (contacto)")
        
        # Planos paralelos contenedores Pi1 y Pi2 con alpha=0.20
        n_comun = np.cross(r1.d, r2.d)
        n_comun = n_comun / np.linalg.norm(n_comun)
        
        u_plane = r1.d / np.linalg.norm(r1.d)
        v_plane = np.cross(n_comun, u_plane)
        
        grid_u, grid_v = np.meshgrid(np.linspace(-2.2, 2.2, 5), np.linspace(-2.2, 2.2, 5))
        
        # Plano 1 (contiene L1 y pasa por Q1)
        p1_x = q1[0] + grid_u * u_plane[0] + grid_v * v_plane[0]
        p1_y = q1[1] + grid_u * u_plane[1] + grid_v * v_plane[1]
        p1_z = q1[2] + grid_u * u_plane[2] + grid_v * v_plane[2]
        ax.plot_surface(p1_x, p1_y, p1_z, color=USS_BLUE, alpha=0.20, shade=False)
        
        # Plano 2 (contiene L2 y pasa por Q2)
        p2_x = q2[0] + grid_u * u_plane[0] + grid_v * v_plane[0]
        p2_y = q2[1] + grid_u * u_plane[1] + grid_v * v_plane[1]
        p2_z = q2[2] + grid_u * u_plane[2] + grid_v * v_plane[2]
        ax.plot_surface(p2_x, p2_y, p2_z, color=USS_GOLD, alpha=0.20, shade=False)
    
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
    print("Modulo 06: Rectas en R3 y Distancia entre Rectas Alabeadas")
    print("Universidad San Sebastian - Departamento de Ciencias Exactas")
    
    # 1. Definicion de rectas
    print("\n--- 1. DEFINICION Y ECUACIONES DE RECTAS ---")
    r1 = RectaR3(punto=np.array([1.0, -2.0, 4.0]), director=np.array([2.0, 3.0, -1.0]), nombre="L1")
    r2 = RectaR3(punto=np.array([0.0, 3.0, -1.0]), director=np.array([1.0, -1.0, 2.0]), nombre="L2")
    
    print(r1.ecuacion_vectorial())
    print(r1.ecuaciones_parametricas())
    print(r1.ecuaciones_simetricas())
    print()
    print(r2.ecuacion_vectorial())
    print(r2.ecuaciones_parametricas())
    print(r2.ecuaciones_simetricas())
    
    # 2. Clasificacion de posicion relativa
    print("\n--- 2. CLASIFICACION DE POSICION RELATIVA ---")
    res = clasificar_posicion_relativa(r1, r2)
    print(f"Posicion Relativa: {res['tipo']}")
    print(f"Descripcion: {res['descripcion']}")
    print(f"Distancia minima d(L1, L2) = {res['distancia']:.4f} [u]")
    
    # 3. Segmento perpendicular comun
    print("\n--- 3. SEGMENTO PERPENDICULAR COMUN ---")
    if res['tipo'] == 'ALABEADAS':
        q1 = res['q1']
        q2 = res['q2']
        vec_q = q2 - q1
        dot1 = float(np.dot(vec_q, r1.d))
        dot2 = float(np.dot(vec_q, r2.d))
        norm_q = float(np.linalg.norm(vec_q))
        
        print(f"Punto Q1 en L1 (t = {res['t_opt']:.4f}): {q1}")
        print(f"Punto Q2 en L2 (s = {res['s_opt']:.4f}): {q2}")
        print(f"Vector Q2 - Q1: {vec_q}")
        print(f"Ortogonalidad (Q2 - Q1) . d1: {dot1:.2e}")
        print(f"Ortogonalidad (Q2 - Q1) . d2: {dot2:.2e}")
        print(f"Longitud ||Q2 - Q1||: {norm_q:.4f} (Coincide con d: {np.isclose(norm_q, res['distancia'])})")
        assert abs(dot1) < 1e-12 and abs(dot2) < 1e-12, "Error en ortogonalidad de puntos mas cercanos."
    
    # 4. Generacion de Figura Cientifica 3D
    print("\n--- 4. GENERACION DE FIGURA CIENTIFICA 3D ---")
    dir_base = os.path.dirname(os.path.abspath(__file__))
    ruta_img = os.path.join(dir_base, "06_rectas_en_r3_y_rectas_alabeadas.png")
    
    generar_grafico_rectas_alabeadas_3d(r1, r2, guardar_ruta=ruta_img)
    print(f"Grafico guardado: {ruta_img}")
    
    print("\nModulo 06 ejecutado con exito.")


if __name__ == '__main__':
    ejecucion_demostrativa()
