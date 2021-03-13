from Quadrado import Quadrado as Q
from Circulo import Circulo as C
from math import sqrt

q: Q = Q(2)
c: C = C(2) 

print(f'Quandrado Área: {q.obter_area():.2f}')
print(f'Quandrado Perimentro: {q.obter_perimetro():.2f}')
print(f'Quandrado Diagonal: {q.obter_diagonal():.2f}')

print("\nAtulazou diag\n")
q.atualizar_diag(sqrt(3)) 

print(f'Quandrado Área: {q.obter_area():.2f}')
print(f'Quandrado Perimentro: {q.obter_perimetro():.2f}')
print(f'Quandrado Diagonal: {q.obter_diagonal():.2f}')

# ===============================================================
# ===============================================================
# ===============================================================

print(f"Obter Área: {c.obter_area()}")
print(f"Obter Circunferencia: {c.obter_circunferencia()}")

print("\nAtualizou PI\n")
c.atualizar_pi(3.1516)

print(f"Obter Área: {c.obter_area()}")
print(f"Obter Circunferencia: {c.obter_circunferencia()}")
