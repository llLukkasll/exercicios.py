lista = []    
pares = []
impares=[]
while True:
    lista.append (int(input('Digite um valor: ')))
    continuar= str(input('Quer continuar [S/N] ? ')).upper()[0]
    if continuar in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
    
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de pares é {impares}')
