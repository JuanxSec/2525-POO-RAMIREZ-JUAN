import json
import os

ARCHIVO = "inventario.json"

class Producto:
    def __init__(self, id_: int, nombre: str, cantidad: int, precio: float):
        self.set_id(id_)
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)
        self.set_precio(precio)

    def get_id(self): return self._id
    def get_nombre(self): return self._nombre
    def get_cantidad(self): return self._cantidad
    def get_precio(self): return self._precio

    def set_id(self, v):
        if v <= 0: raise ValueError("ID inválido")
        self._id = v

    def set_nombre(self, v):
        if not v.strip(): raise ValueError("Nombre vacío")
        self._nombre = v.strip()

    def set_cantidad(self, v):
        if v < 0: raise ValueError("Cantidad inválida")
        self._cantidad = v

    def set_precio(self, v):
        if v < 0: raise ValueError("Precio inválido")
        self._precio = float(v)

    def to_dict(self):
        return {"id": self._id, "nombre": self._nombre,
                "cantidad": self._cantidad, "precio": self._precio}

    @staticmethod
    def from_dict(d):
        return Producto(d["id"], d["nombre"], d["cantidad"], d["precio"])

    def __str__(self):
        return f"ID:{self._id} | {self._nombre} | Cant:{self._cantidad} | ${self._precio:.2f}"


class Inventario:
    def __init__(self):
        self._productos = {}

    def anadir(self, p: Producto):
        if p.get_id() in self._productos: raise KeyError("ID duplicado")
        self._productos[p.get_id()] = p

    def eliminar(self, idp: int):
        if idp not in self._productos: raise KeyError("No existe ID")
        del self._productos[idp]

    def actualizar_cantidad(self, idp: int, cant: int):
        self._existe(idp).set_cantidad(cant)

    def actualizar_precio(self, idp: int, prec: float):
        self._existe(idp).set_precio(prec)

    def buscar_nombre(self, txt: str):
        t = txt.lower().strip()
        return [p for p in self._productos.values() if t in p.get_nombre().lower()]

    def listar(self):
        return [self._productos[k] for k in sorted(self._productos.keys())]

    def guardar(self, ruta=ARCHIVO):
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self._productos.values()], f, ensure_ascii=False, indent=2)

    def cargar(self, ruta=ARCHIVO):
        self._productos.clear()
        if not os.path.exists(ruta): return
        with open(ruta, "r", encoding="utf-8") as f:
            for d in json.load(f):
                p = Producto.from_dict(d)
                self._productos[p.get_id()] = p

    def _existe(self, idp: int):
        if idp not in self._productos: raise KeyError("No existe ID")
        return self._productos[idp]


def leer_int(msg):
    while True:
        try: return int(input(msg))
        except: print("Debe ser entero")

def leer_float(msg):
    while True:
        try: return float(input(msg).replace(",", "."))
        except: print("Debe ser número")

def leer_txt(msg):
    while True:
        s = input(msg).strip()
        if s: return s
        print("No vacío")


def menu():
    inv = Inventario(); inv.cargar()
    while True:
        print("\n1) Añadir  2) Eliminar  3) Act.Cant  4) Act.Prec  5) Buscar  6) Mostrar  7) Guardar  8) Cargar  0) Salir")
        op = input("Opción: ").strip()
        try:
            if op == "1":
                inv.anadir(Producto(leer_int("ID: "), leer_txt("Nombre: "),
                                    leer_int("Cantidad: "), leer_float("Precio: ")))
            elif op == "2":
                inv.eliminar(leer_int("ID: "))
            elif op == "3":
                inv.actualizar_cantidad(leer_int("ID: "), leer_int("Nueva cantidad: "))
            elif op == "4":
                inv.actualizar_precio(leer_int("ID: "), leer_float("Nuevo precio: "))
            elif op == "5":
                for p in inv.buscar_nombre(leer_txt("Buscar: ")): print(p)
            elif op == "6":
                for p in inv.listar(): print(p) if inv.listar() else print("(inventario vacío)")
            elif op == "7":
                inv.guardar(); print("Guardado")
            elif op == "8":
                inv.cargar(); print("Cargado")
            elif op == "0":
                inv.guardar(); break
            else:
                print("Opción inválida")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    menu()
