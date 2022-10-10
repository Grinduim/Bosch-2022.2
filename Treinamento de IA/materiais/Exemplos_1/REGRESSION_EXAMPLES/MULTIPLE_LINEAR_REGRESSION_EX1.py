#############################################################################################################
#
# Exemplo de como realizar regressão linear múltipla considerando 2 variáveis independentes, 
# com ênfase na comparação da métrica de desempenho dos mínimos quadrados R^2 de cada ajuste
# 
##############################################################################################################

# Importando as bibliotecas
import numpy as np
from sklearn.linear_model import LinearRegression

import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.formula.api as smf


x= [[2, 1], [5, 3], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35],
    [64, 40], [70, 41], [78, 32], [83, 45], [90, 51], [95, 55], [100, 64], [104, 65]]
y= [4, 5, 20, 14, 32, 42, 38, 43, 36, 25, 50, 44, 52, 62, 68, 73]


# # Função para transpor os valores da coordenada X
# X = X.reshape(-1, 1)

# Criando a instância para as classes de regressão linear
ajuste1  = LinearRegression(fit_intercept= False) # y(x1, x2) = b1*x1 + b2*x2  (b0 = 0)
ajuste2  = LinearRegression(fit_intercept= True)  # y(x1, x2) = b0 + b1*x + b2*x2


# Passando os dados para fazer os ajustes
ajuste1.fit(x, y)
ajuste2.fit(x, y)

# Variáveis atribuídas para os valores dos mínimos quadrados (R^2) resultantes dos ajustes
R_sq1 = ajuste1.score(x, y)
R_sq2 = ajuste2.score(x, y)

b0_ajuste1 = ajuste1.intercept_ # parâmetro b0 do ajuste1 (Coeficiente Linear da reta, neste caso fizemos b0 = 0)
b1_ajuste1 = ajuste1.coef_[0] # parâmetro b1 do ajuste1 (Coeficiente Angular da reta quando b2 = 0)
b2_ajuste1 = ajuste1.coef_[1] # parâmetro b2 do ajuste1 (Coeficiente Angular da reta quando b1 = 0)

b0_ajuste2 = ajuste2.intercept_ # parâmetro b0 do ajuste2 (Coeficiente Linear da reta)
b1_ajuste2 = ajuste2.coef_[0] # parâmetro b1 do ajuste2 (Coeficiente Angular da reta quando b2 = 0)
b2_ajuste2 = ajuste2.coef_[1] # parâmetro b2 do ajuste2 (Coeficiente Angular da reta quando b1 = 0)

print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA O AJUSTE 1 **")
print("\n========================================================")
print("\n Coeficiente Linear para o ajuste1 (b0): ", b0_ajuste1)
print("\n Coeficiente Angular b1 para o ajuste1: ", b1_ajuste1)
print("\n Coeficiente Angular b2 para o ajuste1: ", b2_ajuste1)
print("\n Valor de R^2 para o ajuste1: ", R_sq1)

print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA O AJUSTE 2 **")
print("\n========================================================")
print("\n Coeficiente Linear para o ajuste2 (b0): ", b0_ajuste2)
print("\n Coeficiente Angular b1 para o ajuste2: ", b1_ajuste2)
print("\n Coeficiente Angular b2 para o ajuste2: ", b2_ajuste2)
print("\n Valor de R^2 para o ajuste2: ", R_sq2)


print("\n===============================================================================")
print("\n** REPRESENTAÇÃO GRÁFICA DE REGRESSÃO LINEAR COM 2 VARIÁVEIS INDEPENDENTES  **")
print("\n================================================================================")
# Regressão linear múltipla usando o pandas e statsmodels
df = pd.DataFrame(x, columns=['x1', 'x2'])
df['y'] = pd.Series(y)

ajuste_modelo = smf.ols(formula = 'y ~ x1 + x2', data = df)
equacao_ajustada = ajuste_modelo.fit()
equacao_ajustada.params

# Preparando os dados para visualização	
x_surf, y_surf = np.meshgrid(np.linspace(df.x1.min(), df.x1.max(), 100), np.linspace(df.x2.min(), df.x2.max(), 100))
onlyX = pd.DataFrame({'x1': x_surf.ravel(), 'x2': y_surf.ravel()})
fittedY = equacao_ajustada.predict(exog = onlyX)

# Converte os resultados preditos em uma array
fittedY = np.array(fittedY)

# Construção do gráfico para a regressão linear com múltiplas variáveis

fig = plt.figure(dpi = 100)
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(df['x1'], df['x2'], df['y'], c = 'red', marker='o', alpha=0.5)
ax.plot_surface(x_surf, y_surf, fittedY.reshape(x_surf.shape), color='blue', alpha=0.3)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.show()
