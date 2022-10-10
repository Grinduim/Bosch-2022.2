# Importando as bibliotecas
import numpy as np
import random
import matplotlib.pyplot as plt
plt.style.use('bmh')


# Definindo as variáveis de entrada aleatoriamente no intervalo delimitado pelo quadrado de lado 1
# x = np.random.uniform(-1, 1)
# y = np.random.uniform(-1, 1)

# if np.sqrt(x**2 + y**2) < 1:
#     print("\n O ponto está dentro do círculo")

N = 10000 # Total de pontos que serão usados para a simulação

n_out = []  # Variável para contar quantos pontos foram gerados for do círculo
n_in = []  # Variável para contar quantos pontos foram gerados dentro do círculo

# Contagem da quantidade de pontos dentro do círculo:  
for i in range(N):
    # Definindo as variáveis de entrada aleatoriamente no intervalo delimitado pelo quadrado de lado 2R
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    
    # Se algum ponto for gerado dentro do círculo, registra a coordenada (x, y) do mesmo na variável nc = []
    if  np.sqrt(x**2 + y**2) <= 1:
        n_in.append((x, y))
    else:
        n_out.append((x, y))
        
plt.figure(figsize = (6,6))

plt.scatter(
    [x[0] for x in n_in], 
    [x[1] for x in n_in],
    marker = ".", 
    alpha = 0.5)

plt.scatter(
    [x[0] for x in n_out],
    [x[1] for x in n_out],
    marker = ".",
    alpha = 0.5)

pi = 4 * float( len(n_in) / N)

print("\n Valor estimado de pi: ", pi)

plt.show()