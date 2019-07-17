"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.projects.views import index, projects_add, projects_view, project_edit, project_delete
from apps.tasks.views import tasks_add, tasks_view, tasks_edit, tasks_delete, tasks_ur, Gantt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projects_view),
    path('projects/addproject',projects_add),
    path('projects/', projects_view, name='projects'),
    path('projects/edit/<str:idpro>/', project_edit),
    path('projects/delete/<str:idpro>/', project_delete),

    path('tasks/', tasks_ur),
    path('projects/<str:idpro>/tasks/', tasks_view, name='tasks'),
    path('projects/<str:idpro>/tasks/addtask', tasks_add),
    path('projects/<str:idpro>/tasks/edittask/<str:idtsk>', tasks_edit),
    path('projects/<str:idpro>/tasks/delete/<str:idtsk>', tasks_delete),
    path('projects/<str:idpro>/tasks/Gantt', Gantt.as_view(),name='simple-candlestick'),
]
