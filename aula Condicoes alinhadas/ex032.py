peso= float(input('Digite seu peso (KG): '))
altura= float (input('Digite sua altura (M): '))
imc= peso / (altura ** 2)
print('seu IMC e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Voce esta no Peso Ideal')
elif 25 <= imc < 30:
    print('VOce esta em Sobrepeso')
elif 30 <= imc < 40:
    print('Voce esta em Obesidade')
else: 
     imc >= 40
     print('Obesidade Morbida')