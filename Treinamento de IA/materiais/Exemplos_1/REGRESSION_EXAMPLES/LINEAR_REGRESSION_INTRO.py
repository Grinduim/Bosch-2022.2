########################################################################
#
#   Example de como realizar regressão linear
#
########################################################################

# Importando as bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# Criando a base de dados
dados = {'Valor': [200, 220, 300, 290, 450, 457, 500, 530, 700, 800],
         'Idade': [18,   22,  23,  30,  35,  44,  49,  50,  67,  75]}

dados = pd.DataFrame(data = dados)

# Separando os dados:
# X é a variável independente
# Y é a variável dependente
X = dados['Idade'].values
Y = dados['Valor'].values

# Função para usar X transposto
X = X.reshape(-1,1)

# Definindo o regressor linear
regressor = LinearRegression()

# Passando os dados para treinar o regressor
regressor.fit(X,Y)

# Visualizando o gráfico
plt.scatter(X,Y, color = 'black')
plt.plot(X, regressor.predict(X), color = 'red')
plt.title('Regressão Linear Simples')
plt.xlabel('Idade')
plt.ylabel('Valor do Plano de Saúde')
plt.show()

# Prevendo novos valores
idade = np.array(57)
#  Duas maneiras de passar valores para a função que foi ajustada
previsao_1 = regressor.predict(idade.reshape(-1, 1))
previsao_2 = regressor.intercept_ + regressor.coef_*idade # Passa o valor da idade para a funcão da reta ajustada.
                                                         # Neste caso representada no forma explicita: f(x) = b0 + b1.x

print("\n Previsão 1: ", previsao_1)
print("\n Previsão 2: ", previsao_2)

