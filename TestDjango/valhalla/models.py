from typing import ClassVar
from django.db import models
from django.forms.fields import EmailField

# Create your models here.

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True,verbose_name='id')
    nombreCategoria=models.CharField(max_length=50,verbose_name='nombre de la categoria')

    def __str__(self) :
        return (self.nombreCategoria)

class Producto(models.Model):
    numeroID=        models.CharField(max_length=20, primary_key=True,verbose_name='numeroID',null=True)
    nombreCompleto=  models.CharField(max_length=20,verbose_name='nombreCompleto',null=True)
    telefono=        models.CharField(max_length=20,verbose_name='telefono',null=True)
    categoria=       models.ForeignKey(Categoria,on_delete=models.CASCADE)
    direccion=       models.CharField(max_length=30,verbose_name='direccion',null=True)
    imagen =         models.ImageField(upload_to='logos_id',null=True)
    email=           models.CharField(max_length=30,verbose_name='email',null=True)
    pais=            models.CharField(max_length=20,verbose_name= 'pais',null=True)
    contrasenna=      models.CharField(max_length=30,verbose_name= 'contrasenna',null=True,blank=True)
    





    def __str__(self) :
        return (self.numeroID)
