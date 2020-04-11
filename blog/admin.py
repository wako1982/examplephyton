from django.contrib import admin
from .models import Post,Autor,Categoria
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class CategoriaResource (resources.ModelResource):
    class Meta:
        model=Categoria

class Autoradmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['nombre']
    list_display=('nombre','estado','fecha_creacion','correo')
    resource_class =AutorResource

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['nombre']
    list_display=('nombre','estado','fecha_creacion')
    resource_class=CategoriaResource







admin.site.register(Post)
admin.site.register(Autor,Autoradmin)
admin.site.register(Categoria,CategoriaAdmin)

# Register your models here.
