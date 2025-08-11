# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados para aplicar encapsulación
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id}, Nombre: {self.__nombre}, Cantidad: {self.__cantidad}, Precio: ${self.__precio:.2f}"


# Clase que maneja la lista de productos y sus operaciones
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Verifica que el ID no esté repetido
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("⚠ Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado.")
                return
        print("⚠ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("✅ Producto actualizado.")
                return
        print("⚠ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("🔍 Resultados de la búsqueda:")
            for p in encontrados:
                print(p)
        else:
            print("⚠ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            print("\n📦 Inventario actual:")
            for p in self.productos:
                print(p)
        else:
            print("⚠ Inventario vacío.")


# Menú interactivo en consola
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_prod = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_prod, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_prod = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == "3":
            id_prod = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            inventario.actualizar_producto(
                id_prod,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Ingrese el nombre o parte del nombre: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠ Opción no válida.")


# Ejecutar el menú si se corre el script directamente
if __name__ == "__main__":
    menu()
