distancia= float (input('Qual é a distancia da sua viagem ? ' ))
print('Voce esta preste a começar uma viagem de {}km'.format (distancia))
if distancia <=200 : 
    preco= distancia * 0.50
else:
    preco= distancia * 0.45
print('E o preco da sua viagem sera de R${:.2f}'.format(preco))