import time
tiempo = int(input("de cuanto tiempo es tu timer men?(en segundos)"))
if tiempo != 0:
    for n in range(0,tiempo):
        print(tiempo)
        tiempo-=1
        time.sleep(1)
        if tiempo != 0:
            continue
        else:
            break

else:
    print("algo hiciste mal")
