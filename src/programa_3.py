from io import SEEK_END
from src.extras import limpiar, pausar, convertir
def proceso():
    limpiar()
    print("En proceso. Trabajando para su pronta implementacion")
matrizA = [[1,1,1],[1,1,1],[1,1,1]]
matrizB = [[1,1,1],[1,1,1],[1,1,1]]
matrizC = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
matrizD = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

def eleccion():
    incorrecto = True
    while incorrecto:
        limpiar()
        opc = input("""1.- Matriz 3x3
2.- Matriz 4x4
Elige una opcion: """)
        opc = convertir(opc)

        if opc == 1 or opc == 2:
            incorrecto = False
            return opc
        else:
            print('Opcion no Valida intenta nuevamente')
            pausar()

def sumarMatrices(ma,mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        mr = []
        for i in range(len(ma)):
            mr.append([])
            for j in range(len(mb[0])):
                mr[i].append(ma[i][j]+mb[i][j])
        print("La suma de las matrices: ")
        print("Matriz 1: ")
        imprimirMatriz(ma)
        print("Matriz 2: ")
        imprimirMatriz(mb)
        print("Es: ")
        imprimirMatriz(mr)
    else:
        print('Las matrices no se pueden sumar')
        print(f'Matriz 1: ({len(ma)},{len(ma[0])})')
        print(f'Matriz 2: ({len(mb)},{len(mb[0])})')

def multiplicarMatrices(ma,mb):
    if len(ma[0]) == len(mb):
        mr = []
        for i in range(len(ma)):
            mr.append([])
            for j in range(len(mb[0])):
                resultado = 0
                for k in range(len(ma[0])):
                    resultado += ma[i][k]*mb[k][j]
                mr[i].append(resultado)
        print("La multiplicacion de las matrices: ")
        print("Matriz 1: ")
        imprimirMatriz(ma)
        print("Matriz 2: ")
        imprimirMatriz(mb)
        print("Es: ")
        imprimirMatriz(mr)
    else:
        print('Las matrices no se pueden multiplicar')
        print(f'Matriz 1: ({len(ma)},{len(ma[0])})')
        print(f'Matriz 2: ({len(mb)},{len(mb[0])})')

def elegirMatriz():
    inc = True
    while inc:
        limpiar()
        print('Matriz 1:')
        imprimirMatriz(matrizA)
        print('Matriz 2:')
        imprimirMatriz(matrizB)
        print('Matriz 3:')
        imprimirMatriz(matrizC)
        print('Matriz 4:')
        imprimirMatriz(matrizD)
        opc = input('Elige una matriz para sacar su inversa: ')
        opc = convertir(opc)
        if opc > 0 and opc < 4:
            inc = False
            return opc
        else:
            print('Opcion no valida intenta nuevamente')
            pausar()

def editarMatriz():
    global matrizA
    global matrizB
    global matrizC
    global matrizD
    opc = elegirMatriz()
    if opc==1:
        matrizA = editar(len(matrizA),len(matrizA[0]))
        limpiar()
        print('La matriz quedo asi: ')
        imprimirMatriz(matrizA)
        pausar()
    elif opc==2:
        matrizB = editar(len(matrizB),len(matrizB[0]))
        limpiar()
        print('La matriz quedo asi: ')
        imprimirMatriz(matrizB)
        pausar()
    elif opc==3:
        matrizC = editar(len(matrizC),len(matrizC[0]))
        limpiar()
        print('La matriz quedo asi: ')
        imprimirMatriz(matrizC)
        pausar()
    elif opc==4:
        matrizD = editar(len(matrizD),len(matrizD[0]))
        limpiar()
        print('La matriz quedo asi: ')
        imprimirMatriz(matrizD)
        pausar()

def editar(filas, columnas, text=''):
    ma=[]
    for i in range(filas):
        ma.append([])
        for j in range(columnas):
            limpiar()
            print(f'Ingresa los datos de la {text} matriz de {filas}x{columnas}')
            imprimirMatriz(ma)
            inc = True
            while inc:
                numero = input(f'\nIngresa el numero de la posicion {i+1},{j+1}: ')
                numero = convertir(numero)
                if numero:
                    ma[i].append(numero)
                    inc = False
                else:
                    print('Numero no valido. Intenta nuevamente')
                    pausar()
    return ma

def imprimirMatriz(mat):
    try:
        filas = len(mat)
        columnas = len(mat[0])
    except:
        filas = 0
        columnas = 0
    for i in range(filas):
        for j in range(columnas):
            try:
                print(f'{mat[i][j]}', end='\t')
                if j == columnas-1: print()
            except:
                pass
                #print(mat)

def det3x3(mat):
    primero = mat[0][0]*((mat[1][1]*mat[2][2])-(mat[1][2]*mat[2][1]))
    segundo = mat[1][0]*((mat[0][1]*mat[2][2])-(mat[0][2]*mat[2][1]))
    tercero = mat[2][0]*((mat[0][1]*mat[1][2])-(mat[0][2]*mat[1][1]))
    determinante = primero-segundo+tercero
    return determinante

def det4x4(mat):
    aux3=[]
    for i in range(3):
        aux3.append([1,1,1])

    auxi=0
    for i in range(3):
        if i==0: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    primero = mat[0][0] * determinante(aux3)

    auxi=0
    for i in range(3):
        if i==1: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    segundo = mat[1][0] * determinante(aux3)

    auxi=0
    for i in range(3):
        if i==2: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    tercero = mat[2][0] * determinante(aux3)

    auxi=0;
    for i in range(3):
        if i==3: auxi+=1
        auxj=0
        for j in range(3):
            if j==0: auxj+=1
            aux3[i][j] = mat[i+auxi][j+auxj]
    cuarto = mat[3][0] * determinante(aux3)

    determinante = primero-segundo+tercero-cuarto;
    return determinante;

def determinante(mat):
    n = len(mat)
    if n == 3:
        return det3x3(mat)
    elif n == 4:
        return det4x4(mat)
    else:
        print('Tranajando matrices mas grandes')
        return False

def inversaCofactores(mat):
    limpiar()
    if len(mat) != len(mat[0]):
        print('No se puede sacar matriz inversa')
        pausar()
    elif len(mat) == 3:
        det = det3x3(mat)
        aux = cofactores3x3(mat)
        aux = transpuesta(aux)
        aux = divisionDirecta(aux,det)
    elif len(mat) == 4:
        proceso()

def cofactores3x3(mat):
    limpiar()
    print('Matriz Original:')
    imprimirMatriz(mat)
    print()
    aux = []
    aux2 = 0
    for i in range(3):
        aux.append([0,0,0])
    for i in range(3):
        for j in range(3):
            a=0
            b=0
            c=0
            d=0
            #if j == 0:
            if a == i:
                a = (a+1)%3
            if b == j:
                b = (b+1)%3
            c = a+1
            d = b+1
            if c == i:
                c = (c+1)%3
            if d == j:
                d = (d+1)%3
            if aux2%2 == 1:
                print(f'mr[{i}][{j}] = -(mat[{a}][{b}]*mat[{c}][{d}] - mat[{c}][{b}]*mat[{a}][{d}])')
            else:
                print(f'mr[{i}][{j}] = mat[{a}][{b}]*mat[{c}][{d}] - mat[{c}][{b}]*mat[{a}][{d}]')
            aux[i][j] = (mat[a][b]*mat[c][d]) - (mat[c][b]*mat[a][d])
            if j == 1:
                pass
            if aux2%2 == 1:
                aux[i][j] = -(aux[i][j])
            aux2 += 1
    print()
    print('Matriz de Cofactores:')
    imprimirMatriz(aux)
    return aux

def transpuesta(mat):
    n = len(mat)
    aux = []
    for i in range(n):
        aux.append([1,1,1])
    for i in range(n):
        for j in range(n):
            aux[j][i]=mat[i][j]
    print()
    print('Matriz de Cofactores Transpuesta: ')
    imprimirMatriz(aux)
    return aux

def mcd(dividendo,divisor):
    if divisor==0:
        return dividendo
    else:
        return mcd(divisor, dividendo%divisor)

def divisionDirecta(mat,det):
    print()
    print('Matriz Inversa: ')
    n = len(mat)
    for i in range(n):
        for j in range(n):
            print(f'{mat[i][j]}/{det}', end='\t')
            if j+1 == n:
                print()
    print()
    print('Matriz Inversa Final: ')
    for i in range(n):
        for j in range(n):
            mcdiv = mcd(mat[i][j], det)
            print(f'{int(mat[i][j]/mcdiv)}/{int(det/mcdiv)}', end='\t')
            if j+1 == n:
                print()
    print()

def inversaGauss(mat):
    limpiar()
    if len(mat) != len(mat[0]):
        print('No se puede sacar matriz inversa')
        pausar()
    else:
        proceso()

def elegirInversa():
    inc = True
    metodo =  0
    while inc:
        limpiar()
        print(f'1.- Cofactores\n2-Gauss')
        metodo = input('Elige el metodo: ')
        metodo = convertir(metodo)
        if metodo == 1:
            inc = False
        elif metodo == 2:
            inc = False
        else:
            print('Opcion no valida. Intenta nuevamente')
            pausar()
    opc = elegirMatriz()
    if opc == 1:
        inc = False
        if metodo == 1:
            inversaCofactores(matrizA)
        elif metodo == 2:
            inversaGauss(matrizA)
    elif opc == 2:
        inc = Falseinc = False
        if metodo == 1:
            inversaCofactores(matrizB)
        elif metodo == 2:
            inversaGauss(matrizB)
    elif opc == 3:
        inc = False
        if metodo == 1:
            inversaCofactores(matrizC)
        elif metodo == 2:
            inversaGauss(matrizC)
    elif opc == 4:
        inc = False
        if metodo == 1:
            inversaCofactores(matrizC)
        elif metodo == 2:
            inversaGauss(matrizC)
    else:
        print('Opcion no valida. Intenta nuevamente')
        pausar()

def menu():
    incorrecto = True
    while incorrecto:
        limpiar()
        opc = input("""1.- Sumar matrices
2.- Multiplicar matrices
3.- Inversa
4.- Operaciones libres
5.- Editar MAtrices
Elige una opcion: """)
        opc = convertir(opc)
        if opc == 1:
            incorrecto = False
            opc = eleccion()
            if opc == 1:
                sumarMatrices(matrizA,matrizB)
            elif opc == 2:
                sumarMatrices(matrizC,matrizD)
        elif opc == 2:
            incorrecto = False
            opc = eleccion()
            if opc == 1:
                multiplicarMatrices(matrizA,matrizB)
            elif opc == 2:
                multiplicarMatrices(matrizC,matrizD)
        elif opc == 3:
            incorrecto = False
            elegirInversa()
        elif opc == 4:
            incorrecto = False
            proceso()
        elif opc == 5:
            editarMatriz()
        else:
            print('Opcion no valida. Intenta nuevamente')
            pausar()

def main():
    menu()
    pausar()