print('{:=^100}'.format('Loja do Zé'))
preço = float (input('Preço das compras: '))
print(''' 
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opção = int (input ('Qual opção voce deseja ? ')) 

if opção == 1:
    descontodez= preço - (preço * 10 / 100) 
    print('O valor sera de {}R$ com o desconto de 10%'.format(descontodez))
elif opção == 2:
    descontocinco= preço - (preço * 5 / 100)
    print('O valor sera de {}R$ com o desconto de 5%'.format(descontocinco))
elif opção == 3:
    print('O valor sera de {}'.format(preço))
elif opção == 4:
    parcelas= int(input('Quantas parcelas? '))
    juros= preço + (preço * 20 / 100)
    parceladiv= juros / parcelas
    print('Voce pagara {}x de {}R$ o valor final sera de {} com 20% de juros'.format(parcelas, parceladiv, juros))
else:
    total = 0 
    print('Opcao invalida de pagamento. TENTE')





