from datetime import date
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def año_nacimiento(self):
        return date.today().year - self.edad
    

    def cedula_loja(self):
        if self.cedula.startswith("11"):
            return "Loja"
        else:
            return "Otra Ciudad"
      

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - CI: {self.cedula_loja()} - Edad: {self.edad} - Año de nacimiento: {self.año_nacimiento()}"
