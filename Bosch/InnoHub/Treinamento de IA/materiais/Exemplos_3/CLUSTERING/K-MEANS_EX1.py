##########################################################################################################
#
# Neste exemplo estudaremos o método de agrupamento (clustering) conhecido por K-means, que nada mais
# é que um método de aprendizado de máquina não supervisionado. O algoritmo divide os dados de maneira
# iterativa em grupos K. A cada iteração o algoritmo tenta reduzir a variância em cada grupo.
# 
# K representa a quandtidade de agrupamentos ou clusters que foi escolhido ou obtido pelo algoritmo.
# 
# Uma maneira de determinar o melhor valor de K é através da curva do cotovelo do inglês Elbow-Curve
##########################################################################################################

# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Criando a base de dados para análise
x = [ 1, 2,  4,   6,  8,  10,  12,  14,  16,  18,  20,  22,  24,  26,  28,   40,  42,  44,  46,  48]
y = [10, 5,  10,  8,  3,  27,  30,  28,  33,  25,  10,  13,   5,   9,   4,   25,  23,  23,  34,  29]

# print("\n Quantidade de elementos em x: ", len(x))
# print("\n Quantidade de elementos em y: ", len(y))
##########################################################################################################
#
#                                   VISUALIZAÇÃO DOS DADOS
#
##########################################################################################################
plt.scatter(x,y)
plt.show()

# Transformando os dados originais em um dataframe
# data = list(zip(x,y)) # Outra forma de criar um dataframe sem o Pandas
data = pd.DataFrame(x, y)


# Para encontrar o melhor valor para K, precisamos executar K-means em nossos dados para um intervalo 
# de valores possíveis. Temos 20 pontos de dados, então o número máximo de clusters é 20. 
# Assim, para cada valor K em range(1,20), treinamos um modelo K-means e plotamos a 
# intertia ("soma dos espalhamentos ou variância de cada cluster") em cada iteração:
espalhamento_clusters = []

for i in range(1, len(data)):
     kmeans = KMeans(n_clusters = i)       
     kmeans.fit(data)
     espalhamento_clusters.append(round(kmeans.inertia_))

# print(espalhamento_clusters)

plt.plot(range(1, len(data)), espalhamento_clusters, marker = 'o')
plt.title("Elbow Plot -> Curva do Cotovelo", fontsize = 14)
plt.xlabel("Número de Clusters -> K")
plt.ylabel("Espalhamento Total dos Clusters")
plt.show()

# Através do Elbow Plot podemos concluir que o ponto de inflexão da curva ocorre quando o número de clusters
# é igual a 4. 
# 
# Logo, K = 4 é a melhor opção para a quantidade de clusters com os dados que temos!

def Plota_Clusters(K):
     
     kmeans = KMeans(n_clusters = K)
     kmeans.fit(data)
     plt.scatter(x, y, c = kmeans.labels_)
     plt.title(f"Valor de K: {K}")
     plt.show()

Plota_Clusters(K = 2)
Plota_Clusters(K = 3)
Plota_Clusters(K = 4)
Plota_Clusters(K = 5)


