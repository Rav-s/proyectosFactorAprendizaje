# descarga la libreria random
# importar random
import random
# random es una libreria de python que te permite generar números al azar
# hacemos una lista con las personas
persona = ["Pedro","Juan","Diego"]
# hacemos una lista con los verbos
verbo = ["juega","Canta","Baila"]
# sacamos numeros al azar para llamar (entre parentecis va el rango numerico)
random1 = random.randrange(1,3)
random2 = random.randrange(1,3)
# llamamos a los numeros de lista y dejamos un espacio
salida1 = persona[random1] + " " + verbo[random2]
# pintamos la salida 
print(salida1)