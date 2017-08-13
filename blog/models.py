from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.user')
    titulo = models.CharField(max_length=200)
    titulo2 = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
