Productos = {}
print("Actividad 06")
print("----INVENTARIO DE UNA TIENDA----")
CantProductos = int(input(f" Ingrese la cantidad de productos que desea ingresar: "))
for i in range(CantProductos):
    print(f"Ingrese el producto {i+1}: ")
    codigo = input(f" Ingrese el codigo del producto: ")
    if codigo in Productos:
        print(f"Codigo ya ingresado")
    else:
        nombre = input(f" Ingrese el nombre del producto: ")
        precio = float(input(f" Ingrese el precio del producto: "))
        if precio <= 0:
            print(f" El precio no puede ser menor a 0")
        else:
            cantidad = int(input(f" Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad ingresad al inventario tiene que ser positiva")
            else:
                Productos[codigo] = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
                }
                print("producto registrado")


print("Inventario total de productos: ")
for codigo,inventario in Productos.items():
    print(f"Codigo : {codigo}" )
    print(f"Nombre : {inventario['nombre']}" )
    print(f"Precio : {inventario['precio']}" )
    print(f"Cantidad : {inventario['cantidad']}" )
