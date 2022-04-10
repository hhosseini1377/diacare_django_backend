from django.contrib import admin

from .models import VisitTime, DietTemplatePart, SpecializedDiet


class DietAdmin(admin.TabularInline):
    model = SpecializedDiet


class VisitTimeAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'type', 'id']
    fieldsets = (
        (None, {'fields': ['start_date', 'end_date', 'type']}),
        ('پزشک معالح', {'fields': ['doctor', ]}),
        ('بیمار', {'fields': ['patient', ]})
    )
    list_filter = ['type', 'start_date', 'end_date', 'doctor', 'patient', 'type', 'id']
    search_fields = ['patient', 'doctor']
    inlines = [DietAdmin]


class DietTemplatePartAdmin(admin.ModelAdmin    ):
    model = DietTemplatePart


class DietAdmin(admin.ModelAdmin):
    model = SpecializedDiet


admin.site.register(SpecializedDiet, DietAdmin)
admin.site.register(VisitTime, VisitTimeAdmin)
admin.site.register(DietTemplatePart, DietTemplatePartAdmin)