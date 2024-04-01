import numpy as np

#Lendo arquivo de texto
arr = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Questão 3
literacy_rate = arr[:, 9].astype(float)

average = np.mean(literacy_rate)

print(f"Taxa média de alfabetização: {average:.2f}%\n")