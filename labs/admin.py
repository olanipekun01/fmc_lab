from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Wards)
admin.site.register(Departments)
admin.site.register(Investigations)
admin.site.register(Specimens)
admin.site.register(Records)