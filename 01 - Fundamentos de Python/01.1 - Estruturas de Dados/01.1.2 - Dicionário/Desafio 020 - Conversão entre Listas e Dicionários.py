# Desafio: Converta duas listas, uma de nomes de alunos e outra de notas, em um dicionário.
# Dica: Combine as listas usando a função zip e converta para um dicionário com dict.

import random

nome_aluno = [
    'Maykel',
    'Vitoria',
    'Miguel',
    'Jaqueline',
    'Marcos',
    'Joana',
    'Maria',
    'Eloisa',
    'Elisa',
    'Rita'
]

nota_aluno = [
    round(random.uniform(5,10),2),
    round(random.uniform(5,10),2),
    round(random.uniform(5,10),2),
    round(random.uniform(5,10),2),
    round(random.uniform(5,10),2),
    round(random.uniform(5,10),2),
    round(random.uniform(5,10),2),
    round(random.uniform(5,10),2),
    round(random.uniform(5,10),2),
    round(random.uniform(5,10),2)
]

dicionario = dict(zip(nome_aluno, nota_aluno))

print(dicionario)