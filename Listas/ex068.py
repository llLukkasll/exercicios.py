lista = []      
while True:
    lista.append (int(input('Digite um valor: ')))
    continuar= str(input('Quer continuar [S/N] ? ')).upper()[0]
    if continuar in 'Nn':
        break

print(f'Vode digitou {len(lista)} elementos ')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {lista}')
if 5 in lista :
    print(' O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parteda lista')


