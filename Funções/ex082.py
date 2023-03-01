from time import sleep


def contador():
    print('Contagem de 1 até 10 de 1 em 1:')
    for c in range(1, 11):
        print(c, end=' ', flush=True)
        sleep(0.7)
    print('\nContagem de 10 até 0 de 2 em 2:')
    for c in range(10, -1, -2):
        print(c, end=' ', flush=True)
        sleep(0.7)
    print('\nAgora é sua vez:')
    início = int(input('Início:'))
    fim = int(input('Fim:'))
    passo = int(input('Passo:'))
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {início} até {fim} indo de {passo} em {passo}:')
    if início < fim:
        for c in range(início, fim+1, passo):
            print(c, end=' ', flush=True)
            sleep(0.7)
    elif início > fim:
        if passo > 0:
            for c in range(início, fim - 1, -passo):
                print(c, end=' ', flush=True)
                sleep(0.7)
    if início == fim:
        print('Não existe contagem.')
    print()
    print('-='*30)
    print('{:>30}'.format('PROGRAMA ENCERRADO!'))
contador()