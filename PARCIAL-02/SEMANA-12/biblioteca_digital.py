from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple

@dataclass(frozen=True)
class Libro:
    titulo_autor: Tuple[str, str]
    categoria: str
    isbn: str

    @property
    def titulo(self): return self.titulo_autor[0]
    @property
    def autor(self): return self.titulo_autor[1]

@dataclass
class Usuario:
    nombre: str
    user_id: str
    prestados: List[str] = field(default_factory=list)

class Biblioteca:
    def __init__(self):
        self.libros: Dict[str, Libro] = {}
        self.usuarios: Dict[str, Usuario] = {}
        self.ids_usuarios: Set[str] = set()
        self.prestamos: Dict[str, str] = {}

    def registrar_usuario(self, nombre: str, user_id: str):
        if user_id in self.ids_usuarios:
            raise ValueError("ID ya existe")
        self.ids_usuarios.add(user_id)
        self.usuarios[user_id] = Usuario(nombre, user_id)

    def dar_baja_usuario(self, user_id: str):
        u = self.usuarios.get(user_id)
        if not u: raise ValueError("Usuario no existe")
        if u.prestados: raise ValueError("Tiene libros prestados")
        self.ids_usuarios.remove(user_id)
        del self.usuarios[user_id]

    def anadir_libro(self, libro: Libro):
        if libro.isbn in self.libros:
            raise ValueError("ISBN ya existe")
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn: str):
        if isbn not in self.libros: raise ValueError("No existe")
        if isbn in self.prestamos: raise ValueError("Está prestado")
        del self.libros[isbn]

    def prestar_libro(self, user_id: str, isbn: str):
        u = self.usuarios.get(user_id)
        if not u: raise ValueError("Usuario no existe")
        if isbn not in self.libros: raise ValueError("Libro no existe")
        if isbn in self.prestamos: raise ValueError("Ya prestado")
        self.prestamos[isbn] = user_id
        u.prestados.append(isbn)

    def devolver_libro(self, user_id: str, isbn: str):
        if self.prestamos.get(isbn) != user_id:
            raise ValueError("No coincide")
        del self.prestamos[isbn]
        try:
            self.usuarios[user_id].prestados.remove(isbn)
        except: pass

    def buscar_por_titulo(self, q: str) -> List[Libro]:
        t = q.lower()
        return [l for l in self.libros.values() if t in l.titulo.lower()]

    def buscar_por_autor(self, q: str) -> List[Libro]:
        a = q.lower()
        return [l for l in self.libros.values() if a in l.autor.lower()]

    def buscar_por_categoria(self, c: str) -> List[Libro]:
        c = c.lower()
        return [l for l in self.libros.values() if l.categoria.lower() == c]

    def listar_prestados_usuario(self, user_id: str) -> List[Libro]:
        u = self.usuarios.get(user_id)
        if not u: raise ValueError("Usuario no existe")
        return [self.libros[i] for i in u.prestados if i in self.libros]

if __name__ == "__main__":
    b = Biblioteca()
    b.registrar_usuario("Ana", "U1")
    b.registrar_usuario("Luis", "U2")

    b.anadir_libro(Libro(("El Quijote", "Cervantes"), "Clasico", "ISBN1"))
    b.anadir_libro(Libro(("Cien años de soledad", "García Márquez"), "Realismo", "ISBN2"))
    b.anadir_libro(Libro(("Python Básico", "Guido"), "Programacion", "ISBN3"))

    b.prestar_libro("U1", "ISBN2")
    print([l.titulo for l in b.listar_prestados_usuario("U1")])

    b.devolver_libro("U1", "ISBN2")
    print([l.titulo for l in b.buscar_por_autor("garcía")])

    b.quitar_libro("ISBN3")
    b.dar_baja_usuario("U2")
