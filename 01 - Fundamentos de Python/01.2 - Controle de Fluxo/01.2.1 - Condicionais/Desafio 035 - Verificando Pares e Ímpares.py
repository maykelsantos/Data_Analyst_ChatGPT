# Desafio: Escreva um programa que peça ao usuário para inserir dois números e verifique se ambos são pares ou ímpares.
# Dica: Use o operador de módulo (%) para determinar se um número é par ou ímpar.

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

if numero_1 % 2 == 0 and numero_2 % 2 == 0:
    print('Ambos os valores digitados são PARES')
elif numero_1 % 2 != 0 and numero_2 % 2 != 0:
    print('Ambos os valores digitados são ÍMPARES')
elif numero_1 % 2 == 0 and numero_2 % 2 != 0:
    print('O primeiro valor digitado é PAR e o segundo valor digitado é ÍMPAR')
elif numero_1 % 2 != 0 and numero_2 % 2 == 0:
    print('O primeiro valor digitado é ÍMPAR e o segundo valor digitado é PAR')
else:
    print('Algo de errado não está certo!')