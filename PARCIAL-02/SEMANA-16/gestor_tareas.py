import tkinter as tk
from tkinter import messagebox

class GestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Campo de entrada para escribir nuevas tareas
        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=10)
        self.entrada.focus()

        # Botón para añadir la tarea escrita
        self.boton_añadir = tk.Button(root, text="Añadir Tarea", command=self.añadir_tarea)
        self.boton_añadir.pack()

        # Listbox para mostrar las tareas actuales
        self.lista_tareas = tk.Listbox(root, width=50, height=15)
        self.lista_tareas.pack(pady=10)

        # Botón para marcar tarea seleccionada como completada
        self.boton_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.pack(pady=2)

        # Botón para eliminar tarea seleccionada
        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=2)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.añadir_tarea())
        self.root.bind("<c>", lambda event: self.marcar_completada())
        self.root.bind("<C>", lambda event: self.marcar_completada())
        self.root.bind("<d>", lambda event: self.eliminar_tarea())
        self.root.bind("<D>", lambda event: self.eliminar_tarea())
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def añadir_tarea(self):
        texto = self.entrada.get().strip()
        if texto:
            self.lista_tareas.insert(tk.END, texto)
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Escribe una tarea antes de añadir.")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            texto = self.lista_tareas.get(indice)
            if not texto.startswith("[✔] "):
                self.lista_tareas.delete(indice)
                self.lista_tareas.insert(indice, "[✔] " + texto)
                self.lista_tareas.itemconfig(indice, {'fg': 'gray'})
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcarla como completada.")

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.lista_tareas.delete(seleccion[0])
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminarla.")

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()
