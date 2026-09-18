#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
UNIVERSIDAD SAN SEBASTIÁN — FACULTAD DE INGENIERÍA, ARQUITECTURA Y DISEÑO
Carrera: Ingeniería Civil Informática
Asignatura: Álgebra Lineal
Docente: Carol Asencio González
Módulo 03: Matrices, Menores, Cofactores, Matriz Adjunta e Inversión Matricial
================================================================================
Trazabilidad de Fuentes:
🎓 [Cátedra USS / Diapositivas Docente] : Expansión de Laplace, matriz de cofactores
    Cof(A), matriz adjunta Adj(A) = [Cof(A)]^T, fórmula A^(-1) = (1/det A)*Adj(A).
📖 [Texto Guía — Grossman / Poole]     : Teorema fundamental de la adjunta A*Adj(A) = det(A)*I,
    cálculo de determinantes n x n y verificación formal de invertibilidad.
🌐 [Computación Científica]            : Aritmética racional exacta con SymPy,
    mapas de calor visuales matriciales anotados con Matplotlib.
================================================================================
"""

import os
import sys
from typing import List, Tuple, Optional, Dict, Any

# Configuración de backend seguro para entornos headless
if os.environ.get('DISPLAY', '') == '':
    import matplotlib
    matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
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


class MatrixCofactorInverter:
    """
    Clase para el cálculo didáctico paso a paso de determinantes (Laplace),
    menores complementarios, cofactores, matriz adjunta e inversa exacta.
    """

    def __init__(self, matrix_data: List[List[Any]]):
        """
        Inicializa con una lista de listas de enteros, racionales o flotantes.
        """
        self.A_sp = sp.Matrix(matrix_data)
        self.n = self.A_sp.rows
        if self.A_sp.cols != self.n:
            raise ValueError(f"La matriz debe ser cuadrada (dimensiones dadas: {self.n}x{self.A_sp.cols}).")

        self.det_A = self.A_sp.det()
        self.is_invertible = (self.det_A != 0)

    def get_minor_matrix(self, i: int, j: int) -> sp.Matrix:
        """
        Obtiene la submatriz que resulta de eliminar la fila i y la columna j (0-indexada).
        """
        rows = [r for r in range(self.n) if r != i]
        cols = [c for c in range(self.n) if c != j]
        return self.A_sp.extract(rows, cols)

    def compute_minors_and_cofactors(self) -> Tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
        """
        Calcula:
        - M: Matriz de menores M_ij = det(submatriz_ij).
        - S: Tablero de signos (-1)^(i+j).
        - C: Matriz de cofactores C_ij = (-1)^(i+j) * M_ij.
        """
        M = sp.zeros(self.n, self.n)
        S = sp.zeros(self.n, self.n)
        C = sp.zeros(self.n, self.n)

        for i in range(self.n):
            for j in range(self.n):
                sign = (-1) ** (i + j)
                sub_M = self.get_minor_matrix(i, j)
                minor_det = sub_M.det()
                cofactor_val = sign * minor_det

                M[i, j] = minor_det
                S[i, j] = sign
                C[i, j] = cofactor_val

        return M, S, C

    def compute_adjugate(self, C: sp.Matrix) -> sp.Matrix:
        """
        Calcula la matriz adjunta clásica: Adj(A) = [Cof(A)]^T.
        """
        return C.T

    def compute_inverse(self) -> Tuple[Optional[sp.Matrix], Dict[str, Any]]:
        """
        Calcula la inversa por el método de cofactores:
            A^(-1) = (1 / det(A)) * Adj(A)
        Retorna la matriz inversa y un informe paso a paso.
        """
        M, S, C = self.compute_minors_and_cofactors()
        Adj = self.compute_adjugate(C)

        report = {
            "n": self.n,
            "det": self.det_A,
            "is_invertible": self.is_invertible,
            "minors": M,
            "signs": S,
            "cofactors": C,
            "adjugate": Adj,
            "inverse": None,
            "verification_A_Adj": self.A_sp * Adj,
            "verification_identity": None
        }

        if not self.is_invertible:
            return None, report

        inv_A = (sp.Rational(1, self.det_A)) * Adj
        report["inverse"] = inv_A
        report["verification_identity"] = self.A_sp * inv_A

        return inv_A, report

    def laplace_expansion_steps(self, row_idx: int = 0) -> List[str]:
        """
        Genera la explicación textual paso a paso del desarrollo de Laplace por la fila seleccionada.
        """
        steps = []
        steps.append(f"Desarrollo de Laplace a lo largo de la Fila {row_idx + 1}:")
        terms_formula = []
        terms_num = []
        total = sp.Rational(0, 1)

        for j in range(self.n):
            a_ij = self.A_sp[row_idx, j]
            sign = (-1) ** (row_idx + j)
            sub_M = self.get_minor_matrix(row_idx, j)
            minor_val = sub_M.det()
            cofactor_val = sign * minor_val
            term_val = a_ij * cofactor_val
            total += term_val

            sign_str = "+" if sign == 1 else "-"
            terms_formula.append(f"({sign_str}1) * ({a_ij}) * det(M_{{{row_idx+1},{j+1}}})")
            terms_num.append(f"({a_ij}) * ({cofactor_val})")

            steps.append(
                f"  • Elemento a_{{{row_idx+1},{j+1}}} = {a_ij}: "
                f"Signo = (-1)^{{{row_idx+1}+{j+1}}} = {sign:+d}, "
                f"Menor M_{{{row_idx+1},{j+1}}} = {minor_val} => "
                f"Cofactor C_{{{row_idx+1},{j+1}}} = {cofactor_val}"
            )

        steps.append(f"Fórmula: det(A) = " + " + ".join(terms_formula))
        steps.append(f"Sustitución: det(A) = " + " + ".join(terms_num) + f" = {total}")
        return steps

    def plot_matrix_diagram(self, save_path: Optional[str] = None, show_plot: bool = True):
        """
        Genera un diagrama gráfico de 6 tableros con mapas de calor anotados:
        1. Matriz A
        2. Tablero de Signos (-1)^(i+j)
        3. Matriz de Cofactores Cof(A)
        4. Matriz Adjunta Adj(A) = [Cof(A)]^T
        5. Matriz Inversa A^(-1) = (1/det A) * Adj(A)
        6. Verificación A * A^(-1) = I
        """
        inv_A, rep = self.compute_inverse()

        fig, axes = plt.subplots(2, 3, figsize=(15, 10), facecolor='white')
        fig.suptitle(
            f"UNIVERSIDAD SAN SEBASTIÁN — DESCOMPOSICIÓN POR COFACTORES E INVERSA\n"
            f"Matriz de Orden {self.n}x{self.n} | det(A) = {self.det_A} "
            f"({'Invertible / No Singular' if self.is_invertible else 'Singular / No Invertible'})",
            fontsize=13, fontweight='bold', color=USS_BLUE, y=0.98
        )

        titles = [
            "1. Matriz Original $A$",
            "2. Tablero de Signos $(-1)^{i+j}$",
            "3. Matriz de Cofactores $\\operatorname{Cof}(A)$",
            "4. Matriz Adjunta $\\operatorname{Adj}(A) = [\\operatorname{Cof}(A)]^T$",
            "5. Matriz Inversa $A^{-1} = \\frac{1}{\\det A}\\operatorname{Adj}(A)$",
            "6. Verificación $A \\cdot A^{-1} = I$"
        ]

        matrices_to_plot = [
            self.A_sp,
            rep["signs"],
            rep["cofactors"],
            rep["adjugate"],
            inv_A if inv_A is not None else sp.zeros(self.n, self.n),
            rep["verification_identity"] if inv_A is not None else sp.zeros(self.n, self.n)
        ]

        # Configuración de mapas de colores institucionales
        cmap_blue = mcolors.LinearSegmentedColormap.from_list("uss_blue_map", [USS_LIGHT_GRAY, USS_ACCENT_BLUE, USS_BLUE])
        cmap_gold = mcolors.LinearSegmentedColormap.from_list("uss_gold_map", [USS_LIGHT_GRAY, USS_GOLD, '#B7950B'])
        cmap_green = mcolors.LinearSegmentedColormap.from_list("uss_green_map", [USS_LIGHT_GRAY, USS_ACCENT_GREEN, '#1E8449'])

        cmaps = [cmap_blue, cmap_gold, cmap_blue, cmap_gold, cmap_blue, cmap_green]

        for idx, ax in enumerate(axes.flat):
            mat = matrices_to_plot[idx]
            # Convertir a float para visualización en imshow
            mat_num = np.array(mat.tolist(), dtype=float)

            # Normalización simétrica para destacar positivos/negativos
            max_abs = max(1.0, float(np.max(np.abs(mat_num))))
            im = ax.imshow(mat_num, cmap=cmaps[idx], vmin=-max_abs, vmax=max_abs, aspect='auto')

            ax.set_title(titles[idx], fontsize=11, fontweight='bold', color=USS_BLUE, pad=10)
            ax.set_xticks(range(self.n))
            ax.set_yticks(range(self.n))
            ax.set_xticklabels([f"C{j+1}" for j in range(self.n)], fontsize=9, color=USS_DARK_GRAY)
            ax.set_yticklabels([f"F{i+1}" for i in range(self.n)], fontsize=9, color=USS_DARK_GRAY)

            # Escribir valores exactos en texto grande en cada celda
            for i in range(self.n):
                for j in range(self.n):
                    val_sp = mat[i, j]
                    # Representación limpia en fracción si aplica
                    if idx == 1:
                        val_str = f"{'+' if val_sp == 1 else '-'}"
                    elif isinstance(val_sp, sp.Rational) and val_sp.q != 1:
                        val_str = f"{val_sp.p}/{val_sp.q}"
                    else:
                        val_str = f"{val_sp}"

                    # Color de texto para garantizar alto contraste
                    cell_val = mat_num[i, j]
                    text_color = 'white' if abs(cell_val) > 0.5 * max_abs else USS_DARK_GRAY
                    ax.text(j, i, val_str, ha="center", va="center", color=text_color,
                            fontweight='bold', fontsize=12)

            # Borde sutil
            for edge, spine in ax.spines.items():
                spine.set_color(USS_DARK_GRAY)
                spine.set_linewidth(1.2)

        plt.tight_layout(rect=[0, 0, 1, 0.94])

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"-> Diagrama de cofactores guardado en: {save_path}")

        if show_plot and os.environ.get('DISPLAY', '') != '':
            plt.show()

        plt.close(fig)


# ==============================================================================
# DEMOSTRACIÓN EN TERMINAL
# ==============================================================================
def run_demonstration():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    print("=" * 80)
    print("UNIVERSIDAD SAN SEBASTIÁN — SIMULADOR 03: COFACTORES E INVERSA MATRICIAL")
    print("=" * 80)

    # Matriz oficial 3x3 de prueba didáctica (valores enteros con inversa limpia)
    # Matriz A:
    #   [ 1,  2, -1 ]
    #   [ 2,  0,  1 ]
    #   [ 1,  1,  1 ]
    matrix_example = [
        [1, 2, -1],
        [2, 0, 1],
        [1, 1, 1]
    ]

    inverter = MatrixCofactorInverter(matrix_example)
    print("\n[1] Matriz Original A:")
    sp.pprint(inverter.A_sp)

    print("\n[2] Determinante por Expansión de Laplace (Fila 1):")
    for step in inverter.laplace_expansion_steps(row_idx=0):
        print(step)

    print(f"\nResultado final: det(A) = {inverter.det_A}")
    if inverter.is_invertible:
        print("-> Como det(A) != 0, la matriz es NO SINGULAR (Invertible).")
    else:
        print("-> Como det(A) == 0, la matriz es SINGULAR (No invertible).")

    inv, report = inverter.compute_inverse()

    print("\n[3] Matriz de Menores Complementarios M = (det(M_ij)):")
    sp.pprint(report["minors"])

    print("\n[4] Tablero de Signos S = (-1)^(i+j):")
    sp.pprint(report["signs"])

    print("\n[5] Matriz de Cofactores Cof(A) = (C_ij):")
    sp.pprint(report["cofactors"])

    print("\n[6] Matriz Adjunta Adj(A) = [Cof(A)]^T:")
    sp.pprint(report["adjugate"])

    print(f"\n[7] Matriz Inversa A^(-1) = (1/{inverter.det_A}) * Adj(A):")
    sp.pprint(inv)

    print("\n[8] Verificación Formal:")
    print("  • A * Adj(A) = det(A) * I:")
    sp.pprint(report["verification_A_Adj"])
    print("  • A * A^(-1) = I:")
    sp.pprint(report["verification_identity"])

    print("\n[9] Generando Diagrama Gráfico Matricial...")
    img_path = os.path.join(output_dir, "03_matrices_cofactores_inversa_diagrama.png")
    inverter.plot_matrix_diagram(save_path=img_path, show_plot=False)

    print("\n" + "=" * 80)
    print("DEMOSTRACIÓN FINALIZADA CON ÉXITO.")
    print("=" * 80)


if __name__ == '__main__':
    run_demonstration()
