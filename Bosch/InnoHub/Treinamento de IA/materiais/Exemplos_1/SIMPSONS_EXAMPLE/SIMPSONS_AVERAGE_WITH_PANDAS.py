############################################################################################
#
#  Cálculo do desvio padrão para as idades dos personagens dos Simpsons
# 
# Cálculo do desvio padrão populacional e amostral para as idades dos personagens dos Simpsons:

# As regras básicas para os cálculos de desvios padrão são:

# * Calculamos o desvio padrão populaconal quando o conjunto  de dados é a população inteira.

# * Consideramos o desvio padrão amostral se nossos conjuntos de dados representarem uma amostra retirada de uma grande população (como é o caso para as idades dos personagems dos Simpsons).
#
# NOTA:
# O desvio padrão amostral sempre será maior que o desvio padrão populacional para
# o mesmo conjunto de dados porque há mais incerteza ao calcular o desvio padrão da amostra,
# assim nossa estimativa do desvio padrão será maior.
###########################################################################################


import pandas as pd

dados = {'Grupo 1': [1, 8, 10, 38, 39],
         'Grupo 2': [8, 10, 39, 45, 49]}
dataframe = pd.DataFrame(data = dados)

print("\n Média: ", dataframe['Grupo 1'].mean())
print("\n Mediana: ", dataframe['Grupo 1'].median())
print("\n Moda: ", dataframe['Grupo 1'].mode())
print("\n Desvio Padrão Amostral do Grupo 1: ", dataframe['Grupo 1'].std()) 

print("\n Média: ", dataframe['Grupo 2'].mean())
print("\n Mediana: ", dataframe['Grupo 2'].median())
print("\n Moda: ", dataframe['Grupo 2'].mode())
print("\n Desvio Padrão Amostral do Grupo 2: ", dataframe['Grupo 2'].std())

