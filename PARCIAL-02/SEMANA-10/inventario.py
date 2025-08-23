import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar()

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    try:
                        n, c, p = linea.strip().split(",")
                        self.productos[n] = Producto(n, int(c), float(p))
                    except ValueError:
                        print("⚠ Archivo corrupto en alguna línea, se omitió.")
        except FileNotFoundError:
            open(self.archivo, "w").close()
        except PermissionError:
            print("❌ No tienes permisos para leer el archivo.")

    def guardar(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos.values():
                    f.write(str(p) + "\n")
        except PermissionError:
            print("❌ No tienes permisos para escribir en el archivo.")

    def agregar(self, nombre, cantidad, precio):
        self.productos[nombre] = Producto(nombre, cantidad, precio)
        self.guardar()
        print(f"✔ Producto '{nombre}' añadido.")

    def actualizar(self, nombre, cantidad=None, precio=None):
        if nombre in self.productos:
            if cantidad is not None: self.productos[nombre].cantidad = cantidad
            if precio is not None: self.productos[nombre].precio = precio
            self.guardar()
            print(f"✔ Producto '{nombre}' actualizado.")
        else:
            print("❌ No existe el producto.")

    def eliminar(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar()
            print(f"✔ Producto '{nombre}' eliminado.")
        else:
            print("❌ No existe el producto.")

    def mostrar(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos.values():
                print(f"{p.nombre} - Cant: {p.cantidad}, Precio: {p.precio}")

def menu():
    inv = Inventario()
    while True:
        print("\n1. Agregar  2. Actualizar  3. Eliminar  4. Mostrar  5. Salir")
        op = input("Opción: ")
        if op == "1":
            inv.agregar(input("Nombre: "), int(input("Cantidad: ")), float(input("Precio: ")))
        elif op == "2":
            inv.actualizar(input("Nombre: "), int(input("Nueva cantidad: ")), float(input("Nuevo precio: ")))
        elif op == "3":
            inv.eliminar(input("Nombre: "))
        elif op == "4":
            inv.mostrar()
        elif op == "5":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
