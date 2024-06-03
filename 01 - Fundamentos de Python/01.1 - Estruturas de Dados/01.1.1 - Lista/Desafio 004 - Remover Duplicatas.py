# Desafio: Remova os elementos duplicados de uma lista [1, 2, 2, 3, 4, 4, 5]. Dica: Converta a lista para um conjunto (set) e depois volte para lista.

lista_numeros = [1, 2, 2, 3, 4, 4, 5]
duplicata_removida = set(lista_numeros)

print(f'Esta é a lista de números após a remoção das duplicatas {duplicata_removida}')