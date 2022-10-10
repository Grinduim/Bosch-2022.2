############################################################################################################
#
#   Construção de histogramas para as densidades das massas de pastel.
#   
#   Construção de histograma de frequencia e histograma de frequencia relativa
############################################################################################################

from fractions import Fraction
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Criando o dataframe
dados = {"Mistura 1":[22.02   ,   23.83  ,   26.67  ,    25.38  ,    25.49   ,   23.50  ,    25.90   ,  24.89],
         "Mistura 2":[21.49   ,   22.67  ,    24.62 ,     24.18 ,     22.78  ,    22.56 ,     24.46  ,  23.79],
         "Mistura 3":[20.33   ,   21.67  ,    24.67 ,     22.45 ,     22.29  ,    21.95 ,     20.49  ,   21.81]
         }



#Constução do Histograma de Frequência para o dataframe das densidades das massas de pastel

# Definindo o tamanho da figura que vai conter os gráficos (histogramas)
fig_Frequency_Histogram = plt.figure(figsize=(10, 20))

Frequency_Histogram_Mistura_1 = fig_Frequency_Histogram.add_subplot(511)

Frequency_Histogram_Mistura_1.set_title("Histograma de frequência para a Mistura 1")

Frequency_Histogram_Mistura_1.hist(dados["Mistura 1"], bins = 50, color = "blue", edgecolor = "black", lw =1)


Frequency_Histogram_Mistura_2 = fig_Frequency_Histogram.add_subplot(513)

Frequency_Histogram_Mistura_2.set_title("Histograma de frequência para a Mistura 2")

Frequency_Histogram_Mistura_2.hist(dados["Mistura 2"], bins = 50, color = "blue", edgecolor = "black", lw =1)


Frequency_Histogram_Mistura_3 = fig_Frequency_Histogram.add_subplot(515)

Frequency_Histogram_Mistura_3.set_title("Histograma de frequência para a Mistura 3")

Frequency_Histogram_Mistura_3.hist(dados["Mistura 3"], bins = 50, color = "blue", edgecolor = "black", lw =1)




#Consturção dos histogramas de freqência relativa para as densidades das massas de pastel

# Definição do tamanho da figura que irá conter os histogramas de freqência relativa
fig_Relative_Frequency_Histogram = plt.figure(figsize=(10, 20))

Relative_Frequency_Histogram_Mistura_1 = fig_Relative_Frequency_Histogram.add_subplot(511)

Relative_Frequency_Histogram_Mistura_1.set_title("Histograma de Frequência Relativa para a Mistura 1")

Relative_Frequency_Histogram_Mistura_1.hist(dados["Mistura 1"], weights = np.ones_like(dados["Mistura 1"]) / len(dados["Mistura 1"]), bins = 50, color = "blue", edgecolor = "black", lw =1)


Relative_Frequency_Histogram_Mistura_2 = fig_Relative_Frequency_Histogram.add_subplot(513)

Relative_Frequency_Histogram_Mistura_2.set_title("Histograma de Frequência Relativa para a Mistura 2")

Relative_Frequency_Histogram_Mistura_2.hist(dados["Mistura 2"], weights = np.ones_like(dados["Mistura 2"]) / len(dados["Mistura 2"]), bins = 50, color = "blue", edgecolor = "black", lw =1)


Relative_Frequency_Histogram_Mistura_3 = fig_Relative_Frequency_Histogram.add_subplot(515)

Relative_Frequency_Histogram_Mistura_3.set_title("Histograma de Frequência Relativa para a Mistura 3")

Relative_Frequency_Histogram_Mistura_3.hist(dados["Mistura 3"], weights = np.ones_like(dados["Mistura 3"]) / len(dados["Mistura 3"]), bins = 50, color = "blue", edgecolor = "black", lw =1)


plt.show()