"""Generate a USS visual summary for Grossman's chapter 1."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


USS_BLUE = "#00205B"
USS_GOLD = "#D4AF37"
WHITE = "#FFFFFF"
GRID_BLUE = "#DCE6F2"


def style_axis(ax, title):
    ax.set_facecolor(WHITE)
    ax.set_title(title, color=USS_BLUE, fontweight="bold", pad=10)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-8, 8)
    ax.set_xlabel("x", color=USS_BLUE)
    ax.set_ylabel("y", color=USS_BLUE)
    ax.axhline(0, color="#AAB8C8", linewidth=0.8, zorder=0)
    ax.axvline(0, color="#AAB8C8", linewidth=0.8, zorder=0)
    ax.grid(True, color=GRID_BLUE, linewidth=0.7, alpha=0.8)
    ax.tick_params(colors=USS_BLUE)
    for spine in ax.spines.values():
        spine.set_color(USS_GOLD)
        spine.set_linewidth(1.2)


def main():
    x = np.linspace(-4, 4, 500)
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.8), facecolor=WHITE)

    # D != 0: the two lines intersect once at (2, 1).
    unique_ax = axes[0]
    style_axis(unique_ax, "Solucion unica")
    unique_ax.plot(x, 1.5 * x - 2, color=USS_BLUE, linewidth=2.4, label="3x - 2y = 4")
    unique_ax.plot(x, -2.5 * x + 6, color=USS_GOLD, linewidth=2.4, label="5x + 2y = 12")
    unique_ax.scatter([2], [1], s=70, color=USS_GOLD, edgecolor=USS_BLUE, linewidth=1.5, zorder=4)
    unique_ax.annotate("(2, 1)", (2, 1), xytext=(2.2, 2.0), color=USS_BLUE, fontweight="bold")
    unique_ax.legend(fontsize=8, loc="lower right", frameon=True, facecolor=WHITE, edgecolor=USS_GOLD)

    # D = 0 with incompatible constants: parallel distinct lines.
    inconsistent_ax = axes[1]
    style_axis(inconsistent_ax, "Sin solucion")
    inconsistent_ax.plot(x, x - 7, color=USS_BLUE, linewidth=2.4, label="x - y = 7")
    inconsistent_ax.plot(x, x - 6.5, color=USS_GOLD, linewidth=2.4, label="2x - 2y = 13")
    inconsistent_ax.text(-3.7, 5.8, "paralelas", color=USS_BLUE, fontweight="bold")
    inconsistent_ax.legend(fontsize=8, loc="lower right", frameon=True, facecolor=WHITE, edgecolor=USS_GOLD)

    # D = 0 with compatible constants: coincident lines.
    infinite_ax = axes[2]
    style_axis(infinite_ax, "Infinitas soluciones")
    infinite_ax.plot(x, x - 7, color=USS_BLUE, linewidth=3.0, label="x - y = 7")
    infinite_ax.plot(x, x - 7, color=USS_GOLD, linewidth=1.2, linestyle="--", label="2x - 2y = 14")
    infinite_ax.text(-3.7, 5.8, "coincidentes", color=USS_BLUE, fontweight="bold")
    infinite_ax.legend(fontsize=8, loc="lower right", frameon=True, facecolor=WHITE, edgecolor=USS_GOLD)

    fig.suptitle(
        "Grossman, capitulo 1: clasificacion geometrica de un sistema 2 x 2",
        color=USS_BLUE,
        fontsize=15,
        fontweight="bold",
        y=1.02,
    )
    fig.text(
        0.5,
        0.01,
        "D != 0 -> una solucion | D = 0 -> ninguna o infinitas",
        ha="center",
        color=USS_BLUE,
        fontsize=10,
    )
    fig.tight_layout(rect=(0, 0.04, 1, 0.95))

    output = Path(__file__).with_name("grossman_capitulo_1_figura.png")
    fig.savefig(output, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print(output)


if __name__ == "__main__":
    main()
