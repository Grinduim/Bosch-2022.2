########################################################################################################
#
# Você quer ajudar seu colega a decidir se deve ou não ir em alguns shows de comédia do próximo mês. 
# Felizmente, ele fez várias anotações numa agenda, marcando algumas características sobre o comediante 
# que o ajudaram a decidir se ia ou não em  shows anteriores.
 
# Com base nas anotações, crie uma árvore de decisão que poderá ser usada para ajudar seu colega decidir 
# se vai ou não aos próximos shows de comédia.
########################################################################################################

# Importando as bibliotecas
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Lendo o arquivo .csv com as anotações e gerando o dataframe
df = pd.read_csv('DECISION_TREES_EXAMPLES\ARQUIVOS_CSV\REGISTRO_SHOWS_DE_COMEDIA.csv', sep = ';')

# Mostra o dataframe criado
print(df)

# Para construir uma Árvore de Decisão, precisamos transformar todos os dados qualitativos em dados quantitativos,
# ou seja, precisamos conveter os dados não numéricos para dados numéricos

# Temos que converter os dados das colunas não numéricas "Estado" e "Foi" em dados numéricos.
# Para fazer essa conversão usaremos o método map() da biblioteca pandas:

# Iremos converter(substituir):

# RJ -> 0, MG -> 1, SP -> 2
d = {'RJ': 0, 'MG': 1, 'SP': 2}
df['estado'] = df['estado'].map(d)

# S -> 1 e N -> 0
d = {'S': 1, 'N': 0}
df['foi'] = df['foi'].map(d)

# Mostra como ficou o dataframe após transformar os dados não numéricos em dados numéricos
print(df)

# Em seguida, precisamos separar as colunas das variáveis preditoras (com as características ou features) da
# coluna respota (alvo ou target)

# Idetificamos as variáveis preditoras do modelo
caracteristicas = ['idade', 'carreira', 'pontos', 'estado']

# Agrupa as variáveis preditoras em X
X = df[caracteristicas] 

# Separa a variável resposta em y
y = df['foi']

# Mostrando a separação das colunas preditoras e a coluna resposta
print(X)
print(y)

# Realiza a construção da Árvore de Decisão para o modelo
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names = caracteristicas)

plt.show()

###############################################################################################
#
#                             PREVENDO SE VAI OU NÃO EM SHOWS FUTUROS
#
###############################################################################################

Idade = 38
Carreira = 12
Pontos = 8
Estado = 1    # RJ -> 0, MG -> 1, SP -> 2


print("\n Deve ir ao show? ", dtree.predict([[Idade, Carreira, Pontos, Estado]]))
print("\n SIM -> [1]")
print("\n NÃO -> [0]")
################################################################################################
#
#                               INTEPRETAÇÃO DO RESULTADO 
#
################################################################################################

# A Árvore de Decisão usa as escolhas anteriores para calcular as próximas escolhas do seu
# colega, se ele vai ou não ao show de comédia neste caso. 
# 
# Cada nó ou bloco da Árvore de Decisão apresenta as caracteristicas ou variáveis preditoras
# com seus respectivos valores:
#
# pontos <=  10.5
# 
# Significa que todo comediante com pontos igual ou menor que 10.5 irá desviar o fluxo de análise 
# para a seta da esquerda (True), e qualquer valor de pontos acima de 10.5 irá desviar
# o fluxo de análise para a direita (False).
#  
# gini = 0.497
#
# O parâmetro "gini" está relacionado com a qualidade da análise que resultou na ramificação de determinado
# nó ou bloco da Árvore de Decisão, sendo sempre um valor entre 0.0 e 0.5. 
#
# gini = 0.0 --> Significa que todas as análises para as amostras chegaram no mesmo resultado (nenhuma ramificação é gerada) 
# 
# gini = 0.5 --> Significa que metade das amostras analisadas produz uma ramificação True/Esquerda 
# e a outra metade produz uma ramificação False/Direita
# 
# Existem muitas maneiras de dividir as amostras, usamos o método GINI neste exemplo.

# O método Gini usa esta fórmula:

# Gini = 1 - (x/n)2 - (s/n)2

# Onde x é o número de respostas positivas ("SIM"), 
# n é o número de amostras e 
# y é o número de respostas negativas ("NÃO"), 
# o que nos dá este cálculo:

# 1 - (7/13)2 - (6/13)2 = 0,497

#
# samples = 13
#
# Representa a quantidade de amostras em cada nó ou bloco da Árvore de Decisão que será analisada para gerar as ramificações posteriores
#
#
# value = [6, 7]
#
# Significa que: Das 13 amostras,
# 6 amostras(shows) resultaram em NÃO (não foi ao show)
# 7 amostras resultaram em SIM (foi ao show) 
