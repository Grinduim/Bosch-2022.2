########################################################################################################
#
# Suponha que uma loja de roupas deseja criar um modelo de predição de lucros. 
# Para tanto, a loja pretende usar um banco de dados com informações sobre hábitos 
# de compras de 100 clientes cadastrados. Os dados de hábitos dos clientes foram 
# registrados por câmeras espalhadas na loja. Sempre que um cliente se aproxima de 
# determinado mostruário de roupas, as câmeras acionam um cronômetro que conta o tempo 
# entre o cliente escolher determinada peça de roupa e realizar o pagamento no caixa. 
# Você foi contratado para desenvolver um modelo usando aprendizado de máquina. 
# Para desenvolver o modelo a loja disponibilizou a você as seguintes informações:
# 
# Intervalo de tempo em minutos que um cliente leva para escolher um produto e efetuar o pagamento no caixa (dados preditores ou inputs);
# Valor da compra efetuada pelo cliente (dados de resposta ou output).
#
###########################################################################################################

# Importando as bibliotecas
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
np.random.seed(2)

# Variável preditora com os intervalos de tempo que 
# o cliente leva entre escolher um produto e pagar no caixa 
# gerada de maneira aleatória com 100 amostras distribuídas 
# normalmente (Gaussiana) em torno da média de 3 minutos com 
# desvio padrão igual a +1 minuto e -1 minuto
tempo = np.random.normal(3, 1, 100) 

# Valores das compras também gerados de maneira aleatória 
# com 100 amostras distribuídas  normalmente (Gaussiana)
# em torno da média de 150 reais e desvio padrão de + 40 reais 
# e - 40 reias
valor_da_compra = np.random.normal(150, 40, 100)

################################################################################################
#
#                            FASE EXPLORATÓRIA (HORA DE INVESTIGAR!)
#
################################################################################################

plt.scatter(tempo, valor_da_compra)
plt.title('Valor da Compra por Tempo (Dados Originais)')
plt.xlabel('Tempo')
plt.ylabel('valor da Compra')
plt.show()


# Após verificar o gráfico de espalhamento dos valores das compras em função do intervalo de tempo 
# gasto pelos clientes. Você nota que tudo parece muito confuso e não existe nenhuma relação entre os dados 
# ou maneira de modelar o sistema usando aprendizado de máquina!

# Então você pensa um instante....E?

# Propõe a seguinte ideia na forma de pergunta: 
# 
# E se ao invés de tentar relacionar o valor da compra diretamente com o tempo que o cliente levou 
# (entre escolher e pagar pelo produto) nós transformarmos a variável de resposta 
# (output ou variável dependente) dividindo a mesma pela variável preditora? 
# Em outras palavras, tomando como nova variável de resposta a razão entre o valor da compra e 
# o tempo gasto pelo cliente para escolher e pagar pelo produto?

# Assim a nova variável de resposta (output) é dada por:

valor_da_compra_por_tempo =  valor_da_compra / tempo

# Gerando o gráfico de espalhamento da nova variável de resposta em função do tempo

plt.scatter(tempo, valor_da_compra_por_tempo)
plt.title('(Valor da Compra / Tempo) por Tempo')
plt.xlabel('Tempo')
plt.ylabel('Valor da Compra / Tempo')
plt.show()

# A partir do novo gráfico é possível notar uma certa relação entre a nova variável resposta
# e a variável preditora, de modo que, podemos tentar ajustar alguma função usando o método de 
# aprendizado de máquina como a regressão linear.

################################################################################################
#
#                      SEPARANDO OS DADOS PARA TREINOS E TESTES
#
################################################################################################

# Então você divide aleatoriamente 70% dos dados originais para treinar o modelo
# e 30% dos dados para testa e verificar a precisão do modelo.

dados_de_treino_preditor = tempo[1:70]
dados_de_treino_resposta = valor_da_compra_por_tempo[1:70]

dados_de_teste_preditor = tempo[70:100] 
dados_de_teste_resposta = valor_da_compra_por_tempo[70:100]

# Mostrando os dados separados aleatoriamente para treinamento
plt.scatter(dados_de_treino_preditor, dados_de_treino_resposta)
plt.title('Dados de Treinamento')
plt.xlabel('Dados de Treino Preditor')
plt.ylabel('Dados de Treino Resposta')
plt.show()

# Mostrando os dados separados aleatoriamente para teste
plt.scatter(dados_de_teste_preditor, dados_de_teste_resposta)
plt.title('Dados de Teste')
plt.xlabel('Dados de Teste Preditor')
plt.ylabel('Dados de Teste Resposta')
plt.show()

################################################################################################
#
#                                       FASE DE TREINOS
#
################################################################################################


# Começando o processo de regressão linear...
# Podemos fazer a seguinte pergunta neste ponto da modelagem:

# Como o conjunto de dados analisados até agora se parece?

# Um palpite é tentar ajustar uma função polinomial, ou seja, uma regressão linear polinomial!

# Para realizar essa regressão linear polinomial podemos usar o recurso da biblioteca numpy:

