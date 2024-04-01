import numpy as np

#Lendo arquivo de texto
arr = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Questão 2
regions = np.unique(arr[:, 1])


print("Quantidade de regiões:", regions.size)
print("Regiões:\n", regions, "\n")