import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
fig.patch.set_facecolor('white')

USSBlue = '#00205B'
USSGold = '#D4AF37'

# Polynomial p(x) = (x - 1)(x + 2)(x - 3) = x^3 - 2x^2 - 5x + 6
x = np.linspace(-3, 4, 200)
y = x**3 - 2*x**2 - 5*x + 6

ax.plot(x, y, color=USSBlue, lw=2.5, label=r'$p(x) = (x - 1)(x + 2)(x - 3)$')
ax.axhline(0, color='gray', linestyle=':', alpha=0.7)
ax.axvline(0, color='gray', linestyle=':', alpha=0.7)

# Mark zeros
roots = [-2, 1, 3]
ax.scatter(roots, [0, 0, 0], color=USSGold, s=80, zorder=5, label='Zeros of $p(x)$')
for r in roots:
    ax.text(r, 1.5, f'x = {r}', fontsize=10, fontweight='bold', color=USSBlue, ha='center')

ax.set_xlim(-3.5, 4.5)
ax.set_ylim(-15, 15)
ax.set_title(r'Fundamental Theorem of Algebra: Factorization of Polynomials over $\mathbb{R}$', fontsize=12, fontweight='bold', color=USSBlue)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('/mnt/9b846436-0407-4e80-b8af-5417ffbdee8e/ObsidianVault/20_University/USS/Ramos_Actuales/Algebra_Lineal/Apuntes/Libro_Axler/Recursos/axler_chapter_4_figura.png')
print("Figura Axler Cap 4 generada con éxito.")
