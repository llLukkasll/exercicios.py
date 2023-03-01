sexo= str(input('Digite seu sexo : [M/F]')).upper()
while sexo not in 'mMFf':
    sexo= str(input('Digite seu sexo valido: '))
print('Sexo {} registrado com sucesso. '.format(sexo)) 