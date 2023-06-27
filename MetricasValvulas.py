import csv
import math

def Manhattan(x,y):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(y)):
        contador = 0
        for j in range(len(y[i]) - 2):
            contador += abs(x[j] - int(y[i][j + 1]))
        resultados.append(contador)

        may = max(resultados)

    for i in range(len(y)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 80.0:
            mp += 1

            a = open('CasosManhattan.txt', 'a')
            a.write(str(y[i][0]) + " " + str(y[i][1]) + " " + str(y[i][2]) + " " + str(y[i][3]) + " " + str(y[i][4]) + " " + str(y[i][5]) + " " + str(resultados[i]) + "\n")
            a.close()

    print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Es: ",mp)

def Euclidiana(x,y):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(y)):
        contador = 0
        for j in range(len(y[i]) - 2):
            contador += math.pow(x[j] - int(y[i][j + 1]), 2)
        resultados.append(math.sqrt(contador))

        may = max(resultados)

    for i in range(len(y)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 80.0:
            mp += 1

            a = open('CasosEuclidiana.txt', 'a')
            a.write(str(y[i][0]) + " " + str(y[i][1]) + " " + str(y[i][2]) + " " + str(y[i][3]) + " " + str(y[i][4]) + " " + str(y[i][5]) + " " + str(resultados[i]) + "\n")
            a.close()

    print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Es: ", mp)

def euclidianaNormalizada(x,y):
    datos = []
    resultados = []
    mp = 0
    for i in range(len(y)):
        contador = 0
        for j in range(len(y[i]) - 2):
            contador += ((math.pow(x[j], 2)) - (2*(x[j] * int(y[i][j + 1]))) + (math.pow(int(y[i][j + 1]),2)))
        resultados.append(contador)

        may = max(resultados)

    for i in range(len(y)):
        datos.append((1 - resultados[i] / may) * 100)
        if datos[i] >= 80.0:
            mp += 1

            a = open('CasosEuclidianaN.txt', 'a')
            a.write(str(y[i][0]) + " " + str(y[i][1]) + " " + str(y[i][2]) + " " + str(y[i][3]) + " " + str(y[i][4]) + " " + str(y[i][5]) + " " + str(resultados[i]) + "\n")
            a.close()

    print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Es: ", mp)


def sorenceDice(x,y):
    datos = []
    resultados = []
    mp = 0

    for i in range(len(y)):
        arriba = 0
        abajo = 0
        for j in range(len(y[i]) - 2):
            arriba += x[j] * int(y[i][j + 1])
            abajo += (math.pow(x[j], 2) + math.pow(int(y[i][j + 1]),2))
        resultados.append((2 * arriba) / abajo)

        may = max(resultados)

    for i in range(len(y)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.8:
            mp += 1

            a = open('CasosSorence.txt', 'a')
            a.write(str(y[i][0]) + " " + str(y[i][1]) + " " + str(y[i][2]) + " " + str(y[i][3]) + " " + str(y[i][4]) + " " + str(y[i][5]) + " " + str(resultados[i]) + "\n")
            a.close()

    print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Es: ", mp)

def Coseno(x,y):
    resultados = []
    datos = []
    mp = 0

    for i in range(len(y)):
        x2 = 0
        y2 = 0
        arriba = 0
        for j in range(len(y[i]) - 2):
            arriba += x[j] * int(y[i][j + 1])
            x2 += (math.pow(x[j], 2))
            y2 += (math.pow(int(y[i][j + 1]),2))
        abajo = math.sqrt(x2 * y2)
        resultados.append(arriba/abajo)

        may = max(resultados)

    for i in range(len(y)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.8:
            mp += 1

            a = open('CasosCoseno.txt', 'a')
            a.write(str(y[i][0]) + " " + str(y[i][1]) + " " + str(y[i][2]) + " " + str(y[i][3]) + " " + str(y[i][4]) + " " + str(y[i][5]) + " " + str(resultados[i]) + "\n")
            a.close()

    print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Es: ", mp)

def Jaccard(x,y):
    resultados = []
    datos = []
    mp = 0

    for i in range(len(y)):
        x2 = 0
        y2 = 0
        arriba = 0
        for j in range(len(y[i]) - 2):
            arriba += x[j] * int(y[i][j + 1])
            x2 += (math.pow(x[j], 2))
            y2 += (math.pow(int(y[i][j + 1]), 2))
        abajo = x2 + y2 - arriba
        resultados.append(arriba / abajo)

        may = max(resultados)

    for i in range(len(y)):
        datos.append((1 - resultados[i] / may) * 100)
        if resultados[i] >= 0.8:
            mp += 1

            a = open('CasosJaccard.txt', 'a')
            a.write(str(y[i][0]) + " " + str(y[i][1]) + " " + str(y[i][2]) + " " + str(y[i][3]) + " " + str(y[i][4]) + " " + str(y[i][5]) + " " + str(resultados[i]) + "\n")
            a.close()

    print("\n",datos)
    print("El Numero De Casos Mayores Al 80% Es: ", mp)

x = [2, 1, 3, 2]
y = []
lista = []

with open('datosvalvula.csv', 'r') as archivo:
    entrada = csv.reader(archivo)
    y = list(entrada)

#Manhattan(x,y)
#Euclidiana(x,y)
#euclidianaNormalizada(x,y)
#sorenceDice(x,y)
#Coseno(x,y)
#Jaccard(x,y)
