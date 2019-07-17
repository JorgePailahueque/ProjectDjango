from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from apps.projects.forms import AddProjects
from apps.projects.models import Project
from apps.tasks.models import Task, Status
from apps.tasks.forms import FormTask
from django.views.generic import TemplateView
from apps.tasks import plots
from apps.persona.models import Persona
# Create your views here.

def index(request):
    return render(request,'projects/index.html')

def projects_add(request):
    if request.method == 'POST':
        form = AddProjects(request.POST)
        if form.is_valid():
            form.save()
        return redirect('projects')
    else:
        form = AddProjects()
        return render(request, 'projects/AddProjects.html', {'form' : form})

def projects_view(request):
    valid()
    project = Project.objects.all().order_by('id')
    context = {'projects':project}
    return render(request, 'projects/ViewProjects.html',context)

def project_edit(request, idpro):
    project = Project.objects.get(id=idpro)
    if request.method == 'GET':
        form = AddProjects(instance=project)
    else:
        form = AddProjects(request.POST, instance=project)
        if form.is_valid():
            form.save()
        return redirect('projects')
    return render(request, 'projects/EditProject.html', {'form' : form})

def project_delete(request, idpro):
    project = Project.objects.get(id=idpro)
    tasks = project.tasks.all()
    if request.method == 'POST':
        for t in tasks:
            dlt = Task.objects.get(id=t.id)
            dlt.delete()
        project.delete()
        return redirect('projects')
    return render(request, 'projects/DelProject.html', {'project' : project})

def valid():
    status = Status.objects.all()
    people = Persona.objects.all()
    if not(status):
        st1= Status(id=0, percent='0')
        st2= Status(id=25, percent='25')
        st3= Status(id=50, percent='50')
        st4= Status(id=75, percent='75')
        st5= Status(id=100, percent='100')
        st1.save()
        st2.save()
        st3.save()
        st4.save()
        st5.save()
    if not(people):
        p1= Persona(nombre='Jorge', apellidos= 'Pailahueque', rut= '1946111111', telefono= '', email= 'j.pailahueque02@ufromail.cl', domicilio='Te', fecha_ingreso= '2019-07-17')
        p2= Persona(nombre='Daniel', apellidos= 'Coronado', rut= '1946111111', telefono= '', email= 'd.coronado@ufromail.cl', domicilio='Te', fecha_ingreso= '2019-07-17')
        p3= Persona(nombre='Matias', apellidos= 'Molina', rut= '1946111111', telefono= '', email= 'm.molina@ufromail.cl', domicilio='Te', fecha_ingreso= '2019-07-17')
        p1.save()
        p2.save()
        p3.save()