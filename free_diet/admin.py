from django.contrib import admin
from .models import FreeDiet
# Register your models here.

class FreeDietAdmin(admin.ModelAdmin):
    model = FreeDiet

admin.site.register(FreeDiet, FreeDietAdmin)