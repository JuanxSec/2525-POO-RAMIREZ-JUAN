# Tarea: Programación Orientada a Objetos
# Nombre: Juan Ramirez
# Descripción: Se aplica herencia, encapsulación y polimorfismo con clases de animales.

class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado para encapsulación
        self.__edad = edad     # Atributo privado para encapsulación

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):  # Método para modificar edad con encapsulación
        if edad >= 0:
            self.__edad = edad

    def hacer_sonido(self):
        return "El animal hace un sonido."  # Método base para polimorfismo

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Herencia de la clase Animal
        self.__raza = raza  # Atributo privado para encapsulación

    def get_raza(self):
        return self.__raza

    def hacer_sonido(self):  # Polimorfismo: sobrescribe el método de la clase base
        return f"{self.get_nombre()} dice: ¡Guau!"

# Crear objetos e imprimir sonidos
animal1 = Animal("AnimalX", 3)
perro1 = Perro("Firulais", 5, "Labrador")

print(animal1.hacer_sonido())
print(perro1.hacer_sonido())
