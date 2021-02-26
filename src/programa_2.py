from src.extras import limpiar, pausar, convertir

nombres = ['Mario', 'Juan', 'Maria', 'Jose']
edades = [23,36,12,65]
numeros = [1847263954, 1782375019, 5687131239, 6712095482]
deportes = ['Baseball','Basquetball', 'Futball', 'Tenis']

def predefinidos():
    limpiar()
    print(f'Nombres\tEdades\tNumeros\t\tDeportes')
    for i in range(len(nombres)):
        print(f'{nombres[i]}', end='\t')
        print(f'{edades[i]}', end='\t')
        print(f'{numeros[i]}', end='\t')
        print(f'{deportes[i]}')

def pedir():
    global nombres
    global edades
    global numeros
    global deportes
    for i in range(len(nombres)):
        limpiar()
        nombres[i] = str(input(f'Ingresa el nombre de la persona {i+1}: '))
        incorrecto = True
        while incorrecto:
            aux = input(f'Ingresa la edad de la persona {i+1}: ')
            edades[i] = convertir(aux)
            if edades[i]:
                incorrecto = False
            else:
                print('Edad no valida. Intenta nuevamente')
        incorrecto = True
        while incorrecto:
            aux = input(f'Ingresa el numero de la persona {i+1}: ')
            numeros[i] = convertir(aux)
            if numeros[i]:
                incorrecto = False
            else:
                print('Numero no valido. Intenta nuevamente')
        deportes[i] = str(input(f'Ingresa el deporte de la persona {i+1}: '))
    input('Presiona Enter para mostrar')
    predefinidos()
    nombres = ['Mario', 'Juan', 'Maria', 'Jose']
    edades = [23,36,12,65]
    numeros = [1847263954, 1782375019, 5687131239, 6712095482]
    deportes = ['Baseball','Basquetball', 'Futball', 'Tenis']



def menu():
    menu = True
    while menu:
        limpiar()
        opc = input("""1.- Ingresar datos
2.- Datos predefinidos
Elige los datos: """)
        opc = convertir(opc)
        if opc == 1:
            pedir()
            menu = False
        elif opc == 2:
            predefinidos()
            menu = False
        else: 
            print('Opcion no valida. Intenta nuevamente')
            pausar()

def main():
    menu()
    pausar()