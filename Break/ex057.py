total=0
mais=0
menor= 0
cont=0
barato=' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Valor do produto: '))
    total += preço
    cont +=1
    if preço > 1000:
        mais += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto  
    
    cont= ' '
    while cont not in 'SN':   
        cont = str (input('Quer continuar ? ')).upper()[0]
    if cont == 'N':
        break

print(f'O total da compra foi de {total}')
print(f'O total de produtos maior de 1000 foi de {mais}')
print(f'O produto mais barato foi {barato} que custa R${menor}')