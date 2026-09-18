#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
UNIVERSIDAD SAN SEBASTIÁN — FACULTAD DE INGENIERÍA, ARQUITECTURA Y DISEÑO
Carrera: Ingeniería Civil Informática
Asignatura: Álgebra Lineal
Docente: Carol Asencio González
Módulo 02: Discusión y Análisis de Sistemas Lineales Parametrizados con Parámetro k
================================================================================
Trazabilidad de Fuentes:
[Cátedra USS — Diapositivas Docente] : Sistemas dependientes de parámetros,
    análisis por determinantes det(A(k)), Teorema de Rouché-Frobenius.
[Texto Guía — Stanley Grossman]     : Discusión de consistencia, casos singulares
    k críticos, geometría del prisma triangular (SI) y planos coincidentes (SCI).
[Computación Científica]            : Álgebra computacional con SymPy, cálculo
    de raíces algebraicas y visualización tridimensional en Matplotlib.
================================================================================
"""

import os
import sys
from typing import Dict, Any, List, Tuple, Optional

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sympy as sp

# ==============================================================================
# PALETA INSTITUCIONAL UNIVERSIDAD SAN SEBASTIÁN (USS)
# ==============================================================================
USS_BLUE = '#00205B'
USS_GOLD = '#D4AF37'
USS_ACCENT_BLUE = '#1E88E5'
USS_ACCENT_GREEN = '#27AE60'
USS_ACCENT_RED = '#C0392B'
USS_DARK_GRAY = '#2C3E50'
USS_LIGHT_GRAY = '#F8F9F9'


class ParametricSystemAnalyzer:
    """
    Analizador analítico y geométrico del sistema simétrico tridimensional estándar:
        k*x +   y +   z = 1
          x + k*y +   z = 1
          x +   y + k*z = 1
    """

    def __init__(self):
        self.k = sp.symbols('k', real=True)
        self.x, self.y, self.z = sp.symbols('x y z', real=True)

        self.A_k = sp.Matrix([
            [self.k, 1, 1],
            [1, self.k, 1],
            [1, 1, self.k]
        ])
        self.b = sp.Matrix([1, 1, 1])
        self.Ab_k = self.A_k.col_insert(3, self.b)

    def compute_symbolic_determinant(self) -> Tuple[sp.Expr, sp.Expr, List[sp.Expr]]:
        """
        Calcula el determinante simbólico det(A(k)), su factorización canónica y raíces críticas.
        """
        det_poly = self.A_k.det()
        det_factored = sp.factor(det_poly)
        critical_roots = sp.solve(det_poly, self.k)
        return det_poly, det_factored, critical_roots

    def analyze_cases(self) -> Dict[str, Any]:
        """
        Clasifica exhaustivamente los casos posibles según el valor de k bajo Rouché-Frobenius.
        """
        det_poly, det_factored, roots = self.compute_symbolic_determinant()

        # Caso k = 1
        A_k1 = self.A_k.subs(self.k, 1)
        Ab_k1 = self.Ab_k.subs(self.k, 1)
        rg_A_k1 = int(A_k1.rank())
        rg_Ab_k1 = int(Ab_k1.rank())

        # Caso k = -2
        A_k_neg2 = self.A_k.subs(self.k, -2)
        Ab_k_neg2 = self.Ab_k.subs(self.k, -2)
        rg_A_k_neg2 = int(A_k_neg2.rank())
        rg_Ab_k_neg2 = int(Ab_k_neg2.rank())

        return {
            "det_poly": det_poly,
            "det_factored": det_factored,
            "roots": roots,
            "case_k_generic": {
                "condition": "k != 1 y k != -2",
                "det": "det(A) != 0",
                "type": "SCD",
                "name": "Sistema Compatible Determinado",
                "rg_A": 3,
                "rg_Ab": 3,
                "n": 3,
                "sol": "x = y = z = 1 / (k + 2)",
                "geom": "Intersección en un único punto P0(1/(k+2), 1/(k+2), 1/(k+2))."
            },
            "case_k_1": {
                "condition": "k = 1",
                "det": 0,
                "rg_A": rg_A_k1,
                "rg_Ab": rg_Ab_k1,
                "n": 3,
                "type": "SCI",
                "name": "Sistema Compatible Indeterminado",
                "degrees_of_freedom": 3 - rg_A_k1,
                "geom": "Los 3 planos coinciden en el plano x + y + z = 1 (2 grados de libertad)."
            },
            "case_k_neg2": {
                "condition": "k = -2",
                "det": 0,
                "rg_A": rg_A_k_neg2,
                "rg_Ab": rg_Ab_k_neg2,
                "n": 3,
                "type": "SI",
                "name": "Sistema Incompatible",
                "geom": "Prisma triangular hueco. Las intersecciones dos a dos son 3 rectas paralelas disjuntas."
            }
        }

    def plot_determinant_curve(self, save_path: Optional[str] = None, show_plot: bool = False):
        """
        Grafica el polinomio det(A(k)) = (k-1)²(k+2) identificando visualmente las raíces críticas.
        """
        fig, ax = plt.subplots(figsize=(9, 5), facecolor='white')

        k_vals = np.linspace(-3.5, 2.5, 400)
        det_vals = (k_vals - 1)**2 * (k_vals + 2)

        ax.plot(k_vals, det_vals, color=USS_BLUE, linewidth=2.5,
                label=r"$\det(A(k)) = (k-1)^2(k+2) = k^3 - 3k + 2$")
        ax.axhline(0, color=USS_DARK_GRAY, linestyle='--', linewidth=1, alpha=0.7)
        ax.axvline(0, color=USS_DARK_GRAY, linestyle='--', linewidth=0.8, alpha=0.5)

        # Resaltar raíces críticas
        ax.scatter([-2, 1], [0, 0], color=USS_ACCENT_RED, s=120, zorder=5, edgecolor='black', linewidth=1.5)
        ax.annotate(r"$k = -2$ (Raíz simple $\to$ SI)", xy=(-2, 0), xytext=(-3.2, 5),
                    arrowprops=dict(facecolor=USS_ACCENT_RED, shrink=0.08, width=1.5, headwidth=8),
                    fontweight='bold', color=USS_ACCENT_RED, fontsize=10)
        ax.annotate(r"$k = 1$ (Raíz doble $\to$ SCI)", xy=(1, 0), xytext=(0.2, -6),
                    arrowprops=dict(facecolor=USS_GOLD, shrink=0.08, width=1.5, headwidth=8),
                    fontweight='bold', color=USS_BLUE, fontsize=10)

        # Regiones de invertibilidad (SCD)
        ax.fill_between(k_vals, det_vals, 0, where=(det_vals > 0), color=USS_ACCENT_BLUE, alpha=0.12, label="Zona SCD (det > 0)")
        ax.fill_between(k_vals, det_vals, 0, where=(det_vals < 0), color=USS_GOLD, alpha=0.15, label="Zona SCD (det < 0)")

        ax.set_title(r"Determinante $\det(A(k))$ vs Parámetro $k$",
                     fontsize=12, fontweight='bold', color=USS_BLUE, pad=12)
        ax.set_xlabel("Parámetro k", fontsize=10, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_ylabel(r"$\det(A(k))$", fontsize=10, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_xlim(-3.5, 2.5)
        ax.set_ylim(-12, 16)
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='upper left', framealpha=0.95, fontsize=9.0)

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        if show_plot:
            plt.show()
        plt.close(fig)

    def plot_individual_3d_case(self, k_val: float, save_path: Optional[str] = None,
                                elev: int = 25, azim: int = -50, show_plot: bool = False):
        """
        Genera una figura 3D individual e independiente para un valor concreto de k.
        Aplica alpha=0.25 y perspectiva elev=25, azim=-50.
        """
        fig = plt.figure(figsize=(10, 8), facecolor='white')
        ax = fig.add_subplot(111, projection='3d')

        x_grid = np.linspace(-3, 3, 30)
        y_grid = np.linspace(-3, 3, 30)
        X, Y = np.meshgrid(x_grid, y_grid)

        colors = [USS_BLUE, USS_GOLD, USS_ACCENT_BLUE]
        A_num = np.array([
            [k_val, 1.0, 1.0],
            [1.0, k_val, 1.0],
            [1.0, 1.0, k_val]
        ])
        b_num = np.array([1.0, 1.0, 1.0])

        plane_labels = [
            f"pi1: {k_val:.1f}x + y + z = 1",
            f"pi2: x + {k_val:.1f}y + z = 1",
            f"pi3: x + y + {k_val:.1f}z = 1"
        ]

        # Graficación según el caso geométrico
        if abs(k_val - 1.0) < 1e-4:
            # Caso SCI (k = 1): Planos coincidentes
            # Graficar el plano común x + y + z = 1 con máxima elegancia
            Z = 1.0 - X - Y
            ax.plot_surface(X, Y, Z, color=USS_BLUE, alpha=0.25, edgecolor='gray', linewidth=0.3)

            # Triángulo de trazas sobre los planos coordenados
            pts_trazas = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]])
            ax.plot(pts_trazas[:, 0], pts_trazas[:, 1], pts_trazas[:, 2], color=USS_GOLD, linewidth=2.5,
                    linestyle='-', label="Traza triangular en ejes cartesianos")
            ax.scatter([1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], color=USS_GOLD, s=60, edgecolors='black')

            # Vector normal unitario n = (1, 1, 1) erigido desde el baricentro (1/3, 1/3, 1/3)
            p_bar = np.array([1/3, 1/3, 1/3])
            ax.quiver(p_bar[0], p_bar[1], p_bar[2], 1.2, 1.2, 1.2, color=USS_ACCENT_RED,
                      linewidth=3.0, arrow_length_ratio=0.18, label=r"$\vec{n} = (1, 1, 1)$ (Normal común)")

            title_str = (f"Rouché-Frobenius: Sistema Compatible Indeterminado (k = 1.0)\n"
                         f"rg(A) = 1, rg(A|b) = 1, n = 3 | 3 Planos coincidentes en x + y + z = 1")

            handles = [
                plt.Rectangle((0, 0), 1, 1, fc=USS_BLUE, alpha=0.35),
                plt.Line2D([0], [0], color=USS_GOLD, lw=2.5),
                plt.Line2D([0], [0], color=USS_ACCENT_RED, lw=3.0)
            ]
            labels = [
                r"$\pi_1 \equiv \pi_2 \equiv \pi_3: x + y + z = 1$",
                "Traza triangular (interceptos en 1)",
                r"Normal común $\vec{n} = (1, 1, 1)$"
            ]

            ax.text(0, 0, 2.0, "Planos Coincidentes\npi1 == pi2 == pi3\nx + y + z = 1\n(2 Grados de libertad)",
                    color=USS_BLUE, fontweight='bold', fontsize=9.5,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=USS_GOLD, lw=1.5, alpha=0.92))

        elif abs(k_val - (-2.0)) < 1e-4:
            # Caso SI (k = -2): Prisma triangular hueco
            # Graficar los 3 planos con alpha=0.22 y contornos grises
            for i in range(3):
                a, b_c, c = A_num[i]
                d = b_num[i]
                if abs(c) >= 1e-4:
                    Z = (d - a * X - b_c * Y) / c
                    ax.plot_surface(X, Y, Z, color=colors[i], alpha=0.22, edgecolor='gray', linewidth=0.3)

            title_str = (f"Rouché-Frobenius: Sistema Incompatible (k = -2.0)\n"
                         f"rg(A) = 2, rg(A|b) = 3, n = 3 | Prisma triangular sin punto común")

            t = np.linspace(-2.5, 2.5, 60)
            # Recta r12: x=t, y=t, z=t+1
            ax.plot(t, t, t + 1, color=USS_ACCENT_RED, linewidth=3.0, linestyle='-')
            # Recta r13: x=t, z=t, y=t+1
            ax.plot(t, t + 1, t, color=USS_ACCENT_GREEN, linewidth=3.0, linestyle='-')
            # Recta r23: y=t, z=t, x=t+1
            ax.plot(t + 1, t, t, color=USS_GOLD, linewidth=3.0, linestyle='-')

            # Secciones transversales triangulares del prisma en t = -1.2, 0.0, 1.2
            for t_sec in [-1.2, 0.0, 1.2]:
                v_tri = np.array([
                    [t_sec, t_sec, t_sec + 1],
                    [t_sec, t_sec + 1, t_sec],
                    [t_sec + 1, t_sec, t_sec],
                    [t_sec, t_sec, t_sec + 1]
                ])
                ax.plot(v_tri[:, 0], v_tri[:, 1], v_tri[:, 2], color=USS_DARK_GRAY,
                        linestyle='--', linewidth=1.5, alpha=0.85)
                ax.scatter(v_tri[:-1, 0], v_tri[:-1, 1], v_tri[:-1, 2], color=USS_DARK_GRAY, s=25, alpha=0.8)

            handles = [
                plt.Rectangle((0, 0), 1, 1, fc=colors[0], alpha=0.35),
                plt.Rectangle((0, 0), 1, 1, fc=colors[1], alpha=0.35),
                plt.Rectangle((0, 0), 1, 1, fc=colors[2], alpha=0.35),
                plt.Line2D([0], [0], color=USS_ACCENT_RED, lw=3.0),
                plt.Line2D([0], [0], color=USS_ACCENT_GREEN, lw=3.0),
                plt.Line2D([0], [0], color=USS_GOLD, lw=3.0),
                plt.Line2D([0], [0], color=USS_DARK_GRAY, lw=1.5, linestyle='--')
            ]
            labels = [
                plane_labels[0],
                plane_labels[1],
                plane_labels[2],
                "Intersección pi1 y pi2: (t, t, t+1)",
                "Intersección pi1 y pi3: (t, t+1, t)",
                "Intersección pi2 y pi3: (t+1, t, t)",
                "Secciones triangulares transversales"
            ]

            ax.text(0, 0, 2.2, "Prisma triangular hueco\n3 Rectas paralelas disjuntas\nVector director d = (1, 1, 1)",
                    color=USS_ACCENT_RED, fontweight='bold', fontsize=9.5,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=USS_ACCENT_RED, lw=1.5, alpha=0.92))

        else:
            # Caso SCD (k != 1 y k != -2): Solución única P0
            for i in range(3):
                a, b_c, c = A_num[i]
                d = b_num[i]
                if abs(c) >= 1e-4:
                    Z = (d - a * X - b_c * Y) / c
                    ax.plot_surface(X, Y, Z, color=colors[i], alpha=0.22, edgecolor='gray', linewidth=0.3)

            sol = np.linalg.solve(A_num, b_num)
            title_str = (f"Rouché-Frobenius: Sistema Compatible Determinado (k = {k_val:.1f})\n"
                         f"rg(A) = 3, rg(A|b) = 3, n = 3 | Solución única P0({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})")

            # Marcador destacado para P0
            ax.scatter([sol[0]], [sol[1]], [sol[2]], color=USS_ACCENT_RED, s=130, zorder=10,
                       edgecolor='black', linewidth=1.5)
            ax.text(sol[0] + 0.25, sol[1] + 0.25, sol[2] + 0.25,
                    f"P0({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})",
                    color=USS_ACCENT_RED, fontweight='bold', fontsize=10,
                    bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=USS_ACCENT_RED, lw=1.2, alpha=0.9))

            # Líneas de proyección punteadas a los planos coordenados
            ax.plot([sol[0], sol[0]], [sol[1], sol[1]], [-3, sol[2]], color=USS_ACCENT_RED, linestyle=':', alpha=0.8, linewidth=1.3)
            ax.plot([sol[0], sol[0]], [-3, sol[1]], [sol[2], sol[2]], color=USS_ACCENT_RED, linestyle=':', alpha=0.8, linewidth=1.3)
            ax.plot([-3, sol[0]], [sol[1], sol[1]], [sol[2], sol[2]], color=USS_ACCENT_RED, linestyle=':', alpha=0.8, linewidth=1.3)

            # Marcadores en las proyecciones
            ax.scatter([sol[0]], [sol[1]], [-3], color=USS_DARK_GRAY, s=35, alpha=0.7, edgecolors='black', linewidths=0.8)
            ax.scatter([sol[0]], [-3], [sol[2]], color=USS_DARK_GRAY, s=35, alpha=0.7, edgecolors='black', linewidths=0.8)
            ax.scatter([-3], [sol[1]], [sol[2]], color=USS_DARK_GRAY, s=35, alpha=0.7, edgecolors='black', linewidths=0.8)

            handles = [
                plt.Rectangle((0, 0), 1, 1, fc=colors[0], alpha=0.35),
                plt.Rectangle((0, 0), 1, 1, fc=colors[1], alpha=0.35),
                plt.Rectangle((0, 0), 1, 1, fc=colors[2], alpha=0.35),
                plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=USS_ACCENT_RED,
                           markeredgecolor='black', markersize=9)
            ]
            labels = list(plane_labels) + [f"Solución P0({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})"]

        ax.set_title(title_str, fontsize=11, fontweight='bold', color=USS_BLUE, pad=15)
        ax.set_xlabel('Eje X', fontsize=10, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_ylabel('Eje Y', fontsize=10, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_zlabel('Eje Z', fontsize=10, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_zlim(-3, 3)
        ax.view_init(elev=elev, azim=azim)
        ax.grid(True, linestyle=':', alpha=0.5)
        ax.legend(handles, labels, loc='upper left', bbox_to_anchor=(0.0, 0.96), fontsize=8.5, framealpha=0.9)

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        if show_plot:
            plt.show()
        plt.close(fig)


# ==============================================================================
# DEMOSTRACIÓN EN TERMINAL
# ==============================================================================
def run_demonstration():
    output_dir = os.path.dirname(os.path.abspath(__file__))

    print("--- Análisis de Sistemas Lineales Parametrizados con Parámetro k ---")
    print("Sistema:")
    print("    kx +  y +  z = 1")
    print("     x + ky +  z = 1")
    print("     x +  y + kz = 1\n")

    analyzer = ParametricSystemAnalyzer()
    res = analyzer.analyze_cases()

    print(f"Polinomio determinante: det(A(k)) = {res['det_poly']}")
    print(f"Forma factorizada:     det(A(k)) = {res['det_factored']}")
    print("Raíces críticas: k = 1 (raíz doble), k = -2 (raíz simple)\n")

    # Caso 1: SCD (k != 1 y k != -2)
    c_scd = res["case_k_generic"]
    print(f"--- Caso 1: {c_scd['condition']} ({c_scd['type']}) ---")
    print(f"Diagnóstico Rouché-Frobenius: rg(A) = {c_scd['rg_A']}, rg(A|b) = {c_scd['rg_Ab']}, n = {c_scd['n']}")
    print(f"Tipo: {c_scd['name']} ({c_scd['type']})")
    print(f"Solución única: {c_scd['sol']}\n")

    # Caso 2: SCI (k = 1)
    c_sci = res["case_k_1"]
    print(f"--- Caso 2: {c_sci['condition']} ({c_sci['type']}) ---")
    print(f"Diagnóstico Rouché-Frobenius: rg(A) = {c_sci['rg_A']}, rg(A|b) = {c_sci['rg_Ab']}, n = {c_sci['n']}")
    print(f"Tipo: {c_sci['name']} ({c_sci['type']})")
    print(f"Grados de libertad: {c_sci['degrees_of_freedom']}")
    print(f"Interpretación: Infinitas soluciones ({c_sci['geom']})\n")

    # Caso 3: SI (k = -2)
    c_si = res["case_k_neg2"]
    print(f"--- Caso 3: {c_si['condition']} ({c_si['type']}) ---")
    print(f"Diagnóstico Rouché-Frobenius: rg(A) = {c_si['rg_A']}, rg(A|b) = {c_si['rg_Ab']}, n = {c_si['n']}")
    print(f"Tipo: {c_si['name']} ({c_si['type']})")
    print(f"Interpretación: Sin solución ({c_si['geom']})\n")

    # Generación de las 4 figuras individuales independientes
    p_curva = os.path.join(output_dir, "02_det_k_curva_analisis.png")
    analyzer.plot_determinant_curve(save_path=p_curva)

    p_scd = os.path.join(output_dir, "02_sistema_k_scd.png")
    analyzer.plot_individual_3d_case(k_val=2.0, save_path=p_scd)

    p_sci = os.path.join(output_dir, "02_sistema_k_sci.png")
    analyzer.plot_individual_3d_case(k_val=1.0, save_path=p_sci)

    p_si = os.path.join(output_dir, "02_sistema_k_si.png")
    analyzer.plot_individual_3d_case(k_val=-2.0, save_path=p_si)


if __name__ == '__main__':
    run_demonstration()
