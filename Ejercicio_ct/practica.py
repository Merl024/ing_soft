
#########################
# 1. Información Personal #
#########################

nombre = 'Melisa Rivas'
edad = 18
altura = 1.55
programOtro = True

### print(f"Hola, mi nombres es {nombre}, tengo {edad} años. Tengo una estatura de {altura}m. ¿Sabe programar en otro lenguaje? {programOtro}")

#########################
# 2. Calculadora Básica #
#########################

nums = 'Ingresa dos números de tu preferencia.'
# num1 = float(input('Ingresa numero 1: '))
# num2 = float(input('Ingresa numero 2: ')) Esta es una manera de hacerlo, pero let's keep it simple
num1 = float(45.353434467)
num2 = float(56.78994332)

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# # # print(f'>>> La suma de {num1} y {num2} es {suma:,.3f}')
# # # print(f'>>> La resta de {num1} y {num2} es {resta:,.3f}')
# # # print(f'>>> La multiplicación de {num1} y {num2} es {multiplicacion:,.3f}')
# # # print(f'>>> La división de {num1} y {num2} es {division:,.3f}')

#############################
# 3. Conversor de Unidades #
#############################

metros = float(10.46)
#Variables para convertir metros a cm y Km
convCm = metros * 100
convKm = metros / 1000 #los ultimos valores son denotados por formula

# # # print(f'{metros}m son {convCm:,.2f}cm y {convKm:,.4f}km')

######################
# 4. Cálculo de Área #
######################

#declarando variables de la formula 
radio = float(5.67)
pi = 3.1415

area = pi * radio**2 # ** sirve para expresar que lo que viene despues es el indice (exponente)

# # # print(f'Teniendo como radio: {radio}. El área del círculo es: {area:,.2f}.')

######################
# 5. Nombre Completo #
######################

nombre = "Melisa"
apellido = "Rivas"

# # # print(f'{apellido}, {nombre}')

#############################
# 6. Comparación de Números #
#############################

# num1 = float(input('Ingresa el primer numero: '))
# num2 = float(input('Ingresa el segundo numero: '))
num1 = 34
num2 = 45

mayor = num1 > num2
menor = num1 < num2
igual = num1 == num2

# # # input(f'{num1} es mayor a {num2}: {mayor}')
# # # input(f'{num1} es menor a {num2}: {menor}')
# # # input(f'{num1} es igual a {num2}: {igual}')

##############################
# 7. Descuento en una Compra #
##############################

precio = float(24.99)
porcetaje = 15
descuento = porcetaje / 100

precioFinal = precio * (1 - descuento)

# # # print(f'El precio final es: ${precioFinal:,.2f}')

#####################
# 8. Cálculo de IMC #
#####################
"""
Pide al usuario que ingrese su peso (en kg) y altura (en metros).
Calcula el índice de masa corporal (IMC) utilizando la fórmula IMC = peso / altura².
"""
pesoKg = float(56.78)
alturaM = float(1.55)

imc = pesoKg / alturaM**2

# # # print(f'Su peso es de {pesoKg}kg y su altura de {alturaM}. Dando un IMC de: {imc:,.2f}.')

##########################
# 9. Tablas de multiplicar
##########################
"""
Crear una mini aplicación tal que, muestre del 1 al 12 los resultados
de la multiplicación por dicho número.
Independientemente del valor ingresado, la multiplicacion sera por numero entero.
Ejemplo: (1.14159)
>> 1 x 1 = 1
>> 1 x 2 = 2
...
>> 1 x 11 = 11
>> 1 x 12 = 12
"""
#######################
# 10. Interés compuesto
#######################
"""
Suponga para un par de números (variables) deberá expresar que monto (uno de esos valores)
será incrementado en porcentaje del segundo número [Monto1 = Monto *(1+(tasa/100))].
Este proceso se hará de manera acumulativa por 10 veces, con 2 decimales.

Ejemplo:
>> Monto= 10,423, Interés= 3
>> Monto 1 = 10,735.69
>> Monto 2 = 11,057.76
...
>> Monto 9 = 13,599.65
>> Monto 10 = 14,007.64
"""
monto = 13,405.68
interes = 87
