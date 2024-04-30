import matplotlib.pyplot as plt
from time import sleep
import os

X1 = input("Digite o nome da primeira variável: ")
X2 = input("Digite o nome da segunda variável: ")

print("=-" * 24)

R1_1 = int(input("Digite a quantidade da primeira restrição para primeira variável: "))
R1_2 = int(input("Digite a quantidade da primeira restrição para segunda variável: "))
R1_3 = int(input("Digite o limite máximo da primeira restrição: "))

print(f"{R1_1} XI + {R1_2} XII < {R1_3}")

print("=-" * 24)

R2_1 = int(input("Digite a quantidade da segunda restrição para primeira variável: "))
R2_2 = int(input("Digite a quantidade da segunda restrição para segunda variável: "))
R2_3 = int(input("Digite o limite máximo da segunda restrição: "))

print(f"{R2_1} XI + {R2_2} XII < {R2_3}")

print("=-" * 24)

Lucro_1 = int(input("Digite o lucro da primeira variável: "))
Lucro_2 = int(input("Digite o lucro da segunda variável: "))

print(f"L = {Lucro_1} XI + {Lucro_2} XII")

os.system("cls")

print("=-" * 24)
sleep(1)
print(f"R1: {R1_1} XI + {R1_2} XII < {R1_3}")
print(f"R2: {R2_1} XI + {R2_2} XII < {R2_3}")
print(f"L = {Lucro_1} XI + {Lucro_2} XII ")
print("=-" * 24)

sleep(1)
print(f"{R1_1} XI + {R1_2} XII == {R1_3}")
print(f"{R2_1} XI + {R2_2} XII == {R2_3}")
print("=-" * 24)

Coordenada_1_1 = R1_3 / R1_2
Coordenada_1_2 = R1_3 / R1_1

Coordenada_2_1 = R2_3 / R2_2
Coordenada_2_2 = R2_3 / R2_1

# coordenada_1 = [[0, Coordenada_1_1], [Coordenada_1_2, 0]]
# coordenada_2 = [[0, Coordenada_2_1], [Coordenada_2_2, 0]]

# print(f"coordenada 1: {coordenada_1}\ncoordenada 2: {coordenada_2}")

x_1 = [0, Coordenada_1_1]
y_1 = [Coordenada_1_2, 0]

x_2 = [0, Coordenada_2_1]
y_2 = [Coordenada_2_2, 0]

sleep(1)
print(f"Ponto 1: {x_1}")
print(f"Ponto 2: {x_2}")
print(f"Ponto 3: {y_1}")
print(f"Ponto 4: {y_2}")

print("=-"*24)


# CALCULOS
parte_divisao = (R2_1 * (- R1_2)) + (R2_2 * R1_1)
xii = float(((R2_1 * R1_3) - (R2_3 * R1_1)) / parte_divisao) * - 1

xi = ((R1_2 * xii) - R1_3) / R1_1 * - 1

# RESULTADOS
sleep(1)
print(f"Quantidade ótima de {X1} == {xi:.2f}")
sleep(1)
print(f"Quantidade ótima de {X2} == {xii:.2f}")
sleep(1)
lucro = Lucro_1 * xi + Lucro_2 * xii
print(f"Resultado do lucro total == R${lucro:.2f}")
print("=-" * 24)
sleep(1)

# GRÁFICO
plt.figure("Gráfico de Decisão")

# Ponto Ótimo
plt.scatter(xi, xii, color="black", label="Ponto Ótimo")

# Ponto Viável
plt.plot(y_1, x_1, label="Restrição 1")
plt.plot(y_2, x_2, label="Restrição 2")

# Mudanças no Gráfico
plt.title("Gráfico de Decisão"), plt.xlabel(xlabel=f"{X1}"), plt.ylabel(ylabel=f"{X2}")

plt.grid(True)
plt.legend()
plt.show()