modelo_1 = np.poly1d(np.polyfit(dados_de_treino_preditor, dados_de_treino_resposta, 1))
curva_1 = np.linspace(0, 6, 100)
plt.scatter(dados_de_treino_preditor, dados_de_treino_resposta)
plt.plot(curva_1, modelo_1(curva_1), color='red')
plt.title('Modelo 1 - > Ajuste com uma reta: y(x) = b1*x + b0')
plt.xlabel('dados_de_treino_preditor')
plt.ylabel('dados_de_treino_resposta')
plt.show()

modelo_2 = np.poly1d(np.polyfit(dados_de_treino_preditor, dados_de_treino_resposta, 2))
curva_2 = np.linspace(0, 6, 100)
plt.scatter(dados_de_treino_preditor, dados_de_treino_resposta)
plt.plot(curva_2, modelo_2(curva_2), color='red')
plt.title('Modelo 2 - > Ajuste com uma parábola: y(x) = b2*x^2 + b1*x + b0')
plt.xlabel('dados_de_treino_preditor')
plt.ylabel('dados_de_treino_resposta')
plt.show()

modelo_3 = np.poly1d(np.polyfit(dados_de_treino_preditor, dados_de_treino_resposta, 3))
curva_3 = np.linspace(0, 6, 100)
plt.scatter(dados_de_treino_preditor, dados_de_treino_resposta)
plt.plot(curva_3, modelo_3(curva_3), color='red')
plt.title('Modelo 3 - > Ajuste com um polinômio de grau 3: y(x) = b3*x^3 + b2*x^2 + b1*x + b0')
plt.xlabel('dados_de_treino_preditor')
plt.ylabel('dados_de_treino_resposta')
plt.show()

modelo_4 = np.poly1d(np.polyfit(dados_de_treino_preditor, dados_de_treino_resposta, 4))
curva_4 = np.linspace(0, 6, 100)
plt.scatter(dados_de_treino_preditor, dados_de_treino_resposta)
plt.plot(curva_4, modelo_4(curva_4), color='red')
plt.title('Modelo 4 - > Ajuste com um polinômio de grau 4: y(x) = b4*x^4 + b3*x^3 + b2*x^2 + b1*x + b0')
plt.xlabel('dados_de_treino_preditor')
plt.ylabel('dados_de_treino_resposta')
plt.show()

modelo_5 = np.poly1d(np.polyfit(dados_de_treino_preditor, dados_de_treino_resposta, 5))
curva_5 = np.linspace(0, 6, 100)
plt.scatter(dados_de_treino_preditor, dados_de_treino_resposta)
plt.plot(curva_5, modelo_5(curva_5), color='red')
plt.title('Modelo 5 - > Ajuste com um polinômio de grau 5: y(x) = b5*x^5 + b4*x^4 + b3*x^3 + b2*x^2 + b1*x + b0')
plt.xlabel('dados_de_treino_preditor')
plt.ylabel('dados_de_treino_resposta')
plt.show()

# Após uma análise de cada ajuste podemos destacar que, quanto maior o grau do polinômio, 
# obtemos uma curva que descreve melhor o comportamento dos dados de treino.
# Vale lembrar que sempre é possível realizar o melhor ajuste com polinômios diversos. 
# No entanto, é preciso verificar se o processo de modelagem tende ao caso de overfitting 
# (quando o modelo é super ajustado), no qual o mesmo deixa de ser preciso quando usamos os dados de testes, 
# apresentando alta variância. 

# podemos usar o parâmetro de qualidade R^2 de cada ajuste para verificar qual modelo é o melhor:

print("\n===============================================================================")
print("\n           ** R^2 OBTIDOS PARA A FASE DE TREINO  **"                            )
print("\n================================================================================")

r2_modelo_1 = r2_score(dados_de_treino_resposta, modelo_1(dados_de_treino_preditor))
print('\n R^2 modelo 1: ', r2_modelo_1)

r2_modelo_2 = r2_score(dados_de_treino_resposta, modelo_2(dados_de_treino_preditor))
print('\n R^2 modelo 2: ', r2_modelo_2)

r2_modelo_3 = r2_score(dados_de_treino_resposta, modelo_3(dados_de_treino_preditor))
print('\n R^2 modelo 3: ', r2_modelo_3)

r2_modelo_4 = r2_score(dados_de_treino_resposta, modelo_4(dados_de_treino_preditor))
print('\n R^2 modelo 4: ', r2_modelo_4)

r2_modelo_5 = r2_score(dados_de_treino_resposta, modelo_5(dados_de_treino_preditor))
print('\n R^2 modelo 5: ', r2_modelo_5)

################################################################################################
#
#                                       FASE DE TESTES
#
################################################################################################

# Depois de treinar os modelos, podemos verificar qual deles apresentará o melhor resultado 
# para os dados separados aleatoriamente para a fase de testes. Para tanto, podemo empregar
# novamente o parâmetro R^2:

