lista = []      

while True:
    n= int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    continuar= str(input('Quer continuar [S/N] ? ')).upper()

    if continuar in 'Nn':
        break
lista.sort()
print(f'Voce digitou os valores {lista}')
