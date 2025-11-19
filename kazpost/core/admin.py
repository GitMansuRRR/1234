from django.contrib import admin
from .models import Department, Service, OperatorWindow

admin.site.register(Department)
admin.site.register(Service)
admin.site.register(OperatorWindow)