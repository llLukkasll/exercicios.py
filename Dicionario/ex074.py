aluno= dict()
aluno['nome']= str(input('Nome:'))
aluno['media']= float(input('Media:'))
print('=-'*20)
print(f'   - Nome igual a {aluno["nome"]}')
print(f'   - Media e igual a {aluno["media"]}')
if aluno['media'] <= 5.9:
    print(f'   -Situação é igual a Reprovado')
else:
    print(f'   - Situação e igual a Aprovado')