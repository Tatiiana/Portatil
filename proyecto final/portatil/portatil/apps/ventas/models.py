from django.db import models

# Create your models here.

class Marca (models.Model):
	nombre_marca		= models.CharField(max_length = 100)

class Conectividad (models.Model):
	nombre_conectividad		= models.CharField(max_length = 100)

class Accesorios (models.Model):
	nombre			= models.CharField(max_length = 50)
	descripcion		= models.CharField(max_length = 200)

class Portatil (models.Model):
	marca 			= models.ForeignKey(Marca)
	conectividad    = models.ManyToManyField(Conectividad)
	accesorios   	= models.ManyToManyField(Accesorios)
	color			= models.CharField(max_length = 100)
	serial			= models.CharField(max_length = 50)
	referencia		= models.CharField(max_length = 50)
	procesador		= models.CharField(max_length = 50)
	memoria_ram		= models.CharField(max_length = 50)
	sistema_operativo	= models.CharField(max_length = 50)
	lapiz_y_entrada_tctil	= models.CharField(max_length = 50)











	