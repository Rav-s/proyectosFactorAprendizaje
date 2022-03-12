# version con input
# saludo
print("hola programador")
# definimos variable mediante input(entrada de texto a la cual tenemos que pasar a int mediante el metodo int)
numero = int(input("dame un número"))
# creamos una variable de comparacion para guardar el residuo de numero
comparador = numero % 2
# comparamos el residuo con 0 (si es = 0 es par , si no es inpar)
if comparador == 0:
    print("es par")
else:
    print("es inpar")