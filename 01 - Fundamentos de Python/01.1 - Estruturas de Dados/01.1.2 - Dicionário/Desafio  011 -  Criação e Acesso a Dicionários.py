# Desafio: Crie um dicionário chamado alunos que armazene o nome do aluno como chave e sua nota como valor. Acesse a nota de todos os alunos. Dica: Use a sintaxe alunos["nome_do_aluno"] para acessar a nota.

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

for nome in nome_aluno:
    print(f'A nota do aluno(a) {nome} é {alunos[nome]}')