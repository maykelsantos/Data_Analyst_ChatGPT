# Desafio: Crie um dicionário chamado turma onde cada chave é o nome de um aluno e o valor é outro dicionário contendo as disciplinas e suas respectivas notas.
# Dica: Estruture seu dicionário como {"nome_do_aluno": {"disciplina1": nota1, "disciplina2": nota2}}.

import random 

nota = random.uniform(1,10)

alunos = {
    'Maykel': {
        'Portugues': round(random.uniform(5,10),2),
        'Matematica': round(random.uniform(5,10),2),
        'Biologia': round(random.uniform(5,10),2)
    },
    'Vitoria': {
        'Portugues': round(random.uniform(5,10),2),
        'Matematica': round(random.uniform(5,10),2),
        'Biologia': round(random.uniform(5,10),2)
    },
    'Miguel': {
        'Portugues': round(random.uniform(5,10),2),
        'Matematica': round(random.uniform(5,10),2),
        'Biologia': round(random.uniform(5,10),2)
    },
    'Jaqueline': {
        'Portugues': round(random.uniform(5,10),2),
        'Matematica': round(random.uniform(5,10),2),
        'Biologia': round(random.uniform(5,10),2)
    },
    'Marcos': {
        'Portugues': round(random.uniform(5,10),2),
        'Matematica': round(random.uniform(5,10),2),
        'Biologia': round(random.uniform(5,10),2)
    },
    'Joana': {
        'Portugues': round(random.uniform(5,10),2),
        'Matematica': round(random.uniform(5,10),2),
        'Biologia': round(random.uniform(5,10),2)
    },
    'Maria': {
        'Portugues': round(random.uniform(5,10),2),
        'Matematica': round(random.uniform(5,10),2),
        'Biologia': round(random.uniform(5,10),2)
    },
    'Eloisa': {
        'Portugues': round(random.uniform(5,10),2),
        'Matematica': round(random.uniform(5,10),2),
        'Biologia': round(random.uniform(5,10),2)
    },
    'Elisa': {
        'Portugues': round(random.uniform(5,10),2),
        'Matematica': round(random.uniform(5,10),2),
        'Biologia': round(random.uniform(5,10),2)
    },
    'Rita': {
        'Portugues': round(random.uniform(5,10),2),
        'Matematica': round(random.uniform(5,10),2),
        'Biologia': round(random.uniform(5,10),2)
    }
}

print(alunos)