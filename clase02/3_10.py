texto1 = 'python'
texto2 = 'b'
texto3 = texto1 + texto2
veces = 5

print(texto1*veces) #>>> Lo que quiere significar veces, es cuantas veces quiero que se repita la variable texto1

print('y' in texto1) #queremos verificar si 'y' esta dentro de la variable texto1, si o no. Lo que va a tirar un booleano (true or false)

print('y' in texto2)

print('y' not in texto1) #para ver SI NO esta en una variable. Va a tirar False porque la letra 'y' SI ESTA en la variable texto1

print(min(texto1)) #Aqui manda cual va primero segun el ABECEDARIO, imprimira h porque va antes de p, sin embargo
#si mi variable dijera texto1 = 'Python' imprimiria P porque TODAS las mayusculas van antes que las minusculas. 

print(texto1.capitalize()) #este metodo ayuda a modificar el comportamiento de la variable original
#yo tengo 'python' .capitalize me imprimira Python
print(texto1.upper().capitalize())
