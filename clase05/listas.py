#Esta es mutable, porque es una lista
miLista = ['uno', 'dos', 'tres']
#Reemplaza el valor que se le esta asiganando a esa posicion
miLista[1] = 2

#En este caso, a pesar de realizar el cambio en la lista, aunque haya sido parcial
# El id no se regenera. 
print(id(miLista))


miTupla = ('uno', 'dos', 'tres')
#Lo de acontinuacion no se puede, ya que es una tupla no inmutable,
#no se puede modificar parcialmente
#miTupla[1] = 4
print(id(miTupla))
#Lo que SI se puede, es modificarlos por completo
miTupla = (1, 2, 3)
print(miTupla[1])

#Tiene diferente id porque como se esta cambiando los elementos, se regenera el numero de id
#Por eso no es el mismo
print(id(miTupla))

""" Es mejor tener listas pequeñas y tuplas grandes, pues las tuplas pesan menos """

