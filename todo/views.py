from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def addtask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')