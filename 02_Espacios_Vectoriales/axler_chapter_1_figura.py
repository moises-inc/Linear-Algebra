import os
import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('default')
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Colors
USSBlue = '#00205B'
USSGold = '#D4AF37'
Teal = '#008080'

# Draw direct sum decomposition V = U1 (+) U2 in R^2
# Line U1 along y = 0.5x
x = np.linspace(-4, 4, 100)
y1 = 0.5 * x
ax.plot(x, y1, color=USSBlue, linewidth=2.5, label=r'Subspace $U_1 = \{(x, 0.5x) : x \in \mathbb{R}\}$')

# Line U2 along y = -1.5x
y2 = -1.5 * x
ax.plot(x, y2, color=USSGold, linewidth=2.5, label=r'Subspace $U_2 = \{(x, -1.5x) : x \in \mathbb{R}\}$')

# Point v = u1 + u2
u1 = np.array([3.0, 1.5])   # on U1
u2 = np.array([-0.5, 0.75])  # on U2
v = u1 + u2

# Vectors
ax.annotate('', xy=v, xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=Teal, lw=3))
ax.text(v[0]+0.2, v[1], r'$v = u_1 \oplus u_2$', fontsize=13, color=Teal, fontweight='bold')

ax.annotate('', xy=u1, xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=USSBlue, lw=2, ls='--'))
ax.text(u1[0]+0.1, u1[1]+0.2, r'$u_1 \in U_1$', fontsize=11, color=USSBlue)

ax.annotate('', xy=u2, xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color=USSGold, lw=2, ls='--'))
ax.text(u2[0]-1.2, u2[1]+0.2, r'$u_2 \in U_2$', fontsize=11, color=USSGold)

# Parallelogram dashed lines
ax.plot([u1[0], v[0]], [u1[1], v[1]], 'k--', alpha=0.5)
ax.plot([u2[0], v[0]], [u2[1], v[1]], 'k--', alpha=0.5)

# Axis & Grid
ax.axhline(0, color='gray', linestyle=':', alpha=0.6)
ax.axvline(0, color='gray', linestyle=':', alpha=0.6)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_title(r'Direct Sum Decomposition $V = U_1 \oplus U_2$ ($U_1 \cap U_2 = \{0\}$)', fontsize=14, pad=12, fontweight='bold', color=USSBlue)
ax.legend(loc='upper right', frameon=True)
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'axler_chapter_1_figura.png'))
print("Figura Axler Cap 1 generada con éxito.")
