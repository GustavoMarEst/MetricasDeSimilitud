import csv
import math

def Manhattan(e,v):
    vp = 0
    vn = 0
    fp = 0
    fn = 0
    mc = [0, 0, 0, 0]
    for i in range(len(v)):
        resultados = []
        mSi = 0
        mNo = 0

        for j in range(len(e)):
            contador = 0

            for k in range(len(v[i]) - 2):
                contador += abs(int(v[i][k + 1]) - int(e[j][k + 1]))

            resultados.append(contador)

        mayor = max(resultados)

        for j in range(len(e)):
            contador = (1 - resultados[j] / mayor)

            if contador >= 0.8:
                a = int(e[j][5])
                if a == 1:
                    mSi += 1
                else:
                    mNo += 1

        if mSi >= mNo:
            re = 1
        else:
            re = 2

        rv = int(v[i][5])

        if rv == 1:
            if rv == re:
                vp = mc[0]
                vp += 1
                mc[0] = vp
            else:
                vn = mc[1]
                vn += 1
                mc[1] = vn

        elif rv == 2:
            if rv == re:
                fn = mc[2]
                fn += 1
                mc[2] = fn
            else:
                fp = mc[3]
                fp += 1
                mc[3] = fp

    print("----------------------------------------")

    p = vp / (vp + fp)
    print("Precision: ", p)

    r = vp / (vp + fn)
    print("Sencibilidad: ", r)

    f1 = (2 * (r * p)) / (r + p)
    print("Score", f1)

    print("\nVerdadero Positivo: ", vp)
    print("Verdadero Negativo: ", vn)
    print("Falso Positivo: ", fp)
    print("Falso Negativo: ", fn)

    print("----------------------------------------")

def Euclidiana(e,v):
    vp = 0
    vn = 0
    fp = 0
    fn = 0
    mc = [0, 0, 0, 0]
    for i in range(len(v)):
        resultados = []
        mSi = 0
        mNo = 0


        for j in range(len(e)):
            arriba = 0

            for k in range(len(v[i]) - 2):
                arriba += math.pow(int(v[i][k + 1]) - int(e[j][k + 1]), 2)

            resultados.append(math.sqrt(arriba))

        mayor = max(resultados)

        for j in range(len(e)):
            arriba = (1 - resultados[j] / mayor)

            if arriba >= 0.8:
                a = int(e[j][0 - 1])
                if a == 1:
                    mSi += 1
                else:
                    mNo += 1

        if mSi >= mNo:
            re = 1
        else:
            re = 2

        rv = int(v[i][0 - 1])

        if rv == 1:
            if rv == re:
                vp = mc[0]
                vp += 1
                mc[0] = vp
            else:
                vn = mc[1]
                vn += 1
                mc[1] = vn

        elif rv == 2:
            if rv == re:
                fn = mc[2]
                fn += 1
                mc[2] = fn
            else:
                fp = mc[3]
                fp += 1
                mc[3] = fp

    print("----------------------------------------")

    p = vp / (vp + fp)
    print("Precision: ", p)

    r = vp / (vp + fn)
    print("Sencibilidad: ", r)

    f1 = (2 * (r * p)) / (r + p)
    print("Score", f1)

    print("\nVerdadero Positivo: ", vp)
    print("Verdadero Negativo: ", vn)
    print("Falso Positivo: ", fp)
    print("Falso Negativo: ", fn)

    print("----------------------------------------")

def euclidianaNormalizada(e,v):
    vp = 0
    vn = 0
    fp = 0
    fn = 0
    mc = [0, 0, 0, 0]
    for i in range(len(v)):
        resultados = []
        mSi = 0
        mNo = 0

        for j in range(len(e)):
            contador = 0

            for k in range(len(v[i]) - 2):
                contador += (math.pow(int(v[i][k + 1]), 2) - (2*(int(v[i][k + 1]) * int(e[j][k + 1]))) + (math.pow(int(e[j][k + 1]), 2)))

            resultados.append(contador)

        mayor = max(resultados)

        for j in range(len(e)):
            contador = (1 - resultados[j] / mayor)

            if contador >= 0.8:
                a = int(e[j][5])
                if a == 1:
                    mSi += 1
                else:
                    mNo += 1

        if mSi >= mNo:
            re = 1
        else:
            re = 2

        rv = int(v[i][5])

        if rv == 1:
            if rv == re:
                vp = mc[0]
                vp += 1
                mc[0] = vp
            else:
                vn = mc[1]
                vn += 1
                mc[1] = vn

        elif rv == 2:
            if rv == re:
                fn = mc[2]
                fn += 1
                mc[2] = fn
            else:
                fp = mc[3]
                fp += 1
                mc[3] = fp

    print("----------------------------------------")

    p = vp / (vp + fp)
    print("Precision: ", p)

    r = vp / (vp + fn)
    print("Sencibilidad: ", r)

    f1 = (2 * (r * p)) / (r + p)
    print("Score", f1)

    print("\nVerdadero Positivo: ", vp)
    print("Verdadero Negativo: ", vn)
    print("Falso Positivo: ", fp)
    print("Falso Negativo: ", fn)

    print("----------------------------------------")

