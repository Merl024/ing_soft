
edades = {
    "Alvin": 42,
    "Carlos": 34,
    "Cecy": 39
}

nombre = input('Ingrese su nombre: ').capitalize() #Agarra el nombre solo si esta dentro del diccionario.


# print(f'La edad {edades[nombre]}')

# del edades['carlos'.capitalize()] # Con "del" se elimina un dato dentro del diccionario
# print(edades)

#edad = edades[nombre]
# print(edad) #Con base al nombre que se escribe tira el dato que eso, solo es valido si esta dentro del diccionario

#Este el metodo .get() sirve para agarrar el dato y si no lo encuentra tira un mensaje
#edad = edades.get(nombre, "No se encontro")
#print(edad)

hijos = {
    "Alvin": ['Mariana', 'Majo', 'Felipe'],
    "Carlos": ['Andre', 'Fabiola'],
    "Cecy": ['Javier', 'Junio']
}

#print(hijos)
hijo = hijos.get(nombre, 'No se encontro')
print(hijo)
# contador = 0
# for h in hijos[nombre]: 
#     contador += 1
#     print(f'Hijo {contador}: {h}')

print(nombre)
for n,i in enumerate(hijos[nombre]):
    print(f'Hijo {n+1}: {i}')

