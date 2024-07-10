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
