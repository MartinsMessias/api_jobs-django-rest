from django.contrib import admin

# Register your models here.
from .models import Tecnologia, Vaga

admin.site.register(Tecnologia)
admin.site.register(Vaga)
