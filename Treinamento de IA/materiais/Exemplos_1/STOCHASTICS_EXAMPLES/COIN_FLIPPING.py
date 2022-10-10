############################################################################################
#
# Qual a probabilidade de jogar 10 vezes uma moeda e obtermos cara em 3 jogadas ou mais? 
############################################################################################

# Importando a biblioteca usada na resolução analítica
from scipy.stats import binom

# Importando a biblioteca usada no método Monte Carlo
import numpy as np

###################################################################
#
# Resolução analítica por Distribuição Binominal
#
###################################################################
jogadas = binom(n = 10, p = 0.5)

probabilidade_calculada = 1 - jogadas.cdf(3)

print("\n Valor obtido analiticamente por Distribuição Binominal")
print("\n Propabilidade de jogar 10 vezes uma moeda e obtermos cara em mais que 3 jogadas: ", probabilidade_calculada)

##############################################################
#
# Valor obtido pelo método Monte Carlo
#
##############################################################
def realiza_jogadas():
    
    # Gera 10 valores aleatórios entre 0 e 1 (0% e 100%)
    jogadas = np.random.uniform(0, 1, 10)
    
    # Imprime o resultado de cada jogada com os 10 valores aleatórios entre 0 e 1 (0% e 100%)
    # print("\n jogadas: ", jogadas)
    
    # print("\n soma das jogadas com valores acima de 0.5 (50 %):", (jogadas > 0.5).sum())
    
    # Retorna a soma das jogadas com valores acima de 0.5 (50 %)
    return (jogadas > 0.5).sum()

N = 100

contagem = 0

for i in range(N):
    # Conta o número de jogadas cujo resultado foi maior que 3 "caras"
    if (realiza_jogadas()) > 3:
        contagem += 1
#Imprime a variável contagem
#print("\n contagem: ", contagem)
        
probabilidade_estimada = float(contagem / N)

print("\n Valor obtido estocasticamente pelo método de Monte Carlo")
print("\n Propabilidade de jogar 10 vezes uma moeda e obtermos cara em 3 jogadas ou mais:", probabilidade_estimada)
