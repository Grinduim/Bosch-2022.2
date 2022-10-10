############################################################################################
# 
# Determinação do Intervalo Interquartil (IQR) e apresentação do Boxplot para as idades dos personagens dos Simpsons
#
# Um gráfico de caixa é um tipo de gráfico que exibe o resumo de cinco números de um conjunto de dados, que inclui:

# O valor mínimo
# O primeiro quartil (o percentil 25)
# O valor mediano
# O terceiro quartil (o percentil 75)
# O valor máximo

# Usamos o seguinte processo para desenhar um gráfico de caixa:

# 1- Desenhe uma caixa do primeiro quartil (Q1) ao terceiro quartil (Q3)
# 2- Faça uma linha dentro da caixa na mediana
# 3- Desenhe “bigodes” entre os quartis Q1 e Q3 para os valores mínimo e máximo respectivamente

# Quando a mediana está mais próxima do fundo da caixa
# e o bigode é mais curto na extremidade inferior ou esquerda da caixa,
# a distribuição é assimétrica à direita (ou assimétrica “positivamente”).

# Quando a mediana está mais próxima do topo da caixa
# e o bigode é mais curto na extremidade superior ou direita da caixa,
# a distribuição é assimétrica à esquerda (ou assimétrica “negativamente”).

# Quando a mediana está no meio da caixa
# e os bigodes são aproximadamente iguais em cada lado,
# a distribuição é simétrica (ou “sem” inclinação).
###########################################################################################

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

dados = {'Grupo 1': [1, 8, 10, 38, 39],
         'Grupo 2': [8, 10, 39, 45, 49]}

dataframe = pd.DataFrame(data = dados)


# Para mostrar o boxplot com o código a seguir (diagrama de caixa) foi necessário executar este script com o Spyder
#boxplot = dataframe.boxplot(['Grupo 1', 'Grupo 2'], grid = False)

# Plot the dataframe
boxplot = dataframe[['Grupo 1', 'Grupo 2']].plot(kind='box', title='boxplot')
plt.show()


################################################# #############################
#
# DETERMINAÇÃO DOS SEGUINTES VALORES:
#
# 1º QUARTIL;
# 2º QUARTIL(mediana);
# 3º QUARTIL;
# 4º QUARTIL;
# IQR;
# VALOR MÍNIMO;
# VALOR MÁXIMO;
#
################################################# #############################

q3_Grupo_1, q1_Grupo_1 = np.percentile(dataframe['Grupo 1'], [75, 25])

IQR_Grupo_1 = q3_Grupo_1 - q1_Grupo_1


print("\n Grupo 1")
print("\n Idade máxima: ", max(dataframe['Grupo 1']))
print("\n Idadae Mínima: ", min(dataframe['Grupo 1']))
print("\n q1: ", q1_Grupo_1)
print("\n q3: ", q3_Grupo_1)
print("\n IQR: ", IQR_Grupo_1)


q3_Grupo_2, q1_Grupo_2 = np.percentile(dataframe['Grupo 2'], [75, 25])

IQR_Grupo_2 = q3_Grupo_2 - q1_Grupo_2

print("\n Grupo 2")
print("\n Idade máxima: ", max(dataframe['Grupo 2']))
print("\n Idadae Mínima: ", min(dataframe['Grupo 2']))
print("\n q1: ", q1_Grupo_2)
print("\n q3: ", q3_Grupo_2)
print("\n IQR: ", IQR_Grupo_2)





