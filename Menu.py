#Gabriela Celeste Tarqui Quintanilla
import math
def resdiv(dividendo,divisor):
    cociente=0
    while (dividendo>=divisor):
        dividendo=dividendo-divisor
        cociente=cociente+1
    return cociente
def resto(dividendo,divisor):
    cociente=resdiv(dividendo,divisor)
    resto=dividendo-(divisor*cociente)
    return resto
def cambio(numero,base):
    d=0
    aux=0
    while(numero>0):
        x=resto(numero,base)
        numero=resdiv(numero,base)
        aux=aux+x*10**d
        d=d+1
    print(aux)
def uno():
    a=int(input("Ingrese el dividendo: "))
    b=int(input("Ingrese el divisor: "))
    res=resdiv(a,b)
    rest=resto(a,b)
    print("El resultado es: ",res," y tiene residuo de: ",rest)       
def dos():
    a=int(input("Ingrese un numero (mayor a 99999999999999): "))
    if(a>99999999999999):
        b=resdiv(a,2)
        print(1,a)
        for i in range(2,b):
            rest=resto(a,i)
            if(rest==0):
                c=resdiv(a,i)
                print(i,c)
    else:
        print("Error, el numero debe ser mayor a 99999999999999")
def tres():
    a=int(input("Ingrese un numero (mayor a 99999999): "))
    if(a>99999999):
        b=int(math.log10(a))
        b=b+1
        j=b
        for i in range(b-3,-1,-1):
            d=resto(a,(10**j))
            c=resdiv(d,(10**i))
            a1=resto(c,10)
            a2=resdiv(c,100)
            if(a1==a2):
                print(c,"es capicua")
            else:
                print(c,"no es capicua")
            j=j-1
    else:
        print("Error, el numero debe ser mayor a 99999999") 
def cuatro():
    a=int(input("Ingrese el numero: "))
    b=int(input("Ingrese la base a la que se convertira: "))
    cambio(a,b)
usuarios=["Rodrigo","Alana","Tadeo"]
contraseña=["w1p5h4","3qtv2z3wx4","t2vh3~"] #saludo,imprevisto,perdiz
usuarioi=input("Ingrese su usuario: ")
contraseñai=input("Ingrese su contraseña: ")
encriptacion=""
a=len(usuarios)
b=len(contraseñai)
for i in range(a):
    if(usuarios[i]==usuarioi):
        for j in range(b):
            if(contraseñai[j]=='a'):
                encriptacion=encriptacion+"1"
            elif(contraseñai[j]=='e'):
                encriptacion=encriptacion+"2"
            elif(contraseñai[j]=='i'):
                encriptacion=encriptacion+"3"
            elif(contraseñai[j]=='o'):
                encriptacion=encriptacion+"4"
            elif(contraseñai[j]=='u'):
                encriptacion=encriptacion+"5"
            else:
                c=ord(contraseñai[j])
                c=c+4
                d=chr(c)
                encriptacion=encriptacion+d
        if(contraseña[i]==encriptacion):
            opcion=1
            nuser=i
            while(opcion<6 and opcion>0):
                print("""---------------MENU---------------
---------Elija una opcion---------
1.- Division de dos numeros
2.- Divisores
3.- Numeros Capicua
4.- Cambio de Base
5.- Salir""")
                opcion=int(input())
                if(opcion==1):
                    print("Operación 1")
                    uno()
                elif(opcion==2):
                    print("Operación 2")
                    dos()
                elif(opcion==3):
                    print("Operación 3")
                    tres()
                elif(opcion==4):
                    print("Operación 4")
                    cuatro()
                else:
                    print("El programa finaliza....\n")
                    opcion=10
                    print("Opcional")
                    contraseñai=str(contraseña[nuser])
                    b=len(contraseñai)
                    comparar=encriptacion
                    encriptacion=""
                    for j in range(b):
                        if(contraseñai[j]=='a'):
                            encriptacion=encriptacion+"1"
                        elif(contraseñai[j]=='e'):
                            encriptacion=encriptacion+"2"
                        elif(contraseñai[j]=='i'):
                            encriptacion=encriptacion+"3"
                        elif(contraseñai[j]=='o'):
                            encriptacion=encriptacion+"4"
                        elif(contraseñai[j]=='u'):
                            encriptacion=encriptacion+"5"
                        else:
                            c=ord(contraseñai[j])
                            c=c+4
                            d=chr(c)
                            encriptacion=encriptacion+d
                    if(comparar==encriptacion):
                        print("La funcion es biyectiva")
                    else:
                        print(comparar," no es igual a ",encriptacion)
                        print("La funcion es inyectiva")
        else:
            print("Contraseña erronea")