import numpy as np

#Lendo arquivo de texto
arr = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Questão 5
latinAndCaribbean = arr[arr[:,1] == 'LATIN AMER. & CARIB    ']
highestGDP = latinAndCaribbean[latinAndCaribbean[:, 8].astype(float).argmax()]
print(f"País com maior GDP da América Latina e Caribe: {highestGDP[0]} com PIB de {highestGDP[8]} dólares per capita\n")