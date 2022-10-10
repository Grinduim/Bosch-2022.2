# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:21:29 2020

@author: olv2ct
"""

# Manipulação de dados
import pandas as pd
import numpy as np
import math
# Algoritmos, Métricas e Funcionalidades de Machine Learning
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score 
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler

# Gráficos
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set()

#Carregar os dados
df = pd.read_csv('2_housing.csv')
df.head()

#Separando os dados
X=df.iloc[:,:-1]
Y=df.iloc[:,-1]

# Podemos observar a relação entre as colunas RM, LSTAT e PTRATIO com a nossa váriavel alvo MEDV
# Podemos observar a possibilidade de aplicar uma regressão linear simples envolvendo a váriavel RM e MEDV
# E podemos obter uma regressão polinomial entre LSTAT e MEDV
sns.pairplot(data=df)
plt.show()


#Dividir os dados
X = df.iloc[:,:-1]
y = df['MEDV']

X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.25, random_state=13)

print('Dataset original: X com {} e y com {}'.format(X.shape, y.shape))
print('\nDivisão escolhida em 75% para treino e 25% para teste. \n')
print('Formato dos dados de treino: X_train com {} e y_train com {}'.format(len(X_train), len(y_train)))
print('Formato dos dados de teste: X_test com {} e y_test com {}'.format(len(X_test), len(y_test)))

#Regressão Linear
# Observando a divisão em relação as váriaveis RM e MEDV

sns.scatterplot(X_train['RM'], y_train, color='blue', label='Dados de treino')
sns.scatterplot(X_test['RM'], y_test, color='green', label='Dados de test')
plt.legend()
plt.show()

linreg=LinearRegression()

X_trainOut = X_train['RM'].values.reshape(-1,1)
X_testOut = X_test['RM'].values.reshape(-1,1)

linreg.fit(X_trainOut, y_train)
y_pred_ = linreg.predict(X_trainOut)
print('R2 de treino:{:.2f}'.format(r2_score(y_train, y_pred_)))
print('R2 de teste:{:.2f}'.format(r2_score(y_test, linreg.predict(X_testOut))))



sns.scatterplot(X_train['RM'], y_train, color='blue', label='Dados de treino')
sns.scatterplot(X_test['RM'], y_test, color='green', label='Dados de test')
sns.lineplot(X_train['RM'], y_pred_, color='red')
plt.legend()
plt.show()

# Observando os coeficientes da função
print('Nosso [B0]: ', linreg.intercept_)
print('Nosso [B1]: ', linreg.coef_)
print('Nossa função gerada foi: Y = {} + {}*X'.format(linreg.intercept_, linreg.coef_[0]))
print("MAE treino: {:.0f}%".format(mean_absolute_error(y_train, linreg.predict(X_trainOut))/1000))
print("MAE teste: {:.0f}%".format(mean_absolute_error(y_test, linreg.predict(X_testOut))/1000))
print("RMSE treino: {:.0f}%".format(math.sqrt(mean_squared_error(y_train, linreg.predict(X_trainOut)))/1000))
print("RMSE teste: {:.0f}%".format(np.sqrt(mean_squared_error(y_test, linreg.predict(X_testOut)))/1000))


#Regressão Polinomial
#
sns.scatterplot(X_train['LSTAT'], y_train, color='blue', label='Dados de treino')
sns.scatterplot(X_test['LSTAT'], y_test, color='green', label='Dados de test')
plt.legend()
plt.show()

linreg=LinearRegression()

X_trainOut = X_train['LSTAT'].values.reshape(-1,1)
X_testOut = X_test['LSTAT'].values.reshape(-1,1)

linreg.fit(X_trainOut, y_train)
y_pred_ = linreg.predict(X_trainOut)
sns.scatterplot(X_train['LSTAT'], y_train, color='blue', label='Dados de treino')
sns.scatterplot(X_test['LSTAT'], y_test, color='green', label='Dados de test')
sns.lineplot(X_train['LSTAT'], y_pred_, color='red')
plt.legend()
plt.show()

# Instanciando
# O valor passado ao PolynomialFeatures será o grau da nossa função de saída.
# Como queremos uma curva basta uma dimensão 2.
poly = PolynomialFeatures(2)
linreg = LinearRegression()



X_train_ls = X_train['LSTAT'].values.reshape(-1,1)
X_test_ls = X_test['LSTAT'].values.reshape(-1,1)


# Aplicamos ao nosso X_train['LSTAT']
# .fit para aprender a caracteristica polinomial
# .transform para aplicar 
# .fit_transform para aprender e já aplica (apenas dados de treino)

X_train_ls2 = poly.fit_transform(X_train_ls)
X_test_ls2 = poly.transform(X_test_ls)
print(X_test_ls2[:,1])

linreg.fit(X_train_ls2, y_train)

# Predizendo valores baseado no X de treino
y_pred = linreg.predict(X_train_ls2)

# Verificando a linha resultante
sns.scatterplot(X_train_ls2[:,1], y_train, color='blue', label='Dados de treino')
sns.scatterplot(X_test_ls2[:,1], y_test, color='green', label='Dados de test')
sns.lineplot(X_train_ls2[:,1], y_pred, color='red')
plt.legend()
plt.show()

# Observando os coeficientes da função
print('Nosso [B0]: ', linreg.intercept_)
print('Nosso [B1]: ', linreg.coef_)
print('Nossa função gerada foi: Y = {} + {}*X + {}*X²'.format(linreg.intercept_, linreg.coef_[1], linreg.coef_[2]))

# Métricas atualizadas com a aplicação polinomial.
print('R2 de treino: {:.2f}'.format(r2_score(y_train, linreg.predict(X_train_ls2))))
print('R2 de teste: {:.2f} \n'.format(r2_score(y_test, linreg.predict(X_test_ls2))))

print('MAE de treino: {:.0f}'.format(mean_absolute_error(y_train, linreg.predict(X_train_ls2))))
print('MAE de teste: {:.0f}\n'.format(mean_absolute_error(y_test, linreg.predict(X_test_ls2))))

print('RMSE de treino: {:.0f}'.format(np.sqrt(mean_squared_error(y_train, linreg.predict(X_train_ls2)))))
print('RMSE de teste: {:.0f}'.format(np.sqrt(mean_squared_error(y_test, linreg.predict(X_test_ls2)))))


