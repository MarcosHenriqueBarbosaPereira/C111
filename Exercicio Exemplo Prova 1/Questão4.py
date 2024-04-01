import numpy as np

#Lendo arquivo de texto
arr = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Questão 4
regions = arr[:,1]
NAcountrys = np.char.count(regions, 'NORTHERN AMERICA').sum()
print("Países da América do Norte:",NAcountrys, "países\n")