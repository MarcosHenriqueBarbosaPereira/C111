import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Média de alfabetização do planeta
meanLiteracy = dfPaises['Literacy (%)'].mean()
print("Média de alfabetização do planeta: ", meanLiteracy.__round__(2), "%")