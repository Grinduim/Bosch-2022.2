########################################################################################################
#   
#   Determinado banco possui os dados de histórico de empréstimo, vistos na tabela abaixo. Com esse dados,
#   o banco solicitou que fosse construído um modelo que fornecendo os dados de entrada, indique se deverá
#   fornecer ou não o empréstimo
#
#########################################################################################################

# Importando as bibliotecas
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing

# Gerando o dataset
dados = {'Renda': ['Alta', 'Média', 'Média', 'Baixa', 'Baixa', 'Baixa', 'Baixa', 'Alta', 'Baixa', 'Média'], 
         'Idade': ['Jovem', 'Idoso', 'Adulto', 'Adulto', 'Adulto', 'Idoso', 'Jovem', 'Jovem', 'Jovem', 'Jovem'],
         'Valor_Empréstimo': ['Alto', 'Alto', 'Médio','Médio', 'Médio', 'Baixo', 'Alto', 'Médio', 'Baixo', 'Baixo'],
         'Emprestou': ['Sim', 'Não', 'Não', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Sim','Sim']} 

dados = pd.DataFrame(data = dados)

# Criando o LabelEncoder
renda_lbencoder = preprocessing.LabelEncoder()
idade_lbencoder = preprocessing.LabelEncoder()
valor_lbencoder = preprocessing.LabelEncoder()
emprestou_lbencoder = preprocessing.LabelEncoder()

# Usando o LabelEncoder para atribuir números às variáveis qualitativas
renda_lbencoder.fit(dados['Renda'].unique())
idade_lbencoder.fit(dados['Idade'].unique())
valor_lbencoder.fit(dados['Valor_Empréstimo'].unique())
emprestou_lbencoder.fit(dados['Emprestou'].unique())

# Transformando o dataset de variáveis qualitativas para variáveis quantitativas
dados['Renda'] = renda_lbencoder.transform(dados['Renda'])
dados['Idade'] = idade_lbencoder.transform(dados['Idade'])
dados['Valor_Empréstimo'] = valor_lbencoder.transform(dados['Valor_Empréstimo'])
dados['Emprestou'] = emprestou_lbencoder.transform(dados['Emprestou'])

# Separando o nosso dataset nos atributos previsores e na classe objetivo
previsor = dados[['Renda','Idade','Valor_Empréstimo']]
classe = dados['Emprestou']

# Criando o classificador NaiveBayes
gnb = GaussianNB()
gnb.fit(previsor, classe)

# Verificando a precisão
print("\n Precisão = ", gnb.score(previsor, classe)*100,"%")

# Inserindo novos dados para serem previstos 
previsao = {'Renda': ['Média', 'Alta'], 'Idade': ['Jovem', 'Jovem'], 'Valor_Empréstimo':['Baixo', 'Alto']}
previsao = pd.DataFrame(data = previsao)

previsao['Renda'] = renda_lbencoder.transform(previsao['Renda'])
previsao['Idade'] = idade_lbencoder.transform(previsao['Idade'])
previsao['Valor_Empréstimo'] = valor_lbencoder.transform(previsao['Valor_Empréstimo'])

# Verificando o resultado
print("\n", gnb.predict(previsao))
print("\n", emprestou_lbencoder.inverse_transform(gnb.predict(previsao)))

# Verificando as probabilidades
print("\n", gnb.predict_proba(previsao))




