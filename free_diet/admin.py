from django.contrib import admin
from .models import FreeDiet, FreeDietTemplatePart
# Register your models here.

class DietTemplatePartAdmin(admin.TabularInline):
    model = FreeDietTemplatePart


class FreeDietAdmin(admin.ModelAdmin):
    fieldsets = (
        ('نام', {'fields': ['name']}),
        ('مشخصات', {'fields': ['free_diet_kind', 'diet_period']})
    )
    inlines = [DietTemplatePartAdmin, ]


admin.site.register(FreeDiet, FreeDietAdmin)