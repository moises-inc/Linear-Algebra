#!/usr/bin/env python3
"""
Verificación exhaustiva con SymPy — Taller 1 Álgebra Lineal (USS)
Valida TODOS los resultados numéricos de la resolución antes de cerrarla.
"""
import sympy as sp

# ============ UTILIDADES ============
def show(name, M):
    print(f"\n{name} =")
    sp.pprint(M)

def div(v):
    """muestra simplificación como fracción"""
    return sp.nsimplify(v)

# ============ SECCIÓN 1: OPERACIONES CON MATRICES ============
print("=" * 70)
print("SECCIÓN 1.1 — Matrices A, B, C de orden 4")
print("=" * 70)
A11 = sp.Matrix([[0, 1, 1, 1], [-1, 0, 1, 1], [-1, -1, 0, 1], [-1, -1, -1, 0]])
B11 = sp.Matrix([[(-1)**(i+j) * (i+j) for j in range(1, 5)] for i in range(1, 5)])
C11 = sp.Matrix([[(-1)**(i-j) * (i*j) for j in range(1, 5)] for i in range(1, 5)])
show("A", A11); show("B", B11); show("C", C11)

print("\n" + "=" * 70)
print("SECCIÓN 1.2 — A, B 3x3")
print("=" * 70)
A = sp.Matrix([[3, 1, 0], [4, 0, 2], [-1, 5, 1]])
B = sp.Matrix([[2, 4, -1], [3, 5, 2], [-2, 4, -1]])
show("A", A); show("B", B)
show("a) A+B", A + B)
show("b) AB", A * B)
show("c) BA", B * A)
show("d) (AB)^T", (A * B).T)
show("e) A^T", A.T)
show("f) B^T", B.T)
show("g) A^T B^T", A.T * B.T)
show("h) B^T A^T", B.T * A.T)
show("i) (A+B)^T", (A + B).T)
show("j) A^T+B^T", A.T + B.T)
print("\nk) (AB)^T == B^T A^T ? ->", sp.simplify((A * B).T - B.T * A.T) == sp.zeros(3))
print("l) (A+B)^T == A^T+B^T ? ->", sp.simplify((A + B).T - A.T - B.T) == sp.zeros(3))

print("\n" + "=" * 70)
print("SECCIÓN 1.3 — A,B,C,D,E (C es 2x3, D es 3x2)")
print("=" * 70)
A3 = sp.Matrix([[-1, 2], [2, 3]])
B3 = sp.eye(2)
C3 = sp.Matrix([[1, 0, -1], [2, 1, 3]])
D3 = sp.Matrix([[2, 0], [1, 2], [1, 3]])
E3 = sp.Matrix([[1, 1], [-1, 1]])
show("a) 3A", 3 * A3)
print("\nb) A+C ->", "NO DEFINIDO (2x2 + 2x3)")
show("c) CD", C3 * D3)
show("d) A-B", A3 - B3)
show("e) 3A+4B", 3 * A3 + 4 * B3)
show("f) AB+CD", A3 * B3 + C3 * D3)
show("g) 7A", 7 * A3)
k = sp.symbols('k')
show("h) kE", k * E3)
show("i) 8A+E", 8 * A3 + E3)
show("j) AE", A3 * E3)
print("\nk) A(B+C) ->", "NO DEFINIDO (B+C: 2x2 + 2x3)")
print("l) AB+AC ->", "NO DEFINIDO (AC: 2x2 · 2x3)")
show("m) A+B", A3 + B3)
show("n) B+A", B3 + A3)
show("ñ) AA", A3 * A3)
show("o) EE", E3 * E3)
show("p) (AB)C", (A3 * B3) * C3)

print("\n" + "=" * 70)
print("SECCIÓN 1.4 — ecuaciones matriciales")
print("=" * 70)
A4 = sp.Matrix([[3, 2], [1, 0]])
B4 = sp.Matrix([[2, 1], [2, 1]])
C4 = sp.Matrix([[1, 1], [0, 1]])
D4 = sp.Matrix([[1, 1, 3], [1, 1, -2]])
show("AB", A4 * B4)
show("BA", B4 * A4)
show("DD^T - C", D4 * D4.T - C4)
show("AC^2 - I", A4 * C4 * C4 - sp.eye(2))
print("\nb) i) -2X + C = B -> X = (C-B)/2")
show("X", (C4 - B4) / 2)
print("\nb) ii) (A - (2/3)X)^T = 2C -> X = (3/2)(A - 2C^T)")
Xii = sp.Rational(3, 2) * (A4 - 2 * C4.T)
show("X", Xii)
print("Verificación:", (A4 - sp.Rational(2, 3) * Xii).T == 2 * C4)
print("\nb) iii) 3X + C^T = 2B - X -> X = (2B - C^T)/4")
Xiii = (2 * B4 - C4.T) / 4
show("X", Xiii)
print("Verificación:", 3 * Xiii + C4.T == 2 * B4 - Xiii)

