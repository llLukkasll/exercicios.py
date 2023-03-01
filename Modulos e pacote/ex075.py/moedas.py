import teste

n= float(input('Digite o valor: '))
print(f'A metade de {teste.moeda(n, "R$")} e {teste.moeda(teste.metade(n))} ')
print(f'O dobro de {teste.moeda(n)} e {teste.moeda(teste.dobro(n))}')
print(f'Aumentando 10%, temos {teste.moeda(teste.aumentar(n))}')

