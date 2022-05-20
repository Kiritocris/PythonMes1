def menu():
    print("*****MENU******")
    print("Agregar producto: 1")
    print("Remover producto: 2")
    print("Añadir a cuenta: 3")
    print("Retirar de la cuenta: 4")
    print("Cobrar: 5")
    print("Salir: 0")


def add(Id,Nameprd,Priceprd,Identificador,Cant):
    print("Agregar un nuevo producto digite 1")
    print("Cancelar y salir digite 2")
    opc=int(input("Digite su opcion:"))
    if(opc==1):
        Id+=1
        Nameprd.append(input("Nombre de su producto: "))
        Priceprd.append(float(input("Precio de su producto: ")))
        Cant.append(int(input("Cantidad en stock: ")))
        Identificador.append(Id)
        return [Id,Nameprd,Priceprd,Identificador,Cant]
    else:
        return [Id,Nameprd,Priceprd,Identificador,Cant]


def rem(Id,Nameprd,Priceprd,Identificador,Cant):
    if(Id==5):
        print("No puedes eliminar mis propios productos U.U")
    else:
        print("Desea borrar el ultimo elemento agregado digite 1")
        print("Desea borrar un elemento especifico digite 2")
        print("Cancelar y salir digite 3")
        opc2=int(input("Digite su opcion:"))
        if(opc2==1):
            Id-=1
            Nameprd.pop()
            Priceprd.pop()
            Identificador.pop()
            Cant.pop()
            print("Hemos realizado su consulta")
        elif (opc2==2):
            i=5
            print("Elemetos disponibles a eliminar")
            for i in range(len(Nameprd)):
                if(i>=5):
                    print(Nameprd[i])
                    
            elemento=input("Elemento a eliminar: ")
            Idtemp=Nameprd.index(elemento)
            Nameprd.pop(Idtemp)
            Priceprd.pop(Idtemp)
            Identificador.pop(Idtemp)
            Cant.pop(Idtemp)
    return [Id,Nameprd,Priceprd,Identificador,Cant]

def addCarrito(Nameprd,Priceprd,Identificador,cuenta,Cant,Cuentacant):
    print("Seleccione el producto a agregar:")
    print("Esta es la lista de productos")
    for i in range(len(Nameprd)):
        print("Producto:",Nameprd[i],"En stock:",Cant[i],'\n')
    element=Nameprd.index(input("Escriba el elemento a agregar:"))
    sup=1
    cuenta+=1
    
    while sup != 0:
        rest=int(input("Digite la cantidad de productos a agregar:"))
        if(rest>Cant[element]):
            print("Supera el stock vuelve a intentarlo")
        else:
            Cant[element]=Cant[element]-rest
            sup=0
    Cuentacant.append(rest)
    print("Añadido al carrito...")
    return [Nameprd[element],Priceprd[element],Identificador[element],cuenta,Cant,Cuentacant]

def remCarrito(Namepdr,Cuentaname,Cuenta):
    print("Seleccione el producto a remover del carrito:")
    print("Esta es la lista de productos en el carrito")
    for i in Cuentaname:
        print(i,'\n')
    componente=input("Escriba el elemento a agregar:")
    element=Cuentaname.index(componente)
    element2=Namepdr.index(componente)
    Cuenta-=1
    print("Removiendo del carrito...")
    return [element,Cuenta,element2]
            
def sum(Cuentaid,Cuentaname,Cuentaprecio,Cuentacant):
    for i in range(len(Cuentaid)):
        print('\n',"ID:",Cuentaid[i]," Producto:",Cuentaname[i]," Cantidad:",Cuentacant[i]," Precio:",Cuentaprecio[i],)
    Total=0
    for i in range(len(Cuentaprecio)):
        Total+=(Cuentaprecio[i]*Cuentacant[i])
    print('\n', "Total a pagar:",Total)