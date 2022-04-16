from django.contrib import admin

from .models import FreeDiet, FreeDietTemplatePart, FreeDietInstance


# Register your models here.

class DietTemplatePartAdmin(admin.TabularInline):
    model = FreeDietTemplatePart


class FreeDietAdmin(admin.ModelAdmin):
    fieldsets = (
        ('نام', {'fields': ['name']}),
        ('مشخصات', {'fields': ['free_diet_kind', 'diet_period']})
    )
    inlines = [DietTemplatePartAdmin, ]


class FreeDietInstanceAdmin(admin.ModelAdmin):
    model = FreeDietInstance


admin.site.register(FreeDiet, FreeDietAdmin)
admin.site.register(FreeDietInstance, FreeDietInstanceAdmin)
