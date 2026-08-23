"""Figura reproducible del capítulo 7 de Grossman.

Compara una transformacion lineal invertible (corte horizontal) con una
proyeccion que reduce el rango. La salida usa la paleta institucional USS.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


USS_BLUE = "#00205B"
USS_GOLD = "#D4AF37"
GRID = "#D9DEE8"
INK = "#1B2430"


def closed(points: np.ndarray) -> np.ndarray:
    """Close a polygon by repeating its first vertex."""
    return np.vstack([points, points[0]])


def style_axis(ax: plt.Axes, title: str) -> None:
    ax.set_title(title, color=USS_BLUE, fontweight="bold")
    ax.axhline(0, color=INK, linewidth=0.8)
    ax.axvline(0, color=INK, linewidth=0.8)
    ax.grid(True, color=GRID, linewidth=0.7, alpha=0.8)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-0.35, 1.85)
    ax.set_ylim(-0.35, 1.55)
    ax.set_xlabel("x")
    ax.set_ylabel("y")


def verify_exact_results() -> None:
    """Verify the chapter's matrix identities with exact arithmetic."""
    A = sp.Matrix([[1, -1, 0], [0, 1, 1]])
    assert A.rank() == 2
    assert len(A.nullspace()) == 1
    assert A.rank() + len(A.nullspace()) == A.cols

    C = sp.Matrix([[12, 10], [-15, -13]])
    P_B = sp.Matrix([[1, 2], [-1, -3]])
    assert P_B.det() != 0
    assert P_B.inv() * C * P_B == sp.diag(2, -3)

    Q = sp.Matrix(
        [
            [sp.Rational(1, 2), -sp.sqrt(3) / 2],
            [sp.sqrt(3) / 2, sp.Rational(1, 2)],
        ]
    )
    assert (Q.T * Q).applyfunc(sp.simplify) == sp.eye(2)


def build_figure(output_path: Path) -> None:
    """Draw the shear/projection comparison and save it as a PNG."""
    square = np.array(
        [
            [0.0, 0.0],
            [1.0, 0.0],
            [1.0, 1.0],
            [0.0, 1.0],
        ]
    )
    shear = np.array([[1.0, 0.65], [0.0, 1.0]])
    projection = np.array([[1.0, 0.0], [0.0, 0.0]])

    sheared_square = square @ shear.T
    projected_square = square @ projection.T

    fig, axes = plt.subplots(1, 2, figsize=(11, 5), facecolor="white")
    fig.suptitle(
        "Capítulo 7 · Transformaciones lineales",
        color=USS_BLUE,
        fontsize=15,
        fontweight="bold",
    )

    ax = axes[0]
    style_axis(ax, "Corte horizontal: rango completo")
    ax.plot(*closed(square).T, linestyle="--", color=INK, linewidth=1.2, label="Original")
    ax.fill(*closed(sheared_square).T, color=USS_GOLD, alpha=0.28)
    ax.plot(*closed(sheared_square).T, color=USS_GOLD, linewidth=2.5, label="Imagen por A")
    ax.arrow(0, 0, 1, 0, color=USS_BLUE, width=0.008, head_width=0.07, length_includes_head=True)
    ax.arrow(0, 0, 0.65, 1, color=USS_BLUE, width=0.008, head_width=0.07, length_includes_head=True)
    ax.text(0.08, 1.33, "A = [[1, 0.65], [0, 1]]", color=USS_BLUE, fontsize=9)
    ax.legend(loc="lower right", frameon=True)

    ax = axes[1]
    style_axis(ax, "Proyección sobre el eje x: núcleo no trivial")
    ax.plot(*closed(square).T, linestyle="--", color=INK, linewidth=1.2, label="Original")
    ax.plot(*closed(projected_square).T, color=USS_BLUE, linewidth=3.0, label="Imagen por P")
    ax.scatter(projected_square[:, 0], projected_square[:, 1], color=USS_BLUE, zorder=4)
    ax.arrow(0, 0, 1, 0, color=USS_GOLD, width=0.008, head_width=0.07, length_includes_head=True)
    ax.text(0.08, 1.33, "P = [[1, 0], [0, 0]]", color=USS_BLUE, fontsize=9)
    ax.text(0.08, 1.18, "ker(P) = span{(0, 1)}", color=USS_BLUE, fontsize=9)
    ax.legend(loc="lower right", frameon=True)

    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(output_path, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main() -> None:
    verify_exact_results()
    output_path = Path(__file__).with_name("grossman_capitulo_7_transformacion.png")
    build_figure(output_path)

    # A numerical norm check complements the exact SymPy checks.
    rotation = np.array([[0.5, -np.sqrt(3) / 2], [np.sqrt(3) / 2, 0.5]])
    vector = np.array([2.0, 1.0])
    assert np.allclose(np.linalg.norm(rotation @ vector), np.linalg.norm(vector))
    print("[PASS] Grossman capítulo 7: rango-nulidad, cambio de base e isometría")
    print(f"[PASS] Figura generada: {output_path}")


if __name__ == "__main__":
    main()
