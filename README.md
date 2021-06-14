# binOps
Evalúa funciones binarias de n variables (con n > 1).

Además del código dispuesto, se deben agregar las funciones que se desean evaluar con la siguiente estructura:
````python
def _nombre_(table):
    A, B [, C, D, ...] = table
    
    return _logica de la funcion_
````

Y llamar a la función printResults de la siguiente manera:
````python
printResults(createTable(_numero de variables_), _funcion_)
````
    
Por ejemplo, para evaluar A + BC:
````python
def fun(table):
  A, B, C = table
  
  return A or (B and C)
  
printResults(createTable(3), fun)
````
