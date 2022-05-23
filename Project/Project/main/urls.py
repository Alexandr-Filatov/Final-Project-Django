from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tasks_list', views.tasks_list, name='tasks_list'),
    path('add_task', views.add_task, name='add_task'),
    path('edit_task', views.edit_task, name='edit_task')
]