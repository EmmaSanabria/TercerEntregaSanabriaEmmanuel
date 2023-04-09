from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def home(self):
    return render(self, "home.html")

def group(request):
    if request.method == 'POST':
        
        miFormulario = GroupForm(request.POST)
        
        if miFormulario.is_valid():

            data_formulario = miFormulario.cleaned_data

            inscripcion = Groups(name_group=data_formulario['name_group'],description =data_formulario['description'])
            inscripcion.save()
            return render(request, 'home.html')
    else:
        miFormulario = GroupForm()

        return render(request, 'group.html',{'miFormulario': miFormulario})
    
    
def post(request):
    if request.method == 'POST':
        
        miFormulario = PostForm(request.POST)
        
        if miFormulario.is_valid():

            data_formulario = miFormulario.cleaned_data

            inscripcion = Post(user_posting=data_formulario['usario'],post =data_formulario['post'])
            inscripcion.save()
            return render(request, 'home.html')
    else:
        miFormulario = PostForm()

        return render(request, 'post.html',{'miFormulario': miFormulario})

def user(request):
    if request.method == 'POST':
        
        miFormulario = UserForm(request.POST)
        
        if miFormulario.is_valid():

            data_formulario = miFormulario.cleaned_data

            inscripcion = User(user=data_formulario['user'], password =data_formulario['password'])
            inscripcion.save()
            return render(request, 'home.html')
    else:
        miFormulario = UserForm()

        return render(request, 'user.html',{'miFormulario': miFormulario})
    
    
def search_post(request):
    
    if request.GET["comentario"]:
        comentario= request.GET["comentario"]
        posteos = Post.objects.filter(user_posting= comentario)
        return render(request, "searchPost.html", {"posteos": posteos, })
    
    else:
        return HttpResponse (f"la busqueda estaba vacia")