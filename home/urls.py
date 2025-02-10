from django.urls import path
from .views import index, task_list

urlpatterns = [
    path('', index, name="index"),
    path('task-list', task_list, name='task_list')
]

app_name = 'home'