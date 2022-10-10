##########################################################################################################
# 
# Este scrip permite visualizar a velocidade de convergência do método de Monte Carlo para o exemplo 
# de estimar o valor de pi, bem como entender a depedência do erro (valor estimado - valor verdadeiro)
# em função do número de iterações N do método Monte Carlo.
#
########################################################################################################
import numpy as np
import random
import matplotlib.pyplot as plt

# Zera ("limpa") a contagem de gotas na área do círculo antes de começar a simulação 
n_in = 0

# Número de iterações
N = 1000

valor_estimado = np.empty(N)

# Realiza a distribuição das gotas de chuva (pontos aleatórios) sobre a área do quadrado:
for  i in range(N):
  
  x = random.random()
  y = random.random()
  
  # Se caiu uma gota dentro do círculo, então contabiliza essa gota e mostra a coordenada dela
  if np.sqrt((x**2) + (y**2)) <= 1:
    n_in += 1
    valor_estimado[i] = 4 * n_in /float(i + 1)
    
plt.semilogx(valor_estimado)
plt.xlabel("Número de Iterações")
plt.ylabel("Valor Estimado Atual")
# Apresenta o valor exato de pi com uma linha horizontal no gráfico
plt.axhline(np.pi, color = 'r', alpha = 0.5)  
plt.show()

plt.plot(np.arange(N), np.abs(valor_estimado-np.pi))
plt.plot(1/np.sqrt(np.arange(N)+1), color="r", alpha=0.5)
plt.xlabel("Número de Iterações")
plt.ylabel("Erro Estimado");
plt.show()

plt.loglog(np.arange(N), np.abs(valor_estimado-np.pi))
plt.loglog(1/np.sqrt(np.arange(N)+1), color="r", alpha=0.5)
plt.xlabel("Número de Iterações")
plt.ylabel("Erro Estimado");
plt.show()