modelo_1 = np.poly1d(np.polyfit(dados_de_teste_preditor, dados_de_teste_resposta, 1))
curva_1 = np.linspace(0, 6, 100)
plt.scatter(dados_de_teste_preditor, dados_de_teste_resposta)
plt.plot(curva_1, modelo_1(curva_1), color='red')
plt.title('Modelo 1 - > Ajuste com uma reta: y(x) = b1*x + b0')
plt.xlabel('dados_de_teste_preditor')
plt.ylabel('dados_de_teste_resposta')
plt.show()

modelo_2 = np.poly1d(np.polyfit(dados_de_teste_preditor, dados_de_teste_resposta, 2))
curva_2 = np.linspace(0, 6, 100)
plt.scatter(dados_de_teste_preditor, dados_de_teste_resposta)
plt.plot(curva_2, modelo_2(curva_2), color='red')
plt.title('Modelo 2 - > Ajuste com uma parábola: y(x) = b2*x^2 + b1*x + b0')
plt.xlabel('dados_de_teste_preditor')
plt.ylabel('dados_de_teste_resposta')
plt.show()

modelo_3 = np.poly1d(np.polyfit(dados_de_teste_preditor, dados_de_teste_resposta, 3))
curva_3 = np.linspace(0, 6, 100)
plt.scatter(dados_de_teste_preditor, dados_de_teste_resposta)
plt.plot(curva_3, modelo_3(curva_3), color='red')
plt.title('Modelo 3 - > Ajuste com um polinômio de grau 3: y(x) = b3*x^3 + b2*x^2 + b1*x + b0')
plt.xlabel('dados_de_teste_preditor')
plt.ylabel('dados_de_teste_resposta')
plt.show()

modelo_4 = np.poly1d(np.polyfit(dados_de_teste_preditor, dados_de_teste_resposta, 4))
curva_4 = np.linspace(0, 6, 100)
plt.scatter(dados_de_teste_preditor, dados_de_teste_resposta)
plt.plot(curva_4, modelo_4(curva_4), color='red')
plt.title('Modelo 4 - > Ajuste com um polinômio de grau 4: y(x) = b4*x^4 + b3*x^3 + b2*x^2 + b1*x + b0')
plt.xlabel('dados_de_teste_preditor')
plt.ylabel('dados_de_teste_resposta')
plt.show()

modelo_5 = np.poly1d(np.polyfit(dados_de_teste_preditor, dados_de_teste_resposta, 5))
curva_5 = np.linspace(0, 6, 100)
plt.scatter(dados_de_teste_preditor, dados_de_teste_resposta)
plt.plot(curva_5, modelo_5(curva_5), color='red')
plt.title('Modelo 5 - > Ajuste com um polinômio de grau 5: y(x) = b5*x^5 + b4*x^4 + b3*x^3 + b2*x^2 + b1*x + b0')
plt.xlabel('dados_de_teste_preditor')
plt.ylabel('dados_de_teste_resposta')
plt.show()

print("\n===============================================================================")
print("\n           ** R^2 OBTIDOS PARA A FASE DE TESTES  **"                            )
print("\n================================================================================")

r2_modelo_1 = r2_score(dados_de_teste_resposta, modelo_1(dados_de_teste_preditor))
print('\n R^2 modelo 1: ', r2_modelo_1)

r2_modelo_2 = r2_score(dados_de_teste_resposta, modelo_2(dados_de_teste_preditor))
print('\n R^2 modelo 2: ', r2_modelo_2)

r2_modelo_3 = r2_score(dados_de_teste_resposta, modelo_3(dados_de_teste_preditor))
print('\n R^2 modelo 3: ', r2_modelo_3)

r2_modelo_4 = r2_score(dados_de_teste_resposta, modelo_4(dados_de_teste_preditor))
print('\n R^2 modelo 4: ', r2_modelo_4)

r2_modelo_5 = r2_score(dados_de_teste_resposta, modelo_5(dados_de_teste_preditor))
print('\n R^2 modelo 5: ', r2_modelo_5)


################################################################################################
#
#                                   PREVENDO LUCROS
#
################################################################################################

# Supondo que escolhemos o modelo_4 para prever o valor de compras de cada cliente em função 
# do tempo que ele leva para escolher um produto ou mais e efetuar a compra, 
# podemos testar alguns valores novos que poderiam ser de interesse da loja de roupas:

# Quanto um cliente gastaria na loja se o tempo entre escolher determinado produto e pagar no caixa
# for igual a 5 minutos?


modelo_4 = np.poly1d(np.polyfit(tempo, valor_da_compra_por_tempo, 4))
curva_4 = np.linspace(0, 6, 100)
plt.scatter(tempo, valor_da_compra_por_tempo)
plt.plot(curva_4, modelo_4(curva_4), color='red')
plt.title('Modelo 4 - > Modelo Escolhido para Prever Lucros da Loja')
plt.xlabel('Tempo (min)')
plt.ylabel('(Valor da Compra / Tempo) (R$/min)')
plt.show()


print("\n Valor de compra previsto pelo modelo 4 para o intervalo de tempo de 5 minutos: ", modelo_4(5))
