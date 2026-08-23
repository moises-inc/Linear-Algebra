import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

USSBlue = '#00205B'
USSGold = '#D4AF37'

ax.text(0.5, 0.85, r'Trace and Determinant of an Operator $T \in \mathcal{L}(V)$', fontsize=14, fontweight='bold', color=USSBlue, ha='center')

tr_formula = r"$\operatorname{tr}(T) = \sum_{j=1}^m \lambda_j d_j = \sum_{i=1}^n A_{ii}$"
ax.text(0.5, 0.60, tr_formula, fontsize=13, ha='center', color=USSBlue)

det_formula = r"$\det(T) = \prod_{j=1}^m \lambda_j^{d_j} = \det(\mathcal{M}(T))$"
ax.text(0.5, 0.35, det_formula, fontsize=13, ha='center', color=USSGold, fontweight='bold')

desc = r"Basis Invariance: $\operatorname{tr}(P^{-1} A P) = \operatorname{tr}(A)$ and $\det(P^{-1} A P) = \det(A)$"
ax.text(0.5, 0.15, desc, fontsize=11, ha='center', color=USSBlue)

ax.axis('off')
plt.tight_layout()
plt.savefig('/mnt/9b846436-0407-4e80-b8af-5417ffbdee8e/ObsidianVault/20_University/USS/Ramos_Actuales/Algebra_Lineal/Apuntes/Libro_Axler/Recursos/axler_chapter_10_figura.png')
print("Figura Axler Cap 10 generada con éxito.")
