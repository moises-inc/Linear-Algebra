import os
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
fig.patch.set_facecolor('white')

USSBlue = '#00205B'
USSGold = '#D4AF37'
Teal = '#008080'

# Matrix A with eigenvector v1=(2,1) lambda1=2 and v2=(-1,1) lambda2=-0.5
A = np.array([[1.5, 1.0], [0.5, 1.0]])

# Eigenvector v1
v1 = np.array([2.0, 1.0])
Av1 = A @ v1 # = (4, 2) = 2*v1

# Arbitrary vector u
u = np.array([1.0, 2.0])
Au = A @ u # = (3.5, 2.5) - changes direction

ax.annotate('', xy=v1, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=USSBlue, lw=2.5))
ax.text(v1[0]+0.1, v1[1]-0.2, r'$v_1$', fontsize=12, color=USSBlue, fontweight='bold')

ax.annotate('', xy=Av1, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=USSGold, lw=2.5, ls='--'))
ax.text(Av1[0]+0.1, Av1[1], r'$T(v_1) = 2 v_1$ (Eigenvector)', fontsize=12, color=USSGold, fontweight='bold')

ax.annotate('', xy=u, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='gray', lw=2))
ax.text(u[0]-0.5, u[1]+0.2, r'$u$', fontsize=11, color='gray')

ax.annotate('', xy=Au, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=Teal, lw=2))
ax.text(Au[0]+0.1, Au[1], r'$T(u)$ (Rotated)', fontsize=11, color=Teal)

ax.axhline(0, color='gray', linestyle=':', alpha=0.6)
ax.axvline(0, color='gray', linestyle=':', alpha=0.6)
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4.5)
ax.set_title(r'Eigenvector $T(v) = \lambda v$: Direction Preserved', fontsize=13, pad=12, fontweight='bold', color=USSBlue)
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'axler_chapter_5_figura.png'))
print("Figura Axler Cap 5 generada con éxito.")
