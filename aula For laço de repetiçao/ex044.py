somaidade= 0
mediaidade= 0
maioridadehomem= 0
nomevelho = ' '
totmulher20= 0
for c in range(1, 5):
    print('----- {}º PESSOA -----'.format(c))
    nome = str(input('nome: '.format(c)))
    idade= int(input('Idade: '.format(c)))
    sexo = str(input('Sexo: [M/F]:'.format(c)))
    somaidade = somaidade + idade
    if c == 1 and sexo in 'mM':
        maioridadehomem =  idade
        nomevelho = nome
    if sexo in 'mM' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho= nome
    if sexo in 'fF' and idade > 20 :
        totmulher20 +=1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print(' O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('A o todo sao {} mulheres com menos de 20 anos'.format(totmulher20))


    