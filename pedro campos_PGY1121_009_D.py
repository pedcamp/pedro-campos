def  grabar():
    list=[]
    j=True
    while j:
        h=input("ingrese (numero de identificacion fiscal)NIF:")
        b=input("ingrese nombre:")
        n=int(input("ingrese edad:"))
        g=int(input("si desea salir ingrese 1 si no seleccione cualquier otro numero:"))
        list1=[]
        cont=0
        while cont<=4:
            if len(h)==12:
                print("NIF correcto")
                list1.append(h)
            else:
                print("NIF incorrecto")
            if len(b)<=8:
                print("nombre correcto")
                list1.append(b)
            else:
                print("nombre incorrecto")
            if n>=0:
                print("edad correcta")
                list1.append(n)
            else:
                print("edad incorrecto")
        list.append(list1)
        if g==1:
            j=False
    return list
#def buscar():
#def imprimir():
def salir():
    print("usted a salido del programa de pedro campos vrs:1.0.0")
    False
a=1
while a:
    print("1)grabar \n2)buscar \n3)imprimir \n4)salir ")
    i=int(input("ingrese opcion:"))
    if i==1:
        grabar()
    if i==4:
        a=salir()
    