def sorenceDice(e,v):
    vp = 0
    vn = 0
    fp = 0
    fn = 0
    mc = [0, 0, 0, 0]
    for i in range(len(v)):
        mSi = 0
        mNo = 0

        for j in range(len(e)):
            arriba = 0
            abajo = 0
            abajo2 = 0
            for k in range(len(v[i]) - 2):
                arriba += (int(v[i][k + 1]) * int(e[j][k + 1]))
                abajo += (math.pow(int(v[i][k + 1]), 2) + (math.pow(int(e[j][k + 1]), 2)))
                ##abajo += (math.pow(int(v[i][k + 1]), 2))
                ##abajo2 += (math.pow(int(e[j][k + 1]), 2))

            resultados = (2 * arriba) / abajo

            if resultados >= 0.8:
                a = int(e[j][5])
                if a == 1:
                    mSi += 1
                else:
                    mNo += 1

        if mSi >= mNo:
            re = 1
        else:
            re = 2

        rv = int(v[i][5])

        if rv == 1:
            if rv == re:
                vp = mc[0]
                vp += 1
                mc[0] = vp
            else:
                vn = mc[1]
                vn += 1
                mc[1] = vn

        elif rv == 2:
            if rv == re:
                fn = mc[2]
                fn += 1
                mc[2] = fn
            else:
                fp = mc[3]
                fp += 1
                mc[3] = fp

    print("----------------------------------------")

    p = vp / (vp + fp)
    print("Precision: ", p)

    r = vp / (vp + fn)
    print("Sencibilidad: ", r)

    f1 = (2 * (r * p)) / (r + p)
    print("Score", f1)

    print("\nVerdadero Positivo: ", vp)
    print("Verdadero Negativo: ", vn)
    print("Falso Positivo: ", fp)
    print("Falso Negativo: ", fn)

    print("----------------------------------------")

def Coseno(e,v):
    vp = 0
    vn = 0
    fp = 0
    fn = 0
    mc = [0, 0, 0, 0]
    for i in range(len(v)):
        mSi = 0
        mNo = 0

        for j in range(len(e)):
            arriba = 0
            x2 = 0
            y2 = 0

            for k in range(len(v[i]) - 2):
                arriba += (int(v[i][k + 1]) * int(e[j][k + 1]))
                x2 += (math.pow(int(v[i][k + 1]), 2))
                y2 += (math.pow(int(e[j][k + 1]), 2))
            abajo = math.sqrt(x2 * y2)
            resultados = (arriba / abajo)

            if resultados >= 0.8:
                a = int(e[j][5])
                if a == 1:
                    mSi += 1
                else:
                    mNo += 1

        if mSi >= mNo:
            re = 1
        else:
            re = 2

        rv = int(v[i][5])

        if rv == 1:
            if rv == re:
                vp = mc[0]
                vp += 1
                mc[0] = vp
            else:
                vn = mc[1]
                vn += 1
                mc[1] = vn

        elif rv == 2:
            if rv == re:
                fn = mc[2]
                fn += 1
                mc[2] = fn
            else:
                fp = mc[3]
                fp += 1
                mc[3] = fp

    print("----------------------------------------")

    p = vp / (vp + fp)
    print("Precision: ", p)

    r = vp / (vp + fn)
    print("Sencibilidad: ", r)

    f1 = (2 * (r * p)) / (r + p)
    print("Score", f1)

    print("\nVerdadero Positivo: ", vp)
    print("Verdadero Negativo: ", vn)
    print("Falso Positivo: ", fp)
    print("Falso Negativo: ", fn)

    print("----------------------------------------")

def Jaccard(e,v):
    vp = 0
    vn = 0
    fp = 0
    fn = 0
    mc = [0, 0, 0, 0]
    for i in range(len(v)):
        mSi = 0
        mNo = 0

        for j in range(len(e)):
            arriba = 0
            x2 = 0
            y2 = 0
            for k in range(len(v[i]) - 2):
                arriba += (int(v[i][k + 1]) * int(e[j][k + 1]))
                x2 += (math.pow(int(v[i][k + 1]), 2))
                y2 += (math.pow(int(e[j][k + 1]), 2))
            abajo = x2 + y2 - arriba
            resultados = (arriba / abajo)


            if resultados >= 0.8:
                a = int(e[j][5])
                if a == 1:
                    mSi += 1
                else:
                    mNo += 1

        if mSi >= mNo:
            re = 1
        else:
            re = 2

        rv = int(v[i][5])

        if rv == 1:
            if rv == re:
                vp = mc[0]
                vp += 1
                mc[0] = vp
            else:
                vn = mc[1]
                vn += 1
                mc[1] = vn

        elif rv == 2:
            if rv == re:
                fn = mc[2]
                fn += 1
                mc[2] = fn
            else:
                fp = mc[3]
                fp += 1
                mc[3] = fp

    print("----------------------------------------")

    p = vp / (vp + fp)
    print("Precision: ",p)

    r = vp / (vp + fn)
    print("Sencibilidad: ",r)

    f1 = (2 * (r * p)) / (r + p)
    print("Score",f1)

    print("\nVerdadero Positivo: ",vp)
    print("Verdadero Negativo: ",vn)
    print("Falso Positivo: ",fp)
    print("Falso Negativo: ",fn)

    print("----------------------------------------")


with open('LimpiezaRecamara.csv', 'r') as archivo:
    entrada = csv.reader(archivo)
    y = list(entrada)
e = y[0:700]
v = y[700:1000]
#y = []

print("Manhattan")
Manhattan(e,v)
print("\nEuclidiana")
Euclidiana(e,v)
print("\nEuclidiana normalizada")
euclidianaNormalizada(e, v)
print("\nSorence-Dice")
sorenceDice(e,v)
print("\nCoseno")
Coseno(e,v)
print("\nJaccard")
Jaccard(e,v)