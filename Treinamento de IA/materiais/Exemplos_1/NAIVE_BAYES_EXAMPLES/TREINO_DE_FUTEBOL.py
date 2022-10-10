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
dados = {'Tempo': ['Ensolarado', 'Ensolarado', 'Nublado', 'Chuvoso', 'Chuvoso', 'Chuvoso', 
                   'Nublado', 'Ensolarado', 'Ensolarado', 'Chuvoso'], 
         'Umidade': ['Alta', 'Alta', 'Alta', 'Alta', 'Normal', 'Normal', 'Normal', 'Alta', 
                     'Normal', 'Normal'],
         'Vento': ['Fraco', 'Forte', 'Fraco','Fraco', 'Fraco', 'Forte', 'Forte', 'Fraco', 'Fraco', 'Fraco'],
         'Treinou': ['Não', 'Não', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim','Sim']} 

dados = pd.DataFrame(data = dados)

# Criando o LabelEncoder
tempo_lbencoder = preprocessing.LabelEncoder()
umidade_lbencoder = preprocessing.LabelEncoder()
vento_lbencoder = preprocessing.LabelEncoder()
treinou_lbencoder = preprocessing.LabelEncoder()

# Usando o LabelEncoder para atribuir números às variáveis qualitativas
tempo_lbencoder.fit(dados['Tempo'].unique())
umidade_lbencoder.fit(dados['Umidade'].unique())
vento_lbencoder.fit(dados['Vento'].unique())
treinou_lbencoder.fit(dados['Treinou'].unique())

# Transformando o dataset de variáveis qualitativas para variáveis quantitativas
dados['Tempo'] = tempo_lbencoder.transform(dados['Tempo'])
dados['Umidade'] = umidade_lbencoder.transform(dados['Umidade'])
dados['Vento'] = vento_lbencoder.transform(dados['Vento'])
dados['Treinou'] = treinou_lbencoder.transform(dados['Treinou'])

# Separando o nosso dataset nos atributos previsores e na classe objetivo
previsor = dados[['Tempo','Umidade','Vento']]
classe = dados['Treinou']

# Criando o classificador NaiveBayes
gnb = GaussianNB()
gnb.fit(previsor, classe)

# Verificando a precisão
print("\n Precisão = ", gnb.score(previsor, classe)*100,"%")

# Inserindo novos dados para serem previstos 
previsao = {'Tempo': ['Ensolarado', 'Nublado', 'Nublado','Chuvoso'], 
            'Umidade': ['Normal', 'Alta','Normal','Alta'], 
            'Vento':['Forte', 'Forte', 'Fraco', 'Forte']}

previsao = pd.DataFrame(data = previsao)

previsao['Tempo'] = tempo_lbencoder.transform(previsao['Tempo'])
previsao['Umidade'] = umidade_lbencoder.transform(previsao['Umidade'])
previsao['Vento'] = vento_lbencoder.transform(previsao['Vento'])

# Verificando o resultado
print("\n", gnb.predict(previsao))
print("\n", treinou_lbencoder.inverse_transform(gnb.predict(previsao)))

# Verificando as probabilidades
print("\n", gnb.predict_proba(previsao))




