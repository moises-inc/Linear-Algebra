#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modulo 04: Vectores Fundamentos y Proyecciones en R2 y R3
Asignatura: Algebra Lineal (DCEX0007) - Universidad San Sebastian (USS)
Carrera: Ingenieria Civil Informatica
Docente: Carol Asencio Gonzalez
Estudiante: Moises Amundarain Romero
Paleta Institucional: USS Blue (#00205B), USS Gold (#D4AF37)

Proposito:
    1. Operaciones fundamentales en R2 y R3: suma, resta, norma y normalizacion.
    2. Producto escalar, calculo angular y verificacion de Cauchy-Schwarz.
    3. Cosenos directores en R3 e identidad pitagorica.
    4. Proyeccion ortogonal de u sobre v, componente u_perp, y verificacion de:
       - Ortogonalidad: u_perp . v == 0
       - Teorema de Pitagoras: ||u||^2 == ||proj_v(u)||^2 + ||u_perp||^2
    5. Generacion de graficos cientificos individuales e independientes.
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


def norma_vector(v: np.ndarray) -> float:
    """Calcula la norma euclidiana de un vector."""
    return float(np.linalg.norm(v))


def vector_unitario(v: np.ndarray) -> np.ndarray:
    """Calcula el vector unitario en la direccion de v."""
    n = norma_vector(v)
    if np.isclose(n, 0.0):
        raise ValueError("No se puede normalizar el vector nulo.")
    return v / n


def producto_punto(u: np.ndarray, v: np.ndarray) -> float:
    """Calcula el producto escalar entre u y v."""
    return float(np.dot(u, v))


def angulo_entre_vectores(u: np.ndarray, v: np.ndarray) -> tuple[float, float]:
    """Calcula el angulo no dirigido theta entre u y v en radianes y grados."""
    nu = norma_vector(u)
    nv = norma_vector(v)
    if np.isclose(nu, 0.0) or np.isclose(nv, 0.0):
        raise ValueError("El angulo no esta definido para vectores nulos.")
    cos_theta = np.clip(producto_punto(u, v) / (nu * nv), -1.0, 1.0)
    theta_rad = float(np.arccos(cos_theta))
    theta_deg = float(np.degrees(theta_rad))
    return theta_rad, theta_deg


def proyeccion_ortogonal(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Calcula la proyeccion ortogonal de u sobre v: proj_v(u) = ((u . v) / ||v||^2) * v."""
    nv2 = producto_punto(v, v)
    if np.isclose(nv2, 0.0):
        raise ValueError("No se puede proyectar sobre el vector nulo.")
    return (producto_punto(u, v) / nv2) * v


def componente_ortogonal(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Calcula la componente perpendicular: u_perp = u - proj_v(u)."""
    return u - proyeccion_ortogonal(u, v)


def cosenos_directores_3d(v: np.ndarray) -> dict:
    """Calcula cosenos directores y angulos respecto a los ejes canonicos en R3."""
    if len(v) != 3:
        raise ValueError("El vector debe pertenecer a R3.")
    nv = norma_vector(v)
    if np.isclose(nv, 0.0):
        raise ValueError("El vector nulo no posee cosenos directores definidos.")
    cos_a = v[0] / nv
    cos_b = v[1] / nv
    cos_c = v[2] / nv
    sum_sq = cos_a**2 + cos_b**2 + cos_c**2
    return {
        'cos_alpha': float(cos_a),
        'cos_beta': float(cos_b),
        'cos_gamma': float(cos_c),
        'alpha_deg': float(np.degrees(np.arccos(np.clip(cos_a, -1.0, 1.0)))),
        'beta_deg': float(np.degrees(np.arccos(np.clip(cos_b, -1.0, 1.0)))),
        'gamma_deg': float(np.degrees(np.arccos(np.clip(cos_c, -1.0, 1.0)))),
        'suma_cuadrados': float(sum_sq)
    }


def verificar_descomposicion_ortogonal(u: np.ndarray, v: np.ndarray) -> dict:
    """Verifica computacionalmente las propiedades de la descomposicion ortogonal."""
    proj = proyeccion_ortogonal(u, v)
    u_perp = componente_ortogonal(u, v)
    
    reconstruccion_error = float(np.linalg.norm(u - (proj + u_perp)))
    dot_perp_v = float(abs(producto_punto(u_perp, v)))
    
    norm_u_sq = norma_vector(u)**2
    norm_proj_sq = norma_vector(proj)**2
    norm_perp_sq = norma_vector(u_perp)**2
    pitagoras_diff = float(abs(norm_u_sq - (norm_proj_sq + norm_perp_sq)))
    
    dot_uv = abs(producto_punto(u, v))
    cauchy_lim = norma_vector(u) * norma_vector(v)
    cauchy_valido = bool(dot_uv <= cauchy_lim + 1e-12)
    
    return {
        'u': u,
        'v': v,
        'proj': proj,
        'u_perp': u_perp,
        'reconstruccion_ok': bool(reconstruccion_error < 1e-12),
        'ortogonalidad_ok': bool(dot_perp_v < 1e-12),
        'pitagoras_ok': bool(pitagoras_diff < 1e-12),
        'cauchy_schwarz_ok': cauchy_valido,
        'dot_perp_v': dot_perp_v,
        'pitagoras_diff': pitagoras_diff
    }


def generar_grafico_operaciones_2d(u: np.ndarray, v: np.ndarray,
                                    guardar_ruta: str = "04_vectores_operaciones_2d.png") -> plt.Figure:
    """
    Genera una figura individual cientifica para operaciones en R2:
    Suma (regla del paralelogramo), resta y vectores fundamentales.
    """
    fig, ax = plt.subplots(figsize=(8, 7), facecolor='white')
    ax.set_facecolor(USS_LIGHT_BG)
    ax.set_title("Operaciones Vectoriales en R2: Suma y Resta",
                 fontsize=13, fontweight='bold', color=USS_BLUE, pad=14)
    
    suma = u + v
    resta = u - v
    
    # Ejes de coordenadas
    ax.axhline(0, color=USS_GRAY, linewidth=0.9, linestyle='--')
    ax.axvline(0, color=USS_GRAY, linewidth=0.9, linestyle='--')
    
    # Lineas del paralelogramo
    ax.plot([u[0], suma[0]], [u[1], suma[1]], color=USS_GOLD, linestyle=':', linewidth=1.6, label='_nolegend_')
    ax.plot([v[0], suma[0]], [v[1], suma[1]], color=USS_BLUE, linestyle=':', linewidth=1.6, label='_nolegend_')
    
    # Vectores u y v
    ax.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1,
              color=USS_BLUE, width=0.016, label=f"u = ({u[0]:g}, {u[1]:g})")
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1,
              color=USS_GOLD, width=0.016, label=f"v = ({v[0]:g}, {v[1]:g})")
    
    # Vector suma (diagonal principal)
    ax.quiver(0, 0, suma[0], suma[1], angles='xy', scale_units='xy', scale=1,
              color=USS_ACCENT_GREEN, width=0.015, label=f"u + v = ({suma[0]:g}, {suma[1]:g})")
    
    # Vector resta (diagonal secundaria desplazada a v)
    ax.quiver(v[0], v[1], resta[0], resta[1], angles='xy', scale_units='xy', scale=1,
              color=USS_ACCENT_RED, width=0.013, label=f"u - v (diagonal)")
    
    # Indicador de angulo theta
    theta_rad_u = np.arctan2(u[1], u[0])
    theta_rad_v = np.arctan2(v[1], v[0])
    arc_rad = min(norma_vector(u), norma_vector(v)) * 0.35
    t_arc = np.linspace(min(theta_rad_u, theta_rad_v), max(theta_rad_u, theta_rad_v), 30)
    ax.plot(arc_rad * np.cos(t_arc), arc_rad * np.sin(t_arc), color=USS_BLUE, linewidth=1.4)
    _, theta_deg = angulo_entre_vectores(u, v)
    ax.text(arc_rad * 1.3 * np.cos(np.mean(t_arc)), arc_rad * 1.3 * np.sin(np.mean(t_arc)),
            f"theta = {theta_deg:.1f} deg", fontsize=9.5, fontweight='bold', color=USS_BLUE)
    
    lims_x = [0, u[0], v[0], suma[0]]
    lims_y = [0, u[1], v[1], suma[1]]
    margin = 1.5
    ax.set_xlim(min(lims_x) - margin, max(lims_x) + margin)
    ax.set_ylim(min(lims_y) - margin, max(lims_y) + margin)
    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_xlabel("Eje X", fontsize=10.5, color=USS_BLUE)
    ax.set_ylabel("Eje Y", fontsize=10.5, color=USS_BLUE)
    ax.legend(loc='upper left', fontsize=9, framealpha=0.95)
    
    plt.tight_layout()
    plt.savefig(guardar_ruta, dpi=300, bbox_inches='tight')
    plt.close(fig)
    return fig


