rn = int(input("Dame la semilla"))
def cuadrado_medio(rn):
    rn2 = rn*rn
    medio = str(rn2)
    medio = medio[1:len(medio)]
    valIz = medio[0:len(str(rn))]

    print(valIz)

    if int(valIz)== 0:
        return 0
    cuadrado_medio(int(valIz))
    return 0

cuadrado_medio(rn)

