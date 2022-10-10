######################################################################################################
#
#   O valor de um imóvel geralmente é calculado com base na usa área, quanto maior a área,
#   mais caro o imóvel tende a ser. Isso nos indica que essa relação, é uma relação linear.
#   Com base nisso, construa o gráfico que mostre a reta de regressão e verifique se existe
#   algum outlier nos dados fornecidos. Utilize o regressor linear para prever também os seguintes
#   valores dos imóveis com as seuintes áreas: 35, 70 e 190.
#
######################################################################################################

# Importando as bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# Criando a base de dados
dados = {'Area': [40, 45,  50,  53,  60,  65,  100,  110,  113,  130],
         'Valor': [120, 180, 190, 187, 195, 200, 300, 320, 305, 400]}

dados = pd.DataFrame(data = dados)

# Separando os dados:
# X é a variável independente
# Y é a variável dependente
X = dados['Area'].values
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
plt.xlabel('Área')
plt.ylabel('Valor do Imóvel')
plt.show()


# Verificando se há outliers a partir de um diagrama de caixa (boxplot)
dados.boxplot(column = ['Area', 'Valor'], grid = False)
plt.show()

# Prevendo novos valores

area_35 = np.array(35)
#  Duas maneiras de passar valores para a função que foi ajustada
previsao_35 = regressor.predict(area_35.reshape(-1, 1))
print("\n Previsão do valor do imóvel com área de 35 mm^2: ", previsao_35)

area_70 = np.array(70)
#  Duas maneiras de passar valores para a função que foi ajustada
previsao_70 = regressor.predict(area_70.reshape(-1, 1))
print("\n Previsão do valor do imóvel com área de 70 mm^2: ", previsao_70)

area_190 = np.array(190)
#  Duas maneiras de passar valores para a função que foi ajustada
previsao_190 = regressor.predict(area_190.reshape(-1, 1))
print("\n Previsão do valor do imóvel com área de 190 mm^2: ", previsao_190)


