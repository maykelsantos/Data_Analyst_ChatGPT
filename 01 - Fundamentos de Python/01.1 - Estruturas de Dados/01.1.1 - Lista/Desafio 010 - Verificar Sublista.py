# Desafio: Verifique se uma lista é uma sublista de outra lista. Dica: Use operações de fatiamento (slicing) e comparação para verificar a presença da sublista.

def is_sublist(lista_principal, sublista):
    len_principal = len(lista_principal)
    len_sublista = len(sublista)
    
    for i in range(len_principal - len_sublista + 1):
        if lista_principal[i:i + len_sublista] == sublista:
            return True
            
    return False

lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 3]
lista3 = [1, 7]

teste1 = is_sublist(lista1, lista2)
if teste1 == True:
    print('A lista 2 é sublista da lista 1')
else:
    print('A lista 2 não é sublista da lista1')

teste2 = is_sublist(lista1, lista3)
if teste2 == True:
    print('A lista 3 é uma sublista da lista 1')
else:
    print('A lista 3 não é uma sublista da lista 1')
