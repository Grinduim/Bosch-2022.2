################################################# #############################
#
# DETERMINAÇÃO DOS SEGUINTES VALORES:
#
# 1º QUARTIL;
# 2º QUARTIL(mediana);
# 3º QUARTIL;
# 4º QUARTIL;
# IQR;
# VALOR MÍNIMO;
# VALOR MÁXIMO;
#
################################################# #############################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


#Criando o dataframe
dados = {'Mistura 1':[22.02   ,   23.83  ,   26.67  ,    25.38  ,    25.49   ,   23.50  ,    25.90   ,  24.89],
         'Mistura 2':[21.49   ,   22.67  ,    24.62 ,     24.18 ,     22.78  ,    22.56 ,     24.46  ,  23.79],
         'Mistura 3':[20.33   ,   21.67  ,    24.67 ,     22.45 ,     22.29  ,    21.95 ,     20.49  ,   21.81]
         }




df = pd.DataFrame(data = dados)

# View dataframe
print(df)

################################################################################
# OBS:
# OS CÓDIGOS ABAIXO NÃO FUNCIONARAM COM O VSCODE (NÃO SÃO MOSTRADOS OS BOXPLOTS).
# NO ENTANTO, COM O ANACONDA SPYDER FUNCIONARAM BEM.
###############################################################################

df.boxplot(column=['Mistura 1', 'Mistura 2', 'Mistura 3'], grid = False, color = 'black')

################################################################################################

###############################################################################################
#   No entanto, os códigos abaixo usando a bib matplotlib funcionaram normalmente
#   
###############################################################################################
# boxplot for dataframe = df
boxplot = df[['Mistura 1', 'Mistura 2', 'Mistura 3']].plot(kind='box', title='boxplot')
plt.show()

# Cálculo do primeiro e terceiro quartis com numpy
q3_Numpy_Mistura1, q1_Numpy_Mistura1 = np.percentile(dados["Mistura 1"], [75, 25])

# Cálculo do intervalo interquartil (IQR) com numpy
IQR_Numpy_Mistura1 = q3_Numpy_Mistura1 - q1_Numpy_Mistura1

print("\n ========================================================================")
print("\n Os valores abaixo foram obtidos usando o numpy")
print("\n ========================================================================")

print("\n Mistura 1")
print("\n Valor máximo da Mistura 1: ", max(dados["Mistura 1"]))
print("\n Valor mínimo da Mistura 1: ", min(dados["Mistura 1"]))
print("\n Primeiro quartil (q1) da Mistura 1: ", q1_Numpy_Mistura1)
print("\n Terceiro quartil (q3) da Mistura 1: ", q3_Numpy_Mistura1)
print("\n IQR_Numpy da Mistura 1: ", IQR_Numpy_Mistura1)


# Cálculo do primeiro e terceiro quartis com numpy
q3_Numpy_Mistura2, q1_Numpy_Mistura2 = np.percentile(dados["Mistura 2"], [75, 25])

# Cálculo do intervalo interquartil (IQR) com numpy
IQR_Numpy_Mistura2 = q3_Numpy_Mistura2 - q1_Numpy_Mistura2


print("\n Mistura 2")
print("\n Valor máximo da Mistura 2: ", max(dados["Mistura 2"]))
print("\n Valor mínimo da Mistura 2: ", min(dados["Mistura 2"]))
print("\n Primeiro quartil (q1) da Mistura 2: ", q1_Numpy_Mistura2)
print("\n Terceiro quartil (q3) da Mistura 2: ", q3_Numpy_Mistura2)
print("\n IQR_Numpy da Mistura 2: ", IQR_Numpy_Mistura2)

# Cálculo do primeiro e terceiro quartis com numpy
q3_Numpy_Mistura3, q1_Numpy_Mistura3 = np.percentile(dados["Mistura 3"], [75, 25])

# Cálculo do intervalo interquartil (IQR) com numpy
IQR_Numpy_Mistura3 = q3_Numpy_Mistura3 - q1_Numpy_Mistura3


