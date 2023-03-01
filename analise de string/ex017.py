frase= str (input('Digite uma frase: ')).upper()
print('Sua frase possui {} letras A' .format(frase.count('a')))
print('A primeira letra A apareceu na posição {}' .format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'   .format(frase.rfind('A')+1))
