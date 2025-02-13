# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response: str = "skibidi sigma"
    return HttpResponse(response)

def task_list(request):
    ctx = {
        "tasks": ["shikanokonokonokonoshitantan" for i in range(1000)]
    }
    return render(request, 'task_list.html', ctx)