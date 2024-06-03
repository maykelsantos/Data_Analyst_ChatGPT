# Desafio: Ordene uma lista de números em ordem crescente [3, 1, 4, 1, 5, 9, 2]. Dica: Use o método sorted() ou o método sort() da lista.

lista_numeros = [3, 1, 4, 1, 5, 9, 2]

met_sorted = sorted(lista_numeros)
print(f'Esta é a lista de número em ordem crescente utilizando o método sorted(): {met_sorted}')

lista_numeros.sort()
print(f'Esta é a lista de número em ordem crescente utilizando o método sort(): {lista_numeros}')