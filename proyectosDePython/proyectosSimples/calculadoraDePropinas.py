# empecemos preguntando cual es el porcentaje de propina. Y pasamos el input a INT con función STR (para poder manipular el número)
porsentajePropina = int(input("pon el porcentaje de propina :) "))
# pidamos el número de ganancia total de la empresa
gananciaTotal = int(input("y la ganancia total "))
# ahora hagamos el número que vamos a dar en el print(el calculo multiplica los dos input y despues los divide en 100 para saber el la cantidad de comición)
numeroDeSalida = porsentajePropina * gananciaTotal / 100
# ahora mostremos el texto con el número (pasandolo a dato STR con función STR)
print("este es tu comición " + str(numeroDeSalida) + " cobrá viste")


