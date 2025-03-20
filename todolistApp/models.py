from django.db import models

class Tickets(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40, verbose_name = 'Titulo del ticket')
    start = models.DateField(auto_now=True,auto_now_add=False, verbose_name='Fecha de creacion')
    description = models.TextField(verbose_name="Descripcion del problema")
    status = models.CharField(verbose_name="Estado del ticket", max_length=20)
    usuario = models.CharField(max_length=50, null=True, verbose_name='Usuario')
    
    def __str__(self):
        return self.title
