import random
from time import sleep
numero= random.randint(0, 5)
acerto= int (input('Descubra o numero escolhido pelo computador de 0 a 5: '))
print('Processando...')
sleep(2)
if acerto <= numero:
    print('voce acertou')
else:
    print('voce errou')
    print('O numero era {} a maquina ganhou'.format(numero))
print('--Fim--')
