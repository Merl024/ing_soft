## Ejercicio 1
"""
Elabore un Script, para que, a partir que un usuario ingrese un NUMERO,
se pueda crear una piramide de asteriscos, como el ejemplo siguiente:
n= 3

   #   
  ###  
 ##### 
"""

numero = int(input('Ingrese un numero:')) #esta es la altura de la piramide

for i in range(1,numero+1):
    print(" " * (numero - i), end = '')  # Imprime los espacios necesarios para centrarlo
    #end ayuda para evitar que se cree una linea debajo
    print('*' * (2 * i - 1))