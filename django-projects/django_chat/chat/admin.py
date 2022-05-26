from django.contrib import admin
from . import models

admin.site.register(models.Message)
admin.site.register(models.Room)
admin.site.register(models.MessageUser)

# Register your models here.
