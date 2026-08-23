"""Generate the USS synthesis figure for Grossman's chapter 3.

The figure connects the geometric meaning of a determinant with cofactors
and Cramer's rule. It is intentionally deterministic so that it can be
regenerated from this file without any interactive backend.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Rectangle


USS_BLUE = "#00205B"
USS_GOLD = "#D4AF37"
WHITE = "#FFFFFF"
GRID = "#D9DEE8"


def style_axis(ax, title):
    """Apply the institutional colors and a readable academic layout."""
    ax.set_title(title, color=USS_BLUE, fontweight="bold", pad=12)
    ax.set_facecolor(WHITE)
    ax.grid(True, color=GRID, linewidth=0.8, alpha=0.75)
    for spine in ax.spines.values():
        spine.set_color(USS_GOLD)
        spine.set_linewidth(1.2)
    ax.tick_params(colors=USS_BLUE)


def draw_vector(ax, vector, color, label, offset=(0.08, 0.08)):
    """Draw a vector from the origin and place its label at the tip."""
    ax.quiver(
        0,
        0,
        vector[0],
        vector[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color=color,
        width=0.009,
        headwidth=5,
        headlength=7,
    )
    ax.text(
        vector[0] + offset[0],
        vector[1] + offset[1],
        label,
        color=color,
        fontweight="bold",
    )


def draw_cofactor_signs(ax, matrix):
    """Show the checkerboard signs and entries of a cofactor matrix."""
    ax.set_xlim(0, matrix.shape[1])
    ax.set_ylim(matrix.shape[0], 0)
    ax.set_aspect("equal")
    ax.set_xticks(np.arange(matrix.shape[1]) + 0.5)
    ax.set_yticks(np.arange(matrix.shape[0]) + 0.5)
    ax.set_xticklabels(["j=1", "j=2", "j=3"], color=USS_BLUE)
    ax.set_yticklabels(["i=1", "i=2", "i=3"], color=USS_BLUE)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            positive = (i + j) % 2 == 0
            ax.add_patch(
                Rectangle(
                    (j, i),
                    1,
                    1,
                    facecolor=USS_GOLD if positive else USS_BLUE,
                    edgecolor=WHITE,
                    linewidth=1.5,
                )
            )
            text_color = USS_BLUE if positive else WHITE
            sign = "+" if positive else "-"
            ax.text(
                j + 0.5,
                i + 0.5,
                f"{matrix[i, j]}\n{sign}",
                ha="center",
                va="center",
                color=text_color,
                fontweight="bold",
            )
    ax.set_xlabel(r"$C_{ij}=(-1)^{i+j}\det(M_{ij})$", color=USS_BLUE, labelpad=10)
    ax.tick_params(length=0)


def main():
    output = Path(__file__).with_name("grossman_capitulo_3_figura.png")

    u = np.array([2.0, 1.0])
    v = np.array([1.0, 3.0])
    determinant = int(round(np.linalg.det(np.column_stack((u, v)))))
    parallelogram = np.array([[0.0, 0.0], u, u + v, v])

    cofactor_matrix = np.array([[1, 2, 0], [2, 1, 1], [0, 1, 1]])
    cramer_labels = ["D", "D1", "D2", "D3"]
    cramer_values = np.array([-4, -4, -8, -12])

    fig = plt.figure(figsize=(14, 5.8), facecolor=WHITE, constrained_layout=True)
    grid = fig.add_gridspec(1, 3, width_ratios=(1.2, 1.0, 1.15), wspace=0.35)
    fig.suptitle(
        "Grossman, Capítulo 3 | Determinantes: área, cofactores y Cramer",
        color=USS_BLUE,
        fontsize=16,
        fontweight="bold",
    )

    ax_geometry = fig.add_subplot(grid[0, 0])
    ax_geometry.add_patch(
        Polygon(
            parallelogram,
            closed=True,
            facecolor=USS_GOLD,
            edgecolor=USS_BLUE,
            linewidth=2,
            alpha=0.28,
        )
    )
    draw_vector(ax_geometry, u, USS_BLUE, r"$u$")
    draw_vector(ax_geometry, v, USS_GOLD, r"$v$", offset=(0.08, -0.20))
    ax_geometry.plot(
        [u[0], u[0] + v[0]],
        [u[1], u[1] + v[1]],
        linestyle="--",
        color=USS_BLUE,
        linewidth=1.2,
    )
    ax_geometry.plot(
        [v[0], v[0] + u[0]],
        [v[1], v[1] + u[1]],
        linestyle="--",
        color=USS_GOLD,
        linewidth=1.2,
    )
    ax_geometry.scatter(*u, color=USS_BLUE, s=32, zorder=3)
    ax_geometry.scatter(*v, color=USS_GOLD, s=32, zorder=3)
    style_axis(ax_geometry, "3.1 Interpretación geométrica")
    ax_geometry.set_xlabel("x", color=USS_BLUE)
    ax_geometry.set_ylabel("y", color=USS_BLUE)
    ax_geometry.set_aspect("equal", adjustable="box")
    ax_geometry.set_xlim(-0.4, 3.5)
    ax_geometry.set_ylim(-0.4, 4.6)
    ax_geometry.text(
        0.04,
        0.04,
        f"$\\det[u\\ v]={determinant}$\nÁrea = $|\\det A|$",
        transform=ax_geometry.transAxes,
        color=USS_BLUE,
        fontweight="bold",
        bbox={"facecolor": WHITE, "edgecolor": USS_GOLD, "alpha": 0.92},
    )

    ax_cofactors = fig.add_subplot(grid[0, 1])
    draw_cofactor_signs(ax_cofactors, cofactor_matrix)
    style_axis(ax_cofactors, "3.3 Cofactores")

    ax_cramer = fig.add_subplot(grid[0, 2])
    bars = ax_cramer.bar(
        cramer_labels,
        cramer_values,
        color=[USS_BLUE, USS_GOLD, USS_GOLD, USS_GOLD],
        edgecolor=USS_BLUE,
        linewidth=1.0,
    )
    ax_cramer.axhline(0, color=USS_BLUE, linewidth=1.0)
    for bar, value in zip(bars, cramer_values):
        vertical = 0.35 if value < 0 else -0.35
        ax_cramer.text(
            bar.get_x() + bar.get_width() / 2,
            value + vertical,
            str(value),
            ha="center",
            va="center",
            color=WHITE if value < 0 else USS_BLUE,
            fontweight="bold",
        )
    style_axis(ax_cramer, "3.4 Regla de Cramer")
    ax_cramer.set_ylabel("determinante", color=USS_BLUE)
    ax_cramer.text(
        0.5,
        0.06,
        r"$(x_1,x_2,x_3)=(D_1/D,D_2/D,D_3/D)=(1,2,3)$",
        transform=ax_cramer.transAxes,
        ha="center",
        color=USS_BLUE,
        fontweight="bold",
        bbox={"facecolor": WHITE, "edgecolor": USS_GOLD, "alpha": 0.92},
    )

    fig.savefig(output, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print(f"Figura generada: {output}")


if __name__ == "__main__":
    main()
