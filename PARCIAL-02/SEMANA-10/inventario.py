import json
import os
import argparse
import tempfile
import stat

# ----- Modelo -----
class Producto:
    def __init__(self, sku, nombre, cantidad, precio):
        self.sku = str(sku).strip()
        self.nombre = str(nombre).strip()
        self.cantidad = int(cantidad)
        self.precio = float(precio)
        self._validar()

    def _validar(self):
        if not self.sku:
            raise ValueError("SKU vacío")
        if not self.nombre:
            raise ValueError("Nombre vacío")
        if self.cantidad < 0:
            raise ValueError("Cantidad < 0")
        if self.precio < 0:
            raise ValueError("Precio < 0")

    def a_dict(self):
        return {
            "sku": self.sku,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio,
        }

    @staticmethod
    def desde_dict(d):
        return Producto(d["sku"], d["nombre"], d["cantidad"], d["precio"])


# ----- Persistencia + Lógica -----
class Inventario:
    """
    Guarda en JSONL (una línea por producto).
    Carga inicial al crear la instancia.
    Escritura atómica (tmp + replace).
    """
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self._asegurar_archivo()
        self.cargar()

    def _asegurar_archivo(self):
        # Crea el archivo si no existe
        try:
            if not os.path.exists(self.archivo):
                with open(self.archivo, "w", encoding="utf-8"):
                    pass
        except PermissionError:
            print("[ERROR] Sin permisos para crear el archivo.")
        except OSError as e:
            print(f"[ERROR] No se pudo crear el archivo: {e}")

    def cargar(self):
        cargados, ignorados = 0, 0
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for i, linea in enumerate(f, 1):
                    linea = linea.strip()
                    if not linea:
                        continue
                    try:
                        d = json.loads(linea)
                        p = Producto.desde_dict(d)
                        self.productos[p.sku] = p
                        cargados += 1
                    except (json.JSONDecodeError, KeyError, ValueError) as e:
                        ignorados += 1
                        print(f"[AVISO] Línea {i} inválida: {e}. Se ignora.")
            print(f"[OK] Cargados: {cargados}. Ignorados: {ignorados}.")
        except FileNotFoundError:
            print("[AVISO] Archivo no encontrado. Se crea vacío.")
            self._asegurar_archivo()
        except PermissionError:
            print("[ERROR] Sin permisos para leer el archivo.")
        except OSError as e:
            print(f"[ERROR] Error al leer el archivo: {e}")

    def _guardar(self):
        # Escribe todo el inventario de forma atómica
        dir_dest = os.path.dirname(self.archivo) or "."
        try:
            fd, tmp_path = tempfile.mkstemp(prefix="inv_", suffix=".tmp", dir=dir_dest, text=True)
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as tmp:
                    for p in self.productos.values():
                        tmp.write(json.dumps(p.a_dict(), ensure_ascii=False) + "\n")
                os.replace(tmp_path, self.archivo)
                return True
            except Exception:
                try:
                    os.remove(tmp_path)
                except Exception:
                    pass
                raise
        except PermissionError:
            print("[ERROR] Sin permisos para escribir en el archivo.")
            return False
        except OSError as e:
            print(f"[ERROR] Error de E/S al guardar: {e}")
            return False

    # ----- CRUD -----
    def agregar(self, producto: Producto):
        if producto.sku in self.productos:
            print("[FALLO] Ya existe ese SKU.")
            return False
        self.productos[producto.sku] = producto
        if self._guardar():
            print("[OK] Producto añadido y guardado.")
            return True
        # revertir si falla
        self.productos.pop(producto.sku, None)
        print("[FALLO] No se pudo guardar. Se revierte.")
        return False

    def actualizar(self, sku, nombre=None, cantidad=None, precio=None):
        p = self.productos.get(sku)
        if not p:
            print("[FALLO] No existe ese SKU.")
            return False
        backup = Producto(p.sku, p.nombre, p.cantidad, p.precio)
        try:
            if nombre is not None and nombre != "":
                p.nombre = str(nombre).strip()
            if cantidad is not None:
                cantidad = int(cantidad)
                if cantidad < 0: raise ValueError("Cantidad < 0")
                p.cantidad = cantidad
            if precio is not None:
                precio = float(precio)
                if precio < 0: raise ValueError("Precio < 0")
                p.precio = precio
            p._validar()
        except (ValueError, TypeError) as e:
            print(f"[FALLO] Datos inválidos: {e}")
            return False

        if self._guardar():
            print("[OK] Producto actualizado y guardado.")
            return True
        # revertir si falla
        self.productos[sku] = backup
        print("[FALLO] No se pudo guardar. Se revierte.")
        return False

    def eliminar(self, sku):
        if sku not in self.productos:
            print("[FALLO] No existe ese SKU.")
            return False
        backup = self.productos.pop(sku)
        if self._guardar():
            print("[OK] Producto eliminado y guardado.")
            return True
        # revertir si falla
        self.productos[sku] = backup
        print("[FALLO] No se pudo guardar. Se revierte.")
        return False

    def listar(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        print("\nSKU         | Nombre                         | Cantidad | Precio")
        print("-" * 70)
        for p in sorted(self.productos.values(), key=lambda x: x.sku):
            print(f"{p.sku:<12} | {p.nombre:<30} | {p.cantidad:>8} | ${p.precio:,.2f}")


# ----- UI consola -----
def pedir_int(msg, minimo=0):
    while True:
        v = input(msg).strip()
        try:
            n = int(v)
            if n < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return n
        except ValueError:
            print("Número inválido.")

def pedir_float(msg, minimo=0.0):
    while True:
        v = input(msg).strip().replace(",", ".")
        try:
            n = float(v)
            if n < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return n
        except ValueError:
            print("Número inválido.")

def menu(inv: Inventario):
    while True:
        print("\n1. Listar  2. Agregar  3. Actualizar  4. Eliminar  5. Buscar  0. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            inv.listar()
        elif op == "2":
            sku = input("SKU: ").strip()
            nombre = input("Nombre: ").strip()
            cant = pedir_int("Cantidad: ", 0)
            prec = pedir_float("Precio: ", 0.0)
            try:
                inv.agregar(Producto(sku, nombre, cant, prec))
            except ValueError as e:
                print(f"[FALLO] Producto inválido: {e}")
        elif op == "3":
            sku = input("SKU a actualizar: ").strip()
            nombre = input("Nuevo nombre (enter para omitir): ").strip()
            nombre = nombre if nombre else None
            txt_cant = input("Nueva cantidad (enter para omitir): ").strip()
            cant = int(txt_cant) if txt_cant else None
            txt_prec = input("Nuevo precio (enter para omitir): ").strip().replace(",", ".")
            prec = float(txt_prec) if txt_prec else None
            inv.actualizar(sku, nombre, cant, prec)
        elif op == "4":
            sku = input("SKU a eliminar: ").strip()
            inv.eliminar(sku)
        elif op == "5":
            sku = input("SKU a buscar: ").strip()
            p = inv.productos.get(sku)
            print(p.a_dict() if p else "No existe.")
        elif op == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida.")


# ----- Pruebas rápidas -----
def pruebas():
    """
    Pruebas básicas:
    - Crea archivo si no existe
    - Agrega y bloquea duplicados
    - Ignora líneas corruptas
    - Simula archivo de solo lectura
    """
    import tempfile
    print("\n== PRUEBAS ==")
    with tempfile.TemporaryDirectory() as d:
        ruta = os.path.join(d, "inv_test.txt")
        inv = Inventario(ruta)
        print("[OK] Archivo creado." if os.path.exists(ruta) else "[FALLO] No se creó el archivo.")

        inv.agregar(Producto("A1", "Lapicero", 10, 0.5))
        inv.agregar(Producto("A2", "Cuaderno", 5, 2.8))
        inv.agregar(Producto("A1", "Duplicado", 1, 1.0))  # debe fallar

        # Inyectar líneas malas
        with open(ruta, "a", encoding="utf-8") as f:
            f.write('{"sku": "X", "nombre": "Malo", "cantidad": -1, "precio": 1}\n')  # inválido
            f.write('NO_JSON\n')  # corrupto

        print("[INFO] Recargando para verificar líneas malas...")
        inv2 = Inventario(ruta)  # carga e ignora las malas
        print(f"[OK] Productos cargados: {len(inv2.productos)}")

        # Simular solo lectura (puede variar por SO)
        try:
            os.chmod(ruta, stat.S_IREAD)
            inv2.agregar(Producto("A3", "Borrador", 3, 0.9))  # debería dar error de permisos
            print("[INFO] Si viste [ERROR] arriba, se manejó bien el permiso.")
        except Exception as e:
            print(f"[AVISO] No se pudo simular solo lectura: {e}")
        finally:
            try:
                os.chmod(ruta, stat.S_IWRITE | stat.S_IREAD)
            except Exception:
                pass
    print("== FIN PRUEBAS ==\n")


# ----- Main -----
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--archivo", default="inventario.txt", help="archivo de inventario")
    parser.add_argument("--probar", action="store_true", help="ejecuta pruebas y sale")
    args = parser.parse_args()

    if args.probar:
        pruebas()
        return

    inv = Inventario(args.archivo)
    menu(inv)

if __name__ == "__main__":
    main()
