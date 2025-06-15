# 🧠 Comparación: Programación Tradicional vs Programación Orientada a Objetos (POO)

Este repositorio presenta dos soluciones al mismo problema: **calcular el promedio semanal del clima**, implementadas bajo dos paradigmas distintos de programación en Python.

## 🔹 Programación Tradicional

- Se utiliza en el archivo: `promedio_clima_tradicional.py`
- Está basada en funciones simples que se encargan de:
  - Ingresar las temperaturas diarias.
  - Calcular el promedio semanal.
- El flujo del programa es lineal y fácil de seguir.
- Es útil para programas pequeños o de propósito específico.

## 🔹 Programación Orientada a Objetos (POO)

- Se utiliza en el archivo: `promedio_clima_poo.py`
- Se definen dos clases:
  - `ClimaDia` representa un día con su temperatura.
  - `SemanaClima` gestiona un conjunto de días y calcula el promedio.
- Se aplica **encapsulamiento** mediante atributos privados.
- Tiene una estructura más modular y escalable.
- Está preparada para una posible extensión con herencia o polimorfismo si el proyecto creciera.

## ⚖️ Comparación

| Aspecto                  | Tradicional                          | POO                                      |
|--------------------------|--------------------------------------|------------------------------------------|
| Organización             | Funciones independientes             | Clases con métodos                       |
| Reutilización            | Baja                                 | Alta                                     |
| Escalabilidad            | Limitada                             | Alta                                     |
| Encapsulamiento          | No                                   | Sí (atributos privados)                  |
| Ideal para               | Tareas simples                       | Proyectos más complejos o extensibles    |

## ✅ Conclusión

La **programación tradicional** es apropiada para tareas rápidas y simples.  
La **POO**, por su parte, permite una mejor organización del código, favorece la reutilización y facilita el mantenimiento en proyectos de mayor tamaño.

---

🎓 **Este ejercicio ayuda a comprender claramente cuándo conviene aplicar cada paradigma según el contexto del problema.**
