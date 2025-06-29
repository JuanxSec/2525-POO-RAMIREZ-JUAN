# Conversor de centímetros a metros usando Programación Orientada a Objetos.
# Solicita una longitud al usuario, la convierte a metros y verifica si es mayor o igual a un metro.

class LengthConverter:
    """
    Clase que permite convertir una longitud de centímetros a metros
    y determinar si es mayor o igual a un metro.
    """

    def __init__(self, user_name: str, length_cm: float):
        """
        Inicializa el conversor con el nombre del usuario y la longitud en centímetros.
        """
        self.user_name: str = user_name
        self.length_cm: float = length_cm
        self.length_m: float = 0.0
        self.is_greater_than_one: bool = False
        self.length_cm_integer: int = int(length_cm)  # uso adicional de int

    def convert_to_meters(self):
        """
        Convierte los centímetros a metros.
        """
        self.length_m = self.length_cm / 100

    def check_if_greater_than_one(self):
        """
        Verifica si la longitud es mayor o igual a un metro.
        """
        self.is_greater_than_one = self.length_m >= 1

    def display_result(self):
        """
        Muestra el resultado final al usuario.
        """
        print(f"\n👋 Hola {self.user_name}!")
        print(f"Ingresaste: {self.length_cm_integer} cm")
        print(f"Equivale a: {self.length_m:.2f} metros.")

        if self.is_greater_than_one:
            print("✅ La longitud es mayor o igual a un metro.")
        else:
            print("❌ La longitud es menor a un metro.")


# ======= BLOQUE PRINCIPAL =======

# Solicitar datos al usuario
user_name_input: str = input("¿Cuál es tu nombre?: ")
length_input_cm: float = float(input("Ingresa una longitud en centímetros: "))

# Crear objeto de conversión
converter = LengthConverter(user_name=user_name_input, length_cm=length_input_cm)

# Ejecutar operaciones
converter.convert_to_meters()
converter.check_if_greater_than_one()
converter.display_result()

# Tipos de datos utilizados:
# - string: user_name_input, user_name
# - float: length_input_cm, length_cm, length_m
# - int: length_cm_integer
# - boolean: is_greater_than_one
