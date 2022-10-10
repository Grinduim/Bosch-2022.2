from pickletools import int4
import numpy as np
import random
import matplotlib.pyplot as plt


#Define as linhas do quadrado:
horiz = np.array(range(100))/100.0
y_1 = np.ones(100)
plt.plot(horiz , y_1, 'b')
vert = np.array(range(100))/100.0
x_1 = np.ones(100)
plt.plot(x_1 , vert, 'b')


# Zera ("limpa") a contagem de gotas na área do círculo antes de começar a simulação 
n_in = 0

# Variável de controle do comado while(), começa em i = 1 sendo incrementado até atingir o número total de gotas nc 
i = 1

# Informar quantas gotas de chuva (pontos aleatórios) serão considerados para a simulação
# No JupyterLab informe diretamente o valor da variável n
N = 1000


# Realiza a distribuição das gotas de chuva (pontos aleatórios) sobre a área do quadrado:
while ( i <= N ):
  
  x = random.random()
  y = random.random()
  
  # Se caiu uma gota dentro do círculo, então contabiliza essa gota e mostra a coordenada dela
  if np.sqrt((x**2) + (y**2)) <= 1:
    n_in += 1
    plt.plot(x , y , 'bo')
    
  # Se caiu uma gota fora do círculo, paenas mostra onde ela caiu
  else:
    plt.plot(x , y , 'ro')
  i += 1


# Calcula o valor de pi estimado pela razão entre a quantidade de gotas dentro do círculo e o total de gotas
pi = float ((4 * n_in) / N)

print ("O valor de pi é: ", pi)

plt.show()