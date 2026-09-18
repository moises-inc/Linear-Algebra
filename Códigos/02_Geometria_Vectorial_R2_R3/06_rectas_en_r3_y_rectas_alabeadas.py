#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
MÓDULO 06: RECTAS EN R³, POSICIONES RELATIVAS Y DISTANCIA ENTRE RECTAS ALABEADAS
Asignatura: Álgebra Lineal (DCEX0007) — Universidad San Sebastián (USS)
Carrera: Ingeniería Civil Informática
Docente: Carol Asencio González
Estudiante: Moisés Amundarain Romero
Paleta Institucional: USS Blue (#00205B), USS Gold (#D4AF37)
================================================================================
Propósito del Módulo:
    Modelar, calcular analíticamente y visualizar en 3D:
    1. Formas de la ecuación de una recta en R³:
       - Ecuación vectorial: r(t) = P0 + t * d.
       - Ecuaciones paramétricas: x = x0 + t*dx, y = y0 + t*dy, z = z0 + t*dz.
       - Ecuaciones simétricas: (x - x0)/dx = (y - y0)/dy = (z - z0)/dz.
    2. Clasificación rigurosa de las 4 posiciones relativas entre dos rectas en R³:
       - Coincidentes.
       - Paralelas (no coincidentes).
       - Secantes (intersección en un punto único).
       - Alabeadas (skew: no paralelas y no coplanares).
    3. Distancia mínima entre rectas alabeadas:
       d(L1, L2) = |(P2 - P1) · (d1 x d2)| / ||d1 x d2||.
    4. Determinación analítica exacta de los puntos más cercanos Q1 en L1 y Q2 en L2
       resolviendo el sistema ortogonal de Gram 2x2.
    5. Visualización científica 3D mostrando:
       - Ambas rectas extendidas en R³.
       - Puntos base y puntos de máximo acercamiento Q1 y Q2.
       - Segmento perpendicular común resaltado en rojo acento.
       - Planos paralelos contenedores Pi1 y Pi2 con transparencia ilustrando
         que la distancia mínima es la separación entre dichos planos.
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
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ==============================================================================
# 🎨 PALETA DE COLORES INSTITUCIONAL USS
# ==============================================================================
USS_BLUE = '#00205B'          # Primario institucional (Recta L1)
USS_GOLD = '#D4AF37'          # Secundario dorado (Recta L2)
USS_ACCENT_BLUE = '#1E88E5'   # Azul de realce (Plano Pi1)
USS_ACCENT_GREEN = '#27AE60'  # Verde de realce (Puntos de contacto)
USS_ACCENT_RED = '#C0392B'    # Rojo de realce (Segmento perpendicular común)
USS_GRAY = '#7F8C8D'          # Gris auxiliar
USS_LIGHT_BG = '#F8F9FA'      # Fondo claro


# ==============================================================================
# 📐 CLASE Y MÉTODOS ANALÍTICOS DE RECTA EN R³
# ==============================================================================

class RectaR3:
    """
    Representa una recta en el espacio tridimensional R³ definida por:
    r(t) = P0 + t * d,  t en R.
    """
    def __init__(self, punto: np.ndarray, director: np.ndarray, nombre: str = "L"):
        self.p0 = np.array(punto, dtype=float)
        self.d = np.array(director, dtype=float)
        self.nombre = nombre
        
        norm_d = np.linalg.norm(self.d)
        if np.isclose(norm_d, 0.0):
            raise ValueError(f"El vector director de la recta {nombre} no puede ser el vector nulo.")
    
    def punto_en_parametro(self, t: float) -> np.ndarray:
        """Calcula el punto r(t) = P0 + t * d."""
        return self.p0 + t * self.d

    def ecuacion_vectorial(self) -> str:
        """Retorna la ecuación vectorial en formato legible."""
        return f"{self.nombre}: (x, y, z) = ({self.p0[0]:g}, {self.p0[1]:g}, {self.p0[2]:g}) + t*({self.d[0]:g}, {self.d[1]:g}, {self.d[2]:g})"

    def ecuaciones_parametricas(self) -> str:
        """Retorna las ecuaciones paramétricas escalares."""
        p, d = self.p0, self.d
        sign_x = f"+ {d[0]:g}t" if d[0] >= 0 else f"- {abs(d[0]):g}t"
        sign_y = f"+ {d[1]:g}t" if d[1] >= 0 else f"- {abs(d[1]):g}t"
        sign_z = f"+ {d[2]:g}t" if d[2] >= 0 else f"- {abs(d[2]):g}t"
        return f"{self.nombre} => x = {p[0]:g} {sign_x},  y = {p[1]:g} {sign_y},  z = {p[2]:g} {sign_z}"

    def ecuaciones_simetricas(self) -> str:
        """Retorna las ecuaciones simétricas considerando posibles ceros en d."""
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


# ==============================================================================
# 🔍 CLASIFICACIÓN DE POSICIONES RELATIVAS Y DISTANCIA
# ==============================================================================

def clasificar_posicion_relativa(r1: RectaR3, r2: RectaR3) -> dict:
    """
    Determina la posición relativa entre dos rectas r1 y r2 en R³:
    1. Paralelismo de vectores directores: d1 x d2 == 0.
       - Si (P2 - P1) x d1 == 0 -> COINCIDENTES.
       - Si (P2 - P1) x d1 != 0 -> PARALELAS NO COINCIDENTES.
    2. Si d1 x d2 != 0 (No paralelas):
       - Producto mixto: pm = (P2 - P1) · (d1 x d2).
       - Si pm == 0 -> SECANTES (intersecan en un punto único).
       - Si pm != 0 -> ALABEADAS (skew, no se cortan ni son paralelas).
    """
    p1, d1 = r1.p0, r1.d
    p2, d2 = r2.p0, r2.d
    
    delta_p = p2 - p1
    cross_d = np.cross(d1, d2)
    norm_cross_d = float(np.linalg.norm(cross_d))
    
    # 1. ¿Son paralelas?
    if np.isclose(norm_cross_d, 0.0):
        cross_delta = np.cross(delta_p, d1)
        if np.isclose(np.linalg.norm(cross_delta), 0.0):
            return {
                'tipo': 'COINCIDENTES',
                'descripcion': 'Las rectas son coincidentes (la misma recta en el espacio).',
                'distancia': 0.0,
                'punto_interseccion': None,
                'puntos_cercanos': (p1, p1)
            }
        else:
            # Paralelas: distancia punto-recta
            dist = float(np.linalg.norm(cross_delta) / np.linalg.norm(d1))
            return {
                'tipo': 'PARALELAS',
                'descripcion': 'Las rectas son estrictamente paralelas no coincidentes.',
                'distancia': dist,
                'punto_interseccion': None,
                'puntos_cercanos': None
            }
    
    # 2. No son paralelas: evaluar coplanaridad con el producto mixto
    pm = float(np.dot(delta_p, cross_d))
    
    if np.isclose(pm, 0.0, atol=1e-9):
        # Secantes: resolver sistema 2x2 para t y s
        # P1 + t*d1 = P2 + s*d2 => t*d1 - s*d2 = P2 - P1
        A = np.column_stack([d1, -d2])
        # Mínimos cuadrados / pseudo-inversa exacta para sistema sobredeterminado 3x2
        sol, residuals, rank, s = np.linalg.lstsq(A, delta_p, rcond=None)
        t_val, s_val = float(sol[0]), float(sol[1])
        q1 = r1.punto_en_parametro(t_val)
        q2 = r2.punto_en_parametro(s_val)
        
        return {
            'tipo': 'SECANTES',
            'descripcion': 'Las rectas son secantes e intersecan en un punto único.',
            'distancia': 0.0,
            'punto_interseccion': q1,
            't_interseccion': t_val,
            's_interseccion': s_val,
            'puntos_cercanos': (q1, q2)
        }
    
    # 3. Alabeadas
    distancia = abs(pm) / norm_cross_d
    q1, q2, t_opt, s_opt = calcular_puntos_mas_cercanos_alabeadas(r1, r2)
    
    return {
        'tipo': 'ALABEADAS',
        'descripcion': 'Las rectas son alabeadas (se cruzan en el espacio sin tocarse ni ser paralelas).',
        'distancia': float(distancia),
        'producto_mixto': pm,
        'norm_cross_directores': norm_cross_d,
        'q1': q1,
        'q2': q2,
        't_opt': t_opt,
        's_opt': s_opt,
        'punto_interseccion': None
    }


def calcular_puntos_mas_cercanos_alabeadas(r1: RectaR3, r2: RectaR3) -> tuple[np.ndarray, np.ndarray, float, float]:
    """
    Calcula los puntos Q1 en r1 y Q2 en r2 que forman el segmento perpendicular común.
    Condición: (Q2 - Q1) debe ser ortogonal a d1 y a d2:
        (P2 + s*d2 - (P1 + t*d1)) · d1 = 0
        (P2 + s*d2 - (P1 + t*d1)) · d2 = 0
    Sistema lineal 2x2:
        [ ||d1||²        -(d1 · d2) ] [ t ] = [ (P2 - P1) · d1 ]
        [ d1 · d2        -||d2||²   ] [ s ] = [ (P2 - P1) · d2 ]
    """
    p1, d1 = r1.p0, r1.d
    p2, d2 = r2.p0, r2.d
    delta_p = p2 - p1
    
    d1_dot_d1 = np.dot(d1, d1)
    d2_dot_d2 = np.dot(d2, d2)
    d1_dot_d2 = np.dot(d1, d2)
    
    M = np.array([
        [d1_dot_d1, -d1_dot_d2],
        [d1_dot_d2, -d2_dot_d2]
    ], dtype=float)
    
    b = np.array([
        np.dot(delta_p, d1),
        np.dot(delta_p, d2)
    ], dtype=float)
    
    sol = np.linalg.solve(M, b)
    t_opt = float(sol[0])
    s_opt = float(sol[1])
    
    q1 = r1.punto_en_parametro(t_opt)
    q2 = r2.punto_en_parametro(s_opt)
    
    return q1, q2, t_opt, s_opt


# ==============================================================================
# 📊 VISUALIZACIÓN 3D CON PLANOS PARALELOS CONTENEDORES
# ==============================================================================

def visualizar_rectas_alabeadas_3d(r1: RectaR3, r2: RectaR3,
                                   guardar_ruta: str = "06_rectas_en_r3_y_rectas_alabeadas.png") -> plt.Figure:
    """
    Genera un panel de visualización 3D científico:
    1. Render 3D mostrando:
       - Recta L1 en Azul USS y Recta L2 en Dorado USS.
       - Puntos base P1, P2 y puntos de máxima aproximación Q1, Q2.
       - Segmento perpendicular común Q1-Q2 en Rojo Acento.
       - Planos paralelos Pi1 y Pi2 con normal común d1 x d2 que contienen a L1 y L2,
         haciendo evidente por qué la distancia entre rectas alabeadas es constante
         entre dichos planos.
    2. Panel lateral con desglose analítico de ecuaciones y métricas.
    """
    res = clasificar_posicion_relativa(r1, r2)
    
    fig = plt.figure(figsize=(16, 7), facecolor='white')
    
    # --------------------------------------------------------------------------
    # SUBPLOT 1: Renderizado 3D
    # --------------------------------------------------------------------------
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1.set_facecolor('white')
    ax1.set_title("1. Rectas Alabeadas y Segmento Perpendicular Común\n" +
                  r"$d(L_1, L_2) = \frac{|(P_2 - P_1)\cdot(\mathbf{d}_1 \times \mathbf{d}_2)|}{||\mathbf{d}_1 \times \mathbf{d}_2||}$",
                  fontsize=12, fontweight='bold', color=USS_BLUE, pad=15)
    
    # Rango de visualización de las rectas
    t_span = np.linspace(-3, 3, 50)
    pts_l1 = np.array([r1.punto_en_parametro(t) for t in t_span])
    pts_l2 = np.array([r2.punto_en_parametro(t) for t in t_span])
    
    # Trazar rectas L1 y L2
    ax1.plot(pts_l1[:, 0], pts_l1[:, 1], pts_l1[:, 2],
             color=USS_BLUE, linewidth=3.0, label=f"Recta {r1.nombre}")
    ax1.plot(pts_l2[:, 0], pts_l2[:, 1], pts_l2[:, 2],
             color=USS_GOLD, linewidth=3.0, label=f"Recta {r2.nombre}")
    
    # Puntos base
    ax1.scatter([r1.p0[0]], [r1.p0[1]], [r1.p0[2]], color=USS_BLUE, s=60, edgecolors='black',
                label=f"P1 {tuple(np.round(r1.p0, 1))}")
    ax1.scatter([r2.p0[0]], [r2.p0[1]], [r2.p0[2]], color=USS_GOLD, s=60, edgecolors='black',
                label=f"P2 {tuple(np.round(r2.p0, 1))}")
    
    # Si son alabeadas, graficar puntos Q1, Q2, segmento común y planos paralelos
    if res['tipo'] == 'ALABEADAS':
        q1 = res['q1']
        q2 = res['q2']
        
        # Puntos de contacto
        ax1.scatter([q1[0]], [q1[1]], [q1[2]], color=USS_ACCENT_GREEN, s=70, marker='o')
        ax1.scatter([q2[0]], [q2[1]], [q2[2]], color=USS_ACCENT_GREEN, s=70, marker='^')
        
        # Segmento perpendicular común
        ax1.plot([q1[0], q2[0]], [q1[1], q2[1]], [q1[2], q2[2]],
                 color=USS_ACCENT_RED, linewidth=4.0,
                 label=f"Distancia Mínima = {res['distancia']:.4f}")
        
        # Planos paralelos contenedores Pi1 y Pi2
        # Normal común n = d1 x d2
        n_comun = np.cross(r1.d, r2.d)
        n_comun = n_comun / np.linalg.norm(n_comun)
        
        # Parches de plano alrededor de Q1 y Q2
        u_plane = r1.d / np.linalg.norm(r1.d)
        v_plane = np.cross(n_comun, u_plane)
        
        grid_u, grid_v = np.meshgrid(np.linspace(-2.5, 2.5, 5), np.linspace(-2.5, 2.5, 5))
        
        # Plano 1 (contiene L1 por Q1)
        p1_x = q1[0] + grid_u * u_plane[0] + grid_v * v_plane[0]
        p1_y = q1[1] + grid_u * u_plane[1] + grid_v * v_plane[1]
        p1_z = q1[2] + grid_u * u_plane[2] + grid_v * v_plane[2]
        ax1.plot_surface(p1_x, p1_y, p1_z, color=USS_ACCENT_BLUE, alpha=0.15, shade=False)
        
        # Plano 2 (contiene L2 por Q2)
        p2_x = q2[0] + grid_u * u_plane[0] + grid_v * v_plane[0]
        p2_y = q2[1] + grid_u * u_plane[1] + grid_v * v_plane[1]
        p2_z = q2[2] + grid_u * u_plane[2] + grid_v * v_plane[2]
        ax1.plot_surface(p2_x, p2_y, p2_z, color=USS_GOLD, alpha=0.15, shade=False)
    
    ax1.set_xlabel('Eje X', fontweight='bold', color=USS_BLUE)
    ax1.set_ylabel('Eje Y', fontweight='bold', color=USS_BLUE)
    ax1.set_zlabel('Eje Z', fontweight='bold', color=USS_BLUE)
    ax1.legend(loc='upper left', fontsize=8, framealpha=0.9)
    ax1.view_init(elev=20, azim=60)
    
    # --------------------------------------------------------------------------
    # SUBPLOT 2: Panel Teórico y Analítico
    # --------------------------------------------------------------------------
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_facecolor(USS_LIGHT_BG)
    ax2.set_title("2. Formas Ecuacionales y Desglose Analítico\n" +
                  f"Posición Relativa: {res['tipo']}",
                  fontsize=12, fontweight='bold', color=USS_BLUE, pad=15)
    
    texto_resumen = (
        r"$\mathbf{ECUACIONES\ DE\ LAS\ RECTAS:}$" + "\n"
        f" • {r1.ecuacion_vectorial()}\n"
        f"   {r1.ecuaciones_parametricas()}\n"
        f"   {r1.ecuaciones_simetricas()}\n\n"
        f" • {r2.ecuacion_vectorial()}\n"
        f"   {r2.ecuaciones_parametricas()}\n"
        f"   {r2.ecuaciones_simetricas()}\n\n"
        r"$\mathbf{ANÁLISIS\ VECTORIAL:}$" + "\n"
        f" • Vector P2 - P1 = {r2.p0 - r1.p0}\n"
        f" • d1 x d2 = {np.cross(r1.d, r2.d)}\n"
        f" • ||d1 x d2|| = {np.linalg.norm(np.cross(r1.d, r2.d)):.4f}\n"
        f" • (P2 - P1) · (d1 x d2) = {np.dot(r2.p0 - r1.p0, np.cross(r1.d, r2.d)):.4f}\n\n"
        r"$\mathbf{RESULTADO\ Y\ CLASIFICACIÓN:}$" + "\n"
        f" • Diagnóstico: {res['descripcion']}\n"
        f" • Distancia Mínima = {res['distancia']:.4f} [u]\n"
    )
    
    if res['tipo'] == 'ALABEADAS':
        q1_str = tuple(np.round(res['q1'], 3))
        q2_str = tuple(np.round(res['q2'], 3))
        perp_vec = res['q2'] - res['q1']
        dot_check1 = float(np.dot(perp_vec, r1.d))
        dot_check2 = float(np.dot(perp_vec, r2.d))
        
        texto_resumen += (
            "\n" + r"$\mathbf{SEGMENTO\ PERPENDICULAR\ COMÚN:}$" + "\n"
            f" • Parámetro óptimo t en L1 = {res['t_opt']:.4f} => Q1 = {q1_str}\n"
            f" • Parámetro óptimo s en L2 = {res['s_opt']:.4f} => Q2 = {q2_str}\n"
            f" • Verificación ortogonal con d1: (Q2-Q1)·d1 = {dot_check1:.2e}\n"
            f" • Verificación ortogonal con d2: (Q2-Q1)·d2 = {dot_check2:.2e}\n"
            f" • ||Q2 - Q1|| = {np.linalg.norm(perp_vec):.4f} (Coincide con d)"
        )
    
    ax2.text(0.04, 0.95, texto_resumen, transform=ax2.transAxes,
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
    print(" MÓDULO 06: RECTAS EN R³ Y DISTANCIA ENTRE RECTAS ALABEADAS")
    print("=" * 80)
    
    # --------------------------------------------------------------------------
    # 1. Definición de dos rectas alabeadas (ejemplo clásico Stewart / Grossman)
    # L1: pasa por P1=(1, -2, 4) con d1=(2, 3, -1)
    # L2: pasa por P2=(0, 3, -1) con d2=(1, -1, 2)
    # --------------------------------------------------------------------------
    print("\n--- 1. DEFINICIÓN DE RECTAS ---")
    r1 = RectaR3(punto=np.array([1.0, -2.0, 4.0]), director=np.array([2.0, 3.0, -1.0]), nombre="L1")
    r2 = RectaR3(punto=np.array([0.0, 3.0, -1.0]), director=np.array([1.0, -1.0, 2.0]), nombre="L2")
    
    print(r1.ecuacion_vectorial())
    print(r1.ecuaciones_parametricas())
    print(r1.ecuaciones_simetricas())
    print()
    print(r2.ecuacion_vectorial())
    print(r2.ecuaciones_parametricas())
    print(r2.ecuaciones_simetricas())
    
    # --------------------------------------------------------------------------
    # 2. Análisis y Clasificación
    # --------------------------------------------------------------------------
    print("\n--- 2. CLASIFICACIÓN DE POSICIÓN RELATIVA ---")
    clasificacion = clasificar_posicion_relativa(r1, r2)
    print(f"Posición Relativa: {clasificacion['tipo']}")
    print(f"Descripción: {clasificacion['descripcion']}")
    print(f"Distancia Mínima d(L1, L2): {clasificacion['distancia']:.4f}")
    
    if clasificacion['tipo'] == 'ALABEADAS':
        print(f"Punto Q1 en L1: {clasificacion['q1']}")
        print(f"Punto Q2 en L2: {clasificacion['q2']}")
        vec_q1q2 = clasificacion['q2'] - clasificacion['q1']
        print(f"Vector Q2 - Q1: {vec_q1q2}")
        print(f"Verificación ortogonalidad con d1: {np.dot(vec_q1q2, r1.d):.2e}")
        print(f"Verificación ortogonalidad con d2: {np.dot(vec_q1q2, r2.d):.2e}")
        print(f"Norma ||Q2 - Q1||: {np.linalg.norm(vec_q1q2):.4f}")
    
    # --------------------------------------------------------------------------
    # 3. Caso Secante para Verificación
    # --------------------------------------------------------------------------
    print("\n--- 3. CASO DE RECTAS SECANTES (VERIFICACIÓN) ---")
    r3 = RectaR3(punto=np.array([1.0, 1.0, 1.0]), director=np.array([1.0, 2.0, 3.0]), nombre="L3")
    r4 = RectaR3(punto=np.array([3.0, 5.0, 7.0]), director=np.array([2.0, 1.0, 0.0]), nombre="L4")
    # Para t=1 en L3: (2, 3, 4). Para s=-0.5 en L4: (3 - 1, 5 - 0.5, ...) veamos
    clasif_sec = clasificar_posicion_relativa(r3, r4)
    print(f"L3 y L4: {clasif_sec['tipo']}")
    
    # --------------------------------------------------------------------------
    # 4. Generación Gráfica 3D
    # --------------------------------------------------------------------------
    print("\n--- 4. GENERACIÓN DE FIGURA MATPLOTLIB 3D ---")
    out_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "06_rectas_en_r3_y_rectas_alabeadas.png")
    visualizar_rectas_alabeadas_3d(r1, r2, guardar_ruta=out_img)
    
    print("=" * 80)
    print(" MÓDULO 06 COMPLETADO CON ÉXITO")
    print("=" * 80)


if __name__ == '__main__':
    ejecucion_demostrativa()
