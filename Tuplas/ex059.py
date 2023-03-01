
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    digite= int(input('Digite o valor entre 0 e 20: '))
    if 0 <= digite <= 20 :
        break
    print('Digite novamente')
print(f'Voce digitou o numero {numeros[digite]}')