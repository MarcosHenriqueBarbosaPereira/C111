import numpy as np

#Lendo arquivo de texto
arr = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Questão 1
slicing = arr[:, 0:4]

print(f"{slicing}\n")