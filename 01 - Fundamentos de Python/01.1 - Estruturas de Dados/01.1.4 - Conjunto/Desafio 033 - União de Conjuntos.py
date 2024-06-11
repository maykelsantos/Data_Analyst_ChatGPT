# Descrição: Crie dois conjuntos e encontre a união deles.
# Dica: Use o método union() ou o operador |.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

uniao1 = set1.union(set2)
uniao2 = set2 | set1

print(f'Este é o resultado da união 01: {uniao1}')
print(f'Este é o resultado do união 02: {uniao2}')