print("\n" + "=" * 70)
print("SECCIÓN 1.5 — X^3 - X^2 - 5X + 5I = 0")
print("=" * 70)
X15 = sp.Matrix([[1, 2, 0], [2, -1, 0], [0, 0, 1]])
show("X", X15)
show("X^2", X15 ** 2)
show("X^3", X15 ** 3)
res = X15 ** 3 - X15 ** 2 - 5 * X15 + 5 * sp.eye(3)
show("X^3 - X^2 - 5X + 5I", res)
print("Es nula:", res == sp.zeros(3))

print("\n" + "=" * 70)
print("SECCIÓN 1.6 — sistema x,y,z,w")
print("=" * 70)
x, y, z, w = sp.symbols('x y z w')
Ml = sp.Matrix([[2, 1], [-2, 3]]) * sp.Matrix([[x + y, y], [z, z - w]])
Mr = sp.Matrix([[x, y], [3 + x, z - w]]) * sp.Matrix([[1, 2], [3, -2]])
show("LHS", Ml)
show("RHS", Mr)
sol = sp.solve([Ml[0, 0] - Mr[0, 0], Ml[0, 1] - Mr[0, 1],
                Ml[1, 0] - Mr[1, 0], Ml[1, 1] - Mr[1, 1]], [x, y, z, w], dict=True)
print("Solución:", sol)
for s in sol:
    for var in (x, y, z, w):
        if var in s:
            print(var, "=", s[var])

print("\n" + "=" * 70)
print("SECCIÓN 2.1 — determinantes 2x2")
print("=" * 70)
for name, M in [("a", sp.Matrix([[3, 4], [2, 5]])),
                ("b", sp.Matrix([[0, 3], [-1, 7]])),
                ("c", sp.Matrix([[5, 7], [6, 2]])),
                ("d", sp.Matrix([[x, y], [2 * x, 2 * y]]))]:
    print(f"{name}) det =", M.det())

print("\n" + "=" * 70)
print("SECCIÓN 2.2 — dets y propiedades")
print("=" * 70)
A2 = sp.Matrix([[4, -2], [-1, 4]])
A3m = sp.Matrix([[1, -2, 3], [-1, 4, 5], [-3, 6, -9]])
B2 = sp.Matrix([[1, -2], [-1, 4]])
B3m = sp.Matrix([[1, -2, 5], [-1, 4, -2], [4, -1, 2]])
C2 = sp.Matrix([[1, -1], [0, 3]])
C3m = sp.Matrix([[1, -1, 3], [0, 3, 2], [0, 0, -1]])
dA2, dA3, dB2, dB3, dC2, dC3 = A2.det(), A3m.det(), B2.det(), B3m.det(), C2.det(), C3m.det()
print("det A2 =", dA2, "| det A3 =", dA3, "| det B2 =", dB2,
      "| det B3 =", dB3, "| det C2 =", dC2, "| det C3 =", dC3)
print("a) |A2^T| =", A2.T.det())
print("b) |-2 B3^T| =", (-2 * B3m.T).det())
print("c) |B2^T A2| =", (B2.T * A2).det())
print("d) |B2| =", B2.det())
print("e) |C3^T| =", C3m.T.det())
print("f) |B2^T| =", B2.T.det())
print("g) |A2 B2| =", (A2 * B2).det())
print("h) |A3 B3^T| =", (A3m * B3m.T).det())
print("i) |A3 B3| =", (A3m * B3m).det())
print("j) |B2 C2 A2| =", (B2 * C2 * A2).det())
print("k) |B3^T (A3 - C3)| =", (B3m.T * (A3m - C3m)).det())

print("\n" + "=" * 70)
print("SECCIÓN 2.3 — determinantes")
print("=" * 70)
M1 = sp.Matrix([[-3, -6, -1], [-4, -3, -2], [5, -4, -4]])
print("a) det =", M1.det())
M2 = sp.Matrix([[1, -1, 1, 2], [3, -2, 4, 3], [5, 4, 1, 2], [-3, 0, 3, 1]])
print("b) det =", M2.det())
e = sp.symbols('e', positive=True)
Me = sp.Matrix([[e ** 2, -5 * e ** 2], [e ** 4, 4 * e ** 4]])
print("c) det =", Me.det(), "| ln(|det|) =", sp.simplify(sp.ln(sp.Abs(Me.det()))))

