## Ejercicio 2
"""
Con las listas proporcionada a continuación, se le pide que:
A partir de una contraseña ingresada por el usuario, se valide que esta cumpla
con los cuatro criterios basicos que se le presenta:
a. Que contenga una letra minuscula
b. Que contenga una letra mayuscula
c. Que contenga un simbolo
d. Que contenga un caracter
"""

contra = input('Ingrese una contraseña valida: ')

mini = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
may = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
car = ['!', '@', '#', '$', '%', '^',' &', '*', '(', ')', '_', '+', '-', '{', '}', '[', ']', ':', ';', '<', '>', '?', '/', '|','~']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Estamos aclarando que cuando el usuario ingresa la contraseña no tiene lo siguiente
siMini = False
siMay = False
siCar = False
siNum = False

#Estamo revisando letra por letra si cumple con lo que se pide. 
for i in contra:
    if i in mini:
        siMini = True
    if i in may:
        siMay = True
    if i in car:
        siCar = True
    if i in num:
        siNum = True

#Validar si es valida la contra
if siMay and siMini and siMini and siCar:
    print(F"La contaseña {contra} es valida ")
else:
    print('La contaseña no es valida. Debe contener:')
    if not siMay:
        print('- Al menos una mayuscula')
    if not siMini:
        print('- Al menos una minuscula')
    if not siNum:
        print('- Al menos un numero')
    if not siCar:
        print('- Al menos un caracter')