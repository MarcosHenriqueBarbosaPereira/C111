import matplotlib.pyplot as plt
import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Northern America countries Birthrate
naCountrys = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA')][['Country', 'Birthrate', 'Deathrate']]

# Plotting Line Graph
plt.plot(naCountrys['Country'], naCountrys['Birthrate'], 'o:r', naCountrys['Country'], naCountrys['Deathrate'], 'o:b')
plt.xlabel('Country')
plt.ylabel('Rate')
plt.show()