from django.contrib import admin
from apps.tasks.models import Task, Status, Resource

# Register your models here.
admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Resource)
