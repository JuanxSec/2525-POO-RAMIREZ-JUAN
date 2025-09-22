import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass

@dataclass
class Evento:
    fecha: str
    hora: str
    descripcion: str

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.eventos = []
        self._crear_interfaz()

    def _crear_interfaz(self):
        frame_tabla = ttk.LabelFrame(self.root, text="Eventos")
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(fill=tk.BOTH, expand=True)

        frame_form = ttk.LabelFrame(self.root, text="Nuevo Evento")
        frame_form.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(frame_form, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_fecha = ttk.Entry(frame_form)
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_hora = ttk.Entry(frame_form)
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_desc = ttk.Entry(frame_form, width=50)
        self.entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        frame_botones = ttk.Frame(self.root)
        frame_botones.pack(fill=tk.X, padx=10, pady=10)

        ttk.Button(frame_botones, text="Agregar", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Salir", command=self.root.quit).pack(side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        fecha = self.entry_fecha.get().strip()
        hora = self.entry_hora.get().strip()
        desc = self.entry_desc.get().strip()

        if not fecha or not hora or not desc:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        evento = Evento(fecha, hora, desc)
        self.eventos.append(evento)
        self.tree.insert("", tk.END, values=(evento.fecha, evento.hora, evento.descripcion))

        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Selecciona un evento para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar el evento seleccionado?"):
            self.tree.delete(seleccionado)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
