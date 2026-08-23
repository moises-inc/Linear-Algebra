#!/usr/bin/env python3
"""
generar_figuras_taller1.py
Genera 3 figuras didácticas de apoyo para la Resolución del Taller 1 de Álgebra
Lineal (USS), con paleta institucional USS (USSBlue #00205B, USSGold #D4AF37)
sobre fondo oscuro pulcro.

Figura 1: Producto de matrices A_{3x3}·B_{3x3} (emparejamiento Fila x Columna).
Figura 2: Regla de Sarrus y desarrollo por cofactores para 3x3.
Figura 3: Raíces del polinomio característico det(A - λI) = 0 (ej. 2.6).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, FancyBboxPatch
from matplotlib.patheffects import withStroke

USS_BLUE = "#00205B"
USS_GOLD = "#D4AF37"
BG = "#101318"
PANEL = "#1B212C"
GRID_LINE = "#2E3A4C"
TEXT_MAIN = "#EDF1F7"
TEXT_SOFT = "#A9B4C4"
GOLD_SOFT = "#E5C86B"

plt.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
    "text.color": TEXT_MAIN,
    "axes.edgecolor": GRID_LINE,
    "axes.labelcolor": TEXT_MAIN,
    "xtick.color": TEXT_SOFT,
    "ytick.color": TEXT_SOFT,
})

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)


def cell_text(ax, x, y, s, size=16, color=TEXT_MAIN, weight="bold", box=True, bg="#0E1218"):
    kw = dict(ha="center", va="center", fontsize=size, color=color, fontweight=weight,
              zorder=5)
    if box:
        kw["bbox"] = dict(boxstyle="round,pad=0.28", fc=bg, ec="none")
    ax.text(x, y, s, **kw)


def draw_matrix(ax, x0, y0, M, cell=0.62, hl_rows=(), hl_cols=(),
                hl_color=USS_GOLD, val_color=None, size=15, title=None):
    n, m = M.shape
    for i in range(n):
        for j in range(m):
            cx, cy = x0 + j * cell, y0 - i * cell
            hl = (i in hl_rows) or (j in hl_cols)
            fc = hl_color if hl else "#141A23"
            ec = hl_color if hl else GRID_LINE
            lw = 2.2 if hl else 1.0
            ax.add_patch(Rectangle((cx - cell / 2, cy - cell / 2), cell, cell,
                                   fc=fc, ec=ec, lw=lw, zorder=2,
                                   alpha=0.95 if hl else 1.0))
            v = M[i, j]
            txt = f"{v:.0f}" if float(v).is_integer() else f"{v:.2f}"
            cell_text(ax, cx, cy, txt, size=size,
                      color=val_color if val_color else (TEXT_MAIN if not hl else BG),
                      weight="bold")
    if title:
        ax.text(x0, y0 + cell * 0.55, title, ha="center", va="bottom",
                fontsize=15, color=GOLD_SOFT, fontweight="bold")


def arrow_curve(ax, x1, y1, x2, y2, color, lw=2.6, rad=0.22, style="-|>", ls="-"):
    a = FancyArrowPatch((x1, y1), (x2, y2), connectionstyle=f"arc3,rad={rad}",
                        arrowstyle=style, mutation_scale=22, lw=lw,
                        color=color, ls=ls, zorder=4)
    ax.add_patch(a)


# ============================================================
# FIGURA 1 — Producto de matrices (ejercicio 1.2)
# ============================================================
A = np.array([[3, 1, 0], [4, 0, 2], [-1, 5, 1]])
B = np.array([[2, 4, -1], [3, 5, 2], [-2, 4, -1]])
C = A @ B

fig, ax = plt.subplots(figsize=(13.2, 7.4))
ax.set_xlim(-1.6, 13.6)
ax.set_ylim(-5.6, 2.6)
ax.axis("off")

ax.text(6.0, 2.35, "Producto de Matrices  $C = A \\cdot B$   (ejercicio 1.2)",
        ha="center", fontsize=20, color=USS_GOLD, fontweight="bold")

# matrices: A en x~0, B en x~5, C en x~10
draw_matrix(ax, 0.0, -1.2, A, hl_rows=(0,), title="$A\\;(3\\times 3)$")
ax.text(0.0, 2.0, "fila 1 de $A$", ha="center", fontsize=13, color=USS_GOLD)
ax.text(0.0, 1.45, "$\\left[3\\;\\;1\\;\\;0\\right]$", ha="center", fontsize=13,
        color=USS_GOLD)

draw_matrix(ax, 5.2, -1.2, B, hl_cols=(1,), title="$B\\;(3\\times 3)$")
ax.text(5.2, 2.0, "columna 2 de $B$", ha="center", fontsize=13, color=USS_GOLD)
ax.text(5.2, 1.45, "$\\left[4\\;\\;5\\;\\;4\\right]^{T}$", ha="center", fontsize=13,
        color=USS_GOLD)

draw_matrix(ax, 10.4, -1.2, C, hl_rows=(0,), hl_cols=(1,), title="$C = A\\cdot B$")

arrow_curve(ax, 0.55, -0.2, 10.4 + 0.62 - 0.3, -1.2 - 0.62 + 0.3, USS_GOLD, rad=-0.15)
arrow_curve(ax, 5.2 + 1 * 0.62 + 0.4, -1.2 - 0.1, 10.4 + 1 * 0.62 + 0.4, -1.2 - 0.62 + 0.3,
            GOLD_SOFT, rad=0.1)

box = FancyBboxPatch((7.8, -5.35), 4.7, 1.7, boxstyle="round,pad=0.15",
                     fc=PANEL, ec=USS_GOLD, lw=1.4, zorder=3)
ax.add_patch(box)
ax.text(10.15, -4.5, "$(AB)_{12} = 3\\cdot4 + 1\\cdot5 + 0\\cdot4$",
        ha="center", fontsize=15, color=TEXT_MAIN)
ax.text(10.15, -5.15, "$= 12 + 5 + 0 = 17$", ha="center", fontsize=17,
        color=USS_GOLD, fontweight="bold")

ax.text(-1.35, -0.35, "fila $i$", rotation=90, fontsize=13, color=TEXT_SOFT, va="center")
ax.text(6.0, -3.55, "columna $j$", fontsize=13, color=TEXT_SOFT, ha="center")

fig.suptitle("", fontsize=1)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "Figura1_producto_matrices.png"), dpi=200)
plt.close(fig)
print("Figura 1 OK")

# ============================================================
# FIGURA 2 — Sarrus y cofactores (B3 del ejercicio 2.2)
# ============================================================
B3 = np.array([[1, -2, 5], [-1, 4, -2], [4, -1, 2]])
detB3 = int(round(np.linalg.det(B3)))

fig, ax = plt.subplots(figsize=(13.6, 6.6))
ax.set_xlim(-1.2, 13.8)
ax.set_ylim(-5.4, 2.6)
ax.axis("off")

ax.text(6.3, 2.3, "Determinante $3\\times 3$: Regla de Sarrus y cofactores",
        ha="center", fontsize=19, color=USS_GOLD, fontweight="bold")
ax.text(6.3, 1.75, "Matriz del ejercicio 2.2  $B_3$  (con $\\det B_3 = -57$)",
        ha="center", fontsize=13, color=TEXT_SOFT)

# ---- panel Sarrus ----
draw_matrix(ax, 0.5, -1.2, B3, size=16)

# diagonales descendentes (productos +)
diag_down = [((0, 0), (1, 1), (2, 2)), ((0, 1), (1, 2)), ((1, 0), (2, 1))]
diag_up = [((0, 2), (1, 1), (2, 0)), ((0, 1), (1, 0)), ((1, 2), (2, 1))]

for (i1, j1), (i2, j2), (i3, j3) in [diag_down[0]]:
    x0, y0 = 0.5 + j1 * 0.62, -1.2 - i1 * 0.62
    x1, y1 = 0.5 + j2 * 0.62, -1.2 - i2 * 0.62
    x2, y2 = 0.5 + j3 * 0.62, -1.2 - i3 * 0.62
    arrow_curve(ax, x0, y0, x1, y1, USS_GOLD, rad=-0.08, lw=2.0)
    arrow_curve(ax, x1, y1, x2, y2, USS_GOLD, rad=-0.08, lw=2.0)

for (i1, j1), (i2, j2), (i3, j3) in [diag_up[0]]:
    x0, y0 = 0.5 + j1 * 0.62, -1.2 - i1 * 0.62
    x1, y1 = 0.5 + j2 * 0.62, -1.2 - i2 * 0.62
    x2, y2 = 0.5 + j3 * 0.62, -1.2 - i3 * 0.62
    arrow_curve(ax, x0, y0, x1, y1, "#5B8DB8", rad=0.08, lw=2.0)
    arrow_curve(ax, x1, y1, x2, y2, "#5B8DB8", rad=0.08, lw=2.0)

ax.text(0.5, -3.9, "$\\det = (1\\cdot4\\cdot2) + (-2\\cdot(-2)\\cdot4) + (5\\cdot(-1)\\cdot(-1))$",
        ha="center", fontsize=12.5, color=TEXT_MAIN)
ax.text(0.5, -4.45, "$-\\,(5\\cdot4\\cdot4) - (1\\cdot(-2)\\cdot(-1)) - (-2\\cdot(-1)\\cdot2)$",
        ha="center", fontsize=12.5, color=TEXT_MAIN)
ax.text(0.5, -5.0, "$= 8 + 16 + 5 - 80 - 2 - 4 = -57$", ha="center", fontsize=15,
        color=USS_GOLD, fontweight="bold")
ax.text(0.5, 0.35, "Regla de Sarrus", ha="center", fontsize=14, color=GOLD_SOFT,
        fontweight="bold")

# ---- panel cofactores ----
xc = 7.2
ax.text(xc, 0.35, "Desarrollo por cofactores (1ª fila)", ha="center", fontsize=14,
        color=GOLD_SOFT, fontweight="bold")
ax.text(xc, -0.05, "$\\det = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}$",
        ha="center", fontsize=14.5, color=TEXT_MAIN)
ax.text(xc, -0.62, "$C_{ij} = (-1)^{i+j}\\,M_{ij}$", ha="center", fontsize=14.5,
        color=TEXT_MAIN)

# matriz de signos
sgn = np.array([["+", "-", "+"], ["-", "+", "-"], ["+", "-", "+"]])
for i in range(3):
    for j in range(3):
        cx = xc - 1.2 + j * 0.62
        cy = -1.7 - i * 0.62
        ax.add_patch(Rectangle((cx - 0.31, cy - 0.31), 0.62, 0.62, fc="#141A23",
                               ec=GRID_LINE, lw=1.0, zorder=2))
        cell_text(ax, cx, cy, sgn[i, j], size=16, color=USS_GOLD)

ax.text(xc + 1.4, -1.7, "Matriz de\nsignos $(-1)^{i+j}$", fontsize=11.5,
        color=TEXT_SOFT, ha="left", va="center")

# menores/cofactores numéricos
ax.text(xc, -3.9, "$M_{11}\\;=\\;4\\cdot2 - (-2)\\cdot(-1) = 8 - 2 = 6$",
        ha="center", fontsize=13, color=TEXT_MAIN)
ax.text(xc, -4.45, "$M_{12}\\;=\\;(-2)\\cdot2 - (-2)\\cdot4 = -2 + 8 = 6$",
        ha="center", fontsize=13, color=TEXT_MAIN)
ax.text(xc, -5.0, "$M_{13}\\;=\\; (-1)\\cdot(-1) - 4\\cdot4 = 1 - 16 = -15$",
        ha="center", fontsize=13, color=TEXT_MAIN)

box = FancyBboxPatch((xc - 2.4, -5.75), 5.4, 0.75, boxstyle="round,pad=0.12",
                     fc=PANEL, ec=USS_GOLD, lw=1.3, zorder=3)
ax.add_patch(box)
ax.text(xc, -5.37, "$\\det = 1\\cdot6 - (-2)\\cdot6 + 5\\cdot(-15) = -57$",
        ha="center", fontsize=14.5, color=USS_GOLD, fontweight="bold")

fig.tight_layout()
fig.savefig(os.path.join(OUT, "Figura2_sarrus_cofactores.png"), dpi=200)
plt.close(fig)
print("Figura 2 OK")

# ============================================================
# FIGURA 3 — Polinomio característico (ejercicio 2.6)
# ============================================================
lam_vals = np.linspace(-2.6, 2.6, 800)
p = -(lam_vals - 1) * (lam_vals ** 2 + 1)

fig = plt.figure(figsize=(12.6, 6.4))
gs = fig.add_gridspec(1, 2, width_ratios=[1.55, 1.0], wspace=0.28)
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

# --- panel izquierdo: curva real ---
ax1.plot(lam_vals, p, color=USS_GOLD, lw=2.8, label=r"$p(\lambda)=\det(A-\lambda I)$")
ax1.axhline(0, color=TEXT_SOFT, lw=1.1, ls="--")
ax1.axvline(1, color="#5B8DB8", lw=1.2, ls=":")
ax1.plot([1], [0], "o", ms=11, mfc=USS_GOLD, mec=BG, mew=2, zorder=6)
ax1.annotate(r"raíz real $\lambda = 1$", xy=(1, 0), xytext=(1.35, -4.2),
             fontsize=13.5, color=USS_GOLD, fontweight="bold",
             arrowprops=dict(arrowstyle="->", color=USS_GOLD, lw=1.6))
ax1.set_xlabel(r"$\lambda$", fontsize=15)
ax1.set_ylabel(r"$p(\lambda)=\det(A-\lambda I)$", fontsize=13.5)
ax1.set_title(r"$A = [0,1,2;\; -1,0,1;\; 0,0,1]$   "
              r"$\Rightarrow$   $p(\lambda)=-( \lambda-1)(\lambda^2+1)$",
              fontsize=13.5, color=TEXT_MAIN)
ax1.grid(True, color=GRID_LINE, lw=0.6, alpha=0.7)
ax1.legend(loc="upper right", fontsize=11.5, framealpha=0.35)

# --- panel derecho: plano complejo ---
ax2.axhline(0, color=TEXT_SOFT, lw=1.0)
ax2.axvline(0, color=TEXT_SOFT, lw=1.0)
ax2.add_patch(plt.Circle((0, 0), 1, fc="none", ec=GRID_LINE, lw=1.0, ls=":"))
for pt, lbl in [((1, 0), r"$\lambda_1 = 1$"), ((0, 1), r"$\lambda_2 = i$"),
                ((0, -1), r"$\lambda_3 = -i$")]:
    ax2.plot([pt[0]], [pt[1]], "o", ms=10, mfc="#5B8DB8", mec=USS_GOLD, mew=2,
             zorder=6)
    ax2.annotate(lbl, xy=pt, xytext=(pt[0] + 0.18 * (1 if pt[0] >= 0 else -1.6),
                                     pt[1] + 0.16 * (1 if pt[1] >= 0 else -1.2)),
                 fontsize=12.5, color=TEXT_MAIN)
ax2.set_xlim(-1.9, 1.9)
ax2.set_ylim(-1.7, 1.7)
ax2.set_aspect("equal")
ax2.set_xlabel(r"$\mathrm{Re}(\lambda)$", fontsize=14)
ax2.set_ylabel(r"$\mathrm{Im}(\lambda)$", fontsize=14)
ax2.set_title("Raíces en el plano complejo", fontsize=13.5, color=TEXT_MAIN)
ax2.grid(True, color=GRID_LINE, lw=0.6, alpha=0.7)

fig.suptitle(r"$p(\lambda)=\det(A-\lambda I)=0$  (ejercicio 2.6):  $\lambda \in \{1,\, i,\, -i\}$",
             fontsize=17, color=USS_GOLD, fontweight="bold", y=0.97)

fig.tight_layout(rect=[0, 0, 1, 0.94])
fig.savefig(os.path.join(OUT, "Figura3_valores_propios.png"), dpi=200)
plt.close(fig)
print("Figura 3 OK")
print("\nFiguras guardadas en:", os.path.abspath(OUT))
