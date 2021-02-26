import os
def limpiar():
    try:
        os.system('clear')
    except:
        os.system('cls')

def pausar():
    input('Presiona Enter para continuar')

def convertir(num):
    try:
        num = int(num)
    except:
        num = False
    return num