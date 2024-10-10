
########################
##### Ejercicio 1 ######
# Validacion de correo #
########################

correo = input('Ingrese su correo electronico: ')

arrobaIn = correo.count('@') == 1
arrobaInicioFin = "@" not in correo[::]
terminacion = '.com' in correo
noDominio = correo[:-10:]

print('Listado de verificacion: ')
print(f'¿Aparece solo 1 vez el @?: {arrobaIn}')
print(f'El arroba se encuentra al principio o al final: {arrobaInicioFin}')
print(f'El correo electronico termina en .com: {terminacion}')
print(f'La parte del correo electronico es {noDominio}')


########################
##### Ejercicio 2 ######
# Impresion de cheques #
########################

nombre = input('Ingrese su primer nombre: ')
apellido = input('Ingrese su primer apellido: ')
monto = float(input('Ingrese el monto del cheque a emitir: '))
caracteresFijos = 70

plantilla = 'Nombre: {}. Apellido: {}. {} Monto: ${:,.2f}'
asteriscos = '*' * (caracteresFijos - (len(nombre) + len(apellido) + len(str(monto)) + len(plantilla)) )

print(plantilla.format(nombre.capitalize(), apellido.capitalize(), asteriscos, monto)) 

