from django.contrib import admin

from .models import VisitTime, DietTemplatePart, SpecializedDiet, Prescription


class VisitTimeAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'type', 'id']
    fieldsets = (
        (None, {'fields': ['start_date', 'end_date', 'type']}),
        ('پزشک معالح', {'fields': ['doctor', ]}),
        ('بیمار', {'fields': ['patient', ]})
    )
    list_filter = ['type', 'start_date', 'end_date', 'doctor', 'patient', 'type', 'id']
    search_fields = ['patient', 'doctor']


class DietTemplatePartAdmin(admin.TabularInline):
    model = DietTemplatePart


class DietAdmin(admin.ModelAdmin):
    fieldsets = (
        ('نام', {'fields': ['name']}),
        ('ویزیت', {'fields': ['visit']}),
    )
    inlines = [DietTemplatePartAdmin, ]


class PrescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('محتوا', {'fields': ['context', 'pk']}),
        ('ویزیت', {'fields': ['visit']}),
    )


admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(SpecializedDiet, DietAdmin)
admin.site.register(VisitTime, VisitTimeAdmin)
