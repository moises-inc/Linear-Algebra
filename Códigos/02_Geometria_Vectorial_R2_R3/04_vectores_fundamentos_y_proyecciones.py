#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
MÓDULO 04: VECTORES FUNDAMENTOS Y PROYECCIONES ORTOGONALES EN R² Y R³
Asignatura: Álgebra Lineal (DCEX0007) — Universidad San Sebastián (USS)
Carrera: Ingeniería Civil Informática
Docente: Carol Asencio González
Estudiante: Moisés Amundarain Romero
Paleta Institucional: USS Blue (#00205B), USS Gold (#D4AF37)
================================================================================
Propósito del Módulo:
    Modelar, calcular analíticamente y visualizar interactivamente:
    1. Operaciones fundamentales en R² y R³: suma (regla del paralelogramo),
       resta, ponderación por escalar, norma euclidiana y normalización.
    2. Producto escalar (punto), ángulo entre vectores y verificación de
       la desigualdad de Cauchy-Schwarz.
    3. Cosenos directores en R³ y verificación de la identidad pitagórica.
    4. Proyección ortogonal de un vector u sobre un vector v, componente
       ortogonal u_perp = u - proj_v(u), y verificación estricta de:
       - Ortogonalidad: u_perp · v == 0
       - Pitágoras vectorial: ||u||² == ||proj_v(u)||² + ||u_perp||²
    5. Visualización dual (2D y 3D) de alta resolución con Matplotlib.
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
from matplotlib.patches import Arc

# ==============================================================================
# 🎨 PALETA DE COLORES INSTITUCIONAL USS
# ==============================================================================
USS_BLUE = '#00205B'          # Color primario institucional
USS_GOLD = '#D4AF37'          # Color secundario dorado
USS_ACCENT_BLUE = '#1E88E5'   # Azul de realce
USS_ACCENT_GREEN = '#27AE60'  # Verde de realce / proyecciones
USS_ACCENT_RED = '#C0392B'    # Rojo de alerta / ortogonalidad
USS_GRAY = '#7F8C8D'          # Gris auxiliar
USS_LIGHT_BG = '#F8F9FA'      # Fondo claro para estética limpia


# ==============================================================================
# 📐 FUNCIONES MATEMÁTICAS ANALÍTICAS Y NUMÉRICAS
# ==============================================================================

def norma_vector(v: np.ndarray) -> float:
    """
    Calcula la norma euclidiana (longitud) de un vector en R^n.
    Fórmula: ||v|| = sqrt(sum(v_i^2))
    """
    return float(np.linalg.norm(v))


def vector_unitario(v: np.ndarray) -> np.ndarray:
    """
    Calcula el vector unitario (versor) en la dirección de v.
    Fórmula: v_hat = v / ||v||
    Lanza ValueError si el vector es nulo.
    """
    n = norma_vector(v)
    if np.isclose(n, 0.0):
        raise ValueError("No se puede normalizar el vector nulo (norma cero).")
    return v / n


def producto_punto(u: np.ndarray, v: np.ndarray) -> float:
    """
    Calcula el producto escalar (punto) entre u y v.
    Fórmula: u · v = sum(u_i * v_i)
    """
    return float(np.dot(u, v))


def angulo_entre_vectores(u: np.ndarray, v: np.ndarray) -> tuple[float, float]:
    """
    Calcula el ángulo no dirigido theta entre u y v.
    Fórmula: cos(theta) = (u · v) / (||u|| * ||v||)
    Retorna: (theta_rad, theta_deg)
    """
    nu = norma_vector(u)
    nv = norma_vector(v)
    if np.isclose(nu, 0.0) or np.isclose(nv, 0.0):
        raise ValueError("El ángulo no está definido para vectores nulos.")
    cos_theta = np.clip(producto_punto(u, v) / (nu * nv), -1.0, 1.0)
    theta_rad = float(np.arccos(cos_theta))
    theta_deg = float(np.degrees(theta_rad))
    return theta_rad, theta_deg


def proyeccion_ortogonal(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Calcula la proyección ortogonal del vector u sobre el vector v.
    Fórmula: proj_v(u) = [(u · v) / (||v||^2)] * v
    """
    nv2 = producto_punto(v, v)
    if np.isclose(nv2, 0.0):
        raise ValueError("No se puede proyectar sobre el vector nulo.")
    escalar_proy = producto_punto(u, v) / nv2
    return escalar_proy * v


def componente_ortogonal(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Calcula la componente ortogonal (u_perp) de u respecto a v.
    Fórmula: u_perp = u - proj_v(u)
    Propiedad fundamental: u_perp · v == 0
    """
    return u - proyeccion_ortogonal(u, v)


def cosenos_directores_3d(v: np.ndarray) -> dict:
    """
    Calcula los cosenos directores y ángulos directores de un vector v en R³.
    alpha: ángulo con eje X (i)
    beta:  ángulo con eje Y (j)
    gamma: ángulo con eje Z (k)
    Propiedad: cos^2(alpha) + cos^2(beta) + cos^2(gamma) == 1
    """
    if len(v) != 3:
        raise ValueError("El vector debe pertenecer a R³ para cosenos directores.")
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
    """
    Verifica computacionalmente todas las propiedades de la proyección ortogonal:
    1. Reconstrucción: u == proj_v(u) + u_perp
    2. Ortogonalidad estricta: u_perp · v == 0
    3. Teorema de Pitágoras: ||u||² == ||proj_v(u)||² + ||u_perp||²
    4. Desigualdad de Cauchy-Schwarz: |u · v| <= ||u|| * ||v||
    """
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
        'pitagoras_diff': pitagoras_diff,
        'escalar_proyeccion': float(producto_punto(u, v) / norma_vector(v))
    }


# ==============================================================================
# 📊 VISUALIZACIÓN GRÁFICA MULTI-PANEL (2D Y 3D)
# ==============================================================================

def generar_visualizacion_completa(u_2d: np.ndarray, v_2d: np.ndarray,
                                   u_3d: np.ndarray, v_3d: np.ndarray,
                                   guardar_ruta: str = "04_vectores_fundamentos_y_proyecciones.png") -> plt.Figure:
    """
    Genera un panel gráfico integral de 3 visualizaciones científicas:
    Panel 1: Álgebra Vectorial 2D (Suma por Regla del Paralelogramo y Resta).
    Panel 2: Descomposición y Proyección Ortogonal en R² con Ángulo theta.
    Panel 3: Proyección Ortogonal en el Espacio R³ con Quiver 3D.
    """
    fig = plt.figure(figsize=(18, 6), facecolor='white')
    
    # --------------------------------------------------------------------------
    # SUBPLOT 1: Suma y Resta Vectorial 2D (Regla del Paralelogramo)
    # --------------------------------------------------------------------------
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.set_facecolor(USS_LIGHT_BG)
    ax1.set_title("1. Álgebra Vectorial en R²\nSuma (Paralelogramo) y Resta",
                  fontsize=12, fontweight='bold', color=USS_BLUE, pad=12)
    
    suma = u_2d + v_2d
    resta = u_2d - v_2d
    
    # Ejes principales
    ax1.axhline(0, color=USS_GRAY, linewidth=0.8, linestyle='--')
    ax1.axvline(0, color=USS_GRAY, linewidth=0.8, linestyle='--')
    
    # Vectores principales
    ax1.quiver(0, 0, u_2d[0], u_2d[1], angles='xy', scale_units='xy', scale=1,
               color=USS_BLUE, width=0.018, label=r'$\mathbf{u} = (%g, %g)$' % (u_2d[0], u_2d[1]))
    ax1.quiver(0, 0, v_2d[0], v_2d[1], angles='xy', scale_units='xy', scale=1,
               color=USS_GOLD, width=0.018, label=r'$\mathbf{v} = (%g, %g)$' % (v_2d[0], v_2d[1]))
    
    # Paralelogramo punteado
    ax1.plot([u_2d[0], suma[0]], [u_2d[1], suma[1]], color=USS_GOLD, linestyle=':', linewidth=1.5)
    ax1.plot([v_2d[0], suma[0]], [v_2d[1], suma[1]], color=USS_BLUE, linestyle=':', linewidth=1.5)
    
    # Vector suma (diagonal principal)
    ax1.quiver(0, 0, suma[0], suma[1], angles='xy', scale_units='xy', scale=1,
               color=USS_ACCENT_GREEN, width=0.016, label=r'$\mathbf{u}+\mathbf{v} = (%g, %g)$' % (suma[0], suma[1]))
    
    # Vector resta
    ax1.quiver(v_2d[0], v_2d[1], resta[0], resta[1], angles='xy', scale_units='xy', scale=1,
               color=USS_ACCENT_RED, width=0.014,
               label=r'$\mathbf{u}-\mathbf{v}$ (diagonal menor)')
    
    lims_x = [0, u_2d[0], v_2d[0], suma[0]]
    lims_y = [0, u_2d[1], v_2d[1], suma[1]]
    margin = 1.5
    ax1.set_xlim(min(lims_x) - margin, max(lims_x) + margin)
    ax1.set_ylim(min(lims_y) - margin, max(lims_y) + margin)
    ax1.set_aspect('equal')
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(loc='upper left', fontsize=8, framealpha=0.9)
    ax1.set_xlabel('Eje X', fontsize=10, color=USS_BLUE)
    ax1.set_ylabel('Eje Y', fontsize=10, color=USS_BLUE)
    
    # --------------------------------------------------------------------------
    # SUBPLOT 2: Proyección Ortogonal en R²
    # --------------------------------------------------------------------------
    ax2 = fig.add_subplot(1, 3, 2)
    ax2.set_facecolor(USS_LIGHT_BG)
    ax2.set_title("2. Proyección Ortogonal en R²\n" + r"$\mathbf{u} = \operatorname{proj}_{\mathbf{v}}(\mathbf{u}) + \mathbf{u}_{\perp}$",
                  fontsize=12, fontweight='bold', color=USS_BLUE, pad=12)
    
    ax2.axhline(0, color=USS_GRAY, linewidth=0.8, linestyle='--')
    ax2.axvline(0, color=USS_GRAY, linewidth=0.8, linestyle='--')
    
    proj_2d = proyeccion_ortogonal(u_2d, v_2d)
    perp_2d = componente_ortogonal(u_2d, v_2d)
    _, theta_deg = angulo_entre_vectores(u_2d, v_2d)
    
    # Línea soporte de v
    v_unit = vector_unitario(v_2d)
    t_vals = np.linspace(-1, max(norma_vector(v_2d), norma_vector(proj_2d)) + 2, 50)
    soporte_x = t_vals * v_unit[0]
    soporte_y = t_vals * v_unit[1]
    ax2.plot(soporte_x, soporte_y, color=USS_GRAY, linestyle='-.', linewidth=1.0, label='Línea soporte de v')
    
    # Vectores u y v
    ax2.quiver(0, 0, u_2d[0], u_2d[1], angles='xy', scale_units='xy', scale=1,
               color=USS_BLUE, width=0.018, label=r'$\mathbf{u}$')
    ax2.quiver(0, 0, v_2d[0], v_2d[1], angles='xy', scale_units='xy', scale=1,
               color=USS_GOLD, width=0.018, label=r'$\mathbf{v}$')
    
    # Vector proyección
    ax2.quiver(0, 0, proj_2d[0], proj_2d[1], angles='xy', scale_units='xy', scale=1,
               color=USS_ACCENT_GREEN, width=0.022,
               label=r'$\operatorname{proj}_{\mathbf{v}}(\mathbf{u}) = (%.2f, %.2f)$' % (proj_2d[0], proj_2d[1]))
    
    # Línea punteada de caída ortogonal
    ax2.plot([u_2d[0], proj_2d[0]], [u_2d[1], proj_2d[1]], color=USS_ACCENT_RED,
             linestyle=':', linewidth=2.0, label=r'Línea proyectante $\perp$')
    
    # Componente ortogonal situada desde el origen
    ax2.quiver(0, 0, perp_2d[0], perp_2d[1], angles='xy', scale_units='xy', scale=1,
               color=USS_ACCENT_RED, width=0.016,
               label=r'$\mathbf{u}_{\perp} = (%.2f, %.2f)$' % (perp_2d[0], perp_2d[1]))
    
    # Indicador de ángulo theta
    theta_rad_u = np.arctan2(u_2d[1], u_2d[0])
    theta_rad_v = np.arctan2(v_2d[1], v_2d[0])
    arc_rad = min(norma_vector(u_2d), norma_vector(v_2d)) * 0.35
    t_arc = np.linspace(min(theta_rad_u, theta_rad_v), max(theta_rad_u, theta_rad_v), 30)
    ax2.plot(arc_rad * np.cos(t_arc), arc_rad * np.sin(t_arc), color=USS_BLUE, linewidth=1.5)
    ax2.text(arc_rad * 1.25 * np.cos(np.mean(t_arc)), arc_rad * 1.25 * np.sin(np.mean(t_arc)),
             r'$\theta = %.1f^\circ$' % theta_deg, fontsize=9, fontweight='bold', color=USS_BLUE)
    
    all_x = [0, u_2d[0], v_2d[0], proj_2d[0], perp_2d[0]]
    all_y = [0, u_2d[1], v_2d[1], proj_2d[1], perp_2d[1]]
    ax2.set_xlim(min(all_x) - 1.5, max(all_x) + 1.5)
    ax2.set_ylim(min(all_y) - 1.5, max(all_y) + 1.5)
    ax2.set_aspect('equal')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc='upper left', fontsize=8, framealpha=0.9)
    ax2.set_xlabel('Eje X', fontsize=10, color=USS_BLUE)
    ax2.set_ylabel('Eje Y', fontsize=10, color=USS_BLUE)
    
    # --------------------------------------------------------------------------
    # SUBPLOT 3: Proyección Ortogonal en R³ (3D)
    # --------------------------------------------------------------------------
    ax3 = fig.add_subplot(1, 3, 3, projection='3d')
    ax3.set_facecolor('white')
    ax3.set_title("3. Proyección Ortogonal en R³\n" + r"$\mathbf{u}_{\perp} \cdot \mathbf{v} = 0$",
                  fontsize=12, fontweight='bold', color=USS_BLUE, pad=12)
    
    proj_3d = proyeccion_ortogonal(u_3d, v_3d)
    perp_3d = componente_ortogonal(u_3d, v_3d)
    
    # Ejes coordenados 3D
    ax3.plot([0, 0], [0, 0], [0, 0], 'k.')
    
    # Quivers 3D
    ax3.quiver(0, 0, 0, u_3d[0], u_3d[1], u_3d[2], color=USS_BLUE, linewidth=2.5,
               arrow_length_ratio=0.1, label=r'$\mathbf{u} = (%g, %g, %g)$' % tuple(u_3d))
    ax3.quiver(0, 0, 0, v_3d[0], v_3d[1], v_3d[2], color=USS_GOLD, linewidth=2.5,
               arrow_length_ratio=0.1, label=r'$\mathbf{v} = (%g, %g, %g)$' % tuple(v_3d))
    ax3.quiver(0, 0, 0, proj_3d[0], proj_3d[1], proj_3d[2], color=USS_ACCENT_GREEN, linewidth=3.0,
               arrow_length_ratio=0.1, label=r'$\operatorname{proj}_{\mathbf{v}}(\mathbf{u})$')
    ax3.quiver(proj_3d[0], proj_3d[1], proj_3d[2],
               perp_3d[0], perp_3d[1], perp_3d[2],
               color=USS_ACCENT_RED, linewidth=2.0,
               arrow_length_ratio=0.1, label=r'$\mathbf{u}_{\perp}$ (segmento)')
    
    # Línea soporte de v en 3D
    v3_unit = vector_unitario(v_3d)
    t_3d = np.linspace(-1, norma_vector(v_3d) + 1, 40)
    ax3.plot(t_3d * v3_unit[0], t_3d * v3_unit[1], t_3d * v3_unit[2],
             color=USS_GRAY, linestyle='--', linewidth=0.8)
    
    # Etiquetas y límites
    ax3.set_xlabel('X', fontweight='bold', color=USS_BLUE)
    ax3.set_ylabel('Y', fontweight='bold', color=USS_BLUE)
    ax3.set_zlabel('Z', fontweight='bold', color=USS_BLUE)
    ax3.legend(loc='upper left', fontsize=7, framealpha=0.9)
    ax3.view_init(elev=25, azim=45)
    
    plt.tight_layout()
    plt.savefig(guardar_ruta, dpi=300, bbox_inches='tight')
    print(f" [Gráfico Guardado]: {guardar_ruta}")
    
    if os.environ.get('DISPLAY', '') != '' and os.environ.get('HEADLESS', '') != '1':
        plt.show()
    
    return fig


