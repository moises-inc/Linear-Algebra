"""Generate the USS visual resource for Grossman chapter 6."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


USS_BLUE = "#00205B"
USS_GOLD = "#D4AF37"
INK = "#1B2430"
GRID = "#D9DEE8"
OUTPUT = Path(__file__).with_name("grossman_capitulo_6_figura.png")


def draw_arrow(ax, vector, color, label, linestyle="-", linewidth=2.6):
    """Draw an arrow from the origin and place a label near its endpoint."""
    ax.annotate(
        "",
        xy=vector,
        xytext=(0, 0),
        arrowprops={
            "arrowstyle": "-|>",
            "color": color,
            "linewidth": linewidth,
            "linestyle": linestyle,
            "shrinkA": 0,
            "shrinkB": 0,
        },
    )
    ax.text(
        vector[0] * 1.04,
        vector[1] * 1.04,
        label,
        color=color,
        fontsize=11,
        fontweight="bold",
    )


def style_axis(ax, title):
    """Apply the common clean USS styling."""
    ax.set_title(title, color=USS_BLUE, fontweight="bold")
    ax.axhline(0, color=INK, linewidth=0.8)
    ax.axvline(0, color=INK, linewidth=0.8)
    ax.grid(True, color=GRID, linewidth=0.7, alpha=0.85)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x")
    ax.set_ylabel("y")


def projection_panel(ax):
    """Illustrate v = projection + orthogonal residual."""
    u = np.array([1.0, 0.5])
    u /= np.linalg.norm(u)
    vector = np.array([3.0, 2.0])
    projection = np.dot(vector, u) * u
    residual = vector - projection

    parameter = np.linspace(-1.0, 4.0, 100)
    ax.plot(
        parameter * u[0],
        parameter * u[1],
        color=USS_BLUE,
        linewidth=2.2,
        label="H = span{u}",
    )
    ax.plot(
        [projection[0], vector[0]],
        [projection[1], vector[1]],
        color=USS_GOLD,
        linestyle="--",
        linewidth=2,
        label="residuo r",
    )
    draw_arrow(ax, projection, USS_BLUE, "h")
    draw_arrow(ax, vector, INK, "v")
    draw_arrow(ax, residual, USS_GOLD, "r", linestyle="--", linewidth=2.1)
    ax.scatter(*projection, color=USS_BLUE, zorder=4)
    ax.scatter(*vector, color=INK, zorder=4)
    ax.set_xlim(-0.7, 3.8)
    ax.set_ylim(-0.7, 2.8)
    ax.legend(loc="lower right", frameon=True)
    ax.text(0.08, 2.42, "v = h + r", color=USS_BLUE, fontsize=11)
    ax.text(0.08, 2.12, "r perpendicular to H", color=USS_GOLD, fontsize=10)


def least_squares_panel(ax):
    """Illustrate a least-squares line and the data residuals."""
    x = np.array([1.0, -2.0, 3.0, 4.0])
    y = np.array([4.0, 5.0, -1.0, 1.0])
    design = np.column_stack((np.ones_like(x), x))
    coefficients, _, _, _ = np.linalg.lstsq(design, y, rcond=None)
    intercept, slope = coefficients
    grid_x = np.linspace(-2.5, 4.5, 200)
    fitted = intercept + slope * grid_x
    predicted = intercept + slope * x

    ax.scatter(x, y, color=USS_BLUE, s=48, zorder=4, label="datos")
    ax.plot(
        grid_x,
        fitted,
        color=USS_GOLD,
        linewidth=2.5,
        label=r"$\hat{y}=\hat{b}+\hat{m}x$",
    )
    for x_i, y_i, y_hat in zip(x, y, predicted):
        ax.plot(
            [x_i, x_i],
            [y_i, y_hat],
            color=INK,
            linestyle=":",
            linewidth=1.4,
        )
    ax.axhline(0, color=INK, linewidth=0.8)
    ax.axvline(0, color=INK, linewidth=0.8)
    ax.grid(True, color=GRID, linewidth=0.7, alpha=0.85)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Minimos cuadrados: residual ortogonal", color=USS_BLUE, fontweight="bold")
    ax.legend(loc="lower left", frameon=True)
    ax.text(
        -2.35,
        5.75,
        rf"$\hat{{y}}={intercept:.2f}{slope:+.2f}x$",
        color=USS_BLUE,
        fontsize=11,
    )
    ax.set_xlim(-2.7, 4.7)
    ax.set_ylim(-2.3, 6.2)


def main():
    """Build and save the chapter 6 synthesis figure."""
    # The numerical checks mirror the two central identities in the note.
    direction = np.array([1.0, 0.5])
    direction /= np.linalg.norm(direction)
    vector = np.array([3.0, 2.0])
    projection = np.dot(vector, direction) * direction
    residual = vector - projection
    assert np.allclose(np.dot(residual, direction), 0.0)

    x = np.array([1.0, -2.0, 3.0, 4.0])
    y = np.array([4.0, 5.0, -1.0, 1.0])
    design = np.column_stack((np.ones_like(x), x))
    coefficients, _, _, _ = np.linalg.lstsq(design, y, rcond=None)
    assert np.allclose(coefficients, [25 / 7, -37 / 42])
    assert np.allclose(design.T @ (y - design @ coefficients), np.zeros(2))

    figure, axes = plt.subplots(1, 2, figsize=(12, 5.4), facecolor="white")
    figure.suptitle(
        "Capitulo 6 | Producto interno, proyeccion y minimos cuadrados",
        color=USS_BLUE,
        fontsize=15,
        fontweight="bold",
    )
    projection_panel(axes[0])
    least_squares_panel(axes[1])
    figure.text(
        0.5,
        0.012,
        "USSBlue #00205B | USSGold #D4AF37",
        ha="center",
        color=USS_BLUE,
        fontsize=9,
    )
    figure.tight_layout(rect=(0, 0.04, 1, 0.93))
    figure.savefig(OUTPUT, dpi=180, facecolor="white", bbox_inches="tight")
    plt.close(figure)
    print(f"PNG generado: {OUTPUT}")


if __name__ == "__main__":
    main()
