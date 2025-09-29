import tkinter as tk
from tkinter import messagebox

# Creamos una clase para encapsular toda la lógica de la aplicación
class ListaDeTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Aquí guardaremos todas las tareas (cada una como un diccionario con texto y estado)
        self.tareas = []

        # ----- INTERFAZ -----

        # Campo de entrada para escribir la nueva tarea
        self.entrada = tk.Entry(root, width=30)
        self.entrada.pack(pady=10)

        # Si el usuario presiona Enter, también se añadirá la tarea
        self.entrada.bind("<Return>", self.agregar_tarea_evento)

        # Botón para añadir la tarea escrita en el Entry
        self.boton_añadir = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_añadir.pack(pady=5)

        # Listbox donde se mostrarán las tareas
        self.lista = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
        self.lista.pack(pady=10)

        # Doble clic sobre una tarea = marcarla como completada
        self.lista.bind("<Double-Button-1>", self.marcar_completada_evento)

        # Botón para marcar como completada la tarea seleccionada
        self.boton_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        # Botón para eliminar la tarea seleccionada
        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

    # Función que se llama cuando se presiona Enter en el campo de entrada
    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    # Añade una nueva tarea a la lista
    def agregar_tarea(self):
        texto = self.entrada.get().strip()  # Eliminamos espacios en blanco
        if texto:
            # Guardamos la tarea con un estado de completada en False
            self.tareas.append({"texto": texto, "completada": False})
            self.actualizar_lista()
            self.entrada.delete(0, tk.END)  # Limpiamos el campo de entrada
        else:
            # Si no se escribió nada, mostramos una advertencia
            messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea.")

    # Doble clic sobre una tarea = marcar como completada
    def marcar_completada_evento(self, event):
        self.marcar_completada()

    # Marca o desmarca una tarea como completada
    def marcar_completada(self):
        seleccion = self.lista.curselection()
        if seleccion:
            indice = seleccion[0]
            # Cambiamos el estado de completada (de True a False o viceversa)
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            self.actualizar_lista()
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcarla como completada.")

    # Elimina la tarea seleccionada
    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]  # Quitamos la tarea de la lista
            self.actualizar_lista()
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminar.")

    # Actualiza el contenido del Listbox con las tareas actuales
    def actualizar_lista(self):
        self.lista.delete(0, tk.END)  # Borra todo lo que hay en el Listbox
        for tarea in self.tareas:
            texto = tarea["texto"]
            # Si la tarea está completada, le agregamos un ✔️ al principio
            if tarea["completada"]:
                texto = f"✔️ {texto}"
            self.lista.insert(tk.END, texto)

# Aquí se ejecuta la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareasApp(root)
    root.mainloop()
