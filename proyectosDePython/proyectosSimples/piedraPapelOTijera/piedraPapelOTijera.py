# definimos que vamos opcion vamos a seleccionar 
entrada = input("¿piedra, papel o tijera? ")
# importamos random para sacar número aleatorio
from random import randrange
# sacamos un numero aleatorio para la lista de nombres
numeroDeListado = randrange(1,3)
# hacer una lista de nombres (piedra ,papel o tijera)
lista = ["piedra","papel","tijera"]
# definimos variable(con el número aleatorio) para compararla más tarde 
salidaDeRobot = lista[numeroDeListado]
# ponemos un bloque condicional. con el que ponemos por ejemplo que si el robot da piedra y el usuario papel se imprima ganaste
if salidaDeRobot == "piedra" and entrada == "papel":
    print("ganaste")
if salidaDeRobot == "papel" and entrada == "tijera":
    print("ganaste")
if salidaDeRobot == "tijera" and entrada == "piedra":
    print("ganaste")

# aqui lo mismo solo que al reves
if entrada == "piedra" and salidaDeRobot == "papel":
    print("perdiste")
if entrada == "papel" and salidaDeRobot == "tijera":
    print("perdiste")
if entrada == "tijera" and salidaDeRobot == "piedra":
    print("perdiste")
# y aqui ponemos un condicional con el que ponemos que si entrada (usuario) es igual que la maqina poner empate
if entrada == salidaDeRobot:
    print("empate")
# ahora pongamos el caso que pongas mal el nombre de la jugada
else:
    print("no entiendo")
# aqui pintamos en terminal que puso la maquina
print(salidaDeRobot)