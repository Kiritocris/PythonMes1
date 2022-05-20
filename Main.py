#from Funcionesproyecto import menufrom multiprocessing.sharedctypes import Value
from operator import index
import Funciones as ftp
import os

os.system("cls")

Id=5
Nameprd=["Laptop","Monitor","Mouse","Headset","Keyboard"]
Priceprd=[200,150,40,100,50]
Identificador=[1,2,3,4,5]
Cant=[20,20,20,20,20]
Cuenta=0
Cuentaname=[]
Cuentaprecio=[]
Cuentacant=[]
Cuentaid=[]
opc=1
while opc != 0:
    ftp.menu()
    opc=int(input("Digita alguna seleccion:"))

    if(opc == 1):

        os.system ("cls")
        print("Quieres agregar un nuevo producto")
        val=ftp.add(Id,Nameprd,Priceprd,Identificador,Cant)
        Id=val[0]
        Nameprd=val[1]
        Priceprd=val[2]
        Identificador=val[3]
        Cant=val[4]

    elif(opc == 2):

        os.system ("cls")
        print("Quieres eliminar un producto")
        val=ftp.rem(Id,Nameprd,Priceprd,Identificador,Cant)
        Id=val[0]
        Nameprd=val[1]
        Priceprd=val[2]
        Identificador=val[3]
        Cant=val[4]

    elif(opc == 3):

        os.system ("cls")
        print("Quieres añadir un producto a la cesta")
        val=ftp.addCarrito(Nameprd,Priceprd,Identificador,Cuenta,Cant,Cuentacant)
        Cuentaname.append(val[0])
        Cuentaprecio.append(val[1])
        Cuentaid.append(val[2])
        Cuenta=val[3]
        Cant=val[4]
        Cuentacant=val[5]

    elif(opc == 4):
        if(Cuenta==0):
            print("No haz comprado nada U.U")
        else:
            os.system ("cls")
            print("Quieres eliminar un producto de la cesta")
            index=ftp.remCarrito(Nameprd,Cuentaname,Cuenta)
            Cuentaname.pop(index[0])
            Cuentaprecio.pop(index[0])
            Cuentaid.pop(index[0])
            dev=Cuentacant[index[0]]
            Cuentacant.pop(index[0])
            Cuenta=index[1]
            Cant[index[2]]=Cant[index[2]]+dev


        

    elif(opc == 5):
        os.system ("cls")
        if(Cuenta==0):
            print("No haz comprado nada U.U")
        else:
            print("***TOTAL Y DESGLOSE***")
            ftp.sum(Cuentaid,Cuentaname,Cuentaprecio,Cuentacant)
            


    os.system ("pause")
    os.system ("cls")

print("Gracias por visitarnos nos vemos c:")