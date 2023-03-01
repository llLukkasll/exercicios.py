num= (  int(input('Digite o primeiro numero: ')),
        int(input('Digite o segundo numero: ')),
        int(input('O penultimo numero: ')),
        int(input('E digite o ultimo numero: ')))

print(f'Voce digitou os valores {num}')
print(f'O valor 9 foi digitado {num.count(9)}º vezes')
print(f'O valor 3 foi digitado {num.count(3)}º vezes')
for n in num :
    if n % 2 == 0:
        print(f'Os valores pares digitados foi {n}' )