# ==============================================================================
# 🚀 DEMOSTRACIÓN SIMBÓLICA Y NUMÉRICA
# ==============================================================================

def ejecucion_demostrativa():
    print("=" * 80)
    print(" UNIVERSIDAD SAN SEBASTIÁN — DEPARTAMENTO DE CIENCIAS EXACTAS")
    print(" MÓDULO 04: VECTORES FUNDAMENTOS Y PROYECCIONES EN R² Y R³")
    print("=" * 80)
    
    # --------------------------------------------------------------------------
    # 1. Verificación Simbólica con SymPy
    # --------------------------------------------------------------------------
    print("\n--- 1. DEMOSTRACIÓN SIMBÓLICA CON SYMPY ---")
    u1, u2, u3 = sp.symbols('u1 u2 u3', real=True)
    v1, v2, v3 = sp.symbols('v1 v2 v3', real=True)
    
    u_sym = sp.Matrix([u1, u2, u3])
    v_sym = sp.Matrix([v1, v2, v3])
    
    dot_sym = u_sym.dot(v_sym)
    norm_v_sq_sym = v_sym.dot(v_sym)
    proj_sym = (dot_sym / norm_v_sq_sym) * v_sym
    perp_sym = u_sym - proj_sym
    
    # Verificación de ortogonalidad simbólica: perp · v == 0
    ortogonalidad_simbolica = sp.simplify(perp_sym.dot(v_sym))
    print(f"Fórmula proj_v(u) = (u · v / ||v||²) * v")
    print(f"Ortogonalidad Simbólica: u_perp · v = {ortogonalidad_simbolica}")
    assert ortogonalidad_simbolica == 0, "Error en demostración simbólica."
    print(" [OK] Teorema de ortogonalidad de la proyección demostrado analíticamente.")
    
    # --------------------------------------------------------------------------
    # 2. Cálculos Numéricos en R²
    # --------------------------------------------------------------------------
    print("\n--- 2. CASO NUMÉRICO EN R² ---")
    u_2d = np.array([4.0, 3.0])
    v_2d = np.array([6.0, 1.0])
    
    res_2d = verificar_descomposicion_ortogonal(u_2d, v_2d)
    theta_rad, theta_deg = angulo_entre_vectores(u_2d, v_2d)
    
    print(f"Vector u = {u_2d}")
    print(f"Vector v = {v_2d}")
    print(f"Norma ||u|| = {norma_vector(u_2d):.4f}")
    print(f"Norma ||v|| = {norma_vector(v_2d):.4f}")
    print(f"u · v = {producto_punto(u_2d, v_2d):.4f}")
    print(f"Ángulo theta = {theta_deg:.2f}° ({theta_rad:.4f} rad)")
    print(f"proj_v(u) = {res_2d['proj']}")
    print(f"u_perp    = {res_2d['u_perp']}")
    print(f"Verificación u_perp · v = {res_2d['dot_perp_v']:.2e} (Debe ser 0)")
    print(f"Pitágoras ||u||² == ||proj||² + ||u_perp||²: Error = {res_2d['pitagoras_diff']:.2e}")
    print(f"Cauchy-Schwarz válido: {res_2d['cauchy_schwarz_ok']}")
    
    # --------------------------------------------------------------------------
    # 3. Cálculos Numéricos en R³ y Cosenos Directores
    # --------------------------------------------------------------------------
    print("\n--- 3. CASO NUMÉRICO EN R³ Y COSENOS DIRECTORES ---")
    u_3d = np.array([3.0, -2.0, 5.0])
    v_3d = np.array([1.0, 4.0, 2.0])
    
    res_3d = verificar_descomposicion_ortogonal(u_3d, v_3d)
    cd = cosenos_directores_3d(u_3d)
    
    print(f"Vector u = {u_3d}")
    print(f"Vector v = {v_3d}")
    print(f"proj_v(u) = {res_3d['proj']}")
    print(f"u_perp    = {res_3d['u_perp']}")
    print(f"Verificación u_perp · v = {res_3d['dot_perp_v']:.2e}")
    print(f"Cosenos directores de u: cos(alpha)={cd['cos_alpha']:.4f}, cos(beta)={cd['cos_beta']:.4f}, cos(gamma)={cd['cos_gamma']:.4f}")
    print(f"Ángulos directores: alpha={cd['alpha_deg']:.2f}°, beta={cd['beta_deg']:.2f}°, gamma={cd['gamma_deg']:.2f}°")
    print(f"Suma de cosenos al cuadrado: {cd['suma_cuadrados']:.6f} (Debe ser exactamente 1.0)")
    
    # --------------------------------------------------------------------------
    # 4. Renderizado Gráfico
    # --------------------------------------------------------------------------
    print("\n--- 4. GENERACIÓN DE FIGURA MATPLOTLIB ---")
    out_img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "04_vectores_fundamentos_y_proyecciones.png")
    generar_visualizacion_completa(u_2d, v_2d, u_3d, v_3d, guardar_ruta=out_img)
    print("=" * 80)
    print(" MÓDULO 04 COMPLETADO CON ÉXITO")
    print("=" * 80)


if __name__ == '__main__':
    ejecucion_demostrativa()
