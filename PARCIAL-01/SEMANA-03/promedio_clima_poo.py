# Programa para calcular el promedio semanal del clima
# Enfoque: Programación Orientada a Objetos

# Clase base para representar datos climáticos
class ClimaDia:
    def __init__(self, temperatura):
        # Encapsulamos el atributo con doble guion bajo
        self.__temperatura = temperatura

    # Método getter para acceder a la temperatura
    def obtener_temperatura(self):
        return self.__temperatura

# Clase SemanaClima que gestiona una colección de ClimaDia
# (Aquí podríamos aplicar herencia o polimorfismo si tuviéramos más tipos de clima, pero no son necesarios en esta tarea)
class SemanaClima:
    def __init__(self):
        self.__dias = []  # Lista privada que almacena los objetos ClimaDia

    # Método para agregar un nuevo día con su temperatura
    def agregar_dia(self, temperatura):
        dia = ClimaDia(temperatura)
        self.__dias.append(dia)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        total = sum(dia.obtener_temperatura() for dia in self.__dias)
        return total / len(self.__dias)

# Función principal que ejecuta el programa
def main():
    print("== Promedio Semanal del Clima (Programación Orientada a Objetos) ==")
    semana = SemanaClima()  # Creamos un objeto de tipo SemanaClima

    for i in range(1, 8):  # 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {i}: "))
        semana.agregar_dia(temp)

    promedio = semana.calcular_promedio()
    print(f"El promedio semanal es: {promedio:.2f} °C")

# Ejecutar el programa
main()
