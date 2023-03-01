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
