############################################################################################
#
#  Cálculo da média para as idades dos personagens dos Simpsons
# 
###########################################################################################

import pandas as pd
import numpy as np

grupo_1 = (1, 8, 10, 38, 39)

grupo_2 = (8, 10, 39, 45, 49)

media_idade_grupo_1 = np.mean(grupo_1)

media_idade_grupo_2 = np.mean(grupo_2)


print ("\n Média para as idades do grupo 1 = ", media_idade_grupo_1)

print ("\n Média para as idades do grupo 2 = ", media_idade_grupo_2)

