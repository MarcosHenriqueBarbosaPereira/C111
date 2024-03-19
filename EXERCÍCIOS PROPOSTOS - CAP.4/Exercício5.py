import numpy as np

#Matriz
mtz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])

l, c = mtz.shape

totalElementos = l * c

if totalElementos%2 == 0:
    print('A matriz poderia se tornar um array com número par de elementos')
else:
    print('A matriz poderia se tornar um array com número ímpar de elementos')