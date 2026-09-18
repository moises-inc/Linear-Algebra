#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modulo 05: Producto Cruz, Producto Mixto y Paralelepipedos 3D
Asignatura: Algebra Lineal (DCEX0007) - Universidad San Sebastian (USS)
Carrera: Ingenieria Civil Informatica
Docente: Carol Asencio Gonzalez
Estudiante: Moises Amundarain Romero
Paleta Institucional: USS Blue (#00205B), USS Gold (#D4AF37)

Proposito:
    1. Producto cruz en R3 mediante determinante formal y evaluacion numerica.
    2. Demostracion rigurosa de ortogonalidad: (u x v) . u = 0 y (u x v) . v = 0.
    3. Verificacion analitica de la Identidad de Lagrange:
       ||u x v||^2 = ||u||^2 ||v||^2 - (u . v)^2.
    4. Anticonmutatividad: u x v = -(v x u).
    5. Interpretacion geometrica de areas: paralelogramo y triangulo sustentado.
    6. Triple producto escalar (mixto) [u, v, w] y calculo de volumenes:
       - Paralelepipedo: V = |[u, v, w]|
       - Tetraedro: V_tet = (1/6) |[u, v, w]|
    7. Generacion de figuras 3D cientificas individuales e independientes.
"""

import os
import sys
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Paleta Institucional USS
USS_BLUE = '#00205B'
USS_GOLD = '#D4AF37'
USS_ACCENT_BLUE = '#1E88E5'
USS_ACCENT_GREEN = '#27AE60'
USS_ACCENT_RED = '#C0392B'
USS_GRAY = '#7F8C8D'
USS_LIGHT_BG = '#F8F9FA'


def producto_cruz_numerico(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Calcula el producto cruz entre dos vectores en R3."""
    if len(u) != 3 or len(v) != 3:
        raise ValueError("El producto vectorial requiere vectores en R3.")
    return np.cross(u, v)


def producto_cruz_simbolico(u_sym: sp.Matrix, v_sym: sp.Matrix) -> sp.Matrix:
    """Calcula el producto cruz formal mediante expansion de cofactores 3x3."""
    cx = u_sym[1] * v_sym[2] - u_sym[2] * v_sym[1]
    cy = -(u_sym[0] * v_sym[2] - u_sym[2] * v_sym[0])
    cz = u_sym[0] * v_sym[1] - u_sym[1] * v_sym[0]
    return sp.Matrix([cx, cy, cz])


def verificar_ortogonalidad_producto_cruz(u: np.ndarray, v: np.ndarray) -> dict:
    """Verifica la ortogonalidad simultanea: (u x v) . u == 0 y (u x v) . v == 0."""
    c = producto_cruz_numerico(u, v)
    dot_u = float(np.dot(c, u))
    dot_v = float(np.dot(c, v))
    return {
        'cross': c,
        'dot_with_u': dot_u,
        'dot_with_v': dot_v,
        'ortogonal_a_u': bool(abs(dot_u) < 1e-12),
        'ortogonal_a_v': bool(abs(dot_v) < 1e-12)
    }


def verificar_identidad_lagrange(u: np.ndarray, v: np.ndarray) -> dict:
    """
    Verifica computacionalmente la Identidad de Lagrange:
    ||u x v||^2 = ||u||^2 ||v||^2 - (u . v)^2
    """
    c = producto_cruz_numerico(u, v)
    lhs = float(np.linalg.norm(c)**2)
    rhs = float((np.linalg.norm(u)**2) * (np.linalg.norm(v)**2) - (np.dot(u, v)**2))
    diff = abs(lhs - rhs)
    return {
        'norm_cross_sq': lhs,
        'lagrange_rhs': rhs,
        'diferencia': diff,
        'valido': bool(diff < 1e-11)
    }


def area_paralelogramo_y_triangulo(u: np.ndarray, v: np.ndarray) -> tuple[float, float]:
    """Calcula el area del paralelogramo (||u x v||) y del triangulo sustentado (0.5 * ||u x v||)."""
    norm_c = float(np.linalg.norm(producto_cruz_numerico(u, v)))
    return norm_c, 0.5 * norm_c


def producto_mixto(u: np.ndarray, v: np.ndarray, w: np.ndarray) -> float:
    """Calcula el triple producto escalar [u, v, w] = u . (v x w)."""
    mat = np.array([u, v, w], dtype=float)
    return float(np.linalg.det(mat))


def volumen_paralelepipedo_y_tetraedro(u: np.ndarray, v: np.ndarray, w: np.ndarray) -> tuple[float, float]:
    """Calcula el volumen del paralelepipedo y tetraedro sustentados por u, v, w."""
    pm = producto_mixto(u, v, w)
    vol_paral = abs(pm)
    vol_tet = vol_paral / 6.0
    return float(vol_paral), float(vol_tet)


def generar_vertices_paralelepipedo(u: np.ndarray, v: np.ndarray, w: np.ndarray,
                                     origen: np.ndarray = np.array([0.0, 0.0, 0.0])) -> dict:
    """Genera los 8 vertices y las 6 caras poligonales del paralelepipedo."""
    o = np.array(origen, dtype=float)
    v0 = o
    v1 = o + u
    v2 = o + u + v
    v3 = o + v
    v4 = o + w
    v5 = o + u + w
    v6 = o + u + v + w
    v7 = o + v + w
    
    vertices = np.array([v0, v1, v2, v3, v4, v5, v6, v7])
    caras = [
        [v0, v1, v2, v3],  # Base inferior (u-v)
        [v4, v5, v6, v7],  # Cara superior
        [v0, v1, v5, v4],  # Cara frontal
        [v2, v3, v7, v6],  # Cara posterior
        [v0, v3, v7, v4],  # Cara lateral izquierda
        [v1, v2, v6, v5]   # Cara lateral derecha
    ]
    return {'vertices': vertices, 'caras': caras}


def generar_grafico_producto_cruz_3d(u: np.ndarray, v: np.ndarray,
                                      guardar_ruta: str = "05_producto_cruz_y_ortogonalidad_3d.png") -> plt.Figure:
    """
    Figura 3D individual:
    Vectores u, v, vector normal u x v y paralelogramo base sombreado (alpha=0.25).
    """
    fig = plt.figure(figsize=(8.5, 7.5), facecolor='white')
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_facecolor('white')
    ax.set_title("Producto Cruz y Ortogonalidad en R3: u x v perpendicular a u, v",
                 fontsize=12.5, fontweight='bold', color=USS_BLUE, pad=16)
    
    uxv = producto_cruz_numerico(u, v)
    area_p, _ = area_paralelogramo_y_triangulo(u, v)
    
    # Paralelogramo sombreado
    v0 = np.array([0.0, 0.0, 0.0])
    v1 = u
    v2 = u + v
    v3 = v
    cara_paral = [v0, v1, v2, v3]
    poly = Poly3DCollection([cara_paral], alpha=0.25, facecolor=USS_GOLD, edgecolor=USS_BLUE, linewidths=1.5)
    ax.add_collection3d(poly)
    
    # Aristas del paralelogramo
    ax.plot([u[0], (u+v)[0]], [u[1], (u+v)[1]], [u[2], (u+v)[2]], color=USS_GOLD, linestyle=':', linewidth=1.5)
    ax.plot([v[0], (u+v)[0]], [v[1], (u+v)[1]], [v[2], (u+v)[2]], color=USS_BLUE, linestyle=':', linewidth=1.5)
    
    # Quivers de vectores
    ax.quiver(0, 0, 0, u[0], u[1], u[2], color=USS_BLUE, linewidth=3.0,
              arrow_length_ratio=0.12, label=f"u = ({u[0]:g}, {u[1]:g}, {u[2]:g})")
    ax.quiver(0, 0, 0, v[0], v[1], v[2], color=USS_GOLD, linewidth=3.0,
              arrow_length_ratio=0.12, label=f"v = ({v[0]:g}, {v[1]:g}, {v[2]:g})")
    ax.quiver(0, 0, 0, uxv[0], uxv[1], uxv[2], color=USS_ACCENT_RED, linewidth=3.2,
              arrow_length_ratio=0.10, label=f"u x v = ({uxv[0]:g}, {uxv[1]:g}, {uxv[2]:g})")
    
    # Origen y vertices
    ax.scatter([0], [0], [0], color='black', s=35, label='Origen O')
    ax.scatter([u[0], v[0], (u+v)[0]], [u[1], v[1], (u+v)[1]], [u[2], v[2], (u+v)[2]],
               color=USS_BLUE, s=30)
    
    # Texto de area
    ax.text((u+v)[0]*0.5, (u+v)[1]*0.5, (u+v)[2]*0.5,
            f"Area = {area_p:.2f} [u^2]", fontsize=9.5, fontweight='bold', color=USS_BLUE)
    
    # Limites dinamicos
    pts = np.vstack([[0, 0, 0], u, v, u+v, uxv])
    margin = 0.8
    ax.set_xlim(pts[:, 0].min() - margin, pts[:, 0].max() + margin)
    ax.set_ylim(pts[:, 1].min() - margin, pts[:, 1].max() + margin)
    ax.set_zlim(pts[:, 2].min() - margin, pts[:, 2].max() + margin)
    
    ax.set_xlabel("Eje X", fontweight='bold', color=USS_BLUE)
    ax.set_ylabel("Eje Y", fontweight='bold', color=USS_BLUE)
    ax.set_zlabel("Eje Z", fontweight='bold', color=USS_BLUE)
    ax.legend(loc='upper left', fontsize=8.5, framealpha=0.95)
    ax.view_init(elev=25, azim=-50)
    
    plt.tight_layout()
    plt.savefig(guardar_ruta, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return fig


def generar_grafico_paralelepipedo_3d(u: np.ndarray, v: np.ndarray, w: np.ndarray,
                                       guardar_ruta: str = "05_paralelepipedo_y_volumen_3d.png") -> plt.Figure:
    """
    Figura 3D individual:
    Paralelepipedo con Poly3DCollection (alpha=0.20), aristas generadoras u, v, w y vector normal u x v.
    """
    fig = plt.figure(figsize=(8.5, 7.5), facecolor='white')
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_facecolor('white')
    
    vol_p, _ = volumen_paralelepipedo_y_tetraedro(u, v, w)
    ax.set_title(f"Paralelepipedo 3D: Volumen V = |[u, v, w]| = {vol_p:.2f} [u^3]",
                 fontsize=12.5, fontweight='bold', color=USS_BLUE, pad=16)
    
    geom = generar_vertices_paralelepipedo(u, v, w)
    caras = geom['caras']
    
    # Coleccion de caras poligonales
    poly = Poly3DCollection(caras, alpha=0.20, facecolor=USS_GOLD, edgecolor=USS_BLUE, linewidths=1.2)
    ax.add_collection3d(poly)
    
    # Resaltar base inferior u-v
    base_poly = Poly3DCollection([caras[0]], alpha=0.30, facecolor=USS_ACCENT_BLUE, edgecolor=USS_BLUE, linewidths=1.8)
    ax.add_collection3d(base_poly)
    
    # Vectores arista
    ax.quiver(0, 0, 0, u[0], u[1], u[2], color=USS_BLUE, linewidth=3.2,
              arrow_length_ratio=0.12, label=f"u = ({u[0]:g}, {u[1]:g}, {u[2]:g})")
    ax.quiver(0, 0, 0, v[0], v[1], v[2], color=USS_GOLD, linewidth=3.2,
              arrow_length_ratio=0.12, label=f"v = ({v[0]:g}, {v[1]:g}, {v[2]:g})")
    ax.quiver(0, 0, 0, w[0], w[1], w[2], color=USS_ACCENT_BLUE, linewidth=3.2,
              arrow_length_ratio=0.12, label=f"w = ({w[0]:g}, {w[1]:g}, {w[2]:g})")
    
    # Vector normal u x v escalado para visualizacion armonica
    uxv = producto_cruz_numerico(u, v)
    norm_uxv = float(np.linalg.norm(uxv))
    escala = min(1.0, max(np.linalg.norm(u), np.linalg.norm(v), np.linalg.norm(w)) / (norm_uxv + 1e-9))
    uxv_vis = uxv * escala
    ax.quiver(0, 0, 0, uxv_vis[0], uxv_vis[1], uxv_vis[2], color=USS_ACCENT_RED, linewidth=2.8,
              arrow_length_ratio=0.12, label="u x v (normal base)")
    
    # Vertices
    verts = geom['vertices']
    ax.scatter(verts[:, 0], verts[:, 1], verts[:, 2], color=USS_BLUE, s=30, edgecolors='black')
    
    # Limites
    all_pts = np.vstack([verts, uxv_vis])
    margin = 0.5
    ax.set_xlim(all_pts[:, 0].min() - margin, all_pts[:, 0].max() + margin)
    ax.set_ylim(all_pts[:, 1].min() - margin, all_pts[:, 1].max() + margin)
    ax.set_zlim(all_pts[:, 2].min() - margin, all_pts[:, 2].max() + margin)
    
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
    print("Modulo 05: Producto Cruz, Producto Mixto y Paralelepipedos 3D")
    print("Universidad San Sebastian - Departamento de Ciencias Exactas")
    
    # 1. Demostracion Simbolica con SymPy
    print("\n--- 1. DEMOSTRACION SIMBOLICA CON SYMPY ---")
    u1, u2, u3 = sp.symbols('u1 u2 u3', real=True)
    v1, v2, v3 = sp.symbols('v1 v2 v3', real=True)
    
    u_s = sp.Matrix([u1, u2, u3])
    v_s = sp.Matrix([v1, v2, v3])
    
    cross_s = producto_cruz_simbolico(u_s, v_s)
    dot_u_s = sp.simplify(cross_s.dot(u_s))
    dot_v_s = sp.simplify(cross_s.dot(v_s))
    
    print(f"Producto cruz formal u x v:")
    print(f"  Componente i: {cross_s[0]}")
    print(f"  Componente j: {cross_s[1]}")
    print(f"  Componente k: {cross_s[2]}")
    print(f"Demostracion ortogonalidad (u x v) . u = {dot_u_s}")
    print(f"Demostracion ortogonalidad (u x v) . v = {dot_v_s}")
    assert dot_u_s == 0 and dot_v_s == 0, "Error en ortogonalidad simbolica."
    
    cross_vu_s = producto_cruz_simbolico(v_s, u_s)
    anticonm = sp.simplify(cross_s + cross_vu_s)
    print(f"Anticonmutatividad u x v + v x u = {anticonm.T}")
    assert anticonm == sp.Matrix([0, 0, 0]), "Error en anticonmutatividad."
    print("[OK] Ortogonalidad y anticonmutatividad demostradas analiticamente.")
    
    # 2. Verificaciones Analiticas Numericas
    print("\n--- 2. VERIFICACIONES ANALITICAS NUMERICAS ---")
    u = np.array([3.0, 0.0, 1.0])
    v = np.array([1.0, 2.0, 0.0])
    w = np.array([0.0, 1.0, 4.0])
    
    c = producto_cruz_numerico(u, v)
    ortog = verificar_ortogonalidad_producto_cruz(u, v)
    lagrange = verificar_identidad_lagrange(u, v)
    area_p, area_t = area_paralelogramo_y_triangulo(u, v)
    vol_p, vol_t = volumen_paralelepipedo_y_tetraedro(u, v, w)
    pm = producto_mixto(u, v, w)
    
    print(f"Vector u = {u}")
    print(f"Vector v = {v}")
    print(f"Vector w = {w}")
    print(f"Producto cruz u x v = {c}")
    print(f"Norma ||u x v|| = {np.linalg.norm(c):.4f}")
    print(f"Ortogonalidad u . (u x v) = {ortog['dot_with_u']:.2e}")
    print(f"Ortogonalidad v . (u x v) = {ortog['dot_with_v']:.2e}")
    print(f"Identidad de Lagrange:")
    print(f"  ||u x v||^2 = {lagrange['norm_cross_sq']:.4f}")
    print(f"  ||u||^2 ||v||^2 - (u . v)^2 = {lagrange['lagrange_rhs']:.4f}")
    print(f"  Diferencia = {lagrange['diferencia']:.2e} (Satisfecha: {lagrange['valido']})")
    print(f"Area paralelogramo base = {area_p:.4f} [u^2]")
    print(f"Area triangulo base     = {area_t:.4f} [u^2]")
    print(f"Triple producto mixto [u, v, w] = {pm:.4f}")
    print(f"Volumen paralelepipedo  = {vol_p:.4f} [u^3]")
    print(f"Volumen tetraedro       = {vol_t:.4f} [u^3]")
    
    # 3. Generacion de Figuras Cientificas 3D
    print("\n--- 3. GENERACION DE FIGURAS CIENTIFICAS INDIVIDUALES ---")
    dir_base = os.path.dirname(os.path.abspath(__file__))
    ruta_cruz = os.path.join(dir_base, "05_producto_cruz_y_ortogonalidad_3d.png")
    ruta_paral = os.path.join(dir_base, "05_paralelepipedo_y_volumen_3d.png")
    
    generar_grafico_producto_cruz_3d(u, v, guardar_ruta=ruta_cruz)
    print(f"Grafico guardado: {ruta_cruz}")
    
    generar_grafico_paralelepipedo_3d(u, v, w, guardar_ruta=ruta_paral)
    print(f"Grafico guardado: {ruta_paral}")
    
    print("\nModulo 05 ejecutado con exito.")


if __name__ == '__main__':
    ejecucion_demostrativa()
