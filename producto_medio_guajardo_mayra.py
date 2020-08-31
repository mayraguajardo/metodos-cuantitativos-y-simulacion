rn = int(input("Dame la semilla"))
rn1 = int(input("Dame la semilla2"))
n = 0
def producto_medio(rn,rn1,n):
    rn2 = rn*rn1
    medio = str(rn2)
    medio = medio[1:len(medio)]
    val1 = medio[0:len(str(rn))]
    print(val1)
    n+=1

    if(int(val1)==0):
        return 
    producto_medio(int(rn1),int(val1),n)
    return 0

producto_medio(rn,rn1,n)