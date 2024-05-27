import pandas as pd
import numpy as np

dfPaises = pd.read_csv('paises.csv', delimiter=';')

# a) Quais os países da Oceania
oceaniaCountrys = dfPaises[dfPaises['Region'].str.contains('OCEANIA')]
print(oceaniaCountrys['Country'], "\n")

# b) Quantos países são da Oceania
oceaniaCountrysCount = oceaniaCountrys.count()
print(oceaniaCountrysCount['Country'], "países são da Oceania")