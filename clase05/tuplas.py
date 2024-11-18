txt = 'Pero qué luz se deja ver allí'
# El split ayuda a que las oraciones se agarre por palabras ylas agrega a una lista
palabras = txt.split()
t = list()
print(t)
for palabra in palabras:
    #Por el split(), por cada iteracion aparecera y se sumara una nueva palabra al print 
    # Aqui el chiste es crear una tupla la cual se ira agregando a una lista
    t.append((len(palabra), palabra))
    print(t)

#Esto es solo una lista
texto = "Hola, como estas, estoy intentando probar el .split() para entenderlo mejor" 
palabra = texto.split()
print(palabra)
tex = list()
print(tex)

for idx,p in enumerate(palabra):
    #creacion de tupla
    tex.append((len(p), p))
    print(idx,(tex))