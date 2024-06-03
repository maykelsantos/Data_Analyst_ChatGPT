# Desafio: Remova um aluno do dicionário alunos. Dica: Use o método del alunos["nome_do_aluno"] ou alunos.pop("nome_do_aluno").

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

del alunos['Rita']

alunos.pop('Elisa')

print(alunos)