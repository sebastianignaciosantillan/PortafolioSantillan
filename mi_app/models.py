from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    asunto = models.CharField(max_length=100)
    consulta = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} - {self.asunto}'
