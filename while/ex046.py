from random import randint
computador = randint(0,10)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar qual!')
num = int(input('Digite seu palpite: '))
tent = 0

while num != computador:
    num = int(input('Errou! Tente novamente: '))
    tent = tent + 1
    if num < computador:
        print('mais... tente dnv')
    else:
        if num > computador:
            print('Menos... tente dnv')
print('Acertou! Número de tentativas: {}.'.format(tent))