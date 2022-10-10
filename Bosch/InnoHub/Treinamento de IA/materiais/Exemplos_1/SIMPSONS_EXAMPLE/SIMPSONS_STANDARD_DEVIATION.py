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

import statistics as stat
import numpy as np


grupo_1 = (1, 8, 10, 38, 39)

grupo_2 = (8, 10, 39, 45, 49)



# Cálculo do desvios padrões populacional e amostral usando a biblioteca Numpy
def Calcula_Desvio_Padrao_Populacional_Numpy(a):
    
    Population_STD_Numpy = np.std(a)
    
    return Population_STD_Numpy

def Calcula_Desvio_Padrao_da_Amostra_Numpy(a):
    
    Sample_STD_Numpy = np.std(a, ddof = 1)
    
    return Sample_STD_Numpy


# Cálculo do desvios padrões populacional e amostral usando a biblioteca Statistics
def Calcula_Desvio_Padrao_Populacional_Stat(a):
    
    Population_STD_Stat = stat.pstdev(a)
    
    return Population_STD_Stat


def Calcula_Desvio_Padrao_da_Amostra_Stat(a):
    
    Sample_STD_Stat = stat.stdev(a)
    
    return Sample_STD_Stat


print("\n Desvio Padrão populacional para o Grupo 1 (usando a biblioteca numpy): ", Calcula_Desvio_Padrao_Populacional_Numpy(grupo_1))

print("\n Desvio Padrão populacional para o Grupo 2 (usando a biblioteca numpy): ", Calcula_Desvio_Padrao_Populacional_Numpy(grupo_2))



print("\n Desvio Padrão amostral para o Grupo 1 (usando a biblioteca numpy): ", Calcula_Desvio_Padrao_da_Amostra_Numpy(grupo_1))

print("\n Desvio Padrão amostral para o Grupo 2 (usando a biblioteca numpy): ", Calcula_Desvio_Padrao_da_Amostra_Numpy(grupo_2))



print("\n Desvio Padrão populacional para o Grupo 1 (usando a biblioteca statistics): ", Calcula_Desvio_Padrao_Populacional_Stat(grupo_1))

print("\n Desvio Padrão populacional para o Grupo 2 (usando a biblioteca statistics): ", Calcula_Desvio_Padrao_Populacional_Stat(grupo_2))



print("\n Desvio Padrão amostral para o Grupo 1 (usando a biblioteca statistics): ", Calcula_Desvio_Padrao_da_Amostra_Stat(grupo_1))

print("\n Desvio Padrão amostral para o Grupo 2 (usando a biblioteca statistics): ", Calcula_Desvio_Padrao_da_Amostra_Stat(grupo_2))

