
name = input('Digite su nombre: ')
n = 0
# en este caso la i sera una variable temporal, pues toma el valor de cada repiticion
for i in name:
    print(name[n])
    #esto sirve para que cada vez se imprima una letra, se vaya sumando el indice y se imprima la siguiente
    n+=1
