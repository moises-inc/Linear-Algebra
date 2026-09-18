#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
UNIVERSIDAD SAN SEBASTIÁN — FACULTAD DE INGENIERÍA, ARQUITECTURA Y DISEÑO
Carrera: Ingeniería Civil Informática
Asignatura: Álgebra Lineal
Docente: Carol Asencio González
Módulo 01: Sistemas de Ecuaciones Lineales, Eliminación Gauss-Jordan y Rouché-Frobenius 3D
================================================================================
Trazabilidad de Fuentes:
🎓 [Cátedra USS / Diapositivas Docente] : Operaciones Elementales por Fila (OEF),
    Forma Escalonada Reducida por Filas (RREF), Teorema de Rouché-Frobenius.
📖 [Texto Guía — Grossman / Poole]     : Interpretación geométrica de sistemas 3x3
    en R³, intersección de hiperplanos, análisis de consistencia.
🌐 [Computación Científica]            : Modelado simbólico con SymPy, renderizado
    vectorial 3D con Matplotlib y visualización volumétrica de planos.
================================================================================
"""

import os
import sys
from typing import Tuple, List, Optional, Dict, Any

# Configuración de backend seguro para entornos headless
if os.environ.get('DISPLAY', '') == '':
    import matplotlib
    matplotlib.use('Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
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


class LinearSystem3D:
    """
    Representa y resuelve sistemas de ecuaciones lineales 3x3 con análisis analítico,
    algorítmico (OEF / RREF paso a paso) y geométrico tridimensional (Rouché-Frobenius).
    """

    def __init__(self, A: List[List[float]], b: List[float], var_names: Tuple[str, ...] = ('x', 'y', 'z')):
        """
        Inicializa el sistema A * x = b.

        :param A: Matriz de coeficientes de dimensión 3x3.
        :param b: Vector de términos independientes de dimensión 3x1.
        :param var_names: Nombres de las variables incógnitas (por defecto: x, y, z).
        """
        if len(A) != 3 or any(len(row) != 3 for row in A):
            raise ValueError("La matriz de coeficientes A debe ser estrictamente de dimensión 3x3.")
        if len(b) != 3:
            raise ValueError("El vector de términos independientes b debe tener 3 elementos.")

        self.A_np = np.array(A, dtype=float)
        self.b_np = np.array(b, dtype=float).reshape(-1, 1)
        self.Ab_np = np.hstack([self.A_np, self.b_np])

        # Representación simbólica exacta con fracciones en SymPy
        self.A_sp = sp.Matrix(A)
        self.b_sp = sp.Matrix(b)
        self.Ab_sp = self.A_sp.col_insert(3, self.b_sp)
        self.var_names = var_names
        self.symbols = sp.symbols(' '.join(var_names))

    def rouche_frobenius_analysis(self) -> Dict[str, Any]:
        """
        Aplica el Teorema de Rouché-Frobenius para clasificar el sistema lineal.

        Retorna:
            Diccionario con rango(A), rango(A|b), número de incógnitas n=3,
            tipo de sistema ('SCD', 'SCI', 'SI') y descripción matemática/geométrica.
        """
        rank_A = self.A_sp.rank()
        rank_Ab = self.Ab_sp.rank()
        n = 3

        if rank_A == rank_Ab:
            if rank_A == n:
                system_type = "SCD"
                nombre = "Sistema Compatible Determinado"
                sol_desc = "Solución única (Intersección de los 3 planos en un único punto P₀)."
                grados_libertad = 0
            else:
                system_type = "SCI"
                nombre = "Sistema Compatible Indeterminado"
                grados_libertad = n - rank_A
                if grados_libertad == 1:
                    sol_desc = "Infinitas soluciones (Intersección en una recta común en R³)."
                else:
                    sol_desc = "Infinitas soluciones (Los 3 planos coinciden en un plano común en R³)."
        else:
            system_type = "SI"
            nombre = "Sistema Incompatible"
            sol_desc = "Sin solución (Planos paralelos disjuntos o prisma triangular sin punto común)."
            grados_libertad = None

        return {
            "rank_A": rank_A,
            "rank_Ab": rank_Ab,
            "n": n,
            "type": system_type,
            "name": nombre,
            "description": sol_desc,
            "degrees_of_freedom": grados_libertad
        }

    def gauss_jordan_step_by_step(self) -> Tuple[sp.Matrix, List[str], Optional[sp.Matrix]]:
        """
        Ejecuta la eliminación de Gauss-Jordan registrando cada Operación Elemental por Fila (OEF).

        Retorna:
            - Matriz RREF final.
            - Lista de explicaciones de cada OEF ejecutada.
            - Vector solución o conjunto solución paramétrico si existe.
        """
        M = self.Ab_sp.copy()
        steps: List[str] = [f"Matriz ampliada inicial (A|b):\n{self._matrix_to_str(M)}"]
        rows, cols = 3, 4
        current_row = 0

        for col in range(3):
            if current_row >= rows:
                break

            # Búsqueda del mejor pivote en la columna actual
            pivot_row = None
            # Heurística TDAH/USS: Priorizar pivotes que sean exactamente 1 o -1
            for r in range(current_row, rows):
                if M[r, col] in (1, -1):
                    pivot_row = r
                    break
            if pivot_row is None:
                for r in range(current_row, rows):
                    if M[r, col] != 0:
                        pivot_row = r
                        break

            if pivot_row is None:
                # Toda la columna debajo es cero, columna libre
                continue

            # 1. Intercambio de filas si no está en current_row (OEF Tipo I)
            if pivot_row != current_row:
                M.row_swap(current_row, pivot_row)
                steps.append(f"OEF [F_{current_row + 1} <-> F_{pivot_row + 1}]: Intercambio de filas para pivote:\n{self._matrix_to_str(M)}")

            pivot_val = M[current_row, col]

            # 2. Escalamiento para hacer pivote = 1 (OEF Tipo II)
            if pivot_val != 1:
                factor = sp.Rational(1, pivot_val)
                M[current_row, :] = M[current_row, :] * factor
                steps.append(f"OEF [F_{current_row + 1} -> ({factor}) * F_{current_row + 1}]: Normalización del pivote a 1:\n{self._matrix_to_str(M)}")

            # 3. Anulación hacia abajo y hacia arriba (OEF Tipo III: Eliminación en bloque)
            for r in range(rows):
                if r != current_row and M[r, col] != 0:
                    multiplier = M[r, col]
                    M[r, :] = M[r, :] - multiplier * M[current_row, :]
                    steps.append(f"OEF [F_{r + 1} -> F_{r + 1} - ({multiplier}) * F_{current_row + 1}]: Anulación en columna {col + 1}:\n{self._matrix_to_str(M)}")

            current_row += 1

        # Análisis de solución final mediante SymPy linsolve
        sol = None
        try:
            raw_sol = sp.linsolve((self.A_sp, self.b_sp), self.symbols)
            sol = list(raw_sol)[0] if raw_sol else None
        except Exception:
            sol = None

        return M, steps, sol

    @staticmethod
    def _matrix_to_str(M: sp.Matrix) -> str:
        """Formatea una matriz ampliada con fracciones exactas y línea divisoria."""
        lines = []
        rows, cols = M.shape
        col_widths = [max(len(str(M[r, c])) for r in range(rows)) for c in range(cols)]
        for r in range(rows):
            left_part = "  ".join(f"{str(M[r, c]):>{col_widths[c]}}" for c in range(cols - 1))
            right_part = f"{str(M[r, cols - 1]):>{col_widths[cols - 1]}}"
            lines.append(f"  [ {left_part}  |  {right_part} ]")
        return "\n".join(lines)

    def plot_system_3d(self, save_path: Optional[str] = None, show_plot: bool = True) -> plt.Figure:
        """
        Genera una representación gráfica tridimensional fotorrealista de los 3 planos en R³,
        el punto de intersección (SCD) o la recta paramétrica (SCI), respetando la paleta USS.
        """
        rf = self.rouche_frobenius_analysis()
        fig = plt.figure(figsize=(12, 9), facecolor='white')
        ax = fig.add_subplot(111, projection='3d')

        # Dominio de graficación en el espacio
        xlim = (-5, 5)
        ylim = (-5, 5)
        x_grid = np.linspace(xlim[0], xlim[1], 35)
        y_grid = np.linspace(ylim[0], ylim[1], 35)
        X, Y = np.meshgrid(x_grid, y_grid)

        colors = [USS_BLUE, USS_GOLD, USS_ACCENT_BLUE]
        plane_labels = [
            f"π₁: {self.A_np[0,0]:.0f}x + {self.A_np[0,1]:.0f}y + {self.A_np[0,2]:.0f}z = {self.b_np[0,0]:.0f}",
            f"π₂: {self.A_np[1,0]:.0f}x + {self.A_np[1,1]:.0f}y + {self.A_np[1,2]:.0f}z = {self.b_np[1,0]:.0f}",
            f"π₃: {self.A_np[2,0]:.0f}x + {self.A_np[2,1]:.0f}y + {self.A_np[2,2]:.0f}z = {self.b_np[2,0]:.0f}",
        ]

        # Graficación de cada plano ax + by + cz = d
        for i in range(3):
            a, b_val, c = self.A_np[i]
            d = self.b_np[i, 0]

            # Manejo robusto para evitar división por cero en planos perpendiculares
            if abs(c) >= 1e-4:
                Z = (d - a * X - b_val * Y) / c
                ax.plot_surface(X, Y, Z, color=colors[i], alpha=0.45, edgecolor='none', label=plane_labels[i])
            elif abs(b_val) >= 1e-4:
                z_grid = np.linspace(-5, 5, 35)
                X_plane, Z_plane = np.meshgrid(x_grid, z_grid)
                Y_plane = (d - a * X_plane - c * Z_plane) / b_val
                ax.plot_surface(X_plane, Y_plane, Z_plane, color=colors[i], alpha=0.45, edgecolor='none', label=plane_labels[i])
            elif abs(a) >= 1e-4:
                z_grid = np.linspace(-5, 5, 35)
                Y_plane, Z_plane = np.meshgrid(y_grid, z_grid)
                X_plane = (d - b_val * Y_plane - c * Z_plane) / a
                ax.plot_surface(X_plane, Y_plane, Z_plane, color=colors[i], alpha=0.45, edgecolor='none', label=plane_labels[i])

        # Elementos según clasificación de Rouché-Frobenius
        if rf["type"] == "SCD":
            # Solución única: Punto en R³
            try:
                x_sol = float(np.linalg.solve(self.A_np, self.b_np.flatten())[0])
                y_sol = float(np.linalg.solve(self.A_np, self.b_np.flatten())[1])
                z_sol = float(np.linalg.solve(self.A_np, self.b_np.flatten())[2])

                # Punto de intersección destacado
                ax.scatter([x_sol], [y_sol], [z_sol], color=USS_ACCENT_RED, s=200, zorder=10,
                           edgecolor='black', linewidth=1.5,
                           label=f"Solución Única P₀({x_sol:.2f}, {y_sol:.2f}, {z_sol:.2f})")

                # Líneas guía discontinuas a los planos cartesianos
                ax.plot([x_sol, x_sol], [y_sol, y_sol], [-5, z_sol], color=USS_ACCENT_RED, linestyle='--', alpha=0.7)
                ax.plot([x_sol, x_sol], [-5, y_sol], [z_sol, z_sol], color=USS_ACCENT_RED, linestyle='--', alpha=0.7)
                ax.plot([-5, x_sol], [y_sol, y_sol], [z_sol, z_sol], color=USS_ACCENT_RED, linestyle='--', alpha=0.7)

                # Texto de coordenadas
                ax.text(x_sol + 0.3, y_sol + 0.3, z_sol + 0.3,
                        f"P₀ = ({x_sol:.2f}, {y_sol:.2f}, {z_sol:.2f})",
                        color=USS_ACCENT_RED, fontweight='bold', fontsize=11)
            except Exception as e:
                print(f"[Aviso] No se pudo proyectar el punto numérico: {e}")

        elif rf["type"] == "SCI" and rf["degrees_of_freedom"] == 1:
            # Recta común de intersección
            try:
                # Obtener solución paramétrica exacta con SymPy
                _, _, sym_sol = self.gauss_jordan_step_by_step()
                free_vars = list(sym_sol.free_symbols) if sym_sol else []
                if free_vars:
                    t_param = free_vars[0]
                    t_vals = np.linspace(-4, 4, 100)
                    line_pts = []
                    for t_val in t_vals:
                        pt = [float(sym_sol[i].subs(t_param, t_val)) for i in range(3)]
                        line_pts.append(pt)
                    line_pts = np.array(line_pts)
                    ax.plot(line_pts[:, 0], line_pts[:, 1], line_pts[:, 2],
                            color=USS_ACCENT_RED, linewidth=4, label="Recta de Soluciones L(t)")
            except Exception as e:
                print(f"[Aviso] No se pudo trazar la recta paramétrica: {e}")

        # Configuración estética institucional USS
        ax.set_xlabel('Eje X', fontsize=11, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_ylabel('Eje Y', fontsize=11, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_zlabel('Eje Z', fontsize=11, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_zlim(-5, 5)

        title_str = (f"Teorema de Rouché-Frobenius: {rf['name']} ({rf['type']})\n"
                     f"rg(A) = {rf['rank_A']}, rg(A|b) = {rf['rank_Ab']}, n = {rf['n']} | {rf['description']}")
        ax.set_title(title_str, fontsize=12, fontweight='bold', color=USS_BLUE, pad=20)

        # Configuración de grilla y perspectiva
        ax.view_init(elev=24, azim=42)
        ax.grid(True, linestyle=':', alpha=0.6)

        # Crear leyenda manual para las superficies y puntos
        proxy_p1 = plt.Rectangle((0, 0), 1, 1, fc=USS_BLUE, alpha=0.55)
        proxy_p2 = plt.Rectangle((0, 0), 1, 1, fc=USS_GOLD, alpha=0.55)
        proxy_p3 = plt.Rectangle((0, 0), 1, 1, fc=USS_ACCENT_BLUE, alpha=0.55)
        handles = [proxy_p1, proxy_p2, proxy_p3]
        labels = plane_labels

        if rf["type"] == "SCD":
            point_proxy = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=USS_ACCENT_RED, markersize=10)
            handles.append(point_proxy)
            labels.append(f"Solución P₀")
        elif rf["type"] == "SCI" and rf["degrees_of_freedom"] == 1:
            line_proxy = plt.Line2D([0], [0], color=USS_ACCENT_RED, lw=3)
            handles.append(line_proxy)
            labels.append("Recta de Intersección L")

        ax.legend(handles, labels, loc='upper left', bbox_to_anchor=(0.0, 0.95), fontsize=9, framealpha=0.9)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"-> Figura guardada exitosamente en: {save_path}")

        if show_plot and os.environ.get('DISPLAY', '') != '':
            plt.show()

        plt.close(fig)
        return fig


# ==============================================================================
# DEMOSTRACIÓN INTEGRAL EN TERMINAL (CASOS SCD, SCI, SI)
# ==============================================================================
def run_demonstration():
    """Ejecuta la suite de pruebas pedagógicas para los tres casos de Rouché-Frobenius."""
    output_dir = os.path.dirname(os.path.abspath(__file__))

    print("=" * 80)
    print("UNIVERSIDAD SAN SEBASTIÁN — SIMULADOR 01: GAUSS-JORDAN Y ROUCHÉ-FROBENIUS 3D")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # CASO 1: Sistema Compatible Determinado (SCD) — Intersección en Punto
    # --------------------------------------------------------------------------
    print("\n" + "#" * 80)
    print("CASO 1: SISTEMA COMPATIBLE DETERMINADO (SCD)")
    print("Ecuaciones:")
    print("  2x +  y -  z =  8")
    print(" -3x -  y + 2z = -11")
    print(" -2x +  y + 2z = -3")
    print("#" * 80)
    A1 = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b1 = [8, -11, -3]

    sys1 = LinearSystem3D(A1, b1)
    rf1 = sys1.rouche_frobenius_analysis()
    print(f"\n[1] Diagnóstico Rouché-Frobenius: {rf1['name']} ({rf1['type']})")
    print(f"    - rg(A)   = {rf1['rank_A']}")
    print(f"    - rg(A|b) = {rf1['rank_Ab']}")
    print(f"    - Grados de libertad = {rf1['degrees_of_freedom']}")
    print(f"    - Interpretación: {rf1['description']}")

    print("\n[2] Resolución Paso a Paso con OEF (Gauss-Jordan):")
    rref1, steps1, sol1 = sys1.gauss_jordan_step_by_step()
    for s in steps1:
        print(f"\n{s}")
    print(f"\n[3] Solución Analítica Exacta: (x, y, z) = {sol1}")

    img1_path = os.path.join(output_dir, "01_gauss_rouche_scd.png")
    sys1.plot_system_3d(save_path=img1_path, show_plot=False)

    # --------------------------------------------------------------------------
    # CASO 2: Sistema Compatible Indeterminado (SCI) — Intersección en Recta
    # --------------------------------------------------------------------------
    print("\n" + "#" * 80)
    print("CASO 2: SISTEMA COMPATIBLE INDETERMINADO (SCI)")
    print("Ecuaciones (Fila 3 = Fila 1 + Fila 2):")
    print("   x +  y +  z = 3")
    print("  2x -  y + 3z = 4")
    print("  3x + 0y + 4z = 7")
    print("#" * 80)
    A2 = [[1, 1, 1], [2, -1, 3], [3, 0, 4]]
    b2 = [3, 4, 7]

    sys2 = LinearSystem3D(A2, b2)
    rf2 = sys2.rouche_frobenius_analysis()
    print(f"\n[1] Diagnóstico Rouché-Frobenius: {rf2['name']} ({rf2['type']})")
    print(f"    - rg(A)   = {rf2['rank_A']}")
    print(f"    - rg(A|b) = {rf2['rank_Ab']}")
    print(f"    - Grados de libertad = {rf2['degrees_of_freedom']}")
    print(f"    - Interpretación: {rf2['description']}")

    print("\n[2] Reducción Gauss-Jordan:")
    rref2, steps2, sol2 = sys2.gauss_jordan_step_by_step()
    print(f"\nForma Escalonada Reducida RREF:\n{sys2._matrix_to_str(rref2)}")
    print(f"Solución Paramétrica: {sol2}")

    img2_path = os.path.join(output_dir, "01_gauss_rouche_sci.png")
    sys2.plot_system_3d(save_path=img2_path, show_plot=False)

    # --------------------------------------------------------------------------
    # CASO 3: Sistema Incompatible (SI) — Sin Intersección Común (Prisma Triangular)
    # --------------------------------------------------------------------------
    print("\n" + "#" * 80)
    print("CASO 3: SISTEMA INCOMPATIBLE (SI)")
    print("Ecuaciones:")
    print("   x + y + z = 1")
    print("   x - y + 2z = 2")
    print("  2x + 0y + 3z = 5  (Incompatible: F1 + F2 daría 2x + 3z = 3 != 5)")
    print("#" * 80)
    A3 = [[1, 1, 1], [1, -1, 2], [2, 0, 3]]
    b3 = [1, 2, 5]

    sys3 = LinearSystem3D(A3, b3)
    rf3 = sys3.rouche_frobenius_analysis()
    print(f"\n[1] Diagnóstico Rouché-Frobenius: {rf3['name']} ({rf3['type']})")
    print(f"    - rg(A)   = {rf3['rank_A']}")
    print(f"    - rg(A|b) = {rf3['rank_Ab']}")
    print(f"    - Interpretación: {rf3['description']}")

    rref3, steps3, sol3 = sys3.gauss_jordan_step_by_step()
    print(f"\nForma Escalonada Reducida RREF con inconsistencia:\n{sys3._matrix_to_str(rref3)}")
    print(f"Conjunto Solución: Vacío (Sistema sin solución)")

    img3_path = os.path.join(output_dir, "01_gauss_rouche_si.png")
    sys3.plot_system_3d(save_path=img3_path, show_plot=False)

    print("\n" + "=" * 80)
    print("DEMOSTRACIÓN FINALIZADA — Las 3 figuras 3D han sido exportadas exitosamente a 300 DPI.")
    print("=" * 80)


if __name__ == '__main__':
    run_demonstration()
