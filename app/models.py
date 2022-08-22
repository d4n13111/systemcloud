from django.db import models
from  embed_video.fields  import  EmbedVideoField

class Person(models.Model):
	names = models.CharField(max_length=100, verbose_name='Nombre completo')
	title = models.CharField(max_length=100, verbose_name='Título')
	insti = models.CharField(max_length=100, verbose_name='Institución')
	descr = models.CharField(max_length=100, verbose_name='Web')

class Contact(models.Model):
	perso = models.ForeignKey(Person, on_delete=models.PROTECT)
	icono = models.CharField(max_length=100, verbose_name='Font-awesome')
	descr = models.CharField(max_length=100, verbose_name='Descripcion')

class Slider(models.Model):
	perso = models.ForeignKey(Person, on_delete=models.PROTECT)
	image = models.ImageField(verbose_name='Imagen', upload_to="slider", null=True, blank=True)
	title = models.CharField(max_length=100, verbose_name='Título')
	descr = models.CharField(max_length=100, verbose_name='Descripcion')
	activ = models.CharField(max_length=6, verbose_name='active', null=True, blank=True)

class Service(models.Model):
	perso = models.ForeignKey(Person, on_delete=models.PROTECT)
	image = models.ImageField(verbose_name='Icono', upload_to="service", null=True, blank=True)
	title = models.CharField(max_length=100, verbose_name='Título')
	descr = models.CharField(max_length=100, verbose_name='Descripcion')

class Portfolio(models.Model):
	FOLIO_CHOICES = [('1', 'Personal'), ('2', 'Cliente'), ('3', 'Privado'),]
	perso = models.ForeignKey(Person, on_delete=models.PROTECT)
	clase = models.CharField(max_length=1, verbose_name='Clase', choices=FOLIO_CHOICES, default='1')
	image = models.ImageField(verbose_name='Icono', upload_to="folio", null=True, blank=True)
	title = models.CharField(max_length=100, verbose_name='Título')
	descr = models.CharField(max_length=255, verbose_name='Descripcion')
	enlac = models.CharField(max_length=100, verbose_name='Enlace', null=True, blank=True)
	youtb = EmbedVideoField(verbose_name='Youtube', null=True, blank=True)