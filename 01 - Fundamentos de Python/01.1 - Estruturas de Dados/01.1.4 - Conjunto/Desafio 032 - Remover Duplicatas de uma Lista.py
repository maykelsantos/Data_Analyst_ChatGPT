# Descrição: Dada uma lista com valores duplicados, remova todas as duplicatas utilizando conjuntos.
# Dica: Conjuntos não permitem duplicatas, então converta a lista para um conjunto.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 5, 6, 4, 3, 5, 9, 8, 1, 2, 4, 6, 4, 6, 5, 7, 6, 4, 8, 3, 2, 4, 4, 6, 9, 10, 5, 6, 3, 7, 8, 9, 2, 1, 6, 5]
lista_sem_duplicata = set(lista)

print(lista_sem_duplicata)