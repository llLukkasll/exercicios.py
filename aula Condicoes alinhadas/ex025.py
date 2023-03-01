print('\033[34;1;43mAprovação de emprestimo bancario\033[m')

valor = float (input('Qual é o valor da casa R$: '))
salario = float(input('Qual é o salario do comprador: '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos))
print('A prestação sera de R${:.2f}' .format(prestacao))
if prestacao <= minimo: 
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')
