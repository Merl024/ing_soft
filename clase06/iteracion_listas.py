
### Listas >> importa el orden
### Diccionarios >> no importa el orden

## Estrutura de un diccionario >> Llave: valor
personas = {
    'Juan': [30, 'Ecuador', ['JavaScript']],
    'Marcelinni': [60, 'China', ['JavaScript', 'C++', 'Python']],
    'Mario Guineño': [ 10, 'El Salvador', ['Java', 'C++']]
}

# print(personas['Mario Guineño'][0])

# ## El .keys() itera por las claves de los diccionarios
# ### Un diccionario itera por los keys por defecto, este metodo es para hacerlo explicito 
# for k in personas.keys():
#     print(k)

# ## El .values() itera por los valores de los diccionarios
# for v in personas.values():
#     print(v[2])

# ## El.items() itera por los pares clave-valor de los diccionarios
# for k,v in personas.items():
#     print(f'Nombre: {k}, Lenguajes de programación: {v[2]}')

for k,v in personas.items():
    if len(v[2]) > 1:
        print(f'Nombre: {k}, Lenguajes de programación: {v[2]}')