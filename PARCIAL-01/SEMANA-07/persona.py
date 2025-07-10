class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.
        Se ejecuta automáticamente al crear un objeto.
        Inicializa los atributos 'nombre' y 'edad'.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"[Constructor] Se ha creado una persona: {self.nombre}, {self.edad} años.")

    def saludar(self):
        """
        Método que imprime un saludo personalizado.
        """
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    def __del__(self):
        """
        Destructor de la clase Persona.
        Se ejecuta automáticamente cuando el objeto se elimina.
        Este método podría usarse para liberar recursos si fuera necesario.
        """
        print(f"[Destructor] El objeto de {self.nombre} ha sido destruido.")


if __name__ == "__main__":
    # Se crea una instancia de la clase Persona
    persona1 = Persona("Ana", 30)

    # Se llama a un método del objeto para mostrar su información
    persona1.saludar()

    # Al finalizar el programa, se elimina el objeto y se invoca el destructor automáticamente
