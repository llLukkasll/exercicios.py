from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento ? '))
idade= atual - nasc
print('''
[1] Masculino
[2] Feminino''')
opçao =int (input('Qual e o seu sexo: '))
print('Quem nasceu em {} tem {} em {}'.format(nasc, idade, atual))


if opçao == 1:
    idade == 18 
    print('Você deve se alistar imediamente')
elif opçao == 1:
    idade < 18
    saldo = idade - 18
    print('Voce ainda nao tem 18 anos. ainda faltam {} anos para o alistamento' .format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}' .format(ano))

elif opçao == 1:
    idade > 18 
    saldo = idade - 18    
    print('Voce ja deveria ter se alistado a {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}' .format(ano))
else:
    opçao == 2
    print('Voce esta nao e obrigada a se alistar')

