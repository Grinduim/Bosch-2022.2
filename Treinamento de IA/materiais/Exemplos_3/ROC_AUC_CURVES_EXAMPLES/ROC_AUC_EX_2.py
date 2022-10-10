##########################################################################################################################
# 
# Muitas vezes é interessante ajustar vários modelos de classificação a um conjunto de dados, criando curvas ROC para 
# cada modelo e verificar qual apresenta o melhor desempenho nas predições dos dados.
#
##########################################################################################################################

# Importando as bibliotecas
from cv2 import threshold
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
import matplotlib.pyplot as plt

# Em seguida, usaremos a função make_classification() do sklearn para criar um conjunto de dados falso com 1.000 linhas, 
# quatro variáveis de previsão e uma variável de resposta binária:

# Criando o conjunto de dados com 1.000 linhas
X, y = datasets.make_classification( n_samples = 1000,
                                     n_features = 4,
                                     n_informative = 3,
                                     n_redundant = 1,
                                     random_state = 0)

# Separa os dados para treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = .3, random_state = 0)

# Em seguida, ajustaremos um modelo de regressão logística e, em seguida, um modelo impulsionado por gradiente 
# aos dados e traçaremos a curva ROC para cada modelo no mesmo gráfico:

# Configura a figura que conterá os gráficos das curvas ROC

# Realiza os processos de treinamento e teste usando Regressão Logísitica e em seguida constrói a curva ROC
modelo_Reg_Log = LogisticRegression()
modelo_Reg_Log.fit(X_treino, y_treino)
y_predito = modelo_Reg_Log.predict_proba(X_teste)[:, 1]
false_positive_rate, true_positive_rate, _ = metrics.roc_curve(y_teste, y_predito)
auc = round(metrics.roc_auc_score(y_teste, y_predito), 4)
plt.plot(false_positive_rate, true_positive_rate, label = "Regressão Logística -> AUC = " + str(auc))

# Realiza os processos de treinamento e teste usando Gradient Boosted e em seguida constrói a curva ROC
modelo_Grad_Boosted = GradientBoostingClassifier()
modelo_Grad_Boosted.fit(X_treino, y_treino)
y_predito = modelo_Grad_Boosted.predict_proba(X_teste)[:, 1]
false_positive_rate, true_positive_rate, _ = metrics.roc_curve(y_teste, y_predito)
auc = round(metrics.roc_auc_score(y_teste, y_predito), 4)
plt.plot(false_positive_rate, true_positive_rate, label = "Gradiente Boosting -> AUC = " + str(auc))

plt.xlabel("Taxa de Falsos Positivos")
plt.ylabel("Taxa de Verdadeiros Positivos")
plt.legend()
plt.show()

# A linha azul mostra a curva ROC para o modelo de regressão logística e a linha laranja mostra a curva ROC para o 
# modelo impulsionado por gradiente (Gradient Boosted).

# Quanto mais a curva ROC apresenta uma dobra localizada no canto superior esquerdo do gráfico, melhor é a capacidade
# do modelo classificar os dados em suas respectivas categorias.

# Para quantificar isso, podemos calcular a AUC – área sob a curva – que nos diz quanto do gráfico está localizado sob a curva.

# Quanto mais próximo AUC estiver de 1, melhor o modelo.

# Em nosso gráfico, podemos ver as seguintes métricas de AUC para cada modelo:

# AUC do modelo de regressão logística: 0.7902
# AUC do modelo impulsionado por gradiente: 0.9712

# Claramente, o modelo impulsionado por gradiente faz um trabalho melhor de classificar os dados em categorias 
# em comparação com o modelo de regressão logística.