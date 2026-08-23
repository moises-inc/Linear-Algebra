import os
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
fig.patch.set_facecolor('white')

USSBlue = '#00205B'
USSGold = '#D4AF37'
Teal = '#008080'

# Vector v1 and v2
v1 = np.array([3.0, 0.0])
v2 = np.array([2.0, 2.5])

# Gram-Schmidt: e1 = v1 / ||v1||
e1 = v1 / np.linalg.norm(v1)

# Projection of v2 onto e1: proj = <v2, e1> e1
proj = np.dot(v2, e1) * e1

# Orthogonal component: u2 = v2 - proj
u2 = v2 - proj
e2 = u2 / np.linalg.norm(u2)

ax.annotate('', xy=v1, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='gray', lw=2))
ax.text(v1[0], v1[1]-0.3, r'$v_1$', fontsize=11, color='gray')

ax.annotate('', xy=v2, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=USSBlue, lw=2.5))
ax.text(v2[0]+0.1, v2[1], r'$v_2$', fontsize=11, color=USSBlue, fontweight='bold')

# Orthonormal basis e1, e2
ax.annotate('', xy=e1, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=USSGold, lw=3))
ax.text(e1[0], e1[1]+0.2, r'$e_1$', fontsize=12, color=USSGold, fontweight='bold')

ax.annotate('', xy=e2, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=Teal, lw=3))
ax.text(e2[0]-0.4, e2[1], r'$e_2 \perp e_1$', fontsize=12, color=Teal, fontweight='bold')

# Projection line
ax.plot([v2[0], proj[0]], [v2[1], proj[1]], 'k--', lw=1.5, alpha=0.7)

ax.axhline(0, color='gray', linestyle=':', alpha=0.6)
ax.axvline(0, color='gray', linestyle=':', alpha=0.6)
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 3.5)
ax.set_title(r'Gram-Schmidt Orthonormalization Procedure ($e_1 \perp e_2, \|e_1\|=\|e_2\|=1$)', fontsize=13, pad=12, fontweight='bold', color=USSBlue)
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'axler_chapter_6_figura.png'))
print("Figura Axler Cap 6 generada con éxito.")
