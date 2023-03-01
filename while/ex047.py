p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma= p + s
        print('A soma dos valores foi de', soma)
    elif opcao == 2:
        mult= p * s
        print('A multiplicacao dos valores foi de', mult)
    elif opcao == 3:
        if p > s :
            maior = p
        else:
            maior = s
        print('Entre {} e {} o maior valor é {}'.format(p, s, maior))
    elif opcao == 4:
        p = int(input('Primeiro valor: '))
        s = int(input('Segundo valor: '))
    else:
        print('Finalizando...')
print('Fim do programa')