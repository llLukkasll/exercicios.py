resp = "S"
soma = 0
quantosforam= 0 
media= 0
maior = 0
menor = 0
while resp in 'Ss':
    n1 = int(input('Digite um numero: '))
    resp= str(input('Quer continuar ? [S/N] ')).upper()
    soma = soma + n1
    quantosforam +=1
    media = soma / quantosforam
    if quantosforam == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

print('Voce digitou {} numeros é a media deles foram {}'.format(quantosforam, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

