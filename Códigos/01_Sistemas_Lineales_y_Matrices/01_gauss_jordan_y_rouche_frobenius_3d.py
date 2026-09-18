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
[Cátedra USS — Diapositivas Docente] : Operaciones Elementales por Fila (OEF),
    Forma Escalonada Reducida por Filas (RREF), Teorema de Rouché-Frobenius.
[Texto Guía — Stanley Grossman]     : Interpretación geométrica de sistemas 3x3
    en R³, intersección de hiperplanos, análisis de consistencia.
[Computación Científica]            : Modelado simbólico con SymPy, renderizado
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
        rank_A = int(self.A_sp.rank())
        rank_Ab = int(self.Ab_sp.rank())
        n = 3

        if rank_A == rank_Ab:
            if rank_A == n:
                system_type = "SCD"
                nombre = "Sistema Compatible Determinado"
                sol_desc = "Solución única (Intersección de los 3 planos en un único punto P0)."
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

    def gauss_jordan_step_by_step(self) -> Tuple[sp.Matrix, List[str], Optional[Any]]:
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

            # Heurística TDAH/USS: Priorizar pivotes que sean exactamente 1 o -1
            pivot_row = None
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

    def plot_system_3d(self, save_path: Optional[str] = None, show_plot: bool = False,
                       elev: int = 25, azim: int = -50) -> plt.Figure:
        """
        Genera una representación gráfica 3D individual y limpia de los 3 planos en R³.
        Aplica alpha=0.25 para máxima transparencia y legibilidad, con perspectiva elev=25, azim=-50.
        """
        rf = self.rouche_frobenius_analysis()
        fig = plt.figure(figsize=(10, 8), facecolor='white')
        ax = fig.add_subplot(111, projection='3d')

        xlim = (-5, 5)
        ylim = (-5, 5)
        x_grid = np.linspace(xlim[0], xlim[1], 35)
        y_grid = np.linspace(ylim[0], ylim[1], 35)
        X, Y = np.meshgrid(x_grid, y_grid)

        colors = [USS_BLUE, USS_GOLD, USS_ACCENT_BLUE]
        plane_labels = [
            f"pi1: {self.A_np[0,0]:.0f}x + {self.A_np[0,1]:.0f}y + {self.A_np[0,2]:.0f}z = {self.b_np[0,0]:.0f}",
            f"pi2: {self.A_np[1,0]:.0f}x + {self.A_np[1,1]:.0f}y + {self.A_np[1,2]:.0f}z = {self.b_np[1,0]:.0f}",
            f"pi3: {self.A_np[2,0]:.0f}x + {self.A_np[2,1]:.0f}y + {self.A_np[2,2]:.0f}z = {self.b_np[2,0]:.0f}",
        ]

        # Graficación de cada plano ax + by + cz = d con alpha=0.22 y contornos edgecolor='gray'
        for i in range(3):
            a, b_val, c = self.A_np[i]
            d = self.b_np[i, 0]

            if abs(c) >= 1e-4:
                Z = (d - a * X - b_val * Y) / c
                ax.plot_surface(X, Y, Z, color=colors[i], alpha=0.22, edgecolor='gray', linewidth=0.3, label=plane_labels[i])
            elif abs(b_val) >= 1e-4:
                z_grid = np.linspace(-5, 5, 35)
                X_plane, Z_plane = np.meshgrid(x_grid, z_grid)
                Y_plane = (d - a * X_plane - c * Z_plane) / b_val
                ax.plot_surface(X_plane, Y_plane, Z_plane, color=colors[i], alpha=0.22, edgecolor='gray', linewidth=0.3, label=plane_labels[i])
            elif abs(a) >= 1e-4:
                z_grid = np.linspace(-5, 5, 35)
                Y_plane, Z_plane = np.meshgrid(y_grid, z_grid)
                X_plane = (d - b_val * Y_plane - c * Z_plane) / a
                ax.plot_surface(X_plane, Y_plane, Z_plane, color=colors[i], alpha=0.22, edgecolor='gray', linewidth=0.3, label=plane_labels[i])

        handles = [
            plt.Rectangle((0, 0), 1, 1, fc=colors[0], alpha=0.4),
            plt.Rectangle((0, 0), 1, 1, fc=colors[1], alpha=0.4),
            plt.Rectangle((0, 0), 1, 1, fc=colors[2], alpha=0.4),
        ]
        labels = list(plane_labels)

        # Visualización específica según clasificación de Rouché-Frobenius
        if rf["type"] == "SCD":
            try:
                x_sol = float(np.linalg.solve(self.A_np, self.b_np.flatten())[0])
                y_sol = float(np.linalg.solve(self.A_np, self.b_np.flatten())[1])
                z_sol = float(np.linalg.solve(self.A_np, self.b_np.flatten())[2])

                # Punto único P0 marcado y destacado
                ax.scatter([x_sol], [y_sol], [z_sol], color=USS_ACCENT_RED, s=130, zorder=10,
                           edgecolor='black', linewidth=1.5)

                # Líneas de proyección punteadas desde P0 hasta los planos coordenados
                ax.plot([x_sol, x_sol], [y_sol, y_sol], [-5, z_sol], color=USS_ACCENT_RED, linestyle=':', alpha=0.8, linewidth=1.3)
                ax.plot([x_sol, x_sol], [-5, y_sol], [z_sol, z_sol], color=USS_ACCENT_RED, linestyle=':', alpha=0.8, linewidth=1.3)
                ax.plot([-5, x_sol], [y_sol, y_sol], [z_sol, z_sol], color=USS_ACCENT_RED, linestyle=':', alpha=0.8, linewidth=1.3)

                # Marcadores en las proyecciones sobre planos coordenados
                ax.scatter([x_sol], [y_sol], [-5], color=USS_DARK_GRAY, s=35, alpha=0.7, edgecolors='black', linewidths=0.8)
                ax.scatter([x_sol], [-5], [z_sol], color=USS_DARK_GRAY, s=35, alpha=0.7, edgecolors='black', linewidths=0.8)
                ax.scatter([-5], [y_sol], [z_sol], color=USS_DARK_GRAY, s=35, alpha=0.7, edgecolors='black', linewidths=0.8)

                ax.text(x_sol + 0.35, y_sol + 0.35, z_sol + 0.35,
                        f"P0({x_sol:.1f}, {y_sol:.1f}, {z_sol:.1f})",
                        color=USS_ACCENT_RED, fontweight='bold', fontsize=10,
                        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=USS_ACCENT_RED, lw=1.2, alpha=0.9))

                p0_proxy = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=USS_ACCENT_RED,
                                      markeredgecolor='black', markersize=9)
                handles.append(p0_proxy)
                labels.append(f"Solución única P0({x_sol:.1f}, {y_sol:.1f}, {z_sol:.1f})")
            except Exception:
                pass

        elif rf["type"] == "SCI" and rf["degrees_of_freedom"] == 1:
            try:
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
                            color=USS_ACCENT_RED, linewidth=3.5, label="Recta común L(t)")

                    # Punto representativo sobre la recta L(t) y líneas de proyección
                    p_mid = line_pts[len(line_pts)//2]
                    ax.scatter([p_mid[0]], [p_mid[1]], [p_mid[2]], color=USS_ACCENT_RED, s=80,
                               zorder=10, edgecolor='black', linewidth=1.2)
                    ax.plot([p_mid[0], p_mid[0]], [p_mid[1], p_mid[1]], [-5, p_mid[2]], color=USS_ACCENT_RED, linestyle=':', alpha=0.7, linewidth=1.1)
                    ax.plot([p_mid[0], p_mid[0]], [-5, p_mid[1]], [p_mid[2], p_mid[2]], color=USS_ACCENT_RED, linestyle=':', alpha=0.7, linewidth=1.1)
                    ax.plot([-5, p_mid[0]], [p_mid[1], p_mid[1]], [p_mid[2], p_mid[2]], color=USS_ACCENT_RED, linestyle=':', alpha=0.7, linewidth=1.1)

                    line_proxy = plt.Line2D([0], [0], color=USS_ACCENT_RED, lw=3.5)
                    handles.append(line_proxy)
                    labels.append("Recta de solución común L(t)")
            except Exception:
                pass

        elif rf["type"] == "SI":
            # Trazado de las rectas de intersección dos a dos que forman el prisma triangular
            line_colors = [USS_ACCENT_RED, USS_ACCENT_GREEN, USS_GOLD]
            pair_names = ["pi1 y pi2", "pi1 y pi3", "pi2 y pi3"]
            pairs = [(0, 1), (0, 2), (1, 2)]

            for p_idx, (i, j) in enumerate(pairs):
                n_i = self.A_np[i]
                n_j = self.A_np[j]
                v_dir = np.cross(n_i, n_j)
                norm_v = np.linalg.norm(v_dir)

                if norm_v > 1e-4:
                    v_dir_unit = v_dir / norm_v
                    N_mat = np.vstack([n_i, n_j])
                    d_vec = np.array([self.b_np[i, 0], self.b_np[j, 0]])
                    p_particular = np.linalg.pinv(N_mat) @ d_vec

                    t_line = np.linspace(-6, 6, 80)
                    pts = p_particular[:, None] + v_dir_unit[:, None] * t_line[None, :]
                    ax.plot(pts[0], pts[1], pts[2], color=line_colors[p_idx], linewidth=2.5,
                            linestyle='-', label=f"Intersección {pair_names[p_idx]}")

                    line_proxy = plt.Line2D([0], [0], color=line_colors[p_idx], lw=2.5)
                    handles.append(line_proxy)
                    labels.append(f"Intersección {pair_names[p_idx]}")

        # Configuración de ejes y estética institucional USS
        ax.set_xlabel('Eje X', fontsize=10, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_ylabel('Eje Y', fontsize=10, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_zlabel('Eje Z', fontsize=10, fontweight='bold', color=USS_DARK_GRAY)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_zlim(-5, 5)

        title_str = (f"Rouché-Frobenius: {rf['name']} ({rf['type']})\n"
                     f"rg(A) = {rf['rank_A']}, rg(A|b) = {rf['rank_Ab']}, n = {rf['n']}")
        ax.set_title(title_str, fontsize=11, fontweight='bold', color=USS_BLUE, pad=15)

        # Vista óptima según estándar USS
        ax.view_init(elev=elev, azim=azim)
        ax.grid(True, linestyle=':', alpha=0.5)

        # Leyenda fuera de colisión
        ax.legend(handles, labels, loc='upper left', bbox_to_anchor=(0.0, 0.96),
                  fontsize=8.5, framealpha=0.9)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')

        if show_plot and os.environ.get('DISPLAY', '') != '':
            plt.show()

        plt.close(fig)
        return fig


# ==============================================================================
# DEMOSTRACIÓN EN TERMINAL (CASOS SCD, SCI, SI)
# ==============================================================================
def run_demonstration():
    """Ejecuta la suite pedagógica limpia para los tres casos de Rouché-Frobenius."""
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # --------------------------------------------------------------------------
    # CASO 1: Sistema Compatible Determinado (SCD)
    # --------------------------------------------------------------------------
    print("--- Caso 1: Sistema Compatible Determinado (SCD) ---")
    print("Sistema:")
    print("   2x +  y -  z =  8")
    print("  -3x -  y + 2z = -11")
    print("  -2x +  y + 2z = -3")

    A1 = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b1 = [8, -11, -3]
    sys1 = LinearSystem3D(A1, b1)
    rf1 = sys1.rouche_frobenius_analysis()

    print(f"Diagnóstico Rouché-Frobenius: rg(A) = {rf1['rank_A']}, rg(A|b) = {rf1['rank_Ab']}, n = {rf1['n']}")
    print(f"Tipo: {rf1['name']} ({rf1['type']})")
    print("Solución única: x = 2, y = 3, z = -1\n")

    img1_path = os.path.join(output_dir, "01_gauss_rouche_scd.png")
    sys1.plot_system_3d(save_path=img1_path, show_plot=False)

    # --------------------------------------------------------------------------
    # CASO 2: Sistema Compatible Indeterminado (SCI)
    # --------------------------------------------------------------------------
    print("--- Caso 2: Sistema Compatible Indeterminado (SCI) ---")
    print("Sistema:")
    print("   x +  y +  z = 3")
    print("  2x -  y + 3z = 4")
    print("  3x + 0y + 4z = 7")

    A2 = [[1, 1, 1], [2, -1, 3], [3, 0, 4]]
    b2 = [3, 4, 7]
    sys2 = LinearSystem3D(A2, b2)
    rf2 = sys2.rouche_frobenius_analysis()
    _, _, sol2 = sys2.gauss_jordan_step_by_step()

    print(f"Diagnóstico Rouché-Frobenius: rg(A) = {rf2['rank_A']}, rg(A|b) = {rf2['rank_Ab']}, n = {rf2['n']}")
    print(f"Tipo: {rf2['name']} ({rf2['type']})")
    print(f"Grados de libertad: {rf2['degrees_of_freedom']}")
    print(f"Solución paramétrica: {sol2}\n")

    img2_path = os.path.join(output_dir, "01_gauss_rouche_sci.png")
    sys2.plot_system_3d(save_path=img2_path, show_plot=False)

    # --------------------------------------------------------------------------
    # CASO 3: Sistema Incompatible (SI)
    # --------------------------------------------------------------------------
    print("--- Caso 3: Sistema Incompatible (SI) ---")
    print("Sistema:")
    print("   x +  y +  z = 1")
    print("   x -  y + 2z = 2")
    print("  2x + 0y + 3z = 5")

    A3 = [[1, 1, 1], [1, -1, 2], [2, 0, 3]]
    b3 = [1, 2, 5]
    sys3 = LinearSystem3D(A3, b3)
    rf3 = sys3.rouche_frobenius_analysis()

    print(f"Diagnóstico Rouché-Frobenius: rg(A) = {rf3['rank_A']}, rg(A|b) = {rf3['rank_Ab']}, n = {rf3['n']}")
    print(f"Tipo: {rf3['name']} ({rf3['type']})")
    print("Interpretación: Sin solución (Prisma triangular sin punto común)\n")

    img3_path = os.path.join(output_dir, "01_gauss_rouche_si.png")
    sys3.plot_system_3d(save_path=img3_path, show_plot=False)


if __name__ == '__main__':
    run_demonstration()
