################################################################################################
# Podemos prever a emissão de CO2 de um carro com base no volume do motor, mas com a regressão 
# múltipla podemos incluir mais variáveis, como o peso do carro, para tornar a previsão mais precisa. 
# Considerando a base de dados do arquivo .csv, que reúne informações sobre algumas marcas e modelos 
# de carros, desenvolva um script em Python para realizar uma regressão linear de múltiplas 
# variáveis e verificar a relação entre a emissão de CO2 com o peso do carro e o volume do motor. 

################################################################################################

# Importando as bibliotecas
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from matplotlib import pyplot as plt

# Definindo a base de dados
df = pd.read_csv('REGRESSION_EXAMPLES\ARQUIVOS_CSV\CO2_&_CARROS_1.csv', sep = ';')

# Gerando uma lista das variáveis preditoras (variáveis independentes) e nomeando-as de X [x1, x2, ..., xn]
X = df[['Volume_Motor', 'Peso_Carro']]  # É comum nomear a lista de variáveis preditoras com letras maiúsculas

# Definindo a varável resposta (variável dependente)
y = df[['CO2']]    # É comum nomear a lista de variáveis respostas com letras minúsculas               

print("\n===============================================================================")
print("\n** REPRESENTAÇÃO GRÁFICA DE REGRESSÃO LINEAR COM 2 VARIÁVEIS INDEPENDENTES  **")
print("\n================================================================================")

ajuste_modelo = smf.ols(formula = 'CO2 ~ Volume_Motor + Peso_Carro', data = df)
equacao_ajustada = ajuste_modelo.fit()
equacao_ajustada.params

# Preparando os dados para visualização
x_surf, y_surf = np.meshgrid(np.linspace(df.Volume_Motor.min(), df.Volume_Motor.max(), 100), np.linspace(df.Peso_Carro.min(), df.Peso_Carro.max(), 100))
onlyX = pd.DataFrame({'Volume_Motor': x_surf.ravel(), 'Peso_Carro': y_surf.ravel()})
fittedY = equacao_ajustada.predict(exog = onlyX)

# Converte os resultados preditos em uma array
fittedY = np.array(fittedY)

# Construção do gráfico para a regresssão linear com múltiplas variáveis
fig = plt.figure(dpi = 100)
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(df['Volume_Motor'], df['Peso_Carro'], df['CO2'], c = 'red', marker='o', alpha=0.5)
ax.plot_surface(x_surf, y_surf, fittedY.reshape(x_surf.shape), color='blue', alpha=0.3)
ax.set_xlabel('Volume_Motor (cm^3)')
ax.set_ylabel('Peso_Carro (kg)')
ax.set_zlabel('CO2 (g/kg)')
plt.show()



# Adiciona uma constante para cada variável preditora
X = sm.add_constant(X)

# Realiza a regressã linear usando a função OLS() --> Ordinary Least Squares
modelo = sm.OLS(y, X).fit()

# Apresenta os resultados da regressão linear
print(modelo.summary())