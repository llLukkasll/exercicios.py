n1 = float (input('Digite a sua primeira nota: '))
n2 = float (input('Digite a sua segunda nota: '))
nota = (n1 + n2) / 2
print('sua nota e {}'.format(nota))
if nota <= 5.0:
    print('Média abaixo de 5.0: REPROVADO')
elif nota < 6.9:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO')
else:
    nota > 7.0
    print('Média 7.0 ou superior: APROVADO')