print("\n Mistura 3")
print("\n Valor máximo da Mistura 3: ", max(dados["Mistura 3"]))
print("\n Valor mínimo da Mistura 3: ", min(dados["Mistura 3"]))
print("\n Primeiro quartil (q1) da Mistura 3: ", q1_Numpy_Mistura3)
print("\n Terceiro quartil (q3) da Mistura 3: ", q3_Numpy_Mistura3)
print("\n IQR_Numpy da Mistura 3: ", IQR_Numpy_Mistura3)

###############################################################################
# OBS:Os parâmetros calculados com o numpy geralmente forneceram resultados
# diferentes em comparação com o método usado pelo site abaixo:
#   
#   view-source:https://www.statology.org/boxplot-generator/

# A seguir, usamos o mesmo método usado no site statology.org para obter os 
# parâmetros obtidos com os numpy 
##############################################################################

# Determinação do primeiro quartil (q1)  
def first_quartile(a):
    
    #Essa array é preenchida com os valores que são menores que a mediana da array de entrada
    first_half_array = [] 
    
    #Determina a mediana da array original
    median_a = np.median(a)
    
    #Preenche a first_half_array (primeira metade da array) com os valores 
    # da array orignal cujos valores são menores que a mediana da array original
    for  i in a:
        if i < median_a: 
            first_half_array.append(i)
    #Determina o primeiro quartil (aqui usamos a biblioteca numpy)          
    q1 = np.median(first_half_array)
    
    #Retorna o primeiro quartil
    return q1 


# Determinação do terceiro quartil (q3) da array passada pela variável a
def third_quartile(a):
    # Essa array é preenchida com os valores maiores que a mediana da array original passada em a
    second_half_array = [] 
    
    #Determina a mediana da array passada pela variável a
    median_a = np.median(a)
    
    # Preenche a sencon_half_array (segunda metade da array) com os valores da array original cujos
    # valores são maiores que a mediana da array original passada em a
    for  i in a:
        if i > median_a: 
            second_half_array.append(i)
    
    # Dtermina o terceiro quartil (ainda usamos o numpy nessa parte)          
    q3 = np.median(second_half_array)
    
    # Retorna o terceiro quartil
    return q3 

# Determina o intervalo interquartil (IQR)
def IQR_calc(a):
                   
    q1 = first_quartile(a)
        
    q3 = third_quartile(a)
        
    IQR = q3 - q1
        
    return IQR   

print("\n ========================================================================")
print("\n Os valores abaxio foram obtidos conforme o método usado em statology.org")
print("\n ========================================================================")

print("\n Mistura 1")
print("\n Valor máximo da Mistura 1: ", max(dados["Mistura 1"]))
print("\n Valor mínimo da Mistura 1: ", min(dados["Mistura 1"]))
print("\n Primeiro quartil (q1) da Mistura 1: ", first_quartile(dados["Mistura 1"]))
print("\n Terceiro quartil (q3) da Mistura 1: ", third_quartile(dados["Mistura 1"]))
print("\n Intervalo Interquartil (IQR) da Mistura 1: ", IQR_calc(dados["Mistura 1"]))

print("\n Mistura 2")
print("\n Valor máximo da Mistura 2: ", max(dados["Mistura 2"]))
print("\n Valor mínimo da Mistura 2: ", min(dados["Mistura 2"]))
print("\n Primeiro quartil (q1) da Mistura 2: ", first_quartile(dados["Mistura 2"]))
print("\n Terceiro quartil (q3) da Mistura 2: ", third_quartile(dados["Mistura 2"]))
print("\n Intervalo Interquartil (IQR) da Mistura 2: ", IQR_calc(dados["Mistura 2"]))

print("\n Mistura 3")
print("\n Valor máximo da Mistura 3: ", max(dados["Mistura 3"]))
print("\n Valor mínimo da Mistura 3: ", min(dados["Mistura 3"]))
print("\n Primeiro quartil (q1) da Mistura 3: ", first_quartile(dados["Mistura 3"]))
print("\n Terceiro quartil (q3) da Mistura 3: ", third_quartile(dados["Mistura 3"]))
print("\n Intervalo Interquartil (IQR) da Mistura 3: ", IQR_calc(dados["Mistura 3"]))

