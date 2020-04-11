from django.shortcuts import render
from .models import Post,Categoria
from django.core.paginator import Paginator

# Create your views here.
def Home(request):
    posts = Post.objects.filter(estado=True)
    paginacion =Paginator(posts,2)
    page = request.GET.get('page')
    posts=paginacion.get_page(page)
    return render(request,'index.html',{'posts':posts})

def Detalle(request,slug):
    posts = Post.objects.get(
        slug=slug
    )
    return render(request,'post_detalle.html',{'detalle_post':posts})    


def Tegnologia(request):
    posts = Post.objects.filter(
        estado=True,
        categoria= Categoria.objects.get(nombre ='Tegnologia')
    )
    return render(request,'tegnologia.html',{'posts':posts})


def Programacion(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre ='Programacion')
    )
    return render(request,'programacion.html',{'posts':posts})


def Proyectos(request):
    posts = Post.objects.filter(
        estado=True,
        categoria= Categoria.objects.get(nombre ='Proyectos')
    )
    return render(request,'proyectos.html',{'posts':posts})

def Contacto(request):
    posts=Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='contacto')
    )

    return render(request,'contacto.html',{'posts':posts})  

