def ficha(nome='<desconhecido>', gols=''):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = input('Nome do Jogador: ')
g = input('Número de Gols: ')
ficha(n, g)