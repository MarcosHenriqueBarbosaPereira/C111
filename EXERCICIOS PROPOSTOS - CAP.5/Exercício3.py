import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Nome e Região do país mais populoso
mostPopulousCountry = dfPaises.iloc[dfPaises['Population'].idxmax()]
print("Nome e Região do país mais populoso:", mostPopulousCountry['Country'], "- ", mostPopulousCountry['Region'], "\n")

