
nota = float(input('Digite la nota: '))

if nota < 0:
    print('La nota debe ser un valor positivo')
elif nota >= 11:
    print('La nota no debe exceder el numero 10')
elif nota >= 6: 
    print('El alumno ha aporbado')
else: 
    print('El alumno ha desaprobado')