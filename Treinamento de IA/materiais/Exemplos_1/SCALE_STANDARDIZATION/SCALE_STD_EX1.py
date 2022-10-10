########################################################################
#
# A partir do conjunto de dados do arquivo CO2_&_CARROS_2.csv, 
# temos que as escalas de volume são dadas dessa vez em litros 
# ao invés de centímetros cúbicos. Realize a padronização dos 
# dados usando um script em Python.
#
########################################################################

# Importando as bibliotecas
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

import statsmodels.formula.api as smf
import statsmodels.api as sm
from matplotlib import pyplot as plt

# Definindo a base de dados
df = pd.read_csv('REGRESSION_EXAMPLES\ARQUIVOS_CSV\CO2_&_CARROS_2.csv', sep = ';')

# Mostra o dataset (dataframe) após a leitura do arquivo CO2_&_CARROS_2.csv
print('\n df: \n', df)

# Realiza a adequação de escalas para as variáveis preditoras
x1 = (df[['Volume_Motor']] - df[['Volume_Motor']].mean()) / df[['Volume_Motor']].std()

x2 = (df[['Peso_Carro']] - df[['Peso_Carro']].mean()) / df[['Peso_Carro']].std()

# Apresenta o resultado obtido para as variáveis preditoras após adequação de escalas
# print('\n', x1)
# print('\n', x2)

# Gera um novo conjunto de dados com as variáveis preditoras com escalas padrozinadas 
# junto com os dados de CO2 do conjunto de dados original (df)
dados_padronizados = [x1['Volume_Motor'], x2['Peso_Carro'], df['CO2']]

# Redefine os nomes (labels) das variáveis preditoras padronizadas e mantem o mesmo nome para
# a variável de resposta do modelo (y = 'CO2') 
novos_nomes_x1_x2_y = ['Volume_Motor_P', 'Peso_Carro_P', 'CO2']

# Gera um novo dataset (dataframe) concatenando os dataframes x1, x2 e df['CO2']
df_P = pd.concat(dados_padronizados, axis = 1, keys = novos_nomes_x1_x2_y)
         
# Mostra o resultado obtido para o novo dataframe após a adequação/padronização de escalas
print('\n df_P: \n', df_P)


print("\n===============================================================================")
print("\n** REPRESENTAÇÃO GRÁFICA DE REGRESSÃO LINEAR COM 2 VARIÁVEIS INDEPENDENTES  **")
print("\n================================================================================")

ajuste_modelo = smf.ols(formula = 'CO2 ~ Volume_Motor_P + Peso_Carro_P', data = df_P)
equacao_ajustada = ajuste_modelo.fit()
equacao_ajustada.params

# Preparando os dados para visualização
x_surf, y_surf = np.meshgrid(np.linspace(df_P.Volume_Motor_P.min(), df_P.Volume_Motor_P.max(), 100), np.linspace(df_P.Peso_Carro_P.min(), df_P.Peso_Carro_P.max(), 100))
onlyX = pd.DataFrame({'Volume_Motor_P': x_surf.ravel(), 'Peso_Carro_P': y_surf.ravel()})
fittedY = equacao_ajustada.predict(exog = onlyX)

# Converte os resultados preditos em uma array
fittedY = np.array(fittedY)

# Construção do gráfico para a regresssão linear com múltiplas variáveis
fig = plt.figure(dpi = 100)
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(df_P['Volume_Motor_P'], df_P['Peso_Carro_P'], df_P['CO2'], c = 'red', marker='o', alpha=0.5)
ax.plot_surface(x_surf, y_surf, fittedY.reshape(x_surf.shape), color='blue', alpha=0.3)

# Eixo_x está relacionado ao Volume do Motor após a padronização de escala, 
# dado em unidade arbitrária (u.a.), pois no processo de padrozinação de escalas
# temos que a  nova variável é apenas um número adimensional.
ax.set_xlabel('Volume_Motor_P (u.a.)')

# Eixo_y está relacionado ao Peso do Carro após a padronização de escala, também
# dado em unidade arbitrária (u.a.), pois no processo de padrozinação de escalas
# temos que a  nova variável é apenas um número adimensional.
ax.set_ylabel('Peso_Carro_P (u.a.)') # Unidade
ax.set_zlabel('CO2 (g/kg)')

plt.show()

# Gerando uma lista das variáveis preditoras (variáveis independentes) e nomeando-as de X [x1, x2, ..., xn]
X = df_P[['Volume_Motor_P', 'Peso_Carro_P']]  # É comum nomear a lista de variáveis preditoras com letras maiúsculas

# Definindo a varável resposta (variável dependente)
y = df_P[['CO2']]    # É comum nomear a lista de variáveis respostas com letras minúsculas 

# Adiciona uma constante para cada variável preditora
X = sm.add_constant(X)

# Realiza a regressã linear usando a função OLS() --> Ordinary Least Squares
modelo = sm.OLS(y, X).fit()

# Apresenta os resultados da regressão linear
print(modelo.summary())
      
