# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response: str = "skibidi sigma"
    return HttpResponse(response)

def task_list(request):
    ctx = {
        "tasks": [
            'Task 1',
            'Task 2',
            'Task 3',
            'Task 4',
            'Task 5',
        ]
    }
    return render(request, 'task_list.html', ctx)