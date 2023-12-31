from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from tasks.formularios import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404

# Create your views here.
#Redirecciona a la pagina principal

def home(request):
    return render(request, 'home.html')
#El sistema de registrarse
def signup(request):
    if request.method == 'GET':
        print('Enviando Formulario')
        return render(request, 'signup.html', {
            'form':UserCreationForm
            })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #Register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                'form':UserCreationForm,
                'error':'El usuario ya existe'
                })   
        return render(request, 'signup.html', {
            'form':UserCreationForm,
            'error':'Contraseña no coinciden'
            })   
#El sistema de iniciar sesion
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form':AuthenticationForm
    })
    else:
       user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       if user is None:
           return render(request, 'signin.html', {
           'form':AuthenticationForm,
           'error':'Usuario o contraseña incorrectos'
           })
       else:
           login(request,user)
           return redirect('tasks')
#Deslogearte de la pagina
def signout(request):
    logout(request)
    return redirect('home')

#Redirecciona a la pagina de 'task'
def tasks(request):
    tasks=Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html',{'tasks':tasks})

#Ver el hospital que seleccionaste y actualizarlo
def task_detail(request,task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task,pk=task_id, user=request.user)
        form =TaskForm(instance=task)
        return render(request, 'task_detail.html',{'task':task,'form':form})
    else:
        try:
            task = get_object_or_404(Task,pk=task_id, user=request.user)
            form =TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html',{'task':task,'form':form, 'error':'Error al actualizar tarea'})
       
#Elimianr hospital
def delete_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


#Crear hospital
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html',{'form':TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task=form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html',{'form':TaskForm, 'error':'Error al crear tarea'})
    




        
        
