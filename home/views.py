# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task, TaskGroup


class TaskListView(ListView):
    model = Task
    template_name = "home/task_list.html"
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        ctx = super(TaskListView, self).get_context_data(**kwargs)
        ctx["taskgroups"] = TaskGroup.objects.all()
        return ctx
    
    def post(self, request, *args, **kwargs):
        t = Task()
        t.name = request.POST.get("task_name")
        t.due_date = request.POST.get("task_due")
        t.taskgroup = TaskGroup.objects.get(pk=request.POST.get("taskgroup"))
        t.save()

        return self.get(request, *args, **kwargs)
    

def index(request):
    response: str = "skibidi sigma"
    return HttpResponse(response)


def task_list(request):
    tasks = Task.objects.all()
    ctx = {
        "tasks": tasks
    }
    return render(request, 'home/task_list.html', ctx)


def task_detail(request, pk):
    ctx = {
        "task": Task.objects.get(pk=pk)
    }
    return render (request, 'home/task_detail.html', ctx)