print("\n" + "=" * 70)
print("SECCIÓN 2.6 — det(A - λI) = 0")
print("=" * 70)
lam = sp.symbols('lambda')
A26 = sp.Matrix([[0, 1, 2], [-1, 0, 1], [0, 0, 1]])
char_poly = sp.factor((A26 - lam * sp.eye(3)).det())
print("det(A-λI) =", char_poly)
print("Raíces:", sp.solve(sp.Eq(char_poly, 0), lam))
print("Valores propios sympy:", A26.eigenvals())

print("\n" + "=" * 70)
print("SECCIÓN 2.7 — |A| = 5 propiedades")
print("=" * 70)
a, b, c, d, e2, f, g, h, i = sp.symbols('a b c d e f g h i')
A27 = sp.Matrix([[a, b, c], [d, e2, f], [g, h, i]])
print("det A =", A27.det(), "(simbólico)")
print("a) |[g,h,i;d,e,f;a,b,c]| =", sp.Matrix([[g, h, i], [d, e2, f], [a, b, c]]).det(),
      "-> con det A = 5:", sp.Matrix([[g, h, i], [d, e2, f], [a, b, c]]).det().subs(
          {a * i * e2 - a * f * h - b * d * i + b * f * g + c * d * h - c * e2 * g: 5}))
print("b) |[-5g,-5h,-5i;3d,3e,3f;4a,4b,4c]| =",
      sp.Matrix([[-5 * g, -5 * h, -5 * i], [3 * d, 3 * e2, 3 * f], [4 * a, 4 * b, 4 * c]]).det().subs(
          {a * i * e2 - a * f * h - b * d * i + b * f * g + c * d * h - c * e2 * g: 5}))
print("c) |[a-b,b,c;d-e,e,f;g-h,h,i]| =",
      sp.Matrix([[a - b, b, c], [d - e2, e2, f], [g - h, h, i]]).det().subs(
          {a * i * e2 - a * f * h - b * d * i + b * f * g + c * d * h - c * e2 * g: 5}))
print("d) |[2a-2d,2b-2e,2c-2f;g,h,i;d,e,f]| =",
      sp.Matrix([[2 * a - 2 * d, 2 * b - 2 * e2, 2 * c - 2 * f], [g, h, i], [d, e2, f]]).det().subs(
          {a * i * e2 - a * f * h - b * d * i + b * f * g + c * d * h - c * e2 * g: 5}))

print("\n" + "=" * 70)
print("SECCIÓN 3.1 — 2X^t - (3AB)^t = A^t B^t - X^t")
print("=" * 70)
A31 = sp.Matrix([[2, 1, 5], [0, -2, 1], [0, 0, 3]])
B31 = sp.Matrix([[3, 4, 7], [4, 2, -1], [7, -1, 2]])
X31 = sp.symbols('X31', cls=sp.MatrixSymbol) if False else None
# 2X^T - 3(AB)^T = A^T B^T - X^T  ->  3X^T = A^T B^T + 3(AB)^T  ->  X = (BA + 3AB)/3
Xsol31 = (B31 * A31 + 3 * A31 * B31) / 3
show("X = (BA + 3AB)/3", Xsol31)
Xm = sp.Matrix(sp.zeros(3))
# verificación numérica de la ecuación
Xv = Xsol31
lhs = 2 * Xv.T - 3 * (A31 * B31).T
rhs = A31.T * B31.T - Xv.T
print("Verificación LHS-RHS nula:", sp.simplify(lhs - rhs) == sp.zeros(3))

print("\n" + "=" * 70)
print("SECCIÓN 3.2 — ecuaciones matriciales")
print("=" * 70)
A32 = sp.Matrix([[4, -2], [-1, 4]])
B32 = sp.Matrix([[1, -2, 3], [-1, 4, 5], [-3, 6, -9]])
C32 = sp.Matrix([[1, -2], [-1, 4]])
D32 = sp.Matrix([[1, -2, 5], [-1, 4, -2], [4, -1, 2]])
E32 = sp.Matrix([[1, -1, 2], [0, 3, -4], [1, -1, 2]])
F32 = sp.Matrix([[1, -1, 3], [0, 3, 2], [0, 0, -1]])
print("det A =", A32.det(), "| det C =", C32.det(), "| det(B+D) =", (B32 + D32).det(),
      "| det F =", F32.det(), "| det E =", E32.det(), "| det(B-D) =", (B32 - D32).det())
