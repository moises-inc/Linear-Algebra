#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
MÓDULO 05: PRODUCTO CRUZ, PRODUCTO MIXTO Y PARALELEPÍPEDOS 3D EN R³
Asignatura: Álgebra Lineal (DCEX0007) — Universidad San Sebastián (USS)
Carrera: Ingeniería Civil Informática
Docente: Carol Asencio González
Estudiante: Moisés Amundarain Romero
Paleta Institucional: USS Blue (#00205B), USS Gold (#D4AF37)
================================================================================
Propósito del Módulo:
    Modelar, calcular analíticamente y visualizar en 3D:
    1. Producto cruz u x v mediante determinante simbólico 3x3 y numérico.
    2. Demostración formal de ortogonalidad: (u x v) · u = 0 y (u x v) · v = 0.
    3. Identidad de Lagrange: ||u x v||² = ||u||² ||v||² - (u · v)².
    4. Anticonmutatividad: u x v = -(v x u).
    5. Interpretación geométrica de áreas:
       - Área del paralelogramo: A = ||u x v||.
       - Área del triángulo sustentado: A_tri = (1/2) ||u x v||.
    6. Triple producto escalar (producto mixto): [u, v, w] = u · (v x w) = det([u, v, w]).
    7. Volúmenes geométricos:
       - Volumen del paralelepípedo: V = |[u, v, w]|.
       - Volumen del tetraedro: V_tet = (1/6) |[u, v, w]|.
    8. Renderizado 3D de alta fidelidad con Poly3DCollection (6 caras poligonales
       con semitransparencia), vectores generadores y vector normal ortogonal.
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
USS_BLUE = '#00205B'          # Primario institucional (arista u / base)
USS_GOLD = '#D4AF37'          # Secundario dorado (arista v / paralelogramo)
USS_ACCENT_BLUE = '#1E88E5'   # Azul de realce (arista w / altura)
USS_ACCENT_GREEN = '#27AE60'  # Verde de realce
USS_ACCENT_RED = '#C0392B'    # Rojo de realce (vector normal u x v)
USS_GRAY = '#7F8C8D'          # Gris auxiliar
USS_LIGHT_BG = '#F8F9FA'      # Fondo claro


# ==============================================================================
# 📐 FUNCIONES ANALÍTICAS Y COMPUTACIONALES
# ==============================================================================

def producto_cruz_numerico(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Calcula el producto cruz (vectorial) entre dos vectores u, v en R³.
    Fórmula por componentes:
    u x v = (u_y * v_z - u_z * v_y, u_z * v_x - u_x * v_z, u_x * v_y - u_y * v_x)
    """
    if len(u) != 3 or len(v) != 3:
        raise ValueError("El producto vectorial sólo está definido en R³.")
    return np.cross(u, v)


def producto_cruz_simbolico(u_sym: sp.Matrix, v_sym: sp.Matrix) -> sp.Matrix:
    """
    Calcula el producto cruz formal mediante el determinante simbólico 3x3:
    | i   j   k  |
    | u1  u2  u3 |
    | v1  v2  v3 |
    """
    i_sym, j_sym, k_sym = sp.symbols('i_hat j_hat k_hat')
    det_mat = sp.Matrix([
        [i_sym, j_sym, k_sym],
        [u_sym[0], u_sym[1], u_sym[2]],
        [v_sym[0], v_sym[1], v_sym[2]]
    ])
    # Expansión simbólica
    cx = u_sym[1]*v_sym[2] - u_sym[2]*v_sym[1]
    cy = -(u_sym[0]*v_sym[2] - u_sym[2]*v_sym[0])
    cz = u_sym[0]*v_sym[1] - u_sym[1]*v_sym[0]
    return sp.Matrix([cx, cy, cz])


def verificar_ortogonalidad_producto_cruz(u: np.ndarray, v: np.ndarray) -> dict:
    """
    Verifica que u x v sea estrictamente ortogonal tanto a u como a v:
    (u x v) · u == 0
    (u x v) · v == 0
    """
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
    ||u x v||² = ||u||² ||v||² - (u · v)²
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
    """
    Calcula el área del paralelogramo y del triángulo determinados por u y v.
    A_paralelogramo = ||u x v||
    A_triangulo     = (1/2) * ||u x v||
    """
    norm_c = float(np.linalg.norm(producto_cruz_numerico(u, v)))
    return norm_c, 0.5 * norm_c


def producto_mixto(u: np.ndarray, v: np.ndarray, w: np.ndarray) -> float:
    """
    Calcula el triple producto escalar (producto mixto) [u, v, w].
    Fórmula: [u, v, w] = u · (v x w) = det([u, v, w]^T)
    """
    mat = np.array([u, v, w])
    return float(np.linalg.det(mat))


def volumen_paralelepipedo_y_tetraedro(u: np.ndarray, v: np.ndarray, w: np.ndarray) -> tuple[float, float]:
    """
    Calcula los volúmenes del paralelepípedo y del tetraedro generados por u, v, w.
    V_paralelepipedo = |[u, v, w]|
    V_tetraedro      = (1/6) * |[u, v, w]|
    """
    pm = producto_mixto(u, v, w)
    vol_paral = abs(pm)
    vol_tet = vol_paral / 6.0
    return float(vol_paral), float(vol_tet)


# ==============================================================================
# 🧊 GENERACIÓN GEOMÉTRICA DE CARAS Y VÉRTICES DEL PARALELEPÍPEDO
# ==============================================================================

def generar_vertices_paralelepipedo(u: np.ndarray, v: np.ndarray, w: np.ndarray,
                                     origen: np.ndarray = np.array([0.0, 0.0, 0.0])) -> dict:
    """
    Calcula los 8 vértices del paralelepípedo sustentado por los vectores arista
    u, v, w a partir de un punto origen dado:
    V0 = O
    V1 = O + u
    V2 = O + u + v
    V3 = O + v
    V4 = O + w
    V5 = O + u + w
    V6 = O + u + v + w
    V7 = O + v + w
    """
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
    
    # Definición de las 6 caras poligonales cuadrangulares
    caras = [
        [v0, v1, v2, v3],  # Cara inferior (Z=0 relativa / base u-v)
        [v4, v5, v6, v7],  # Cara superior (paralela a base)
        [v0, v1, v5, v4],  # Cara frontal (plano u-w)
        [v2, v3, v7, v6],  # Cara trasera (plano u-w opuesto)
        [v0, v3, v7, v4],  # Cara lateral izquierda (plano v-w)
        [v1, v2, v6, v5]   # Cara lateral derecha (plano v-w opuesto)
    ]
    
    return {
        'vertices': vertices,
        'caras': caras,
        'v0': v0, 'v1': v1, 'v2': v2, 'v3': v3,
        'v4': v4, 'v5': v5, 'v6': v6, 'v7': v7
    }


# ==============================================================================
# 📊 VISUALIZACIÓN GRÁFICA 3D CIENTÍFICA
# ==============================================================================

def visualizar_paralelepipedo_3d(u: np.ndarray, v: np.ndarray, w: np.ndarray,
                                 guardar_ruta: str = "05_producto_cruz_y_paralelepipedos_3d.png") -> plt.Figure:
    """
    Renderiza un gráfico 3D científico de alta precisión con Matplotlib:
    1. Las 6 caras poligonales semitransparentes del paralelepípedo usando Poly3DCollection.
    2. Las 3 aristas generadoras u (USS Blue), v (USS Gold) y w (USS Accent Blue).
    3. El vector normal producto cruz u x v (USS Accent Red) erigido en la base.
    4. El paralelogramo de la base sombreado.
    5. Caja de texto con métricas analíticas (Área, Volumen, Ángulo).
    """
    fig = plt.figure(figsize=(15, 7), facecolor='white')
    
    # --------------------------------------------------------------------------
    # SUBPLOT 1: Renderizado 3D Completo del Paralelepípedo
    # --------------------------------------------------------------------------
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1.set_facecolor('white')
    ax1.set_title("1. Paralelepípedo 3D y Vector Normal\n" +
                  r"$\mathbf{u} \times \mathbf{v} \perp \mathbf{u}, \mathbf{v} \quad \text{y} \quad V = |[\mathbf{u}, \mathbf{v}, \mathbf{w}]|$",
                  fontsize=12, fontweight='bold', color=USS_BLUE, pad=15)
    
    # Generar geometría
    geom = generar_vertices_paralelepipedo(u, v, w)
    caras = geom['caras']
    
    # Caras del paralelepípedo con Poly3DCollection
    poly_collection = Poly3DCollection(caras, alpha=0.25, edgecolor=USS_BLUE, linewidths=1.2)
    poly_collection.set_facecolor(USS_GOLD)
    ax1.add_collection3d(poly_collection)
    
    # Resaltar cara base (u-v) con tono azulado semitransparente
    base_poly = Poly3DCollection([caras[0]], alpha=0.45, edgecolor=USS_BLUE, linewidths=2.0)
    base_poly.set_facecolor(USS_ACCENT_BLUE)
    ax1.add_collection3d(base_poly)
    
    # Quivers de vectores arista
    ax1.quiver(0, 0, 0, u[0], u[1], u[2], color=USS_BLUE, linewidth=3.5,
               arrow_length_ratio=0.12, label=r'$\mathbf{u} = (%g, %g, %g)$' % tuple(u))
    ax1.quiver(0, 0, 0, v[0], v[1], v[2], color=USS_GOLD, linewidth=3.5,
               arrow_length_ratio=0.12, label=r'$\mathbf{v} = (%g, %g, %g)$' % tuple(v))
    ax1.quiver(0, 0, 0, w[0], w[1], w[2], color=USS_ACCENT_GREEN, linewidth=3.5,
               arrow_length_ratio=0.12, label=r'$\mathbf{w} = (%g, %g, %g)$' % tuple(w))
    
    # Vector normal u x v
    uxv = producto_cruz_numerico(u, v)
    # Escalar para visualización proporcional si es muy grande
    norm_uxv = float(np.linalg.norm(uxv))
    escala_vis = min(1.0, max(np.linalg.norm(u), np.linalg.norm(v), np.linalg.norm(w)) / (norm_uxv + 1e-9))
    uxv_vis = uxv * escala_vis
    
    ax1.quiver(0, 0, 0, uxv_vis[0], uxv_vis[1], uxv_vis[2],
               color=USS_ACCENT_RED, linewidth=3.0, arrow_length_ratio=0.12,
               label=r'$\mathbf{u} \times \mathbf{v}$ (normal base)')
    
    # Vértices etiquetados
    ax1.scatter(geom['vertices'][:, 0], geom['vertices'][:, 1], geom['vertices'][:, 2],
                color=USS_BLUE, s=25, alpha=0.7)
    
    # Límites dinámicos
    all_pts = geom['vertices']
    all_pts_with_normal = np.vstack([all_pts, uxv_vis])
    margin = 0.5
    min_xyz = all_pts_with_normal.min(axis=0) - margin
    max_xyz = all_pts_with_normal.max(axis=0) + margin
    
    ax1.set_xlim(min_xyz[0], max_xyz[0])
    ax1.set_ylim(min_xyz[1], max_xyz[1])
    ax1.set_zlim(min_xyz[2], max_xyz[2])
    
    ax1.set_xlabel('Eje X', fontweight='bold', color=USS_BLUE)
    ax1.set_ylabel('Eje Y', fontweight='bold', color=USS_BLUE)
    ax1.set_zlabel('Eje Z', fontweight='bold', color=USS_BLUE)
    ax1.legend(loc='upper left', fontsize=8, framealpha=0.9)
    ax1.view_init(elev=20, azim=55)
    
    # --------------------------------------------------------------------------
    # SUBPLOT 2: Base Paralelogramo y Vista Proyectada / Cuadro Métrico
    # --------------------------------------------------------------------------
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_facecolor(USS_LIGHT_BG)
    ax2.set_title("2. Métricas Analíticas y Base Sustentada\n" +
                  "Área del Paralelogramo y Volumen del Paralelepípedo",
                  fontsize=12, fontweight='bold', color=USS_BLUE, pad=15)
    
    # Métricas
    area_paral, area_tri = area_paralelogramo_y_triangulo(u, v)
    vol_paral, vol_tet = volumen_paralelepipedo_y_tetraedro(u, v, w)
    ortog = verificar_ortogonalidad_producto_cruz(u, v)
    lagrange = verificar_identidad_lagrange(u, v)
    pm = producto_mixto(u, v, w)
    
    # Cuadro informativo de alta legibilidad
    cuadro_texto = (
        r"$\mathbf{DATOS\ DE\ ENTRADA:}$" + "\n"
        f" • Vector u = {u}\n"
        f" • Vector v = {v}\n"
        f" • Vector w = {w}\n\n"
        r"$\mathbf{PRODUCTO\ CRUZ\ \mathbf{u} \times \mathbf{v}:}$" + "\n"
        f" • u x v = {uxv}\n"
        f" • ||u x v|| = {norm_uxv:.4f}\n"
        f" • (u x v) · u = {ortog['dot_with_u']:.2e} (Ortogonal a u: {ortog['ortogonal_a_u']})\n"
        f" • (u x v) · v = {ortog['dot_with_v']:.2e} (Ortogonal a v: {ortog['ortogonal_a_v']})\n\n"
        r"$\mathbf{ÁREAS\ GEOMÉTRICAS:}$" + "\n"
        f" • Área Paralelogramo (Base) = {area_paral:.4f} [u²]\n"
        f" • Área Triángulo Sustentado = {area_tri:.4f} [u²]\n\n"
        r"$\mathbf{PRODUCTO\ MIXTO\ Y\ VOLÚMENES:}$" + "\n"
        f" • Triple Producto [u, v, w] = {pm:.4f}\n"
        f" • Volumen Paralelepípedo V = {vol_paral:.4f} [u³]\n"
        f" • Volumen Tetraedro V_tet  = {vol_tet:.4f} [u³]\n\n"
        r"$\mathbf{IDENTIDAD\ DE\ LAGRANGE:}$" + "\n"
        f" • ||u x v||² = {lagrange['norm_cross_sq']:.4f}\n"
        f" • ||u||²||v||² - (u·v)² = {lagrange['lagrange_rhs']:.4f}\n"
        f" • Identidad Satisfecha: {lagrange['valido']}"
    )
    
    ax2.text(0.05, 0.95, cuadro_texto, transform=ax2.transAxes,
             fontsize=10, verticalalignment='top', fontfamily='monospace',
             bbox=dict(boxstyle='round,pad=0.8', facecolor='white',
                       edgecolor=USS_GOLD, linewidth=2.0, alpha=0.95))
    
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
    print(" MÓDULO 05: PRODUCTO CRUZ, PRODUCTO MIXTO Y PARALELEPÍPEDOS 3D")
    print("=" * 80)
    
    # --------------------------------------------------------------------------
    # 1. Demostración Simbólica con SymPy
    # --------------------------------------------------------------------------
    print("\n--- 1. DEMOSTRACIÓN SIMBÓLICA CON SYMPY ---")
    u1, u2, u3 = sp.symbols('u1 u2 u3', real=True)
    v1, v2, v3 = sp.symbols('v1 v2 v3', real=True)
    w1, w2, w3 = sp.symbols('w1 w2 w3', real=True)
    
    u_s = sp.Matrix([u1, u2, u3])
    v_s = sp.Matrix([v1, v2, v3])
    w_s = sp.Matrix([w1, w2, w3])
    
    cross_s = producto_cruz_simbolico(u_s, v_s)
    print(f"Expresión u x v = \n{cross_s}")
    
    # Comprobar ortogonalidad simbólica
    dot_u_s = sp.simplify(cross_s.dot(u_s))
    dot_v_s = sp.simplify(cross_s.dot(v_s))
    print(f"Demostración (u x v) · u = {dot_u_s}")
    print(f"Demostración (u x v) · v = {dot_v_s}")
    assert dot_u_s == 0 and dot_v_s == 0, "Error en ortogonalidad simbólica."
    print(" [OK] Ortogonalidad demostrada analíticamente para todo vector en R³.")
    
    # Anticonmutatividad
    cross_vu_s = producto_cruz_simbolico(v_s, u_s)
    anticonm = sp.simplify(cross_s + cross_vu_s)
    print(f"Anticonmutatividad u x v + v x u = {anticonm}")
    assert anticonm == sp.Matrix([0, 0, 0]), "Error en anticonmutatividad."
    print(" [OK] Anticonmutatividad u x v = -(v x u) comprobada con éxito.")
    
    # --------------------------------------------------------------------------
    # 2. Casos Numéricos y Métricas Geométricas
    # --------------------------------------------------------------------------
    print("\n--- 2. CÁLCULO NUMÉRICO Y VOLÚMENES ---")
    u = np.array([3.0, 0.0, 1.0])
    v = np.array([1.0, 2.0, 0.0])
    w = np.array([0.0, 1.0, 4.0])
    
    c = producto_cruz_numerico(u, v)
    area_p, area_t = area_paralelogramo_y_triangulo(u, v)
    vol_p, vol_t = volumen_paralelepipedo_y_tetraedro(u, v, w)
    pm = producto_mixto(u, v, w)
    
    print(f"Vector u = {u}")
    print(f"Vector v = {v}")
    print(f"Vector w = {w}")
    print(f"Producto cruz u x v = {c}")
    print(f"Área paralelogramo base = {area_p:.4f}")
    print(f"Área triángulo base     = {area_t:.4f}")
    print(f"Triple producto escalar [u,v,w] = {pm:.4f}")
    print(f"Volumen paralelepípedo  = {vol_p:.4f}")
    print(f"Volumen tetraedro       = {vol_t:.4f}")
    
    # --------------------------------------------------------------------------
    # 3. Generación Gráfica 3D
    # --------------------------------------------------------------------------
    print("\n--- 3. GENERACIÓN DE FIGURA MATPLOTLIB 3D ---")
    out_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "05_producto_cruz_y_paralelepipedos_3d.png")
    visualizar_paralelepipedo_3d(u, v, w, guardar_ruta=out_img)
    
    print("=" * 80)
    print(" MÓDULO 05 COMPLETADO CON ÉXITO")
    print("=" * 80)


if __name__ == '__main__':
    ejecucion_demostrativa()
