f=list()
g=list()
while True:
    n=str(input('Digite o nome do aluno: '))
    n1=float(input('nota 1:  '))
    n2=float(input('nota 2:  '))
    media=(n1+n2)/2 
    g.append([n,n1,n2])
    f.append([n,media])
    n3=str(input('quer continuar?  ')).strip()[0]
    while n3 not in 'SsNn':
        print('tente novamente')
        n3=str(input('quer continuar?  ')).strip()[0]
    if n3 in 'Nn' :
        break
print('numero   nome   media')
for i,j in enumerate(f):
    print('{}        {}      {}'.format(i,f[i][0],f[i][1])) 
while True:
    n4=int(input('digite o numero do aluno(digite 999 para interromper): '))
    for c, k in enumerate(g):
        if c ==n4:
            print('{} com as notas [{},{}]'.format(g[c][0],g[c][1],g[c][2]))
    if n4==999:
        print('****finalizado****')
        break