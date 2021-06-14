from copy import deepcopy

''' 
    Crea la tabla de evaluaciones, de manera que
    tiene 2^(num_vars) filas y num_vars columnas
'''
def createTable(num_vars):
    if num_vars == 2:
        return [
            [False, False],
            [False, True],
            [True, False],
            [True, True]
        ]

    else:
        # Aumenta el tamaño de la tabla cuanto sea necesario de forma recursiva
        bigger_table = createTable(num_vars - 1)
        aux = deepcopy(bigger_table)

        for i in range(2 ** (num_vars - 1)):
            bigger_table[i].insert(0, False)
            aux[i].insert(0, True)
        
        bigger_table.extend(aux)

        return bigger_table


'''
    Función que imprime las evaluaciones. 
    Toma por parámetros la tabla generada con el número de variables, 
    así como la función a   evaluar.
'''
def printResults(table, f):
    n = 0
    for x in table:
        print(n, '. ', f(x))
        n += 1


'''
    Funciones de operadores compuestos.
'''
def nand(A, B):
    return not(A and B)

def nor(A, B):
    return not(A or B)

def xor(A, B):
    return (not A and B) or (not B and A)

def xnor(A, B):
    return not xor(A, B)


'''
    Ejemplo que corresponde a la función
    /(/(AB) + /(CD)) * (A + B)
'''
def fun(table):
    A, B, C, D = table

    return nor(nand(A, B), nand(C, D)) and (A or B)


# Llamadas a las funciones
printResults(createTable(4), fun)
