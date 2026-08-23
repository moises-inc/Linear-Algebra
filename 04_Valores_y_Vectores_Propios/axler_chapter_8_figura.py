import os
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

USSBlue = '#00205B'
USSGold = '#D4AF37'

# Draw Jordan Block J_k(lambda)
ax.text(0.5, 0.85, r'Jordan Canonical Form & Nilpotent Decomposition', fontsize=14, fontweight='bold', color=USSBlue, ha='center')

jordan_mat = r"$\mathbf{J} = \mathbf{diag}(J_{k_1}(\lambda_1), J_{k_2}(\lambda_2), \dots, J_{k_m}(\lambda_m))$"
ax.text(0.5, 0.65, jordan_mat, fontsize=13, ha='center', color=USSBlue)

block_mat = r"$J_k(\lambda) = \lambda I_k + N_k, \quad \text{where } N_k^k = \mathbf{0}$"
ax.text(0.5, 0.45, block_mat, fontsize=13, ha='center', color=USSGold, fontweight='bold')

desc = r"Every operator $T \in \mathcal{L}(V)$ on a complex vector space $V$" + "\n" + r"decomposes as $T = S + N$ ($S$ diagonalizable, $N$ nilpotent, $SN = NS$)"
ax.text(0.5, 0.25, desc, fontsize=11, ha='center', color=USSBlue)

ax.axhline(0.1, color='gray', linestyle='--', alpha=0.3)
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'axler_chapter_8_figura.png'))
print("Figura Axler Cap 8 generada con éxito.")
