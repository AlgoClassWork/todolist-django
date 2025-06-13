from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task

def index(request):
    tasks = Task.objects.order_by('-created_at')
    return render(request, 'index.html', {"tasks" : tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title') 
        if title:
            Task.objects.create(title=title)

    return redirect('home')

