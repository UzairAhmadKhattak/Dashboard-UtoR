from django.contrib import admin
from .models import App
from .models import Plan

# Register your models here.

admin.site.register(App)
admin.site.register(Plan)
