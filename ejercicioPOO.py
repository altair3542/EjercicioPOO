# Ejercicio Completo: Sistema de Gestión de Biblioteca
# Descripción:
# Crear un sistema de gestión de biblioteca que permita manejar libros y revistas, gestionar usuarios y préstamos, y realizar búsquedas en el catálogo de publicaciones. El sistema debe utilizar los principios de programación orientada a objetos: encapsulamiento, herencia y polimorfismo.
# Requisitos:
# 1.	Encapsulamiento: Usa atributos protegidos para manejar los datos de las publicaciones.
# 2.	Herencia: Crea clases Libro y Revista que hereden de la clase Publicacion.
# 3.	Polimorfismo: Implementa métodos polimórficos para mostrar información específica de cada tipo de publicación.
# 4.	Gestión de Préstamos: Implementa una clase Usuario que pueda tomar prestadas publicaciones.
# 5.	Búsquedas: Permite buscar publicaciones por título, autor o año.

#creamos la clase publicación.

class Publicacion:
    def __init__(self, titulo, autor, año):
        self._titulo = titulo
        self._autor = autor
        self._año = año

    def mostrar_informacion(self):
        print(f"Publicación: {self._titulo}, Autor: {self._autor}, Año: {self._año}")

# Clase Libro que hereda de publicación.
class Libro(Publicacion):
    def __init__(self, titulo, autor, año, genero):
        super().__init__(titulo, autor, año)
        self._genero = genero

    def mostrar_informacion(self):
        print(f"Libro: {self._titulo}, Autor: {self._autor}, Año: {self._año}, Género: {self._genero}")


# clase revista que hereda de publicación.
class Revista(Publicacion):
    def __init__(self, titulo, autor, año, numero_edicion):
        super().__init__(titulo, autor, año)
        self._numero_edicion = numero_edicion

    def mostrar_informacion(self):
        print(f"Revista: {self._titulo}, Autor: {self._autor}, Año: {self._año}, Número de Edición: {self._numero_edicion}")


# clase usuario

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self._prestamos = []

    def tomar_prestado(self, publicacion):
        self._prestamos.append(publicacion)
        print(f"{self.nombre} ha tomado prestado '{publicacion._titulo}'")

    def devolver_publicacion(self, publicacion):
        if publicacion in self._prestamos:
            self._prestamos.remove(publicacion)
            print(f"{self.nombre} ha devuelto '{publicacion._titulo}'")
        else:
            print(f"{self.nombre} no ha tomado prestados los siguientes titulos:")
            for publicacion in self._prestamos:
                publicacion.mostrar_informacion()

    def mostrar_prestamos(self):
        print(f"{self.nombre} ha tomado prestado los siguientes títulos:")
        for publicacion in self._prestamos:
            publicacion.mostrar_informacion()

# clase biblioteca para gestionar publicaciones y usuarios.
class Biblioteca:
    def __init__(self):
        self._catalogo = []
        self._usuarios = []

    def agregar_publicacion(self, publicacion):
        self._catalogo.append(publicacion)
        print(f"Se ha agregado '{publicacion._titulo}' al catálogo. ")

    def registrar_usuario(self, usuario):
        self._usuarios.append(usuario)
        print(f"Usuario: '{usuario.nombre}' ha sido registrado")

    def buscar_por_titulo(self, titulo):
        resultados = [pub for pub in self._catalogo if pub._titulo.lower() == titulo.lower()]
        self._mostrar_resultados_busqueda(resultados)

    def buscar_por_autor(self, autor):
        resultados = [pub for pub in self._catalogo if pub._autor.lower() == autor.lower()]
        self._mostrar_resultados_busqueda(resultados)

    def buscar_por_año(self, año):
        resultados = [pub for pub in self._catalogo if pub._año == año]
        self._mostrar_resultados_busqueda(resultados)

    def _mostrar_resultados_busqueda(self, resultados):
        if resultados:
            print("Resultados de la búsqueda")
            for pub in resultados:
                pub.mostrar_informacion()
        else:
            print("no se encontraron resultados.")

# función para mostrar informacion de cualquier publicacion.

def mostrar_publicacion(publicacion):
    publicacion.mostrar_informacion()

#crear instancias de libro y revista
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Ficción")

revista1 = Revista("National Geographic", "Varios Autores", 2021, 7)

libro2 = Libro("1984", "George Orwell", 1949, "Distopía")

revista2 = Revista("Science", "Varios Autores", 2023, 12)

# Crear instancia de Usuario
usuario1 = Usuario("Juan Pérez")
usuario2 = Usuario("Ana Gómez")

# Crear instancia de Biblioteca
biblioteca = Biblioteca()

# Agregar publicaciones al catálogo de la biblioteca
biblioteca.agregar_publicacion(libro1)
biblioteca.agregar_publicacion(revista1)
biblioteca.agregar_publicacion(libro2)
biblioteca.agregar_publicacion(revista2)

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)


# Mostrar información de publicaciones
mostrar_publicacion(libro1)
mostrar_publicacion(revista1)

# Gestionar préstamos
usuario1.tomar_prestado(libro1)
usuario1.tomar_prestado(revista2)
usuario1.mostrar_prestamos()
usuario1.devolver_publicacion(libro1)
usuario1.mostrar_prestamos()

# Búsquedas en el catálogo de la biblioteca
print("\nBúsqueda por título:")
biblioteca.buscar_por_titulo("1984")
print("\nBúsqueda por autor:")
biblioteca.buscar_por_autor("Antoine de Saint-Exupéry")
print("\nBúsqueda por año:")
biblioteca.buscar_por_año(2021)
