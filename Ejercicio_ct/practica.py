
#########################
# 1. Información Personal #
#########################

nombre = 'Melisa Rivas'
edad = 18
altura = 1.55
programOtro = True

# print(f"Hola, mi nombres es {nombre}, tengo {edad} años. Tengo una estatura de {altura}m. ¿Sabe programar en otro lenguaje? {programOtro}")

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

# print(f'>>> La suma de {num1} y {num2} es {suma:,.3f}')
# print(f'>>> La resta de {num1} y {num2} es {resta:,.3f}')
# print(f'>>> La multiplicación de {num1} y {num2} es {multiplicacion:,.3f}')
# print(f'>>> La división de {num1} y {num2} es {division:,.3f}')

#############################
# 3. Conversor de Unidades #
#############################

metros = float(10.46)
#Variables para convertir metros a cm y Km
convCm = metros * 100
convKm = metros / 1000 #los ultimos valores son denotados por formula

# print(f'{metros}m son {convCm:,.2f}cm y {convKm:,.4f}km')

######################
# 4. Cálculo de Área #
######################

#declarando variables de la formula 
radio = float(5.67)
pi = 3.1415

area = pi * radio**2 # ** sirve para expresar que lo que viene despues es el indice (exponente)

# print(f'Teniendo como radio: {radio}. El área del círculo es: {area:,.2f}.')

######################
# 5. Nombre Completo #
######################

nombre = "Melisa"
apellido = "Rivas"

# print(f'{apellido}, {nombre}')

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

# input(f'{num1} es mayor a {num2}: {mayor}')
# input(f'{num1} es menor a {num2}: {menor}')
# input(f'{num1} es igual a {num2}: {igual}')

##############################
# 7. Descuento en una Compra #
##############################

precio = float(24.99)
porcetaje = 15
descuento = porcetaje / 100

precioFinal = precio * (1 - descuento)

# print(f'El precio final es: ${precioFinal:,.2f}')

#####################
# 8. Cálculo de IMC #
#####################

pesoKg = float(56.78)
alturaM = float(1.55)

imc = pesoKg / alturaM**2

# print(f'Su peso es de {pesoKg}kg y su altura de {alturaM}. Dando un IMC de: {imc:,.2f}.')

##########################
# 9. Tablas de multiplicar
##########################

numero=int(23.45)
uno= numero* 1
dos= numero* 2
Tres=numero* 3
cuatro=numero* 4
cinco=numero*5
seis=numero* 6
siete=numero * 7
ocho=numero * 8
nueve=numero* 9
diez=numero*10
once=numero*11
doce= numero*12
# print(f"{numero} X 1 es: {uno}")
# print(f"{numero} X 2 es: {dos}")
# print(f"{numero} X 3 es: {Tres}")
# print(f"{numero} X 4 es: {cuatro}")
# print(f"{numero} X 5 es: {cinco}")
# print(f"{numero} X 6 es: {seis}")
# print(f"{numero} X 7 es: {siete}")
# print(f"{numero} X 8 es: {ocho}")
# print(f"{numero} X 9 es: {nueve}")
# print(f"{numero} X 10 es: {diez}")
# print(f"{numero} X 11 es: {once}")
# print(f"{numero} X 12 es: {doce}")

#######################
# 10. Interés compuesto
#######################

monto= 10423
tasa=3
Monto1 = monto * (1+(tasa/100))
Monto2 = Monto1 * (1+(tasa/100))
Monto3 = Monto2 * (1+(tasa/100))
Monto4 = Monto3 * (1+(tasa/100))
Monto5 = Monto4 * (1+(tasa/100))
Monto6 = Monto5 * (1+(tasa/100))
Monto7 = Monto6 * (1+(tasa/100))
Monto8 = Monto7 * (1+(tasa/100))
Monto9 = Monto8 * (1+(tasa/100))
Monto10 = Monto9 * (1+(tasa/100))
# print(f"Monto1 es {Monto1:,.2f}")
# print(f"Monto2 es {Monto2:,.2f}")
# print(f"Monto3 es {Monto3:,.2f}")
# print(f"Monto4 es {Monto4:,.2f}")
# print(f"Monto5 es {Monto5:,.2f}")
# print(f"Monto6 es {Monto6:,.2f}")
# print(f"Monto7 es {Monto7:,.2f}")
# print(f"Monto8 es {Monto8:,.2f}")
# print(f"Monto9 es {Monto9:,.2f}")
# print(f"Monto10 es {Monto10:,.2f}")
