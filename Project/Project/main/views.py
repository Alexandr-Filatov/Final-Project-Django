from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):

    return render(request, 'main/index.html',
                  {
                      "title": "Главная страница",
                      "header": "Главная"
                  })

def tasks_list(request):
    tasks_list = Task.objects.all()
    form = TaskForm()
    context = {
        'form': form
    }
    return  render(request, 'main/tasks_list.html',
                   {
                    "title": "Список задач",
                    "header": "Список задач",
                    "tasks_list": tasks_list,
                    })

def add_task(request):
    form = TaskForm
    task = Task.objects.all()
    return render(request, 'main/add_task.html',
                  {
                      "title": "Новая задача",
                      "header": "Новая задача",
                      "task": task,
                      "form": form
                  })

def edit_task(request):
    return render(request, 'main/edit_task.html',
                  {
                      "title": "Редактор задач",
                      "header": "Редактор задач",


                  })