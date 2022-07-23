from django.test import TestCase

from EdbooksApp.models import Autores, Libro

# Create your tests here.
class LibroTest(TestCase):
    
    def setUp(self):
        Libro.objects.create(titulo="Mil soles esplendidos", autor="Khaled Hosseini", año=2022)
        
    def test_libro_titulo(self):
        libro = Libro.objects.get(año=2022)
        self.assertEqual(libro.titulo, "Mil soles esplendidos")
    
    def test_libro_creado(self):
        curso = Libro.objects.get(año=2022)
        self.assertNotEquals(curso, None)

class AutorTest(TestCase):
    
    def setUp(self):
        Autores.objects.create(nombre="Alan", apellido="Ramirez", nacionalidad="mexico")
        
    def test_autor_nacionalidad(self):
        autor = Autores.objects.get(nombre="Alan")
        self.assertEqual(autor.nacionalidad, "mexico")
    
    def test_autor_creado(self):
        autor = Autores.objects.get(nacionalidad="mexico")
        self.assertNotEquals(autor, None)