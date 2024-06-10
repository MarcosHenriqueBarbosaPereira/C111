import matplotlib.pyplot as plt
import pandas as pd

dfSpace = pd.read_csv('space.csv', delimiter=';')

# USA mission count
usaMissions = len(dfSpace[dfSpace['Location'].str.contains("USA")]['Company Name'].unique())

# China mission count
chinaMissions = len(dfSpace[dfSpace['Location'].str.contains("China")]['Company Name'].unique())

# Plotting Bar Graph
plt.bar(['USA', 'China'], [usaMissions, chinaMissions], color= 'blue')
plt.xlabel('Country')
plt.ylabel('Number of Unique Space Companies')
plt.show()
