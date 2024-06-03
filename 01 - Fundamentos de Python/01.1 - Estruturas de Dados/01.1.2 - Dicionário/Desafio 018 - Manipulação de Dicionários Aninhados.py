# Desafio: Adicione uma nova disciplina com nota para todos os alunos no dicionário turma.
# Dica: Use turma["nome_do_aluno"]["nova_disciplina"] = nova_nota.

import random 

nota = random.uniform(1,10)

turma = {
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
    turma[nome]['Historia'] = round(random.uniform(5,10),2)

print(turma)