from django.urls import path
from .views import index, task_list, task_detail, TaskListView

urlpatterns = [
    path('', index, name="index"),
    path('task-list', TaskListView.as_view(), name='task-list'),
    path('task.<int:pk>', task_detail, name="task-detail")
]

app_name = 'home'