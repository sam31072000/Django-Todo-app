from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from .models import todolist
from django.contrib import messages
from .formm import too

# Create your views here.
def index(request):
    if request.method == "POST":
        task = request.POST.get('task')
        desc = request.POST.get('desc')
        dte = f"{datetime.datetime.now()}"[:20]
        todo = todolist(task = task,desc = desc , date = dte)
        todo.save()
        return HttpResponseRedirect('/todo/')
    a = todolist.objects.all()
    fm = too()
    return render(request,"index.html",{"todoitems":a,"form":fm})
def deleteTask(request,myid):
    itemToDelete = todolist.objects.get(id=myid)
    itemToDelete.delete()
    messages.success(request,"Congrats..You have completed your task!!")
    return HttpResponseRedirect('/todo/')
