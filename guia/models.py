from django.db import models

# Create your models here.

class ContenidoAudiovisual(models.Model):
    OPCIONES_ANIO = [
        ('2', 'Segundo Año'),
        ('4', 'Cuarto Año'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name="Título del Video")
    descripcion = models.TextField(verbose_name="Párrafo Informativo")
    video = models.FileField(upload_to='videos/', verbose_name="Archivo de Video")
    anio = models.CharField(max_length=10, choices=OPCIONES_ANIO, verbose_name="Año Escolar")

    def __str__(self):
        return f"{self.titulo} - {self.get_anio_display()}"