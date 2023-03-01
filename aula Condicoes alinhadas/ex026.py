num= int (input(' Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] conversao para BINARIO
[2] conversao para OCTAL
[3] conversao para HEXADECIMAL''')
opçao =int (input('Sua opçao: '))
if opçao == 1:
    print('{} Convertido para Binario e igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} Convertido para Octal e igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} Convertido para Hexadecimal e igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opcao invalida tente novamente')