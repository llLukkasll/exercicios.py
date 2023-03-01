from datetime import date
atual= date.today().year
totmaior = 0
totmenos= 0
for c in range (1, 8): 
    anos = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = atual - anos
    if anos <= 21:
        totmaior = totmaior + 1
    else:
        totmenos = totmenos + 1
print('A o todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E tivemos {} menor de idade.'.format(totmenos))