def generar_grafico_proyeccion_ortogonal_3d(u: np.ndarray, v: np.ndarray,
                                            guardar_ruta: str = "04_vectores_proyeccion_ortogonal_3d.png") -> plt.Figure:
    """
    Genera una figura individual cientifica para la proyeccion ortogonal en R3:
    Vectores u, v, proj_v(u) y componente perpendicular u_perp con caida punteada.
    """
    proj = proyeccion_ortogonal(u, v)
    perp = componente_ortogonal(u, v)
    
    fig = plt.figure(figsize=(9, 8), facecolor='white')
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_facecolor('white')
    ax.set_title("Proyeccion Ortogonal en R3: u = proj_v(u) + u_perp",
                 fontsize=13, fontweight='bold', color=USS_BLUE, pad=16)
    
    # Origen
    ax.scatter([0], [0], [0], color='black', s=35, label='Origen O(0,0,0)')
    
    # Vector u
    ax.quiver(0, 0, 0, u[0], u[1], u[2], color=USS_BLUE, linewidth=2.8,
              arrow_length_ratio=0.10, label=f"u = ({u[0]:g}, {u[1]:g}, {u[2]:g})")
    
    # Vector v
    ax.quiver(0, 0, 0, v[0], v[1], v[2], color=USS_GOLD, linewidth=2.8,
              arrow_length_ratio=0.10, label=f"v = ({v[0]:g}, {v[1]:g}, {v[2]:g})")
    
    # Proyeccion proj_v(u)
    ax.quiver(0, 0, 0, proj[0], proj[1], proj[2], color=USS_ACCENT_GREEN, linewidth=3.2,
              arrow_length_ratio=0.10, label=f"proj_v(u) = ({proj[0]:.2f}, {proj[1]:.2f}, {proj[2]:.2f})")
    
    # Caida ortogonal (segmento punteado desde u hasta proj)
    ax.plot([u[0], proj[0]], [u[1], proj[1]], [u[2], proj[2]],
            color=USS_ACCENT_RED, linestyle='--', linewidth=2.0,
            label='Segmento proyectante u_perp')
    
    # Componente u_perp erigida desde proj
    ax.quiver(proj[0], proj[1], proj[2], perp[0], perp[1], perp[2],
              color=USS_ACCENT_RED, linewidth=2.2, arrow_length_ratio=0.12,
              label=f"u_perp = ({perp[0]:.2f}, {perp[1]:.2f}, {perp[2]:.2f})")
    
    # Marcadores en extremos
    ax.scatter([u[0], proj[0]], [u[1], proj[1]], [u[2], proj[2]],
               color=[USS_BLUE, USS_ACCENT_GREEN], s=40, edgecolors='black')
    
    # Linea soporte de v
    v_dir = vector_unitario(v)
    t_vals = np.linspace(-1.5, norma_vector(v) + 1.5, 40)
    ax.plot(t_vals * v_dir[0], t_vals * v_dir[1], t_vals * v_dir[2],
            color=USS_GRAY, linestyle=':', linewidth=1.0, label='Recta soporte de v')
    
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
    print("Modulo 04: Vectores Fundamentos y Proyecciones en R2 y R3")
    print("Universidad San Sebastian - Departamento de Ciencias Exactas")
    
    # 1. Demostracion Simbolica con SymPy
    print("\n--- 1. DEMOSTRACION SIMBOLICA CON SYMPY ---")
    u1, u2, u3 = sp.symbols('u1 u2 u3', real=True)
    v1, v2, v3 = sp.symbols('v1 v2 v3', real=True)
    
    u_sym = sp.Matrix([u1, u2, u3])
    v_sym = sp.Matrix([v1, v2, v3])
    
    dot_sym = u_sym.dot(v_sym)
    norm_v_sq_sym = v_sym.dot(v_sym)
    proj_sym = (dot_sym / norm_v_sq_sym) * v_sym
    perp_sym = u_sym - proj_sym
    
    ortogonalidad_simbolica = sp.simplify(perp_sym.dot(v_sym))
    print(f"Formula: proj_v(u) = (u . v / ||v||^2) * v")
    print(f"Ortogonalidad simbolica: u_perp . v = {ortogonalidad_simbolica}")
    assert ortogonalidad_simbolica == 0, "Error en demostracion simbolica."
    print("[OK] Teorema de ortogonalidad demostrado analiticamente.")
    
    # 2. Calculos Numericos en R2
    print("\n--- 2. CALCULOS NUMERICOS EN R2 ---")
    u_2d = np.array([4.0, 3.0])
    v_2d = np.array([6.0, 1.0])
    
    res_2d = verificar_descomposicion_ortogonal(u_2d, v_2d)
    theta_rad, theta_deg = angulo_entre_vectores(u_2d, v_2d)
    
    print(f"Vector u = {u_2d}")
    print(f"Vector v = {v_2d}")
    print(f"Norma ||u|| = {norma_vector(u_2d):.4f}")
    print(f"Norma ||v|| = {norma_vector(v_2d):.4f}")
    print(f"u . v = {producto_punto(u_2d, v_2d):.4f}")
    print(f"Angulo theta = {theta_deg:.2f} deg ({theta_rad:.4f} rad)")
    print(f"proj_v(u) = {res_2d['proj']}")
    print(f"u_perp    = {res_2d['u_perp']}")
    print(f"u_perp . v = {res_2d['dot_perp_v']:.2e}")
    print(f"Pitagoras ||u||^2 == ||proj||^2 + ||u_perp||^2: error {res_2d['pitagoras_diff']:.2e}")
    print(f"Cauchy-Schwarz valido: {res_2d['cauchy_schwarz_ok']}")
    
    # 3. Calculos Numericos en R3 y Cosenos Directores
    print("\n--- 3. CALCULOS NUMERICOS EN R3 Y COSENOS DIRECTORES ---")
    u_3d = np.array([3.0, -2.0, 5.0])
    v_3d = np.array([1.0, 4.0, 2.0])
    
    res_3d = verificar_descomposicion_ortogonal(u_3d, v_3d)
    cd = cosenos_directores_3d(u_3d)
    
    print(f"Vector u = {u_3d}")
    print(f"Vector v = {v_3d}")
    print(f"proj_v(u) = {res_3d['proj']}")
    print(f"u_perp    = {res_3d['u_perp']}")
    print(f"u_perp . v = {res_3d['dot_perp_v']:.2e}")
    print(f"Cosenos directores de u: cos(alpha)={cd['cos_alpha']:.4f}, cos(beta)={cd['cos_beta']:.4f}, cos(gamma)={cd['cos_gamma']:.4f}")
    print(f"Angulos directores: alpha={cd['alpha_deg']:.2f} deg, beta={cd['beta_deg']:.2f} deg, gamma={cd['gamma_deg']:.2f} deg")
    print(f"Suma de cosenos al cuadrado: {cd['suma_cuadrados']:.6f}")
    
    # 4. Generacion de Figuras
    print("\n--- 4. GENERACION DE FIGURAS CIENTIFICAS INDIVIDUALES ---")
    dir_base = os.path.dirname(os.path.abspath(__file__))
    ruta_2d = os.path.join(dir_base, "04_vectores_operaciones_2d.png")
    ruta_3d = os.path.join(dir_base, "04_vectores_proyeccion_ortogonal_3d.png")
    
    generar_grafico_operaciones_2d(u_2d, v_2d, guardar_ruta=ruta_2d)
    print(f"Grafico 2D guardado: {ruta_2d}")
    
    generar_grafico_proyeccion_ortogonal_3d(u_3d, v_3d, guardar_ruta=ruta_3d)
    print(f"Grafico 3D guardado: {ruta_3d}")
    
    print("\nModulo 04 ejecutado con exito.")


if __name__ == '__main__':
    ejecucion_demostrativa()
