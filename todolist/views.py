from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.models import TaskList
from todolist.forms import TaskForm
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = TaskList.objects.filter(user=request.user)
    context = {
    'data_todolist': data_todolist,
    'username': request.user.get_username(),
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_json(request):
    data_todolist = TaskList.objects.filter(user=request.user)   
    return HttpResponse(serializers.serialize('json', data_todolist), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_add_task(request):
    if request.method == 'POST':
        user = request.user
        date = datetime.datetime.now()
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_finished = False
        TaskList.objects.create(date=date, user=user, title=title, description=description, is_finished=is_finished)
        return JsonResponse({"Message": 'Your new task has been added!'},status=200)
    return redirect('todolist:todolist')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created successfully!')
            return redirect('todolist:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:todolist')
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def show_create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            user = request.user
            date = datetime.datetime.now()
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            is_finished = False
            TaskList.objects.create(date=date, user=user, title=title, description=description, is_finished=is_finished)
            messages.success(request, 'Your new task has been added!')
            return redirect('todolist:todolist')
    else:
        form = TaskForm()
    return render(request, 'create-task.html', {'form': form, 'username': request.user.get_username()} )

@login_required(login_url='/todolist/login/')
def update_status(request, id):
    data = TaskList.objects.get(user = request.user, pk = id)
    data.is_finished = not data.is_finished
    data.save()
    return redirect('todolist:todolist')

@login_required(login_url='/todolist/login/')
def delete(request, id):
    data = TaskList.objects.get(user = request.user, pk = id)
    data.delete()
    messages.success(request, 'Your task has been successfully deleted!')
    return redirect('todolist:todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    data = TaskList.objects.get(user = request.user, pk = id)
    data.delete()
    return JsonResponse({"Message": 'Your task has been successfully deleted!'},status=200)