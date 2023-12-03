from django.contrib import admin
from .models import DataModel, Client

# Register your models here.
admin.site.register(DataModel)
admin.site.register(Client)
