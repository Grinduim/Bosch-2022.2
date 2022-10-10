############################################################################################################################
# Curva ROC (Receiver Operator Characteristic) e AUC (Area Under the Curve)
#
# Na classificação, existem muitas métricas de avaliação diferentes. A mais popular é a acurácia, que mede a frequência com 
# que o modelo realiza predições corretas. Essa é uma ótima métrica porque é fácil de entender e obter, pois a suposição 
# mais correta geralmente é desejada. Há alguns casos em que você pode considerar o uso de outra métrica de avaliação.
#
# Outra métrica comum é a AUC, área sob a curva ROC (Receiver Operating Characteristic). 
# A ROC traça a taxa de verdadeiros positivos (TP) versus a taxa de falsos positivos (FP) em diferentes limites de classificação. 
# Os limites são diferentes pontos de corte de probabilidade que separam as duas classes na classificação binária. 
#
###############################################################################################################################

# Suponha que temos um conjunto de dados desequilibrado em que, a maioria de nossos dados possuí apenas um valor. 
# Podemos obter alta precisão para o modelo prevendo a classe majoritária.

# Importando as bibliotecas
from cv2 import threshold
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Criando uma base de dados não balanceada
n = 1000
razao = .95
n_A = int((1-razao)*n)
n_B = int(razao * n)

y = np.array([0] * n_A + [1] * n_B)

# A seguir, estão as probabilidades obtidas de um modelo hipotético que sempre prevê a classe majoritária
# A probabilidade de prever a classe 1 será 100%
y_proba_1 = np.array([1]*n)
y_pred_1 = y_proba_1 > .5

print(f'Acurácia: {accuracy_score(y, y_pred_1)}')
cf_mat = confusion_matrix(y, y_pred_1)
print('Matriz de Confusão')
print(cf_mat)
print(f'Acurácia para a classe A: {cf_mat[0][0]/n_A}')
print(f'Acurácia para a classe B: {cf_mat[1][1]/n_B}')

# Apesar de obtermos uma precisão muito alta, o modelo não forneceu informações sobre os dados, portanto, não é útil. 
# 
# Prevemos com precisão a classe A 100% das vezes, enquanto prevemos imprecisamente a classe B 0% das vezes. 
# Em detrimento da precisão, pode ser melhor ter um modelo que possa separar um pouco as duas classes.

y_proba_2 = np.array(
    np.random.uniform(0, .7, n_A).tolist() + 
    np.random.uniform(.3, 1, n_B).tolist()
)

y_pred_2 = y_proba_2 > .5

print(f'Acurácia: {accuracy_score(y, y_pred_2)}')
cf_mat = confusion_matrix(y, y_pred_2)
print('Matriz de Confusão')
print(cf_mat)
print(f'Acurácia da classe A: {cf_mat[0][0]/n_A}')
print(f'Acurácia da classe B: {cf_mat[1][1]/n_B}')

# Para o segundo conjunto de previsões, não temos uma pontuação de precisão tão alta quanto a primeira, 
# mas a precisão para cada classe é mais equilibrada. Usando a precisão como uma métrica de avaliação, 
# classificaríamos o primeiro modelo mais alto que o segundo, embora ele não nos diga nada sobre os dados.

# Em casos como este, seria preferível usar outra métrica de avaliação como AUC.

# Plota a curva ROC baseado nas probabilidades par as previsões do modelo
def plota_Curva_ROC(y_verdadeiro, y_prob):
    
    false_positive_rate, true_positive_rate, _ = roc_curve(y_verdadeiro, y_prob)
    plt.plot(false_positive_rate, true_positive_rate)
    plt.xlabel('Taxa de Falsos Positivos')
    plt.ylabel('Taxa de Verdadeiros Positivos') 
    plt.show()

# Calcula a área sob a curva AUC para o modelo 1
print(f'Valor AUC para o modelo 1: {roc_auc_score(y, y_proba_1)}')
# Constrói o gráfico ROC para o modelo 1
plota_Curva_ROC(y, y_proba_1)

# Calcula a área sob a curva AUC para o modelo 2
print(f'Valor AUC para o modelo 2: {roc_auc_score(y, y_proba_2)}')
# Constrói o gráfico ROC para o modelo 2
plota_Curva_ROC(y, y_proba_2)

# Uma pontuação AUC de cerca de 0.5 significaria que o modelo é incapaz de fazer uma distinção entre as duas classes 
# e a curva pareceria uma linha com uma inclinação de 1. 
# 
# Uma pontuação AUC mais próxima de 1 significa que o modelo tem a capacidade de separar as duas classes e a curva 
# se aproximará do canto superior esquerdo do gráfico.





