################################################################################################
#
# Exemplo de como realizar regressão linear simples, com ênfase na comparação 
# da métrica ou parâmetro de desempenho dos mínimos quadrados R^2 de cada ajuste
# 
################################################################################################

# Importando as bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


# Criando a base de dados
dados = {'X': [5, 15, 25, 35, 45, 55],
         'Y': [5, 20, 14, 32, 22, 38]}

dados = pd.DataFrame(data = dados)

# Separando os dados:
# X é a variável independente
# Y é a variável dependente
X = dados['X'].values
Y = dados['Y'].values

# Função para transpor os valores da coordenada X
X = X.reshape(-1, 1)

# Criando a instância para as classes de regressão linear
ajuste1  = LinearRegression(fit_intercept= False) # y(x) = b1*x  (b0 = 0)
ajuste2  = LinearRegression(fit_intercept= True)  # y(x) = b0 + b1*x


# Passando os dados para fazer os ajustes
ajuste1.fit(X, Y)
ajuste2.fit(X, Y)


# Variáveis atribuídas para os valores dos mínimos quadrados (R^2) resultantes dos ajustes
R_sq1 = ajuste1.score(X, Y)
R_sq2 = ajuste2.score(X, Y)

b0_ajuste1 = ajuste1.intercept_ # parâmetro b0 do ajuste1 (Coeficiente Linear da reta, neste caso fizemos b0 = 0)
b1_ajuste1 = ajuste1.coef_ # parâmetro b1 do ajuste1 (Coeficiente Angular da reta)

b0_ajuste2 = ajuste2.intercept_ # parâmetro b0 do ajuste2 (Coeficiente Linear da reta)
b1_ajuste2 = ajuste2.coef_ # parâmetro b do ajuste2 (Coeficiente Angular da reta)

print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA O AJUSTE 1 **")
print("\n========================================================")
print("\n Coeficiente Linear para o ajuste1 (b0): ", b0_ajuste1)
print("\n Coeficiente Angular para o ajuste1 (b1): ", b1_ajuste1)
print("\n Valor de R^2 para o ajuste1: ", R_sq1)

print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA O AJUSTE 2 **")
print("\n========================================================")
print("\n Coeficiente Linear para o ajuste2 (b0): ", b0_ajuste2)
print("\n Coeficiente Angular para o ajuste2 (b1): ", b1_ajuste2)
print("\n Valor de R^2 para o ajuste2: ", R_sq2)


# Visualizando o gráfico
fig_size = plt.figure(figsize=(10,6))

plot_ajuste1 = fig_size.add_subplot(121)
plot_ajuste1 = plt.scatter(X, Y, color = 'blue')
plot_ajuste1 = plt.plot(X, ajuste1.predict(X), color = 'red')
plot_ajuste1 = plt.title('Ajuste 1')
plot_ajuste1 = plt.xlabel('X')
plot_ajuste1 = plt.ylabel('Y')

plot_ajuste2 = fig_size.add_subplot(122)
plot_ajuste2 = plt.scatter(X, Y, color = 'blue')
plot_ajuste2 = plt.plot(X, ajuste2.predict(X), color = 'red')
plot_ajuste2 = plt.title('Ajuste 2')
plot_ajuste2 = plt.xlabel('X')
plot_ajuste2 = plt.ylabel('Y')


plt.show()

