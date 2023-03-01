
num = 0
cont = 0
soma= 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma deles foram {} '.format(cont , soma))
