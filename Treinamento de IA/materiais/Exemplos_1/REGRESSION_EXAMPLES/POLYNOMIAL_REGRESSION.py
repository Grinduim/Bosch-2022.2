################################################################################################
#
# Exemplo de como realizar regressão linear polinomial, com ênfase na comparação 
# da métrica de desempenho dos mínimos quadrados R^2 para cada ajuste
# 
################################################################################################

# Importando as bibliotecas úteis a este script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Base de dados
dados={'X': [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22],
'Y': [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]}

dados = pd.DataFrame(data = dados)

# Separando os dados:
# X é a variável independente
# Y é a variável dependente
X = dados['X'].values
Y = dados['Y'].values

ajuste_grau_1 = np.poly1d(np.polyfit(X, Y, 1))  # y(x) = b0 + b1*x (Equação da Reta)
ajuste_grau_1_line = np.linspace(1, 22, 100)
# Calcula o valor de R^2 para o ajuste realizado
R_sq1 = r2_score(Y, ajuste_grau_1(X))  


# Realizando os ajustes com funções polinomiais de grau 2, 3, 4  e 5

ajuste_grau_2 = np.poly1d(np.polyfit(X, Y, 2))                      # Funcão polinomial de grau 2 (Parábola) (y(x) = b2*x^2 + b1*x + b0)
ajuste_grau_2_line = np.linspace(1, 22, 100)
# Calcula o valor de R^2 para o ajuste realizado
R_sq2 = r2_score(Y, ajuste_grau_2(X))             

ajuste_grau_3 = np.poly1d(np.polyfit(X, Y, 3))                      # Funcão polinomial de grau 3  (y(x) = b3*x^3 + b2*x^2 + b1*x + b0)
ajuste_grau_3_line = np.linspace(1, 22, 100)
# Calcula o valor de R^2 para o ajuste realizado
R_sq3 = r2_score(Y, ajuste_grau_3(X))             

ajuste_grau_4 = np.poly1d(np.polyfit(X, Y, 4))                      # Funcão polinomial de grau 4 ( y(x) = b4*x^4 + b3*x^3 + b2*x^2 + b1*x + b0 )
ajuste_grau_4_line = np.linspace(1, 22, 100)
# Calcula o valor de R^2 para o ajuste realizado
R_sq4 = r2_score(Y, ajuste_grau_4(X))             

ajuste_grau_5 = np.poly1d(np.polyfit(X, Y, 5))                      # Funcão polinomial de grau 5 ( y(x) = b5*x^5 + b4*x^4 + b3*x^3 + b2*x^2 + b1*x + b0 )
ajuste_grau_5_line = np.linspace(1, 22, 100)
# Calcula o valor de R^2 para o ajuste realizado
R_sq5 = r2_score(Y, ajuste_grau_5(X))             



print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA A RETA **")
print("\n========================================================")
print("\n Valor de R^2 para o ajuste polinomial de grau 1: ", R_sq1)

plot_ajuste_grau_1 = plt.scatter(X, Y, color = 'blue')
plot_ajuste_grau_1 = plt.plot(ajuste_grau_1_line, ajuste_grau_1(ajuste_grau_1_line), color = 'red')
plot_ajuste_grau_1 = plt.title('Ajuste com uma função do primeiro grau: y(x) = b0 + b1*x')
plot_ajuste_grau_1 = plt.xlabel('X')
plot_ajuste_grau_1 = plt.ylabel('Y')
plt.show()



print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA O AJUSTE POLINOMIAL DE GRAU 2 **")
print("\n========================================================")
print("\n Valor de R^2 para o ajuste polinomial de grau 2: ", R_sq2)

plot_ajuste_grau_2 = plt.scatter(X, Y, color = 'blue')
plot_ajuste_grau_2 = plt.plot(ajuste_grau_2_line, ajuste_grau_2(ajuste_grau_2_line), color = 'red')
plot_ajuste_grau_2 = plt.title('Ajuste com uma função do segundo grau: y(x) = b2*x^2 + b1*x + b0')
plot_ajuste_grau_2 = plt.xlabel('X')
plot_ajuste_grau_2 = plt.ylabel('Y')
plt.show()

print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA O AJUSTE POLINOMIAL DE GRAU 3 **")
print("\n========================================================")
print("\n Valor de R^2 para o ajuste polinomial de grau 3: ", R_sq3)

plot_ajuste_grau_3 = plt.scatter(X, Y, color = 'blue')
plot_ajuste_grau_3 = plt.plot(ajuste_grau_3_line, ajuste_grau_3(ajuste_grau_3_line), color = 'red')
plot_ajuste_grau_3 = plt.title('Ajuste com uma função de terceiro grau: y(x) = b3*x^3 + b2*x^2 + b1*x + b0')
plot_ajuste_grau_3 = plt.xlabel('X')
plot_ajuste_grau_3 = plt.ylabel('Y')
plt.show()


print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA O AJUSTE POLINOMIAL DE GRAU 4 **")
print("\n========================================================")
print("\n Valor de R^2 para o ajuste polinomial de grau 4: ", R_sq4)


plot_ajuste_grau_4 = plt.scatter(X, Y, color = 'blue')
plot_ajuste_grau_4 = plt.plot(ajuste_grau_4_line, ajuste_grau_4(ajuste_grau_4_line), color = 'red')
plot_ajuste_grau_4 = plt.title('Ajuste com uma função de quarto grau: y(x) = b4*x^4 + b3*x^3 + b2*x^2 + b1*x + b0')
plot_ajuste_grau_4 = plt.xlabel('X')
plot_ajuste_grau_4 = plt.ylabel('Y')
plt.show()


print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA O AJUSTE POLINOMIAL DE GRAU 5 **")
print("\n========================================================")
print("\n Valor de R^2 para o ajuste polinomial de grau 5: ", R_sq5)

plot_ajuste_grau_5 = plt.scatter(X, Y, color = 'blue')
plot_ajuste_grau_5 = plt.plot(ajuste_grau_5_line, ajuste_grau_5(ajuste_grau_5_line), color = 'red')
plot_ajuste_grau_5 = plt.title('Ajuste com uma função de quinto grau: y(x) = b5*x^5 + b4*x^4 + b3*x^3 + b2*x^2 + b1*x + b0')
plot_ajuste_grau_5 = plt.xlabel('X')
plot_ajuste_grau_5 = plt.ylabel('Y')
plt.show()