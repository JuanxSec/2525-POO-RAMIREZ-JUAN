# Programa para calcular el promedio semanal del clima
# Enfoque: Programación Tradicional usando funciones

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(1, 8):  # Para cada día de la semana
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Función principal que coordina el flujo del programa
def main():
    print("== Promedio Semanal del Clima (Programación Tradicional) ==")
    temperaturas = ingresar_temperaturas()       # Entrada de datos
    promedio = calcular_promedio(temperaturas)   # Procesamiento
    print(f"El promedio semanal es: {promedio:.2f} °C")  # Salida

# Ejecutar el programa
main()
