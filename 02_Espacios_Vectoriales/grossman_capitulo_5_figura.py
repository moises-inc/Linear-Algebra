"""Generate the USS visual resource for Grossman chapter 5."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


USSBlue = "#00205B"
USSGold = "#D4AF37"
OUTPUT = Path(__file__).resolve().parent / "grossman_capitulo_5_espacios_vectoriales.png"


def draw_vector(ax, vector, color, label, width=0.012):
    """Draw a vector from the origin with a consistent visual style."""
    ax.quiver(
        0,
        0,
        vector[0],
        vector[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color=color,
        width=width,
        headwidth=5,
        headlength=7,
    )
    ax.text(vector[0] * 1.04, vector[1] * 1.04, label, color=color, fontsize=12)


def main():
    basis = np.array([[2.0, 1.0], [1.0, 3.0]])
    coordinates = np.array([1.5, -0.5])
    target = basis @ coordinates

    fig, axes = plt.subplots(1, 2, figsize=(11, 5), facecolor="white")
    fig.suptitle(
        "Capitulo 5 | Bases, coordenadas y combinaciones lineales",
        color=USSBlue,
        fontsize=15,
        fontweight="bold",
    )

    ax = axes[0]
    draw_vector(ax, basis[:, 0], USSBlue, r"$v_1$")
    draw_vector(ax, basis[:, 1], USSGold, r"$v_2$")
    draw_vector(ax, target, "#333333", r"$x=1.5v_1-0.5v_2$", width=0.009)
    ax.axhline(0, color="#BBBBBB", linewidth=0.8)
    ax.axvline(0, color="#BBBBBB", linewidth=0.8)
    ax.set_xlim(-2.5, 4.5)
    ax.set_ylim(-2.5, 4.5)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Una base ordenada determina coordenadas", color=USSBlue)
    ax.set_xlabel("componente 1")
    ax.set_ylabel("componente 2")
    ax.grid(alpha=0.25)

    ax = axes[1]
    categories = ["Genera", "LI", "Base", "Rango"]
    values = [1.0, 1.0, 1.0, 2.0]
    colors = [USSGold, USSBlue, USSGold, USSBlue]
    bars = ax.bar(categories, values, color=colors, width=0.62)
    ax.set_ylim(0, 2.5)
    ax.set_ylabel("indicador conceptual")
    ax.set_title("Puente entre estructura y calculo", color=USSBlue)
    ax.grid(axis="y", alpha=0.25)
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.06,
            str(value).rstrip(".0"),
            ha="center",
            color=USSBlue,
            fontweight="bold",
        )

    fig.text(
        0.5,
        0.01,
        "USSBlue #00205B | USSGold #D4AF37",
        ha="center",
        color=USSBlue,
        fontsize=9,
    )
    fig.tight_layout(rect=(0, 0.04, 1, 0.92))
    fig.savefig(OUTPUT, dpi=180, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    print(f"PNG generado: {OUTPUT}")


if __name__ == "__main__":
    main()
