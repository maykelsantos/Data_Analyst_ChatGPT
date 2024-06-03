# Desafio: Calcule o produto de todos os elementos de uma lista [1, 2, 3, 4]. Dica: Use a função reduce() da biblioteca functools.
from functools import reduce

lista_numeros = [1, 2, 3, 4]

def multiplicar(x, y):
    return x * y

produto = reduce(multiplicar, lista_numeros)

print(produto)