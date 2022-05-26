from django.contrib import admin
from .models import *

[admin.site.register(x) for x in [Quiz]]