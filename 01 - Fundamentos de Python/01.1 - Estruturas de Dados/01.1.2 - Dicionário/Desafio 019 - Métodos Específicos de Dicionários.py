# Desafio: Utilize o método get para acessar a nota de uma disciplina específica para um aluno, retornando "Não Encontrado" se a disciplina não existir.
# Dica: Use turma["nome_do_aluno"].get("disciplina", "Não Encontrado").

import random

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
    print(f'A nota do aluno(a) {nome} em Português é: {turma[nome].get('Portugues', 'Não Encontrado')}')
    print(f'A nota do aluno(a) {nome} em Matemática é: {turma[nome].get('Matematica', 'Não Encontrado')}')
    print(f'A nota do aluno(a) {nome} em Biologia é: {turma[nome].get('Biologia', 'Não Encontrado')}')
    print(f'A nota do aluno(a) {nome} em História é: {turma[nome].get('Historia', 'Não Encontrado')}')


    