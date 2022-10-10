#############################################################################################################
#
# AGREGAÇÃO DE BOOTSTRAP (BAGGING / ACONDIONAMENTO)
#
# Bootstrap Aggregating (Bagging) é um método de agrupamento (ensemble) geralmente usado para 
# otimizar modelos de aprendizado de máquina e contornar efeitos de overfitting para problemas 
# de classificação ou regressão. 
# 
# O Bagging visa melhorar a precisão e o desempenho dos algoritmos de aprendizado de máquina. 
# Ele faz isso pegando subconjuntos aleatórios de um conjunto de dados original, com substituição, 
# e ajusta um classificador (para classificação) ou regressor (para regressão) a cada subconjunto. 
# As previsões para cada subconjunto são então agregadas por meio de votação majoritária para 
# classificação ou média para regressão, aumentando a precisão do modelo.
#
# Procuraremos identificar diferentes classes de vinhos encontradas no conjunto de dados de vinhos 
# da Sklearn.
#
###############################################################################################################

# Importando as bibliotecas
import random
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Em seguida, precisamos carregar os dados e armazená-los em X (características de entrada) e y (saída ou resposta). 
# O parâmetro as_frame é escolhido como True para não perdermos os nomes dos recursos ao carregar os dados. 
# (a versão do sklearn anterior a 0.23 deve ignorar o argumento as_frame, pois não é suportado)

dados = datasets.load_wine(as_frame = True)

# print(dados)

X = dados.data
# print(X)

y = dados.target
# print(y)

# Para avaliar adequadamente nosso modelo em dados não vistos, precisamos dividir X e y em conjuntos de treinamento e teste.

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.25, random_state = 22)

# Com nossos dados preparados, agora podemos instanciar um classificador base e ajustá-lo aos dados de treinamento.
dtree = DecisionTreeClassifier(random_state = 22)
dtree.fit(X_treino, y_treino)


# Agora podemos prever a classe de vinho do conjunto de teste não visto e avaliar o desempenho do modelo.
y_predito = dtree.predict(X_teste)

print("\n Acurácia obtida com os dados de treinamento: ", accuracy_score(y_true = y_treino, y_pred = dtree.predict(X_treino)))
print("\n Acurácia obtida com os dados de teste: ", accuracy_score(y_true = y_teste, y_pred = y_predito))

# O classificador base funciona razoavelmente bem no conjunto de dados, alcançando 82% de precisão no conjunto de dados de teste 
# com os parâmetros atuais (resultados diferentes podem ocorrer se você não tiver o conjunto de parâmetros random_state).

# Agora que temos uma precisão de linha de base para o conjunto de dados de teste, podemos ver como o Bagging Classifier 
# executa um único classificador de árvore de decisão.

############################################################################################
#
#                           CRIANDO UM CLASSIFICADOR BAGGING
#
############################################################################################

# Para o bagging, precisamos definir o parâmetro n_estimators, este é o número de classificadores base que nosso modelo vai agregar.
# Para este conjunto de dados o número de estimadores é relativamente baixo, geralmente se usa intervalos muito maiores 
# O ajuste de hiperparâmetros geralmente é feito com uma pesquisa em grade, mas por enquanto usaremos um conjunto selecionado de 
# valores para o número de estimadores.

# Começamos importando o modelo necessário:
from sklearn.ensemble import BaggingClassifier
 
# Agora vamos criar um intervalo de valores que representam o número de estimadores que queremos usar 
# em cada ensemble.

intervalo_estimador = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
 
# Para ver como o classificado Bagging funciona com diferentes valores de estimadores, precisamos de uma maneira de iterar 
# sobre o intervalo de valores e armazenar os resultados de cada ensemble. Para fazer isso, criaremos um loop for, 
# armazenando os modelos e as pontuações em listas separadas para visualizações posteriores.

# Nota: O parâmetro padrão para o classificador base no BaggingClassifier é o DicisionTreeClassifier, 
# portanto, não precisamos defini-lo ao instanciar o modelo de Bagging.

modelos =[]
pontos = []

for n_estimators in intervalo_estimador:
    
    # Criação do classificador de Bagging
    clf = BaggingClassifier(n_estimators = n_estimators, random_state = 22)
    
    # Realizando o ajuste
    clf.fit(X_treino, y_treino)
    
    # Registra o número do modelo testado e a respectiva pontuação do mesmo
    modelos.append(clf)
    pontos.append(accuracy_score(y_true = y_teste, y_pred = clf.predict(X_teste)))
    
# Com os modelos e pontuações armazenados, agora podemos visualizar a melhoria no desempenho do modelo.
    
# Construção do gráfico das pontuações em função do número de estimadores
plt.figure(figsize=(9, 6))
plt.plot(intervalo_estimador, pontos)
plt.xlabel("Número do estimador", fontsize = 18)
plt.ylabel("Pontuação", fontsize = 18)
plt.tick_params(labelsize = 16)
plt.show()

# Interpretação dos Resultados

# Ao iterar através de diferentes valores para o número de estimadores, podemos ver um aumento no desempenho do modelo de 
# 82% para 95%. Após 15 estimadores, a precisão começa a cair novamente, se você definir um random_state diferente, 
# observará valores diferentes. É por isso que é uma boa prática usar a validação cruzada para garantir resultados estáveis.

# Neste caso, vemos um aumento de 13% na precisão para a identificação do tipo de vinho.

#############################################################################################################
#
#                   GERANDO ÁRVORES DE DECISÃO A PARTIR DO CLASSIFICADOR BAGGING
#
#############################################################################################################

# É possível ver as árvores de decisão individuais que entraram no classificador agregado. 
# Isso nos ajuda a obter uma compreensão mais intuitiva de como o modelo de bagging chega aos resultados.

# OBS: Isso só é funcional com conjuntos de dados menores, onde as árvores são relativamente pequenas, 
# facilitando a visualização.

# for i in intervalo_estimador:
#     clf = BaggingClassifier(n_estimators = i, oob_score = True, random_state = 22)

#     clf.fit(X_treino, y_treino)

#     plt.figure(figsize = (10, 10))

#     plot_tree(clf.estimators_[0], feature_names = X.columns)

#     plt.show()


clf = BaggingClassifier(n_estimators = 13, oob_score = True, random_state = 22)

clf.fit(X_treino, y_treino)

plt.figure(figsize = (10, 10))

plot_tree(clf.estimators_[0], feature_names = X.columns)

plt.show()

# Podemos ver as árvores de decisão que foram geradas no modelo. 
# Alterando o índice do classificador.