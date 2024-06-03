# Desafio: Atualize a nota de todos os alunos no dicionário alunos. Dica: Para atualizar, basta usar a sintaxe alunos["nome_do_aluno"] = nova_nota.

alunos = {
    'Maykel': 8.9,
    'Vitoria': 10,
    'Miguel': 8.7,
    'Jaqueline': 9.5,
    'Marcos': 7.5,
    'Joana': 6.7,
    'Maria': 5.9,
    'Eloisa': 7.8,
    'Elisa': 6.5,
    'Rita': 9.8
}

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

novas_notas = [
    9.8,
    8.9,
    10,
    6.5,
    8.7,
    7.8,
    9.5,
    5.9,
    7.5,
    6.7
]

indice_notas = 0

for nome in nome_aluno:
    alunos[nome] = novas_notas[indice_notas]
    indice_notas = indice_notas + 1

    print(f'A nota do aluno(a) {nome} foi atualizada para {alunos[nome]}')