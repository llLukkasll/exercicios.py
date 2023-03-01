import urllib   
import urllib.request

try:
    site= urllib.request.urlopen ('https://www.youtube.com/')
except:
    print('O site nao esta acessivel no momento')
else:
    print('Consegui acessar o site com sucesso')
