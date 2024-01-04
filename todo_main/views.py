from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed=True).order_by('-updated_at')

    dict = {
        'tasks': tasks,
        'ct': completed_task
    }
    return render(request, 'home.html', dict)