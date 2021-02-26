# Garcia Rodriguez Erick Israel ------ Practica 0
import time
import os
from src.extras import limpiar, pausar, convertir
from src.programa_1 import mostrarNumeros as programa1
from src.programa_2 import main as programa2
from src.programa_3 import main as programa3
#Asunto: Practica 0, Grupo "4CV24"
#Programa 1: Z del zorro 
"""
1 2 3 4
- - 5
- 6
7 8 9 0
"""

#Programa 2: 5 datos de 5 personas
#   Nombre edad telefono deporte

#Programa 3: Sumar matrices, multiplicar matrices->Validar Antes si se puede, Inversa de matriz
#   Usuario insertar operaciones,
#   Matrices minimo de 3x3
#   Mostrar matrices

def menu():
    menu = True
    while menu:
        limpiar()
        opc = input("""1.- Z de Zorro
2.- Datos de personas
3.- Matrices
4.- Salir
Elige una opcion: """)
        opc = convertir(opc)
        if opc == 1:
            programa1()
        elif opc == 2:
            programa2()
        elif opc == 3:
            programa3()
        elif opc == 4:
            print('Adios. Vuelve pronto')
            time.sleep(.5)
            menu = False
        else:
            print('Opcion Incorrecta intenta nuevamente')
            pausar()


def main():
    menu()
if __name__ == "__main__":
    main()
    limpiar()