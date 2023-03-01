from random import randint
v = 0
while True:
    print('=-'*15)
    print('Vamos jogar par ou impar')
    print('=-'*15)
    jogador = int(input('Diga um Valor: '))
    computador = randint(0 , 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]')).upper()
    print(f'voce jogou {jogador} e a maquina {computador}')
    if tipo =='I':
        if total % 2 == 0:
            print('Voce ganhou')
            v +=1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'P':
        if total % 2 == 1:
            print('Voce ganhou')
            v +=1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Voce venceu {v} vezes.')

    
    
    



    