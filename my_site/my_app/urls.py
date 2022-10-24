from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:task_id>', views.task_by_id, name='task_by_id')
]
