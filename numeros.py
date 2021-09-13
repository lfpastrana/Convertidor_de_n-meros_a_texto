uninum=[0,1,2,3,4,5,6,7,8,9]
unile=["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
doscifras=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
doscifrasL=[" diez"," once"," doce"," trece"," catorce"," quince"," dieciséis"," diecisiete"," dieciocho"," diecinueve"," veinte"," veintiuno"," veintidos"," veintitres"," veinticuatro"," veinticinco"," veintiseis"," veintisiete"," veintiocho"," veintinueve"," treinta"," treinta y uno"," treinta y dos"," treinta y tres"," treinta y cuatro"," treinta y cinco"," treinta y seis"," treinta y siete"," treinta y ocho"," treinta y nueve"," cuarenta"," cuarenta y uno"," cuarenta y dos"," cuarenta y tres"," cuarenta y cuatro"," cuarenta y cinco"," cuarenta y seis"," cuarenta y siete"," cuarenta y ocho"," cuarenta y nueve"," cincuenta"," cincuenta y uno"," cincuenta y dos"," cincuenta y tres"," cincuenta y cuatro"," cincuenta y cinco"," cincuenta y seis"," cincuenta y siete"," cincuenta y ocho"," cincuenta y nueve"," sesenta"," sesenta y uno"," sesenta y dos"," sesenta y tres"," sesenta y cuatro"," sesenta y cinco"," sesenta y seis"," sesenta y siete"," sesenta y ocho"," sesenta y nueve"," setenta"," setenta y uno"," setenta y dos"," setenta y tres"," setenta y cuatro"," setenta y cinco"," setenta y seis"," setenta y siete"," setenta y ocho"," setenta y nueve"," ochenta"," ochenta y uno"," ochenta y dos"," ochenta y tres"," ochenta y cuatro"," ochenta y cinco"," ochenta y seis"," ochenta y siete"," ochenta y ocho"," ochenta y nueve"," noventa"," noventa y uno"," noventa y dos"," noventa y tres"," noventa y cuatro"," noventa y cinco"," noventa y seis"," noventa y siete"," noventa y ocho"," noventa y nueve"]
decenum=["",1,2,3,4,5,6,7,8,9]
decelet=["","vinti","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
centenum=[0,1,2,3,4,5,6,7,8,9]
centenas=["","ciento","doscientos","trescientos","cuatroscientos","quinientos","seiscientos","setecientos","ochocientos","novecientos"]
miles = ["","mil","dos mil","tres mil","cuatro mil","cinco mil","seis mil","siete mil","ocho mil","nueve mil"]         


def una(convertir):
    for i in range(len(uninum)):
        if int(convertir)==uninum[i]:
            return unile[i]

def dos(convertir):
    for i in range(len(doscifras)):
        if int(convertir)==doscifras[i]:
            return doscifrasL[i]

def tres(convertir):
    if int(convertir) == 100:
        return "cien"
    if int(convertir[1]) == 0:
        for i in range(len(doscifras)):
            if  int(convertir[0]) == centenum[i]:
                a = centenas[i] + " " + str(una(convertir[1:3]))
                return a
    if int(convertir[1]) != 0:
        for i in range(len(doscifras)):
            if  int(convertir[0]) == centenum[i]:
                b = centenas[i] + str(dos(convertir[1:3]))
                return b

def cuatro(convertir):
    if int(convertir[1]) == 0 and int(convertir[2]) == 0 and int(convertir[3]) == 0:
            for i in range(len(miles)):
                if int(convertir[0]) == uninum[i]:
                    a = miles[i] 
                    return a
    if int(len(convertir))== 4:
            for i in range(len(miles)):
                if int(convertir[0]) == uninum[i]:
                    a = miles[i] +" "+ tres(convertir[1:4])
                    return a

def cinco(convertir):
    if int(len(convertir))== 5:
        a = dos(convertir[0:2]) +" mil " + tres(convertir[2:5])
        return a

def seis(convertir):
    if int(len(convertir))== 6:
        a = tres(convertir[0:3]) +" mil " + tres(convertir[3:6])
        return a

def siete(convertir):
    if int(len(convertir))== 7:
        if int(convertir) == 1000000:
            a = "un millón"
            return a
        if int(convertir[0]) == 1 and int(convertir[1:4]) ==000:
            a =una(convertir[0])+ " millón " + tres(convertir[1:4]) +tres(convertir[4:7])
            return a
        if int(convertir[0]) == 1 and int(convertir[1:4]) !=000:
            a =una(convertir[0])+ " millón " + tres(convertir[1:4]) +" mil "+ tres(convertir[4:7])
            return a
        if int(convertir[0]) != 1 and int(convertir[1:4]) ==000:
            a =una(convertir[0])+ " millones " + tres(convertir[1:4]) +tres(convertir[4:7])
            return a
        if int(convertir[0]) != 1 and int(convertir[1:4]) !=000:
            a =una(convertir[0])+ " millones " + tres(convertir[1:4]) +" mil "+ tres(convertir[4:7])
            return a

def ocho(convertir):    
    if int(len(convertir))== 8:
            if int(convertir[2:5]) == 000 and int(convertir[4:7]) ==000:
                a =dos(convertir[0:2]) + " millones"
                return a
            if int(convertir[2:5]) ==000:
                a =dos(convertir[0:2])+ " millones " + tres(convertir[2:5]) +tres(convertir[5:8])
                return a
            else:
                a =dos(convertir[0:2])+ " millones " + tres(convertir[2:5]) +" mil "+ tres(convertir[5:8])
                return a

def nueve(convertir):    
    if int(len(convertir))== 9:
            if int(convertir[3:6]) == 000 and int(convertir[6:9]) ==000:
                a =tres(convertir[0:3]) + " millones"
                return a
            if int(convertir[3:6]) ==000:
                a =tres(convertir[0:3])+ " millones " + tres(convertir[3:6]) +tres(convertir[6:9])
                return a
            else:
                a =tres(convertir[0:3])+ " millones " + tres(convertir[3:6]) +" mil "+ tres(convertir[6:9])
                return a

while True:
    try:
        convertir=input("Ingrese un número entero entre 0 y 1.000.000.000==>")
        largo=len(convertir)
        if str(convertir) == " ":
            print("No se aceptan letras")
        if int(convertir)==0:
            print("cero")
        if int(convertir)==1000000000:
            print("mil millones")
        if int(convertir) < 0 or int(convertir) > 1000000001:
            print("Número fuera del rango")
        else:
            if largo == 1:
                x = una(convertir)
                print(x)
            if largo == 2:
                x = dos(convertir)
                print(x)
            if largo == 3:
                x = tres(convertir)
                print(x)
            if largo == 4:
                x = cuatro(convertir)
                print(x)
            if largo == 5:
                x = cinco(convertir)
                print(x)
            if largo == 6:
                x = seis(convertir)
                print(x)
            if largo == 7:
                x = siete(convertir)
                print(x)
            if largo == 8:
                x = ocho(convertir)
                print(x)
            if largo == 9:
                x = nueve(convertir)
                print(x)
            break
    except:
        print("Solamente cargar números enteros entre 0 y 1.000.000.000")
        print("Gracias")



