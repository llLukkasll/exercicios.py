def area(lar, comp):
    s = lar * comp
    print(f'A area de um terrono {lar}x{comp} é de {s}m2')

print('--- Controle de terrenos ---')
print('=-'*30)
c= float(input('Largura (m): '))
l= float(input('Comprimeiro (m): '))
area(l , c)


