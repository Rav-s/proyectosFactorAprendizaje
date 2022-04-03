import tkinter
import random

from click import command
def ventanaDeInicio():
    ventana = tkinter.Tk()
    btnBorrar = tkinter.Button(text="empezar operaciónes", command=ventana.destroy).pack()
    ventana.mainloop()
ventana = None

calculos = 0

def reiniciar():
    global calculos
    global ventana
    if calculos <1:
        print("seguir")
        ventanaDeInicio()
    else:
        print("parar") 
    calculos = calculos +1
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
# pongamos unos bloques condicionales donde se elimine el ultimo y primer caracter si es un signo de operación
# ahora un bloque condicional en el que si son 6 vueltas al bucle se detenga y muestre la operación
        if contador==6:
                break
    print(operacion)
    print("estamos activos papi")
    operacion2 = operacion
    operacion3 = operacion
    if operacion[0] == "x" and ":":
            operacion2 = operacion[1:-0]
    if operacion[-1] == "x" and ":":
            operacion3 = operacion2[0:-1]
    ventana = tkinter.Tk()
    ventana.geometry("250x125")
    tkinter.Label(ventana,text=operacion3,font=("cursive",12)).pack()
    btn = tkinter.Button(text="otra operacion", command=lambda:[ventana.destroy(), reiniciar()]).pack()
    btnBorrar1 = tkinter.Button(text="borrar",command=ventana.destroy)
    ventana.mainloop()

reiniciar()
