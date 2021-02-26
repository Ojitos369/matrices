from src.extras import limpiar,pausar

def mostrarNumeros():
    limpiar()
    for i in range(10):
        if i>=0 and i<=3:
            print(f'{i+1}', end='\t')
        elif i == 4:
            print(f'\n\n\t\t{i+1}')
        elif i == 5:
            print(f'\n\t{i+1}\n')
        else:
            print(f'{i+1}', end='\t')
    print('\n')
    pausar()