contadoridade= 0
homem = 0 
mulher = 0
while True:
    print ('Cadastre uma pessoa')
    idade = int(input('Idade: '))
    sexo =  ' '
    while sexo not in 'MF':
       sexo = str(input('Sexo: [M/F] ')).upper()[0]
    continuar= ' '
    if idade >= 18:
        contadoridade +=1
    if sexo == 'M':
        homem +=1
    if sexo == 'F' and idade < 20:
        mulher += 1

    while continuar not in 'SN':   
        continuar = str (input('Quer continuar ? ')).upper()[0]
    
    if continuar == 'N':
        break

    
print(f'Total de pessoas com mais de 18 anos: {contadoridade}') 
print(f'A o total temos {homem} homem cadastrado cadastrado')
print(f'E temos {mulher} de mulher a baixo de 20 anos ')

