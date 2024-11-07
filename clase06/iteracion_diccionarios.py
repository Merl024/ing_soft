personas = [
    {"Nombre": "Juan","edad": 40, 'pais': 'El Salvador', 'lenguajes': {'Javascript'}},
    {"Nombre": "Maria", "edad": 25, 'pais': 'India', 'lenguajes': {'Python'}},
    {"Nombre": "Marcelinni", "edad": 60, 'pais': 'China', 'lenguajes': {'SQL', 'Python', 'JavaScript'}}
]

print(f'{personas[0]['lenguajes']}\n')

for a in personas:
    print(a['lenguajes'])

