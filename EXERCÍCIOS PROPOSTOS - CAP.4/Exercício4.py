import numpy as np

mtzOnes = np.ones(12).reshape(3, 4)

#transformando a matriz em um array de 1 dimensão utilizando reshape
arrOnes = mtzOnes.reshape(12)
print(arrOnes)