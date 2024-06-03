# Desafio: Crie uma nova lista que contenha apenas os elementos pares de uma lista original [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Dica: Use uma compreensão de lista para filtrar os elementos.

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = []
for numero in lista_original:
    if numero % 2 == 0:
        lista_pares.append(numero)


print(f'Esta é a nova lista criada apenas com números pares da lista original: {lista_pares}')