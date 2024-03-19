import numpy as np

#Array de 0 até 50 de pares
arr1 = np.arange(0,51,2)

#Array de 100 até 50 de pares
arr2 = np.arange(100,50,-2)

#Concatenando e ordenando os arrays
arr3 = np.concatenate([arr1, arr2])
arr3.sort()

#Invertendo o array ordenado
arrDecreasing = np.flip(arr3)
print(arrDecreasing)