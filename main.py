

def Manhattan(x,y):
    t = 0
    for i in range(len(y)):
        contador = 0
        for j in range(len(y[i])-2):
            contador += abs(x[j] - y[i][j+1])
        R[i] = contador

    mayor = max(R)
    for i in range(len(y)):
        dato = (1 - R[i] / mayor)

        if dato >= 0.8:
            t += 1
            txt = open('DatosManhattan.txt','a')
            txt.write(str(y[i][0]) + " " + str(R[i]) + " " + str(y[i][1]) + " " + str(y[i][2]) + " " + str(y[i][3]) + " " + str(y[i][4]) + " " + str(y[i][5]) + "\n")
            txt.close()

    for i in range(len(y)):
        datos = ((1 - R[i] / mayor) * 100)

    print(dato)
    print("Datos mayores al 80%: ", t)


x = [2, 1, 3, 2]
dato = []
datos = []
y = []
R = []
