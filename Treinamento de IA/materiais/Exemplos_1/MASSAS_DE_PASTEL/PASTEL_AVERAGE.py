#######################################################################################################################################

# Cálculo da Média Aritmética para as densidades das massas de pastel:

#######################################################################################################################################

import numpy as np

#Criando o dataframe
dados = {"Mistura 1":[22.02   ,   23.83  ,   26.67  ,    25.38  ,    25.49   ,   23.50  ,    25.90   ,  24.89],
         "Mistura 2":[21.49   ,   22.67  ,    24.62 ,     24.18 ,     22.78  ,    22.56 ,     24.46  ,  23.79],
         "Mistura 3":[20.33   ,   21.67  ,    24.67 ,     22.45 ,     22.29  ,    21.95 ,     20.49  ,   21.81]
         }



print ("\n Densidade média para a Mistura 1: ", np.mean(dados["Mistura 1"]))
print ("\n Densidade média para a Mistura 2: ", np.mean(dados["Mistura 2"]))
print ("\n Densidade média para a Mistura 2: ", np.mean(dados["Mistura 3"]))









