Productos = {}
opcion = ""
while opcion != "6":
    print("Actividad 06")
    print("----INVENTARIO DE UNA TIENDA----")
    print("Bienvenidos")
    print("1.- Agregar producto")
    print("2.- Mostrar lista completa de productos")
    print("3.- Buscar por medio de un codigo y mostrar detalles")
    print("4.- Mostrar valor total de inventario")
    print("5.- Mostrar cuantos productos hay por categoria")
    print("6.- Salir del programa")
    opcion = input(f" Ingrese la opcion que desea ingresar: ")
    if opcion == "1":
        CantProductos = int(input(f" \n Ingrese la cantidad de productos que desea ingresar: "))
        for i in range(CantProductos):
            print(f"Ingrese el producto {i + 1}: ")
            codigo = input(f" Ingrese el codigo del producto: ")
            if codigo in Productos:
                print(f"Codigo ya ingresado")
            else:
                nombre = input(f" Ingrese el nombre del producto: ")
                categoria = input(f" Ingrese el categoria del producto: ")
                talla = input(f" Ingrese el talla del producto: ")
                precio = float(input(f" Ingrese el precio del producto: "))
                if precio <= 0:
                    print(f" El precio no puede ser menor a 0")
                else:
                    cantidad = int(input(f" Ingrese la cantidad del producto: "))
                    if cantidad < 0:
                        print("La cantidad ingresad al inventario tiene que ser positiva")
                    else:
                        Productos[codigo] = {
                            "Nombre": nombre,
                            "Categoria": categoria,
                            "Talla": talla,
                            "Precio": precio,
                            "Cantidad": cantidad
                        }
                        print("producto registrado")
    elif opcion == "2":
        print("Inventario total de productos: ")
        for codigo, inventario in Productos.items():
            print(f"Codigo : {codigo}")
            print(f"Nombre : {inventario['Nombre']}")
            print(f"Categoria : {inventario['Categoria']}")
            print(f"Talla : {inventario['Talla']}")
            print(f"Precio : {inventario['Precio']}")
            print(f"Cantidad : {inventario['Cantidad']}")
    elif opcion == '3':
        print("Ingrese el codigo del producto que desea buscar: ")
        buscar = input(f" Ingrese el codigo del producto: ")
        if buscar in Productos:
            print(f"Nombre del producto: {Productos[buscar]['Nombre']}")
            print(f"Categoria : {inventario['Categoria']}")
            print(f"Talla : {inventario['Talla']}")
            print(f"El precio del producto: {Productos[buscar]['Precio']}")
            print(f"La cantidad existente es: {Productos[buscar]['Cantidad']}")
        else:
            print("No se encontro el producto o no existe")
    elif opcion == '4':
        Valor = 0
        for producto in Productos.values():
            Valor += producto['Precio'] * producto['Cantidad']
            print(f"1 El valor total del inventario es: Q{Valor:.2f}")
    elif opcion == '5':
        print("Categorías")
    elif opcion == '6':
        print = ("Gracias poe utilizar nuestro programa bye")
    else:
        print("Opcion no valida")