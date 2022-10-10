###########################################################################################################
#
# Suponha que você deseja criar um modelo de classificação usando regressão logística para prever 
# se será aprovado ou reprovado em uma matéria da faculdade. 

# Os dados que você possuí são: 

# Horas de estudos semanais;
# Métodos de estudo A e B;
# Resultados das provas anteriores: se foi aprovado ou reprovado.
##########################################################################################################

# Importando as bibliotecas
import pandas as pd
import statsmodels.formula.api as smf
from sklearn import metrics 
import seaborn as sn
import matplotlib.pyplot as plt


# Criando o dataframe de treinamento
df_treino = pd.DataFrame({'resultados_das_provas': [1, 1, 0, 1, 0, 1, 0, 1, 1, 0,
                              0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                   'horas_de_estudo': [2, 4, 5, 6, 2, 3, 2, 1, 8, 6,
                            5, 8, 8, 7, 6, 7, 5, 4, 8, 9],
                   'metodos_de_estudo': ['A', 'A', 'A', 'B', 'B', 'B', 'B',
                             'B', 'B', 'A', 'B', 'A', 'B', 'B',
                             'A', 'A', 'B', 'A', 'B', 'A']})

# Imprime o dataframe apenas para conferência e depuração caso seja necessário
print(df_treino)

############################################################################################
#
#                          TREINANDO O MODELO DE REGRESSÃO LOGÍSTICA
#
############################################################################################

# A partir da função logit() da biblioteca statsmodels podemos realizar a regressão logísitica
modelo = smf.logit('resultados_das_provas ~ horas_de_estudo + metodos_de_estudo', data = df_treino)
modelo = modelo.fit()

# Apresentamos o resultado após realizar otreinamento do modelo com regressão logísitica
print("\n==========================================================================================")
print("\n   ** RESULTADOS OBTIDOS PARA O TREINAMENTO DO MODELO DE REGRESSÃO LOGÍSITICA  **"         )
print("\n==========================================================================================")
print(modelo.summary())


############################################################################################
#
#                          TESTANDO O MODELO DE REGRESSÃO LOGÍSTICA
#
############################################################################################

# Realizando o teste do modelo
print("\n==========================================================================================")
print("\n        ** RESULTADOS OBTIDOS PARA O TESTE DO MODELO DE REGRESSÃO LOGÍSITICA  **"          )
print("\n==========================================================================================")

# Criando o dataframe de teste
df_teste = pd.DataFrame({'resultados_das_provas': [1, 1, 0, 0, 1, 1, 0, 0, 1, 0],
                   'horas_de_estudo': [2, 2, 4, 4, 4, 3, 2, 2, 4, 5],
                   'metodos_de_estudo': ['A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A']})

# Identificando as varáveis independentes e dependetes
X_teste = df_teste[['horas_de_estudo', 'metodos_de_estudo']]
y_teste = df_teste['resultados_das_provas']

# Realizando o processo de predição sobre os dados de teste
y_predito = modelo.predict(X_teste)
y_predito_aprox = list(map(round, y_predito))

# Mostrando o resultado para as predições sobre os dados de teste, 
# bem como os próprios valores de teste para comparação 
print("\n Valores usados no teste do modelo: ", list(y_teste.values))
print("\n Predições feitas pelo modelo:      ", y_predito_aprox)


############################################################################################
#
#                VERIFICANDO O DESEMPENHO (QUALIDADE) DO MODELO
#
############################################################################################
# Para verificar o desempenho do modelo podemos criar uma Matriz de Confusão para verificar
# a quantidade de predições corretas e incorretas que o mesmo realizou.
# 
############################################################################################
print("\n==========================================================================================")
print("\n                         ** MATRIZ DE CONFUSÃO E ACURÁCIA  **"                             )
print("\n==========================================================================================")


Matriz_Confusao = pd.crosstab(y_predito_aprox, y_teste, rownames=['Predito'], colnames=['Real'], margins= False)

# Apresenta a Matriz de Confusão gerada
print("\n Matriz de Confusão: \n", Matriz_Confusao)

# Transformando a matriz de confusão para podermos visualizar e interpretar a mesma como um mapa de calor
sn.heatmap(Matriz_Confusao, annot = True)

#Mostrando a matriz de confusão com a bibliotecas matplotlib
plt.show()

Matriz_Confusao = metrics.confusion_matrix(y_teste, y_predito_aprox)

Sensibilidade_Recall = metrics.recall_score(y_teste, y_predito_aprox)
print("\n Sensibilidade (Recall): ", Sensibilidade_Recall)

Especificidade = metrics.recall_score(y_teste, y_predito_aprox, pos_label = 0)
print("\n Especificidade: ", Especificidade)

Acuracia = metrics.accuracy_score(y_teste, y_predito_aprox)
print("\n Acurácia: ", Acuracia)

Precisao = metrics.precision_score(y_teste, y_predito_aprox)
print("\n Precisão: ", Precisao)


F1_Score = metrics.f1_score(y_teste, y_predito_aprox)
print("\n F1-Score: ", F1_Score)


############################################################################################
#
#                          PREVISÃO PARA NOVOS VALORES DE ENTRADA
#
############################################################################################

# Realizando a previsão para novos dados
print("\n==========================================================================================")
print("\n                           ** PREVISÃO PARA NOVOS DADOS  **"                               )
print("\n==========================================================================================")

# Criando o dataframe para previsão de novos dados
x_novos_dados = pd.DataFrame({'horas_de_estudo':   [ 2,   2,   2,   3 ],
                              'metodos_de_estudo': ['B', 'A', 'B', 'A']})

# Realizando o processo de predição sobre novos dados
y_predito_novos_dados = modelo.predict(x_novos_dados)
y_predito_novos_dados_aprox = pd.DataFrame(list(map(round, y_predito_novos_dados)))


# Gera um novo conjunto de dados para ser apresentado 
# contendo as variáveis preditoras junto com os dados previstos pelo modelo
df_saida = [x_novos_dados['horas_de_estudo'], x_novos_dados['metodos_de_estudo'], y_predito_novos_dados_aprox]

nomes_colunas = ['', '', 'Aprovado?']
# Gera um novo dataset (dataframe) concatenando os dataframes x1, x2 e df['CO2']
df_apresentacao = pd.concat(df_saida, axis = 1, keys = nomes_colunas)

# Mostrando o resultado para as predições sobre novos dados
print("\n Resultado da predição para novos dados:")
print("\n", df_apresentacao)


print("\n As previsões obtidas são valores fracionários (entre 0 e 1 ou 0% e 100%)") 
print("\n que denotam a probabilidade de ser aprovado. Esses valores são, portanto,") 
print("\n arredondados, para obter os valores discretos de 1 (aprovado) ou 0 (reprovado).\n")

############################################################################################
#
#                            INTEPRETAÇÃO DOS RESULTADOS
#
############################################################################################

# Na saída, ‘Iterations‘ referem-se ao número de vezes que o modelo itera sobre os dados, 
# tentando otimizar o modelo. Neste exemplo tivemos 5 iterações. 
# Por padrão, o número máximo de iterações executadas é 35, após o qual a otimização falha.

# Os valores na coluna coef da saída nos informam a mudança média nas probabilidades logarítmicas 
# de passar no exame.

# Por exemplo:

# O uso do método de estudo B está associado a um aumento médio de 0.0875 no log das chances de passar 
# no exame em comparação ao uso do método de estudo A.
#
# Cada hora adicional estudada está associada a um aumento médio de 0.4909 nas chances de aprovação no exame.
# Os valores da coluna P>|z| representam os p-valores para cada coeficiente.

# Por exemplo:

# Os métodos de estudo possuem um valor de p de 0.934. Como esse valor não é inferior a 0.05, 
# significa que não há uma relação estatisticamente significativa entre métodos de estudo e se 
# um aluno passa ou não no exame.
# 
# As horas estudadas têm um valor de p igual a 0.045. Como esse valor é inferior a 0.05, 
# significa que há uma relação estatisticamente significativa entre horas estudadas 
# e se um aluno passa ou não no exame.

# 
# Para avaliar a qualidade do modelo de regressão logística, podemos usar a métrica de 
# desempenho na saída abaixo:

# Pseudo R-Squared:

# Esse valor pode ser considerado o substituto do valor R-quadrado para um modelo de regressão linear.
# É calculado como a razão da função log-likelihood maximizada do modelo nulo para o modelo completo.
# Esse valor pode variar de 0 a 1, com valores mais altos indicando um melhor ajuste do modelo.
# Neste exemplo, o valor pseudo R-quadrado é 0.1894, sendo um valor baixo. Isso nos diz que 
# as variáveis preditoras no modelo não fazem um trabalho muito bom de prever o valor da variável de resposta.

# Log-Likelihood : 
# 
# O logaritmo natural da função Maximum Likelihood Estimation (MLE). MLE é o processo de otimização de encontrar 
# o conjunto de parâmetros que resulta no melhor ajuste.

# LL-Null : 
# 
# O valor de log-likelihood do modelo quando nenhuma variável independente é incluída (x1, x2,...), 
# ou seja, apenas o termo beta_0 é levado em conta (só a interceptação é incluída) na equação logística.
#
#                       P(x) = 1 / (1 - e^(beta_0)) ou ln[ P(x) / ( 1 - P(x))] = beta_0
#
#
