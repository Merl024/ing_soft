
valor1 = float(input('Digite numero uno: '))
valor2 = float(input('Digite numero dos: '))

mensaje = 'El numero mayor es: '

if valor1 > valor2: 
    mayor = 'Valor 1'
elif valor1 == valor2:  
    mayor = 'Ninguno de los dos es mayor'
else:
    mayor = 'Valor 2'

print(mensaje + mayor)