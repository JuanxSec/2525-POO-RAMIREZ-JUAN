import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, ventana):
        ventana.title("Gestor de Datos Básico")
        ventana.geometry("400x300")

        # Etiqueta de instrucción
        self.lbl = tk.Label(ventana, text="Escribe un dato:")
        self.lbl.pack(pady=5)

        # Entrada de texto
        self.caja_texto = tk.Entry(ventana, width=35)
        self.caja_texto.pack(pady=5)

        # Botón para agregar
        self.boton_agregar = tk.Button(ventana, text="Agregar", command=self.agregar)
        self.boton_agregar.pack(pady=5)

        # Botón para limpiar
        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.pack(pady=5)

        # Etiqueta para lista
        self.lbl_lista = tk.Label(ventana, text="Lista de datos:")
        self.lbl_lista.pack(pady=5)

        # Lista para mostrar los datos
        self.lista = tk.Listbox(ventana, width=45)
        self.lista.pack(pady=5)

    def agregar(self):
        texto = self.caja_texto.get()
        if texto != "":
            self.lista.insert(tk.END, texto)
            self.caja_texto.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "No escribiste nada")

    def limpiar(self):
        self.caja_texto.delete(0, tk.END)

# Código principal
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
