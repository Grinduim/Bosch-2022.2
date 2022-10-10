##########################################################################################################
#
# O KNN é um algoritmo simples e supervisionado de aprendizado de máquina (ML) que pode ser usado para 
# tarefas de classificação ou regressão. É frequentemente usado na imputação de valores ausentes. 
# Baseia-se na ideia de que as observações mais próximas de um determinado ponto de dados são as observações 
# mais "semelhantes" em um conjunto de dados, e podemos, portanto, classificar pontos imprevistos com base 
# nos valores dos pontos existentes mais próximos. 
# Ao escolher K, o usuário pode selecionar o número de observações próximas a serem usadas no algoritmo.
#
#
# Neste exemplo, mostraremos como implementar o algoritmo KNN para classificação e mostraremos como diferentes 
# valores de K afetam os resultados.

# Como funciona?
# 
# K é o número de vizinhos mais próximos a serem usados. Para classificação, um voto majoritário é usado para 
# determinar em qual classe uma nova observação deve se enquadrar. Valores maiores de K geralmente são mais 
# robustos a valores discrepantes e produzem limites de decisão mais estáveis do que valores muito pequenos 
# (K=3 seria melhor que K=1, o que pode produzir resultados indesejáveis.
#
#############################################################################################################

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Criando a base de dados para análise
x = [ 1, 2,  4,   6,  8,  10,  12,  14,  16,  18,  20,  22,  24,  26,  28,   40,  42,  44,  46,  48]
y = [10, 5,  10,  8,  3,  27,  30,  28,  33,  25,  10,  13,   5,   9,   4,   25,  23,  23,  34,  29]

# Definimos previamento os tipos de classificadores (labels de etrada para o medelo)
classes = [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]

# print("\n Quantidade de elementos em x: ", len(x))
# print("\n Quantidade de elementos em y: ", len(y))
# print("\n Quantidade de elementos em classes: ", len(classes))

plt.scatter(x, y, c = classes)
plt.show()

dados = list(zip(x, y))

# Define a função com o objeto KNN passando o valore K = n_neighbors
def Preditor_KNN(K):
    knn = KNeighborsClassifier(n_neighbors = K) 
    knn.fit(dados, classes)

    # Escolhemos as coordenadas do novo elemento
    novo_x = 20
    novo_y = 25
    novo_ponto = [(novo_x, novo_y)]

    predicao = knn.predict(novo_ponto)

    plt.scatter(x + [novo_x], y + [novo_y], c = classes + [predicao[0]])
    
    plt.scatter(x*x + y*y)
    # Comando para escrever no gráfico a localização e a classificação predita pelo modelo para o novo ponto (elemento incluído)
    plt.text(x = novo_x - 2.7, y = novo_y - 1.7, s = f"Novo Ponto, Classe: {predicao[0]}")
    plt.title(f"Valor de K: {K}")
    plt.show()

# Escolhendo alguns valores de K
Preditor_KNN(K = 1)
Preditor_KNN(K = 5)
Preditor_KNN(K = 20)

