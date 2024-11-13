# Las sentencias de excepciones es como el try y catch de JS, catch siendo except en PY

## Se puede ver como un tipo if - else, ya que si cumple con las condiciones se resuelve, sino, se maneja de otra manera
try:
    numero = int(input('Ingrese un numero: '))
    numero2 = int(input('Ingrese otro numero: '))
    resultado = numero * numero2
    print('El resultado es:', resultado)
except: 
    # Lo que hace aqui es que maneja el error y le avisa al usuario POR QUE no funciona, 
    # esto se hace con el fin de que no se rompa el codigo
    print('Hubo un error, ingrese valores numericos.')


##### FINALLY #####
# Esta sentencia se va a ejecutar SI O SI

try:
    numero = int(input('Ingrese un numero: '))
    numero2 = int(input('Ingrese otro numero: '))
    resultado = numero * numero2
    print('El resultado es:', resultado)
except:
    print('Hubo un error, ingrese valores numericos.')
finally: 
    print('En esta parte siempre se va a ejecutar, haya o no error')