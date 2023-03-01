salario= float (input('Qual e o salario antigo do funcionario :'))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100)

else: 
    aumento = salario + (salario * 10 / 100)
print(' seu novo salario sera de {:.2f}' .format(aumento))