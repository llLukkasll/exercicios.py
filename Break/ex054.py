
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('=-'*20)
    if n <= 0:
      break 
    for x in range (1,11):
        print(f'{n} x {x} = {n*x} ')
    print('=-'*20)
print('Programa de tabuada encerrado. ')


