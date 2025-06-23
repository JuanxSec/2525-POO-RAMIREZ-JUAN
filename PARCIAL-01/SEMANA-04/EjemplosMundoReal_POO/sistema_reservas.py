# sistema_reservas.py

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Cliente: {self.nombre} | Teléfono: {self.telefono}")


class Reserva:
    def __init__(self, cliente, fecha, hora):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora

    def mostrar_reserva(self):
        print(f"Reserva para {self.cliente.nombre} el {self.fecha} a las {self.hora}.")


class Consultorio:
    def __init__(self):
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def mostrar_reservas(self):
        print("\n=== Reservas Registradas ===")
        for reserva in self.reservas:
            reserva.mostrar_reserva()


# Interfaz interactiva
consultorio = Consultorio()

print("=== Sistema de Reservas ===")
while True:
    nombre = input("\nIngrese nombre del cliente: ")
    telefono = input("Ingrese teléfono: ")
    fecha = input("Ingrese fecha de la reserva (YYYY-MM-DD): ")
    hora = input("Ingrese hora de la reserva (HH:MM): ")

    cliente = Cliente(nombre, telefono)
    reserva = Reserva(cliente, fecha, hora)
    consultorio.agregar_reserva(reserva)

    opcion = input("¿Desea agregar otra reserva? (s/n): ")
    if opcion.lower() != 's':
        break

consultorio.mostrar_reservas()
