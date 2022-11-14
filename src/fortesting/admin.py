from django.contrib import admin

# Register your models here.

from .models import DummyModel

admin.site.register(DummyModel)