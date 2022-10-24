from django.db import models


class Task(models.Model):
    task_id = models.IntegerField()
    description = models.CharField(max_length=1000)
    due_date = models.DateField()
    assigned_to = models.CharField(max_length=20)
