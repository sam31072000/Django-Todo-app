from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from .models import todolist

# Create your views here.
def index(request):
    if request.method == "POST":
        task = request.POST.get('task')
        desc = request.POST.get('desc')
        dte = f"{datetime.datetime.now()}"[:20]
        todo = todolist(task = task,desc = desc , date = dte)
        todo.save()
    a = todolist.objects.all()
    return render(request,"index.html",{"todoitems":a})
def deleteTask(request,myid):
    itemToDelete = todolist.objects.get(id=myid)
    itemToDelete.delete()
    return HttpResponseRedirect('/todo/')
