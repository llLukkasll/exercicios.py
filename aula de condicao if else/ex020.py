carro= float (input('Qual a velocidade do carro ?'))

if carro <= 80:
    print('voce esta dentro da velocidade')
else:
    multa = (carro-80) * 7
    print("Voce ultrapassou 80km/h voce foi multado no valor de {:.2f}." .format(multa))
    
