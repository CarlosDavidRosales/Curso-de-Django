from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import TareasForm
from .models import Tareas

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request): 
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1']) 
                user.save()
                login(request, user)
                return redirect('main')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists.'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })
def signout(request):
    logout(request)
    return redirect('home')

def main(request):
    tasks = Tareas.objects.all()
    return render(request, 'main.html', {
        'tasks': tasks
    })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Username or password was incorrect'
        })
        else:
            login(request, user)
            return redirect('main')
        
def create_task(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TareasForm
        })
    else:
        try:
            form = TareasForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()

            return redirect('main')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TareasForm,
                'error': 'Bad data passed in. Try again.'
            })
            
            
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Tareas, pk=task_id)
        form = TareasForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Tareas, pk=task_id)
            form = TareasForm(request.POST, instance=task)
            form.save()
            return redirect('main')
        except Exception as e:
            print(e)
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating taks'})