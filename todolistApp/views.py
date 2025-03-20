from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .models import Tickets
from .forms import TicketForm

def inicio(request):
    return render(request, 'paginas/index.html' )

def is_superuser(user):
    return user.is_superuser

@login_required(login_url='/InicioSesion/')
def tareas(request):

    tickets = Tickets.objects.all()
    
    return render(request, 'tareasPorHacer/index.html', {'tickets': tickets})

@user_passes_test(is_superuser)
def dashboard(request):

    tickets = Tickets.objects.all()
    
    return render(request, 'dashboard/index.html', {'tickets': tickets})

def crearTarea(request):
    formulario = TicketForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('tareas')
    return render(request, 'tareasPorHacer/agregar.html', {'formulario': formulario})



def editarTarea(request, id):
    tarea = Tickets.objects.get(id=id)
    usuario = request.user
    formulario = TicketForm(request.POST or None, instance=tarea)
    if str(usuario) == str(tarea.usuario):

        if formulario.is_valid() and request.method == 'POST':
            formulario.save()
            return redirect('tareas')
    else:
        redirect('tareas')
    return render(request, 'tareasPorHacer/editar.html', { 'formulario' : formulario })

def eliminarTareas(request, id):
    tarea = Tickets.objects.get(id=id)
    usuario= request.user
    if str(usuario) == str(tarea.usuario):
        tarea.delete()
    return redirect('tareas')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def login(request):
    return render(request, 'registration/login.html')

def procesar_ticket(request, id):

    ticket = Tickets.objects.get(id=id)
    ticket.status = 'Procesando'  
    ticket.save()  

    return redirect('dashboard')

def cerrar_ticket(request, id):

    ticket = Tickets.objects.get(id=id)
    ticket.status = 'Cerrado'  
    ticket.save()  

    return redirect('dashboard')
