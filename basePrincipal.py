import requests 


def pular_linha():
    print('\n')


def printDoMiguel(mensagem):
    print(mensagem)

def codigoFonte(URL):
    print(requests.get(URL).text)

def carneMoida(carne, moedorDeCarne):
    if carne == ''.strip(''):
        print('Você precisa adicionar a carne')
    else:
        print(f'a carne está moida, Carne: {carne}')