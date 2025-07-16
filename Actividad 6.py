productos = {}
print("Actividad 06")
print("----INVENTARIO DE UNA TIENDA----")
productos = int(input(f" \n Ingrese la cantidad de productos que desea ingresar: "))
for i in range(productos):
    print(f"\n Ingrese el producto {i+1}: ")
    while(productos > 0):
        print(f"\n Ingrese los siguientes datos")
        codigo = input(f" \n Ingrese el codigo del producto: ")
        if codigo == codigo:
            print(f"\n Codigo ya ingresado")
            break
        else:
            productos -= 1


