# tienda_en_linea.py

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"{self.nombre} - ${self.precio:.2f}")


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_producto(self, producto):
        self.carrito.append(producto)
        print(f"{producto.nombre} añadido al carrito.")

    def mostrar_carrito(self):
        print(f"\n=== Carrito de {self.nombre} ===")
        total = 0
        for prod in self.carrito:
            prod.mostrar()
            total += prod.precio
        print(f"Total a pagar: ${total:.2f}")


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"\n=== Productos en {self.nombre} ===")
        for i, p in enumerate(self.productos):
            print(f"{i + 1}. ", end="")
            p.mostrar()


# Crear tienda y productos base
tienda = Tienda("Tech Store")
tienda.agregar_producto(Producto("Mouse", 12.99))
tienda.agregar_producto(Producto("Teclado", 25.50))
tienda.agregar_producto(Producto("Pantalla", 120.00))

# Cliente interactivo
print("=== Bienvenido a la tienda en línea ===")
nombre_cliente = input("Ingrese su nombre: ")
cliente = Cliente(nombre_cliente)

while True:
    tienda.mostrar_productos()
    eleccion = int(input("Seleccione el número del producto a comprar (0 para salir): "))
    if eleccion == 0:
        break
    elif 1 <= eleccion <= len(tienda.productos):
        producto_seleccionado = tienda.productos[eleccion - 1]
        cliente.agregar_producto(producto_seleccionado)
    else:
        print("Opción inválida.")

cliente.mostrar_carrito()
