import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), dpi=300)
fig.patch.set_facecolor('white')

USSBlue = '#00205B'
USSGold = '#D4AF37'
Teal = '#008080'

# Left Plot: Domain V (R^3 represented in 2D with Null Space)
ax1.set_facecolor('white')
x = np.linspace(-3, 3, 100)
ax1.plot(x, 0.8*x, color=USSGold, lw=3, label=r'Null Space $\operatorname{null}(T)$')
ax1.scatter([0], [0], color='black', zorder=5)
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)
ax1.set_title(r'Domain $V$ ($\dim V = \dim \operatorname{null}(T) + \dim \operatorname{range}(T)$)', fontsize=11, fontweight='bold', color=USSBlue)
ax1.grid(True, linestyle='--', alpha=0.3)
ax1.legend()

# Right Plot: Target W (R^2 with Range T)
ax2.set_facecolor('white')
ax2.plot(x, -0.4*x, color=Teal, lw=3, label=r'Range $\operatorname{range}(T)$')
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)
ax2.set_title(r'Target $W$ (Range of $T$)', fontsize=11, fontweight='bold', color=USSBlue)
ax2.grid(True, linestyle='--', alpha=0.3)
ax2.legend()

plt.suptitle(r'Fundamental Theorem of Linear Maps: $\dim V = \dim \operatorname{null}(T) + \dim \operatorname{range}(T)$', fontsize=13, fontweight='bold', color=USSBlue)
plt.tight_layout()
plt.savefig('/mnt/9b846436-0407-4e80-b8af-5417ffbdee8e/ObsidianVault/20_University/USS/Ramos_Actuales/Algebra_Lineal/Apuntes/Libro_Axler/Recursos/axler_chapter_3_figura.png')
print("Figura Axler Cap 3 generada con éxito.")
