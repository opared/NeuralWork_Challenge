from django.contrib import admin

# Register your models here.

from .models import ArchViajes, DatosCsv


admin.site.register(ArchViajes)
admin.site.register(DatosCsv)

