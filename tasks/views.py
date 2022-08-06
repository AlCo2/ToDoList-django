
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        task_get = request.POST.get('task')
        data = Task(title = task_get)
        data.save()
        return redirect('/')
    return render(request, 'tasks/index.html',{'tasks':tasks})



def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'tasks/delete.html', context)