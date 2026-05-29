import os

def listar_arquivosDiretorio():
    itens = os.listdir('.')
    for i in itens:
        print(itens)

listar_arquivosDiretorio()