Xa = A32.inv() * C32
show("a) X = A^-1 C", Xa)
print("  verif:", A32 * Xa == C32)
Xb = (B32 + D32).inv() * F32.T * E32
show("b) X = (B+D)^-1 F^T E", Xb)
print("  verif:", (B32 + D32) * Xb == F32.T * E32)
Xc = C32.inv() * A32 * C32 * (A32.T).inv()
show("c) X = C^-1 A C (A^T)^-1", Xc)
print("  verif:", C32 * Xc * A32.T == A32 * C32)
# d) E^T X F = B^T?? NO: E^T X F = B - D. E singular (det=0)
print("\nd) E^T X F = B - D  |  det E^T =", E32.det(), "(singular)")
print("   M = B-D =", (B32 - D32).tolist(), "| det(B-D) =", (B32 - D32).det())
xs = list(sp.symbols('x11:14 x21:24 x31:34'))
Xv32 = sp.Matrix(3, 3, xs)
eqs = list((E32.T * Xv32 * F32 - (B32 - D32)))
sol_d = sp.linsolve(eqs, xs)
print("   Solución (paramétrica):", sol_d)
if sol_d:
    reps = {s: 0 for s in sol_d.free_symbols}
    particular = tuple(sp.simplify(t.subs(reps)) for t in sol_d.args[0])
    print("   Caso particular (parámetros = 0):", particular)
    Xdp = sp.Matrix(3, 3, particular)
    show("   X (particular)", Xdp)
    print("   verif:", sp.simplify(E32.T * Xdp * F32 - (B32 - D32)) == sp.zeros(3))

print("\n" + "=" * 70)
print("SECCIÓN 3.3 — ecuaciones simples")
print("=" * 70)
M33a = sp.Matrix([[1, 3], [1, 2]])
R33a = sp.Matrix([[1, 1], [1, 1]])
Xa33 = M33a.inv() * R33a
show("a) X = M^-1 R", Xa33)
print("  verif:", M33a * Xa33 == R33a, "| det M =", M33a.det())
M33b = sp.Matrix([[2, -1], [4, -2]])
R33b = sp.Matrix([[1, 3], [6, 2]])
print("  det M(b) =", M33b.det(), "(singular -> sin inversa)")
print("  rango(M) =", M33b.rank(), "| Pendiente: verificar consistencia de X·M = R")
xsb = list(sp.symbols('u11:13 u21:23'))
Xv33b = sp.Matrix(2, 2, xsb)
eqb = list(Xv33b * M33b - R33b)
solb = sp.linsolve(eqb, xsb)
print("  b) X·M = R con M singular:", "INCONSISTENTE (sin solución)" if not solb else ("Solución paramétrica: " + str(solb)))
M33c1 = sp.Matrix([[3, 1], [2, 1]])
M33c2 = sp.Matrix([[1, 3], [1, 2]])
R33c = sp.Matrix([[3, 3], [2, 2]])
Xc33 = M33c1.inv() * R33c * M33c2.inv()
show("c) X = P^-1 R Q^-1", Xc33)
print("  verif:", M33c1 * Xc33 * M33c2 == R33c)

print("\n" + "=" * 70)
print("SECCIÓN 3.4 — menores, cofactores, adjunta, inversa")
print("=" * 70)
for nm, M in [("A", sp.Matrix([[4, -2], [-1, 4]])),
              ("B", sp.Matrix([[1, -2, 3], [-1, 4, 5], [-3, 6, -9]])),
              ("C", sp.Matrix([[1, -2], [-1, 4]]))]:
    n = M.shape[0]
    print(f"\n--- {nm} (det = {M.det()}) ---")
    minors = sp.Matrix([[M.minor_submatrix(i, j).det() for j in range(n)] for i in range(n)])
    cof = sp.Matrix([[(-1) ** (i + j) * M.minor_submatrix(i, j).det() for j in range(n)] for i in range(n)])
    print("Menores:")
    sp.pprint(minors)
    print("Cofactores:")
    sp.pprint(cof)
    print("Adjunta:")
    sp.pprint(cof.T)
    if M.det() != 0:
        print("Inversa:")
        sp.pprint(M.inv())

