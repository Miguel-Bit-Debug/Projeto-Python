import requests 


def pular_linha():
    print('\n')


def printDoMiguel(mensagem):
    print(mensagem)

def codigoFonte(URL):
    print(requests.get(URL).text)