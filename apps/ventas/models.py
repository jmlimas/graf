from django.db import models

# Create your models here.

class Inventario(models.Model):

	Op = (
        ('Fruta', 'Fruta'),
        ('Liquidos', 'Liquidos'),
        ('Congelado', 'Congelados'),
        ('Carnes', 'Carnes'),
        )

	nombre = models.CharField(max_length=120)
	categoria = models.CharField(max_length=30,choices=Op) 
	existencia = models.IntegerField()

	def __unicode__(self):
		return self.nombre
