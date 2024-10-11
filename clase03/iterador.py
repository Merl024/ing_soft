"""
validacionDeSaludo = True

#La variable entra como true, cuando esta se convierte false, se detiene. Mientras se mantegna
#True, el bucle seguira
while validacionDeSaludo:   
    saludo = input('Hola, soy Melisa: ')
    #hay una validacion booleana cuando diga 'Hola Melisa'
    validacionDeSaludo = saludo != 'Hola, Melisa'
    print(validacionDeSaludo)
"""

"""
print('Hola, bienvenido a nuestra aplicacion')
opciones = 0 

#While revisa no asigna, por eso se crean las variables antes
while opciones != 3:
    opciones = int(input('Elija la opcion 3 para salir: '))
"""
palabraClave = ''
contador = 0

while palabraClave != 'Pera':
    palabraClave = input('Ingrese la palabra clave: ').capitalize()
    contador += 1
    print(contador)