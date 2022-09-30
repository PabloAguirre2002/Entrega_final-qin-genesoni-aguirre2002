from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User 

class Carteras(models.Model):
    nombre = models.CharField(max_length=128)
    codigo= models.CharField(max_length=128)
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.codigo}, {self.nombre}, {self.stock}'


class Camperas(models.Model):
    nombre = models.CharField(max_length=128)
    codigo= models.CharField(max_length=128)
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.codigo}, {self.nombre}, {self.stock}'

class Zapatos(models.Model):
    nombre = models.CharField(max_length=128)
    codigo= models.CharField(max_length=128)
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.codigo}, {self.nombre}, {self.stock}'

class Accesorios(models.Model):
    nombre = models.CharField(max_length=128)
    codigo= models.CharField(max_length=128)
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.codigo}, {self.nombre}, {self.stock}' 

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"

        




