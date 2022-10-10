#############################################################################################################
#
#  Suponha que desejamos saber se o número de horas gasto estudando e o número de provas simuladas tiveram
#  efeito na nota que determinado estudante consegue obter numa prova oficial. Para explorar essa relação,
#  podemos aplicar o método de regressão linear com múltiplas variáveis em Python.
#
#############################################################################################################
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from matplotlib import pyplot as plt

df = pd.DataFrame({'horas_de_estudo': [1, 2, 2, 4, 2, 1, 5, 4, 2, 4, 4, 3, 6, 5, 3, 4, 6, 2, 1, 2],
                   'numero_de_simulados': [1, 3, 3, 5, 2, 2, 1, 1, 0, 3, 4, 3, 2, 4, 4, 4, 5, 1, 0, 1],
                   'notas_das_provas': [76, 78, 85, 88, 72, 69, 94, 94, 88, 92, 90, 75, 96, 90, 82, 85, 99, 83, 62, 76]})


print("\n===============================================================================")
print("\n** REPRESENTAÇÃO GRÁFICA DE REGRESSÃO LINEAR COM 2 VARIÁVEIS INDEPENDENTES  **")
print("\n================================================================================")

ajuste_modelo = smf.ols(formula = 'notas_das_provas ~ horas_de_estudo + numero_de_simulados', data = df)
equacao_ajustada = ajuste_modelo.fit()
equacao_ajustada.params

# Preparando os dados para visualização
x_surf, y_surf = np.meshgrid(np.linspace(df.horas_de_estudo.min(), df.horas_de_estudo.max(), 100), np.linspace(df.numero_de_simulados.min(), df.numero_de_simulados.max(), 100))
onlyX = pd.DataFrame({'horas_de_estudo': x_surf.ravel(), 'numero_de_simulados': y_surf.ravel()})
fittedY = equacao_ajustada.predict(exog = onlyX)

# Converte os resultados preditos em uma array
fittedY = np.array(fittedY)

# Construção do gráfico para a regresssão linear com múltiplas variáveis
fig = plt.figure(dpi = 100)
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(df['horas_de_estudo'], df['numero_de_simulados'], df['notas_das_provas'], c = 'red', marker='o', alpha=0.5)
ax.plot_surface(x_surf, y_surf, fittedY.reshape(x_surf.shape), color='blue', alpha=0.3)
ax.set_xlabel('horas_de_estudo')
ax.set_ylabel('numero_de_simulados')
ax.set_zlabel('notas_das_provas')
plt.show()


# Define a variável de resposta (variável dependente)
y = df['notas_das_provas']

# Define as variáveis preditoras (variáveis independentes)
x = df[['horas_de_estudo', 'numero_de_simulados']]

# Adiciona uma constante para cada variável preditora
x = sm.add_constant(x)

# Realiza a regressã linear usando a função OLS() --> Ordinary Least Squares
modelo = sm.OLS(y, x).fit()

# Apresenta os resultados da regressão linear
print(modelo.summary())

################################################################
#
# A seguir temos a interpretação para alguns dos parâmetros
# resultantes da regressão linear
#
################################################################

# R-squared: 0.734

# Esse é o resultado dos mínimos quadrados e é conhecido como 
# coeficiente de determinação. Ele representa a proporção da variância 
# para a variável de resposta (variável dependente) que pode ser explicada 
# pelas variáveis preditoras (variáveis independentes). Neste exemplo,
# 73.4% da variação das notas das provas oficiais podem ser explicadas 
# pelo número de horas estudadas e o número de provas simuladas.
#
###################################################################

# F-statistic: 23.46

# O teste F de significância geral indica se seu modelo de regressão linear 
# fornece um ajuste melhor aos dados do que um modelo que não contém 
# variáveis independentes
#
####################################################################

# Prob (F-statistic): 1.29e-05

# Este é o valor p associado à estatística F geral. Ele nos diz se o modelo 
# de regressão como um todo é estatisticamente significativo. 
# Em outras palavras, ele nos diz se as duas variáveis preditoras combinadas 
# têm uma associação estatisticamente significativa com a variável resposta. 
# Nesse caso, o valor de p é menor que 0,05, o que indica que as variáveis preditoras 
# “horas de estudo” e “numero de provas simuladas” combinadas têm associação 
# estatisticamente significativa com as notas das provas oficiais.

#coef: 

# Os coeficientes para cada variável preditora nos informam a mudança média esperada 
# na variável de resposta, supondo que a outra variável preditora permaneça constante. 
# Por exemplo, para cada hora adicional de estudo, espera-se que a pontuação média do exame 
# aumente em 5.56, supondo que os exames preparatórios realizados permaneçam constantes.

# Aqui está outra maneira de pensar sobre isso: 

# se o aluno A e o aluno B fizerem a mesma quantidade de provas simuladas, 
# mas o aluno A estudar por mais uma hora, espera-se que o aluno A obtenha 
# uma pontuação 5.56 pontos maior do que o aluno B.

# Interpretamos o coeficiente para o intercept como significando que a nota 
# esperada para um aluno que estuda zero horas e faz zero exames preparatórios 
# é 67.67.

# P>|t|:

# Os valores de p individuais nos dizem se cada variável preditora é estatisticamente 
# significativa. Podemos ver que “horas de estudo” é estatisticamente significativo (p = 0.00) 
# enquanto “numero de provas simuladas” (p = 0.52) não é estatisticamente significativa. 
# Como “numero de provas simuladas” não é estatisticamente significativo, podemos acabar 
# decidindo removê-lo do modelo.

# Equação de regressão estimada: 
# 
# Podemos usar os coeficientes da saída do modelo para criar a seguinte equação de regressão estimada:

# notas das provas oficiais = 67.67 + 5.56*(horas de estudo) – 0.60*(numro de provas simuladas)
