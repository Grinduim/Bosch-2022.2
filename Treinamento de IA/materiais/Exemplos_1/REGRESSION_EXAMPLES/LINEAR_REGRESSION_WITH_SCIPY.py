################################################################################################
#
# Exemplo de como realizar regressão linear simples usando a bib scipy, com ênfase na comparação 
# da métrica de desempenho dos mínimos quadrados R^2 para cada ajuste
# 
################################################################################################

# Importando as bibliotecas
from code import interact
from matplotlib import pyplot as plt
from scipy import stats


# Base de dados 1
x1 = [5, 15, 25, 35, 45, 55, 69, 65, 70, 75, 80, 85, 90, 95, 100]
y1 = [5, 20, 14, 32, 22, 38, 43, 35, 50, 62, 55, 64, 78, 87, 72]

# Base de dados 2
x2 = [5, 15, 25, 35, 45, 55, 69, 65, 70, 75, 80, 85, 90, 95, 100]
y2 = [21, 46,  3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38]

b1_ajuste1, b0_ajuste1, R_sq1, p_ajuste1, std_err_ajuste1 = stats.linregress(x1,y1)

b1_ajuste2, b0_ajuste2, R_sq2, p_ajuste2, std_err_ajuste2 = stats.linregress(x2,y2)


def realiza_ajuste_1(x):
    
    return b0_ajuste1 + b1_ajuste1*x


def realiza_ajuste_2(x):
    
    return b0_ajuste2 + b1_ajuste2*x

ajuste1 = list(map(realiza_ajuste_1, x1))

ajuste2 = list(map(realiza_ajuste_2, x2))

print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA O AJUSTE 1 **")
print("\n========================================================")
print("\n Coeficiente Linear para o ajuste1 (b0): ", b0_ajuste1)
print("\n Coeficiente Angular para o ajuste1 (b1): ", b1_ajuste1)
print("\n Valor de R^2 para o ajuste1: ", R_sq1)

# Visualizando o gráfico do ajuste 1
print("\n========================================================")
print("\n** GRÁFICO REFERENTE AO AJUSTE 1 **")
print("\n========================================================")
plot_ajuste1 = plt.scatter(x1, y1, color = 'blue')
plot_ajuste1 = plt.plot(x1, ajuste1, color = 'red')
plot_ajuste1 = plt.title('Ajuste 1')
plot_ajuste1 = plt.xlabel('X')
plot_ajuste1 = plt.ylabel('Y')
plt.show()



print("\n========================================================")
print("\n** PARÂMETROS OBTIDOS PARA O AJUSTE 2 **")
print("\n========================================================")
print("\n Coeficiente Linear para o ajuste2 (b0): ", b0_ajuste2)
print("\n Coeficiente Angular para o ajuste2 (b1): ", b1_ajuste2)
print("\n Valor de R^2 para o ajuste2: ", R_sq2)

# Visualizando o gráfico do ajuste 2
print("\n========================================================")
print("\n** GRÁFICO REFERENTE AO AJUSTE 2 **")
print("\n========================================================")
plot_ajuste2 = plt.scatter(x2, y2, color = 'blue')
plot_ajuste2 = plt.plot(x2, ajuste2, color = 'red')
plot_ajuste2 = plt.title('Ajuste 2')
plot_ajuste2 = plt.xlabel('X')
plot_ajuste2 = plt.ylabel('Y')
plt.show()
