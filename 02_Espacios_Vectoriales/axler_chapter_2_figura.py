import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

USSBlue = '#00205B'
USSGold = '#D4AF37'
Teal = '#008080'

# Plot basis vectors for R^2
v1 = np.array([2.0, 0.5])
v2 = np.array([0.8, 2.2])

ax.annotate('', xy=v1, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=USSBlue, lw=3))
ax.text(v1[0]+0.1, v1[1]-0.2, r'$v_1 = (2, 0.5)$', fontsize=12, color=USSBlue, fontweight='bold')

ax.annotate('', xy=v2, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=USSGold, lw=3))
ax.text(v2[0]-1.1, v2[1]+0.1, r'$v_2 = (0.8, 2.2)$', fontsize=12, color=USSGold, fontweight='bold')

# Target vector w = 1.5*v1 + 1.2*v2
w = 1.5 * v1 + 1.2 * v2
ax.annotate('', xy=w, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=Teal, lw=3))
ax.text(w[0]+0.1, w[1], r'$w = 1.5 v_1 + 1.2 v_2$', fontsize=12, color=Teal, fontweight='bold')

# Grid span lines
c1_v1 = 1.5 * v1
c2_v2 = 1.2 * v2
ax.plot([c1_v1[0], w[0]], [c1_v1[1], w[1]], 'k--', alpha=0.6)
ax.plot([c2_v2[0], w[0]], [c2_v2[1], w[1]], 'k--', alpha=0.6)

ax.axhline(0, color='gray', linestyle=':', alpha=0.6)
ax.axvline(0, color='gray', linestyle=':', alpha=0.6)
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4.5)
ax.set_title(r'Basis $(v_1, v_2)$ Spanning $\mathbb{R}^2$ ($\dim \mathbb{R}^2 = 2$)', fontsize=14, pad=12, fontweight='bold', color=USSBlue)
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('/mnt/9b846436-0407-4e80-b8af-5417ffbdee8e/ObsidianVault/20_University/USS/Ramos_Actuales/Algebra_Lineal/Apuntes/Libro_Axler/Recursos/axler_chapter_2_figura.png')
print("Figura Axler Cap 2 generada con éxito.")
