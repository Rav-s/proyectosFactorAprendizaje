# importemos Random
# si no tienes random escribe pip intall random en terminal
import random
# informemos al usuario pintado en terminal
print("es hora de adivinar un número, \n pon en la primera petición el número más bajo que vallas a adivinar y despúes el más alto")
# pidamos los parametros del número Random y pasemos los datos STR a INT con la función INT
entrada = int(input("primer número ")) 
entrada2 =  int(input("segundo número "))
# pidamos al usuario el número en que piensa
suposicion = int(input("que número crees que es? "))
# generemos un número aleatorio con los parametros pedidos anteriormente
numeroAlAzar = random.randrange(entrada,entrada2)
# creemos un bloque condicional que se ejecute si el número adivinado es igual al generado
if numeroAlAzar == suposicion:
# si este bloque se ejecuta se pondra el texto pintado en termina y se pasara el número al azar a str
    print("ganaste el número es = " + str(numeroAlAzar))
# aquí lo mismo solo que si hay desigualdad
if numeroAlAzar != suposicion:
    print("perdiste el número es =" + str(numeroAlAzar))