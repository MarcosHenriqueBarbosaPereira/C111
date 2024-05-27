import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Paises sem costa marítima
landlockedCountrys = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]
landlockedCountrys.to_csv('paisesSemCostaMaritima.csv', sep=';', index=False)