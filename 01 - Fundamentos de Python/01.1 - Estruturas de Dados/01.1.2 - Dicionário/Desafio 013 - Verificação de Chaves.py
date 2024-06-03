# Desafio: Verifique se uma lista de nomes está presente no dicionário alunos. Dica: Utilize a expressão "nome_do_aluno" in alunos.

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

lista_nome = [
    'Maykel',
    'Vitoria',
    'Miguel',
    'Jaqueline',
    'Marcos',
    'Joana',
    'Maria',
    'Eloisa',
    'Elisa',
    'Rita',
    'Ana',
    'Aldo',
    'Beatriz',
    'Beto',
    'Carla',
    'Cauan',
    'Daniela',
    'Diogo',
    'Estefani',
    'Everton'
]

for nome in lista_nome:
    if nome in alunos:
        print(f'O nome {nome} CONSTA em nosso banco de dados.')
    else:
        print(f'O nome {nome} NÃO CONSTA em nosso banco de dados')