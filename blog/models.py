from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre=models.CharField(max_length=100,null=False,blank=False)
    estado=models.BooleanField('categoria activada /categoria no activada',default=True)
    fecha_creacion=models.DateField('fecha creacion ',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre=models.CharField(max_length=50,null=False,blank=False)
    apellido=models.CharField(max_length=30)
    correo=models.URLField('EMAIL')
    facebook=models.URLField('facebook')
    estado=models.BooleanField('activo/no activo',default=True)
    fecha_creacion =models.DateField('fecha creacion',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'

    def __str__(self):
        return self.nombre
        


class Post(models.Model):
    titulo=models.CharField(max_length=100,null=False,blank=False)
    slug=models.CharField(max_length=30,null=False,blank=False)
    autor=models.CharField(max_length=30)
    contenido=RichTextField ()
    imagen=models.URLField(max_length=255)
    estado=models.BooleanField('activo/no activo',default=True)
    fecha_creacion=models.DateField('fecha cracion',auto_now=False,auto_now_add=True)
    categoria=models.ForeignKey(Categoria ,on_delete=models.CASCADE)


    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.titulo
        
