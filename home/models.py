from django.db import models
from django.urls import reverse


class TaskGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey(
        TaskGroup,
        on_delete=models.SET_NULL,
        null=True,
        related_name="task_list"
    )

    def __str__(self):
        return f"{self.name}, due on {self.due_date}"

    def get_absolute_url(self):
        return reverse("home:task-detail", kwargs={"pk": self.pk})
     