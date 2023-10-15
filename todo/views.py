from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task


# Create your views here.
def addTask(request):
    task_des = request.POST["task"]
    Task.objects.create(task=task_des)
    return redirect("home")
