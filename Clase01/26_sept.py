nombre = "Melisa"
apellido = "Rivas"
nombre_completo = nombre + " " + apellido

edad = 18
meta = 2000.00

# int: Integer, Entero
# str: String, texto (cadena de texto)

texto_completo = nombre_completo + " tiene " + str(edad) + " años, "
texto_completo_f = texto_completo + "y su meta es... " + str(meta)
texto_formateado = f"La meta es... ${meta:,.2f}" 
#El f al inicio es para que se pueda trabajar mejor con un string, son como las backticks en JS
# Al final de meta se ocupa 2f para darle dos decimales, en caso que quisiera mas decimales, pongo
# numero_f

print(nombre)
print(apellido)

print(nombre_completo)
print(texto_completo)
print(texto_completo_f)
print(texto_formateado)