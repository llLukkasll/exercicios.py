n= s= q= 0 
while True:
    n = int (input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    s = s + n 
    q = q + 1
print(f'Foram digitados {q} numeros e a soma deles deu {s}')