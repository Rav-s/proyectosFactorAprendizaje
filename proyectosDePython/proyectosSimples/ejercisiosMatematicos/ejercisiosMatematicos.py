# importamos random
import random
# generamos una variable STR para poner la operacion (más tarde lo entenderas)
operacion = ""
#ponemos un contador para el bucle while
contador = 0
# una lista de números listos para concatenar
numeros = ["1","2","3","4","5","6","7","8","9",]
# una de signos positivo y de operación
signos1 = ["+","-"]
signos2 = ["x",":"]
condiciónDeSigno = [1,2,3]
# y el bucle while (con una condición algo...)
while contador == contador:
# generamos un elemto extraido aleatoriamente de cada lista para hacer esta operación matématica
    randomSigno = random.choice(signos1)
    randomNumero = random.choice(numeros)
    randomNumero1 = random.choice(numeros)
    randomSigno1 = random.choice(signos2)
    randomCodicion = random.choice(condiciónDeSigno)
# pasamos los datos de tipo slices (tipo lista) a STR para poder concatenar
    str(randomSigno)
    str(randomNumero)
    str(randomNumero1)
    str(randomSigno1)
#hacemos que el contador creesca uno 
    contador = contador + 1
# ponemos signo positivo o negativo 
    operacion = operacion + randomSigno
# ponemos un número
    operacion = operacion + randomNumero
# ponemos bloque condicional para poner 1 o dos digitos
    if random.randrange(1,2) == 1:
        operacion = operacion + randomNumero1
# ponemos un signo de operación si se cumple la condición
    if randomCodicion == 2:
        operacion = operacion + randomSigno1
# ahora un bloque condicional en el que si son 6 vueltas al bucle se detenga y muestre la operación
    if contador == 6:
        break
operacion2 = operacion
operacion3 = operacion
if operacion[0] == "x" and ":":
    operacion2 = operacion[1:-0]
if operacion[-1] == "x" and ":":
    operacion3 = operacion2[0:-1]
print(operacion)




















