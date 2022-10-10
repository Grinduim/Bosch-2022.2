############################################################################################
#
#  Determinação da mediana para as idades dos personagens dos Simpsons
# 
###########################################################################################

import pandas as pd
import numpy as np

grupo_1 = (1, 8, 10, 38, 39)

grupo_2 = (8, 10, 39, 45, 49)

def calcula_mediana(a):
    
    mediana = np.median(a)
    
    return mediana


mediana_grupo_1 = calcula_mediana(grupo_1)

mediana_grupo_2 = calcula_mediana(grupo_2)

print("Mediana para as idades do grupo 1: ", mediana_grupo_1)

print("Mediana para as idades do grupo 2: ", mediana_grupo_2)