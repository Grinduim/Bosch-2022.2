# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

# Importando bibliotecas importantes:

# Para manipulação dos dados
import pandas as pd

# Para utilizar modelo de regressão e dividir os dados em treino e teste
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

# Para visualização dos dados
import matplotlib.pyplot as plt

# Setando configurações dos gráficos (opcional)
#plt.style.use('ggplot')

# Importando os dados
df = pd.read_csv('3_grade.csv', sep=',')
print(df.head())

# Devemos associar as váriaveis X e y de acordo com suas respectivas colunas
# O .values.reshape(-1,1) garantirá que nossos dados sairão no formato de array
X = df['SAT'].values.reshape(-1,1)
y = df['GPA'].values.reshape(-1,1)
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Visualizando dados
plt.scatter(X_train, y_train, color='blue', label='Dados de treino')
plt.scatter(X_test, y_test, color='green', label='Dados de teste')

# Ajuste da imagem
plt.legend()
plt.show()

# Instanciamos o algoritmo
linreg = LinearRegression()
linreg.fit(X_train, y_train)
y_pred_lr = linreg.predict(X_train)

# Visualizando dados
plt.scatter(X_train, y_train, color='blue', label='Dados de treino')
plt.scatter(X_test, y_test, color='green', label='Dados de teste')

# Visualizando linha gerada pela função
plt.plot(X_train, y_pred_lr, color='black', label = 'Regressão Linear')
plt.legend()
plt.show()

# Observando os coeficientes da função
print('Para Regressão Linear')
print('Nosso [b0]: ', linreg.intercept_)
print('Nosso [b1]: ', linreg.coef_)
print('Nossa função gerada foi: Y = {} + {}*X'.format(linreg.intercept_[0], linreg.coef_[0][0]))


# Visualizando dados de treino e teste
#plt.scatter(X_train, y_train, color='blue', label='Dados de teste')
#plt.scatter(X_test, y_test, color='green', label='Dados de treino')
#plt.scatter(X_new, y_new, color='red', label='Pontos novos')
#plt.legend()
#plt.show()

#Algoritmo de árvore
# Aplicando os mesmos conceitos porém utilizando um algoritmo de árvore
# Instanciamos o algoritmo
# Faremos um loop para testar vários valores para max_depth e observar a influencia nos gráficos.
for i in [None, 5, 1, 2]:
    dtr = DecisionTreeRegressor(max_depth=i)# Profundidade máxima é um hyperparâmetro
    #porque nós setamos de forma manual 
    #None você deixa a árvore crescer indefinidademente 
    #Nesta árvore é possível verificar que a árvore abraçou quase todos os pontos com alta
    #variância
    
    # Aplicamos ele nos dados de treino para gerar o modelo
    dtr.fit(X_train, y_train)

    # Predizendo valores baseado no X de treino
    y_pred_dtr = dtr.predict(sorted(X_train))

    # Visualizando dados
    plt.scatter(X_train, y_train, color='blue', label='Dados de teste')
    plt.scatter(X_test, y_test, color='green', label='Dados de treino')

    # Visualizando linha gerada pela função
    plt.plot(sorted(X_train), y_pred_dtr, color='black', label = 'Regressão Linear')

    # Ajuste da imagem
    plt.title('Algoritmo de árvore com max_depth = {}'.format(i)) 
    plt.legend()
    plt.show()
    
    print('Valor de R2 em dados de treino para max_depth = {}: R2 = {:.2f}'.format(i, dtr.score(X_train, y_train)))
    print('Valor de R2 em dados de teste para max_depth = {}: R2 = {:.2f}'.format(i, dtr.score(X_test, y_test)))
    
# Melhor valor de profundidade foi o de 2, vamos plotar para ver o resultado desta árvore.
    
# Instanciamos o algoritmo
rfr = RandomForestRegressor(max_depth=2, random_state=27) # a profundidade padrão é 8

# Aplicamos ele nos dados de treino para gerar o modelo
rfr.fit(X_train, y_train)

# Predizendo valores baseado no X de treino
y_pred_rfr = rfr.predict(sorted(X_train))

plt.scatter(X_train, y_train, color='blue', label='Dados de teste')
plt.scatter(X_test, y_test, color='green', label='Dados de treino')
plt.plot(sorted(X_train), y_pred_rfr, color='black', label = 'Regressão Linear')
# Informações dos modelos

clf = [linreg, dtr, rfr]
nomes = ['Linear Regression', 'Decision Tree', 'Random Forest']

for i, model in enumerate(clf):
    print('\n')
    print(nomes[i])
    print('Métricas para dados de teste: ')
    print('R2 (treino) - {:.1%}'.format(model.score(X_train, y_train)))
    print('R2 (teste) - {:.1%}'.format(model.score(X_test, y_test)))
    print('Erro médio absoluto - {:.3f}'.format(mean_absolute_error(y_test, model.predict(X_test))))
    print('Erro médio quadrático - {:.3f}'.format(mean_squared_error(y_test, model.predict(X_test))))