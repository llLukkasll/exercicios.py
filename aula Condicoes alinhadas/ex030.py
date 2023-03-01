from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento ? '))
idade= atual - nasc

if idade <= 9:
    print('Voce tem {} anos e atua na categoria MIRIM' .format(idade))

elif idade <= 14:
    print('Voce tem {} anos e atua na categoria INTANTIL' .format(idade))

elif idade <= 19:
    print('Voce tem {} anos e atua na categoria JÚNIOR' .format(idade))

elif idade <= 25:
    print('Voce tem {} anos e atua na categoria SÊNIOR' .format(idade))

else:
    idade >= 25
    print('Voce tem {} anos e atua na categoria MASTER' .format(idade))
