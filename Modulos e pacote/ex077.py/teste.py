def metade(preco=0):
    res = preco - (preco * 50/ 100)
    return res

def dobro(preco=0):
    res = ( preco * 2)
    return res


def aumentar(preco):
    res = preco + (preco * 10 / 100)
    return res

def moeda (preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}' .replace('.', ',')

def resumo (preco=0 ):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco)}')
    print(f'Metade do preco: \t{metade(preco)}')
    print(f'O almento de 10% \t{aumentar(preco)}')
    print('-'*30)
    