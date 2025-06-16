"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todo.views import index, add_task, complete_task, delete_task

urlpatterns = [
    #http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/delete/10
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    #http://127.0.0.1:8000/complete/5
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    #http://127.0.0.1:8000/add
    path('add/', add_task, name='add'),
    #http://127.0.0.1:8000
    path('', index, name='home'),
]
