from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.projects.models import Project
from apps.tasks.models import Task
from apps.tasks.forms import FormTask
from django.views.generic import TemplateView
from apps.tasks import plots
# Create your views here.


def tasks_view(request, idpro):
    pro = Project.objects.get(id=idpro)
    tasks = pro.tasks.all().order_by('id')
    context = {'tasks':tasks, 'project': pro}
    return render(request, 'tasks/ViewTasks.html',context)

def tasks_add(request, idpro):
    pro = Project.objects.get(id=idpro)
    if request.method == 'POST':
        form = FormTask(request.POST)
        if form.is_valid():
            form.save()
            tss = Task.objects.get(id=request.POST.get('id'))
            pro.tasks.add(tss)
        
        return redirect('tasks', idpro= idpro)
    else:
        form = FormTask()
        return render(request, 'tasks/AddTask.html', {'form' : form, 'pro' : pro})

def tasks_edit(request, idpro, idtsk):
    pro = Project.objects.get(id=idpro)
    task = Task.objects.get(id=idtsk)
    if request.method == 'GET':
        form = FormTask(instance=task)
    else:
        form = FormTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks', idpro= idpro)
    return render(request, 'tasks/EditTask.html', {'form' : form, 'pro' : pro})

def tasks_delete(request, idpro, idtsk):
    pro = Project.objects.get(id=idpro)
    task = Task.objects.get(id=idtsk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks', idpro= idpro)
    return render(request, 'tasks/DelTask.html', {'pro' : pro, 'task' : task})

def tasks_ur(request):
    project = Project.objects.all().order_by('id')
    context = {'projects':project}
    return render(request,'tasks/Tasks.html', context)

class Gantt(TemplateView):
    template_name = 'tasks/Gantt.html'
    def get_context_data(self, **kwargs):
        context = super(Gantt, self).get_context_data(**kwargs)
        idpro = kwargs['idpro']
        pro = Project.objects.get(id=idpro)
        tasks = pro.tasks.all()
        context['tasks'] = tasks
        if tasks:
            context['gantt'] = plots.gantt(tasks)
            
        context['pro'] = pro
        return context