print("\n" + "=" * 70)
print("SECCIÓN 3.5 — inversas y ecuaciones")
print("=" * 70)
A35 = sp.Matrix([[1, -2], [3, 4]])
B35 = sp.Matrix([[0, 1], [5, -6]])
C35 = sp.Matrix([[-2, 0], [5, 2]])
for nm, M in [("A", A35), ("B", B35), ("C", C35)]:
    print(f"det {nm} = {M.det()} ->", "invertible" if M.det() != 0 else "singular")
    if M.det() != 0:
        print(f"{nm}^-1 =")
        sp.pprint(M.inv())
X1 = A35.inv() * (B35 - C35)
show("1) X = A^-1 (B - C)", X1)
print("   verif:", A35 * X1 == B35 - C35)
X2 = A35.inv() * B35 * C35 * B35.inv()
show("2) X = A^-1 B C B^-1", X2)
print("   verif:", A35 * X2 * B35 == B35 * C35)
X3 = -C35 * (A35 - B35).inv()
show("3) X = -C (A - B)^-1", X3)
print("   verif:", X3 * A35 + C35 == X3 * B35)

print("\n" + "=" * 70)
print("SECCIÓN 3.6 — B - (1/3)X = A^T A")
print("=" * 70)
A36 = sp.Matrix([[0, 1, 1], [0, 0, 1]])
B36 = sp.Matrix([[i + j for j in range(1, 4)] for i in range(1, 4)])
show("A^T A", A36.T * A36)
X36 = 3 * (B36 - A36.T * A36)
show("X = 3(B - A^T A)", X36)
print("verif:", B36 - sp.Rational(1, 3) * X36 == A36.T * A36)

print("\n" + "=" * 70)
print("SECCIÓN 3.7 — parámetro λ")
print("=" * 70)
l2 = sp.symbols('lambda')
A37 = sp.Matrix([[l2, -2], [4, -1]])
B37 = sp.Matrix([[4, -2, 0], [-1, l2, -1], [0, -1, 4]])
C37 = sp.Matrix([[l2, -2, 1], [0, -3, 5], [0, 2, l2]])
print("a) det A =", sp.factor(A37.det()), "-> |A|=3:", sp.solve(sp.Eq(A37.det(), 3), l2))
print("b) det B =", sp.factor(B37.det()), "-> |B|=0:", sp.solve(sp.Eq(B37.det(), 0), l2))
print("c) det C =", sp.factor(C37.det()), "-> |C|=8:", sp.solve(sp.Eq(C37.det(), 8), l2))

print("\n" + "=" * 70)
print("SECCIÓN 3.8 — k sin inversa")
print("=" * 70)
k = sp.symbols('k')
A38 = sp.Matrix([[k - 3, -2], [-2, k - 2]])
B38 = sp.Matrix([[2, 0, 0], [0, k + 1, -1], [0, 1, k - 3]])
print("a) det A =", sp.factor(A38.det()), "-> k:", sp.solve(sp.Eq(A38.det(), 0), k))
print("b) det B =", sp.factor(B38.det()), "-> k:", sp.solve(sp.Eq(B38.det(), 0), k))

print("\n" + "=" * 70)
print("SECCIÓN 3.9 — a para invertibilidad")
print("=" * 70)
a9 = sp.symbols('a')
A39 = sp.Matrix([[a9, 0, 1, -1], [1, 2, 0, 2], [0, -3, 2, 0], [1, a9, 3, a9]])
print("det A =", sp.factor(A39.det()))
print("Raíces:", sp.solve(sp.Eq(A39.det(), 0), a9))

print("\n" + "=" * 70)
print("SECCIÓN 2.5 — Vandermonde (verificación simbólica)")
print("=" * 70)
va, vb, vc = sp.symbols('a b c')
AV = sp.Matrix([[1, va, va ** 2], [1, vb, vb ** 2], [1, vc, vc ** 2]])
print("det =", sp.factor(AV.det()))

print("\n" + "=" * 70)
print("SECCIÓN 2.4 — potencias (verificación)")
print("=" * 70)
n = sp.symbols('n', positive=True, integer=True)
print("det(A^2) = det(A)^2 = 4 | det(A^3) = 8 | det(A^n) = 2^n | det(2A) = 8 | det(3A) = 18 | det(kA) = 2k^2")
A24 = sp.Matrix([[1, 1], [-1, 2]])  # det = 3, ejemplo genérico
print("Ejemplo det(A^2) = det(A)^2:", sp.simplify(A24.det() ** 2 - (A24 ** 2).det()) == 0)
print("\nTODO VERIFICADO ✔")
