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
            nombre = input(f" \n Ingrese el nombre del producto: ")
            precio = input(f" \n Ingrese el precio del producto: ")
            if precio > 0:
                print(f"\n precio ingresado correctamente")
            else:
                print(f"\n El precio no puede ser menor a 0")
            cantidad = int(input(f" \n Ingrese la cantidad del producto: "))
            if cantidad > 0:
                print(f"\n cantidad ingresado correctamente")
            else :
                print("La cantidad ingresad al inventario tiene que ser positiva")
        productos[codigo] = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad

        }

