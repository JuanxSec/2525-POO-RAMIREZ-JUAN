# Adaptado por Juan Ramirez
# Dashboard personalizado para gestión de tareas de POO

import os

def limpiar_pantalla():
    # Limpia la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_bienvenida():
    print("=" * 50)
    print("        Bienvenido al Dashboard de POO")
    print("        Autor: Juan Ramirez (JuanxSec)")
    print("=" * 50)

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("⚠️  El archivo no se encontró.")
    except Exception as e:
        print(f"⚠️  Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 1/1.3. Principios SOLID/ejemplo_SOLID.py',
        '3': 'UNIDAD 2/2.1. Clases y Objetos/ejemplo_clase_objeto.py',
        '4': 'UNIDAD 2/2.2. Herencia/ejemplo_herencia.py',
        '5': 'UNIDAD 3/3.1. Polimorfismo/ejemplo_polimorfismo.py'
        # Puedes seguir agregando más rutas si las creas
    }

    while True:
        limpiar_pantalla()
        mostrar_bienvenida()

        print("\n📚 Menu Principal - Selecciona un script para ver su código:\n")
        for key in opciones:
            nombre_script = os.path.basename(opciones[key])
            print(f"{key} - {nombre_script}")
        print("0 - Salir")

        eleccion = input("\n🔸 Elige una opción: ")
        if eleccion == '0':
            print("👋 ¡Hasta pronto!")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            limpiar_pantalla()
            mostrar_codigo(ruta_script)
            input("\nPresiona Enter para volver al menú...")
        else:
            print("❌ Opción no válida. Intenta de nuevo.")
            input("\nPresiona Enter para continuar...")

# Punto de entrada
if __name__ == "__main__":
    mostrar_menu()
