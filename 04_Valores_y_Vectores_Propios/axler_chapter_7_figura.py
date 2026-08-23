import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), dpi=300)
fig.patch.set_facecolor('white')

USSBlue = '#00205B'
USSGold = '#D4AF37'
Teal = '#008080'

# Left: Unit circle in domain V
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

ax1.set_facecolor('white')
ax1.plot(x, y, color=USSBlue, lw=2, label=r'Unit Circle $\|v\|=1$')
ax1.annotate('', xy=(1, 0), xytext=(0,0), arrowprops=dict(arrowstyle='->', color=USSGold, lw=2.5))
ax1.text(1.1, 0.1, r'$v_1$', fontsize=11, color=USSGold, fontweight='bold')
ax1.annotate('', xy=(0, 1), xytext=(0,0), arrowprops=dict(arrowstyle='->', color=Teal, lw=2.5))
ax1.text(0.1, 1.1, r'$v_2$', fontsize=11, color=Teal, fontweight='bold')
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.set_title(r'Domain $V$ (Orthonormal Basis $v_1, v_2$)', fontsize=11, fontweight='bold', color=USSBlue)
ax1.grid(True, linestyle='--', alpha=0.3)
ax1.legend()

# Right: Ellipse in target W under T (SVD)
A = np.array([[2.5, 0.5], [0.0, 1.2]])
u_vec = np.vstack([x, y])
t_vec = A @ u_vec

ax2.set_facecolor('white')
ax2.plot(t_vec[0], t_vec[1], color=USSBlue, lw=2, label=r'Ellipse $T(\text{Unit Circle})$')
# Singular values sigma1, sigma2
sigma1_vec = A @ np.array([1, 0])
sigma2_vec = A @ np.array([0, 1])

ax2.annotate('', xy=sigma1_vec, xytext=(0,0), arrowprops=dict(arrowstyle='->', color=USSGold, lw=2.5))
ax2.text(sigma1_vec[0]+0.1, sigma1_vec[1], r'$\sigma_1 u_1$', fontsize=11, color=USSGold, fontweight='bold')

ax2.annotate('', xy=sigma2_vec, xytext=(0,0), arrowprops=dict(arrowstyle='->', color=Teal, lw=2.5))
ax2.text(sigma2_vec[0]+0.1, sigma2_vec[1]+0.2, r'$\sigma_2 u_2$', fontsize=11, color=Teal, fontweight='bold')

ax2.set_xlim(-3.5, 3.5)
ax2.set_ylim(-2.5, 2.5)
ax2.set_title(r'Target $W$ (Singular Values $\sigma_1, \sigma_2$)', fontsize=11, fontweight='bold', color=USSBlue)
ax2.grid(True, linestyle='--', alpha=0.3)
ax2.legend()

plt.suptitle(r'Singular Value Decomposition (SVD): $T(v_j) = \sigma_j u_j$', fontsize=13, fontweight='bold', color=USSBlue)
plt.tight_layout()
plt.savefig('/mnt/9b846436-0407-4e80-b8af-5417ffbdee8e/ObsidianVault/20_University/USS/Ramos_Actuales/Algebra_Lineal/Apuntes/Libro_Axler/Recursos/axler_chapter_7_figura.png')
print("Figura Axler Cap 7 generada con éxito.")
