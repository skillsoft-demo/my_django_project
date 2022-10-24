from my_app.models import Task
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")


def task_by_id(request, task_id):
    task = Task.objects.get(task_id=task_id)
    return HttpResponse(
        f'''
        <p>Description: {task.description}</p>
        <p>Due Date: {task.due_date}</p>
        <p>Assigned To: {task.assigned_to}</p>
        '''
    )
