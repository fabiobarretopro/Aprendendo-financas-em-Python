import numpy

# Criando uma matriz 4x4 ou (4, 4)
x = (numpy.array([[0, 1, 2, 3], [4, 5, 6, 7]]))
print(x)

"""
RESULTADO: [[0 1 2 3]
            [4 5 6 7]]
"""

# Mostra o número de linhas e colunas da matriz.
print(x.shape)
"""
2 linhas e 4 colunas.

RESULTADO: (2, 4)
"""

#Coloca um número na posição dada.

x[1, 3] = 20
print(x)

"""
Irá colocar o "20" na 1º linha e 3ª coluna.

RESULTADO: [[ 0  1  2  3]
            [ 4  5  6 20]] 
"""