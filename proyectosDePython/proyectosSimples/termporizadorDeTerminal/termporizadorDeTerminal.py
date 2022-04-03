import time
tDDV = int(input("¿de cuanto es timer requerido? (si es de horas pon 1, minutos 2 y segundos 3)solo puedes poner y tipo de dato"))
tiempo = int(input("de cuanto tiempo es tu timer men?"))


if tDDV == 1:
    tiempo=tiempo * 3600
if tDDV == 2:
    tiempo=tiempo * 60
# if tDDV == 3:
    # tiempo=tiempo * 0



while tiempo != 0:
    print(str(tiempo)[0:4])
    tiempo-=1
    time.sleep(1)
    if tiempo != 0:
        continue
    else:
        break

else:
    print("algo hiciste mal")
