# Descrição: Crie dois conjuntos e encontre a interseção deles.
# Dica: Use o método intersection() ou o operador &.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersecao1 = set1.intersection(set2)
intersecao2 = set1 & set2

print(f'Este é o resultado da interseção 01: {intersecao1}')
print(f'Este é o resultado da interseção 02: {intersecao2}')