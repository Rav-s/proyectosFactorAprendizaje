import random
print("es hora de adivinar un número, \n pon en la primera petición el número más bajo que vallas a adivinar y despúes el más alto")
entrada = int(input("primer número ")) 
entrada2 =  int(input("segundo número "))
suposicion = int(input("que número crees que es? "))

numeroAlAzar = random.randrange(entrada,entrada2)
if numeroAlAzar == suposicion:
    print("ganaste el número es = " + str(numeroAlAzar))
if numeroAlAzar != suposicion:
    print("perdiste el número es =" + str(numeroAlAzar))