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
🎓 [Cátedra USS / Diapositivas Docente] : Sistemas dependientes de parámetros,
    análisis por determinantes det(A(k)), Teorema de Rouché-Frobenius.
📖 [Texto Guía — Grossman / Poole]     : Discusión de consistencia, casos singulares
    k_críticos, geometría del prisma triangular (SI) y planos coincidentes (SCI).
🌐 [Computación Científica]            : Álgebra computacional con SymPy, cálculo
    de raíces algebraicas y visualización tridimensional comparativa en Matplotlib.
================================================================================
"""

import os
import sys
from typing import Dict, Any, List, Tuple, Optional

# Configuración de backend seguro para entornos headless
if os.environ.get('DISPLAY', '') == '':
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
USS_LIGHT_GRAY = '#ECF0F1'


class ParametricSystemAnalyzer:
    """
    Analizador analítico y geométrico del sistema simétrico tridimensional estándar:
        k*x +   y +   z = 1
          x + k*y +   z = 1
          x +   y + k*z = 1
    """

    def __init__(self):
        # Definición de símbolos
        self.k = sp.symbols('k', real=True)
        self.x, self.y, self.z = sp.symbols('x y z', real=True)

        # Matriz simétrica paramétrica y vector b
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

        # Solución general para k no crítico (Cramer / Inversa)
        gen_sol = self.A_k.inv() * self.b

        # Caso k = 1
        A_k1 = self.A_k.subs(self.k, 1)
        Ab_k1 = self.Ab_k.subs(self.k, 1)
        rg_A_k1 = A_k1.rank()
        rg_Ab_k1 = Ab_k1.rank()

        # Caso k = -2
        A_k_neg2 = self.A_k.subs(self.k, -2)
        Ab_k_neg2 = self.Ab_k.subs(self.k, -2)
        rg_A_k_neg2 = A_k_neg2.rank()
        rg_Ab_k_neg2 = Ab_k_neg2.rank()

        return {
            "det_poly": det_poly,
            "det_factored": det_factored,
            "roots": roots,
            "general_solution": gen_sol,
            "case_k_generic": {
                "condition": "k != 1 y k != -2",
                "det": "det(A) != 0",
                "type": "SCD",
                "name": "Sistema Compatible Determinado",
                "sol": f"x = y = z = 1 / (k + 2)",
                "geom": "Los 3 planos se intersectan en un único punto P₀(1/(k+2), 1/(k+2), 1/(k+2))."
            },
            "case_k_1": {
                "condition": "k = 1",
                "det": 0,
                "rg_A": rg_A_k1,
                "rg_Ab": rg_Ab_k1,
                "type": "SCI",
                "name": "Sistema Compatible Indeterminado",
                "degrees_of_freedom": 3 - rg_A_k1,
                "geom": "Los 3 planos son idénticos y coincidentes (x + y + z = 1). Infinitas soluciones en un plano."
            },
            "case_k_neg2": {
                "condition": "k = -2",
                "det": 0,
                "rg_A": rg_A_k_neg2,
                "rg_Ab": rg_Ab_k_neg2,
                "type": "SI",
                "name": "Sistema Incompatible",
                "geom": "Los 3 planos forman un prisma triangular hueco infinito. Las intersecciones dos a dos son 3 rectas paralelas disjuntas."
            }
        }

    def plot_determinant_curve(self, save_path: Optional[str] = None):
        """
        Grafica el polinomio det(A(k)) = (k-1)²(k+2) identificando visualmente las raíces críticas.
        """
        fig, ax = plt.subplots(figsize=(9, 5), facecolor='white')

        k_vals = np.linspace(-3.5, 2.5, 400)
        det_vals = (k_vals - 1)**2 * (k_vals + 2)

        ax.plot(k_vals, det_vals, color=USS_BLUE, linewidth=2.5, label=r"$\det(A(k)) = (k-1)^2(k+2) = k^3 - 3k + 2$")
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

        # Regiones sombreadas de invertibilidad (SCD)
        ax.fill_between(k_vals, det_vals, 0, where=(det_vals > 0), color=USS_ACCENT_BLUE, alpha=0.12, label="Zona SCD (det > 0)")
        ax.fill_between(k_vals, det_vals, 0, where=(det_vals < 0), color=USS_GOLD, alpha=0.15, label="Zona SCD (det < 0)")

        ax.set_title(r"Comportamiento del Determinante $\det(A(k))$ vs Parámetro $k$",
                     fontsize=13, fontweight='bold', color=USS_BLUE, pad=12)
        ax.set_xlabel("Parámetro k", fontsize=11, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_ylabel(r"$\det(A(k))$", fontsize=11, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_xlim(-3.5, 2.5)
        ax.set_ylim(-12, 16)
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='upper left', framealpha=0.95, fontsize=9.5)

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"-> Curva del determinante guardada en: {save_path}")

        if os.environ.get('DISPLAY', '') != '':
            plt.show()
        plt.close(fig)

    def plot_comparative_3d_cases(self, save_path: Optional[str] = None):
        """
        Genera un panel comparativo de 3 visualizaciones 3D en Matplotlib:
        1. SCD (k = 2) -> Punto único.
        2. SCI (k = 1) -> Planos coincidentes.
        3. SI (k = -2) -> Prisma triangular sin punto común.
        """
        fig = plt.figure(figsize=(18, 6), facecolor='white')

        cases = [
            {"k_val": 2.0, "title": "1. Caso SCD: k = 2\n(Solución Única P₀)", "type": "SCD"},
            {"k_val": 1.0, "title": "2. Caso SCI: k = 1\n(Planos Coincidentes)", "type": "SCI"},
            {"k_val": -2.0, "title": "3. Caso SI: k = -2\n(Prisma Triangular Hueco)", "type": "SI"}
        ]

        x_grid = np.linspace(-3, 3, 25)
        y_grid = np.linspace(-3, 3, 25)
        X, Y = np.meshgrid(x_grid, y_grid)

        colors = [USS_BLUE, USS_GOLD, USS_ACCENT_BLUE]

        for idx, case in enumerate(cases, 1):
            ax = fig.add_subplot(1, 3, idx, projection='3d')
            k_val = case["k_val"]

            A_num = np.array([
                [k_val, 1.0, 1.0],
                [1.0, k_val, 1.0],
                [1.0, 1.0, k_val]
            ])
            b_num = np.array([1.0, 1.0, 1.0])

            # Graficar los 3 planos
            for i in range(3):
                a, b_c, c = A_num[i]
                d = b_num[i]
                if abs(c) >= 1e-4:
                    Z = (d - a * X - b_c * Y) / c
                    ax.plot_surface(X, Y, Z, color=colors[i], alpha=0.45, edgecolor='none')

            if case["type"] == "SCD":
                # Intersección en P0 = (1/(k+2), 1/(k+2), 1/(k+2)) = (0.25, 0.25, 0.25)
                sol = np.linalg.solve(A_num, b_num)
                ax.scatter([sol[0]], [sol[1]], [sol[2]], color=USS_ACCENT_RED, s=150, zorder=10, edgecolor='black')
                ax.text(sol[0] + 0.2, sol[1] + 0.2, sol[2] + 0.2,
                        f"P₀({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})",
                        color=USS_ACCENT_RED, fontweight='bold', fontsize=10)

            elif case["type"] == "SCI":
                # Plano único x + y + z = 1
                ax.text(0, 0, 1.5, "3 Planos Coincidentes\nπ₁ ≡ π₂ ≡ π₃\nx + y + z = 1",
                        color=USS_BLUE, fontweight='bold', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=USS_GOLD, lw=1.5))

            elif case["type"] == "SI":
                # Prisma triangular: trazar las 3 rectas de intersección dos a dos
                # π1 y π2: (k=-2)
                # -2x + y + z = 1
                # x - 2y + z = 1
                # Resta: -3x + 3y = 0 => x = y.
                # Sustituyendo x=y en ecuacion 1: -x + z = 1 => z = x + 1.
                t = np.linspace(-2.5, 2.5, 50)
                # Recta r12: x=t, y=t, z=t+1
                ax.plot(t, t, t + 1, color=USS_ACCENT_RED, linewidth=2.5, linestyle='-', label="Recta π₁ ∩ π₂")
                # Recta r13: x=t, z=t, y=t+1
                ax.plot(t, t + 1, t, color=USS_ACCENT_GREEN, linewidth=2.5, linestyle='-', label="Recta π₁ ∩ π₃")
                # Recta r23: y=t, z=t, x=t+1
                ax.plot(t + 1, t, t, color=USS_GOLD, linewidth=2.5, linestyle='-', label="Recta π₂ ∩ π₃")

                ax.text(0, 0, 2.2, "3 Rectas Paralelas Disjuntas\n(Sin intersección común)",
                        color=USS_ACCENT_RED, fontweight='bold', fontsize=9, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=USS_ACCENT_RED, lw=1.5))

            ax.set_title(case["title"], fontsize=11, fontweight='bold', color=USS_BLUE, pad=15)
            ax.set_xlabel('X', fontsize=9, fontweight='bold', color=USS_DARK_GRAY)
            ax.set_ylabel('Y', fontsize=9, fontweight='bold', color=USS_DARK_GRAY)
            ax.set_zlabel('Z', fontsize=9, fontweight='bold', color=USS_DARK_GRAY)
            ax.set_xlim(-3, 3)
            ax.set_ylim(-3, 3)
            ax.set_zlim(-3, 3)
            ax.view_init(elev=22, azim=45)
            ax.grid(True, linestyle=':', alpha=0.5)

        plt.suptitle("UNIVERSIDAD SAN SEBASTIÁN — DISCUSIÓN GEOMÉTRICA SEGÚN PARÁMETRO k",
                     fontsize=14, fontweight='bold', color=USS_BLUE, y=0.98)
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"-> Visualización comparativa 3D guardada en: {save_path}")

        if os.environ.get('DISPLAY', '') != '':
            plt.show()
        plt.close(fig)


# ==============================================================================
# DEMOSTRACIÓN EN TERMINAL
# ==============================================================================
def run_demonstration():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    print("=" * 80)
    print("UNIVERSIDAD SAN SEBASTIÁN — SIMULADOR 02: SISTEMA PARAMETRIZADO CON k")
    print("=" * 80)

    analyzer = ParametricSystemAnalyzer()
    res = analyzer.analyze_cases()

    print("\n[1] Sistema Paramétrico Simétrico:")
    print("      k*x +   y +   z = 1")
    print("        x + k*y +   z = 1")
    print("        x +   y + k*z = 1")

    print("\n[2] Cálculo Simbólico del Determinante:")
    print(f"    - Polinomio:    det(A(k)) = {res['det_poly']}")
    print(f"    - Factorizado:  det(A(k)) = {res['det_factored']}")
    print(f"    - Raíces det=0: k = {res['roots']}")

    print("\n[3] Clasificación Exhaustiva de Casos (Rouché-Frobenius):")

    c_scd = res["case_k_generic"]
    print(f"\n  • CASO 1 ({c_scd['condition']}):")
    print(f"    - Tipo:            {c_scd['name']} ({c_scd['type']})")
    print(f"    - Condición det:   {c_scd['det']}")
    print(f"    - Solución Única:  {c_scd['sol']}")
    print(f"    - Geometría:       {c_scd['geom']}")

    c_sci = res["case_k_1"]
    print(f"\n  • CASO 2 ({c_sci['condition']}):")
    print(f"    - Tipo:            {c_sci['name']} ({c_sci['type']})")
    print(f"    - Rangos:          rg(A) = {c_sci['rg_A']}, rg(A|b) = {c_sci['rg_Ab']}")
    print(f"    - Grados libertad: {c_sci['degrees_of_freedom']} (Plano de soluciones)")
    print(f"    - Geometría:       {c_sci['geom']}")

    c_si = res["case_k_neg2"]
    print(f"\n  • CASO 3 ({c_si['condition']}):")
    print(f"    - Tipo:            {c_si['name']} ({c_si['type']})")
    print(f"    - Rangos:          rg(A) = {c_si['rg_A']}, rg(A|b) = {c_si['rg_Ab']}  (rg(A) < rg(A|b))")
    print(f"    - Geometría:       {c_si['geom']}")

    print("\n[4] Generando Gráficos de Alta Resolución...")
    p1 = os.path.join(output_dir, "02_sistema_parametrico_k_analisis.png")
    analyzer.plot_determinant_curve(save_path=p1)

    p2 = os.path.join(output_dir, "02_sistema_parametrico_k_3d.png")
    analyzer.plot_comparative_3d_cases(save_path=p2)

    print("\n" + "=" * 80)
    print("DEMOSTRACIÓN FINALIZADA EXITOSAMENTE.")
    print("=" * 80)


if __name__ == '__main__':
    run_demonstration()
