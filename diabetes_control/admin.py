from django.contrib import admin

from .models import VisitTime, Template, DietTemplatePart, Diet


class DietAdmin(admin.TabularInline):
    model = Diet


class VisitTimeAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'type']
    fieldsets = (
        (None, {'fields': ['start_date', 'end_date', 'type']}),
        ('پزشک معالح', {'fields': ['doctor', ]}),
        ('بیمار', {'fields': ['patient', ]})
    )
    list_filter = ['type', 'start_date', 'end_date', 'doctor', 'patient', 'type']
    search_fields = ['patient', 'doctor']
    inlines = [DietAdmin]


class DietTemplatePartAdmin(admin.ModelAdmin):
    pass


class TemplateAdmin(admin.ModelAdmin):
    fields = ['name', 'owner', 'template_parts']
    search_fields = ['owner', 'name']
    list_filter = ['name', 'owner', 'template_parts']
    list_display = ['name', 'owner']
    filter_horizontal = ['template_parts', ]


class DietAdmin(admin.ModelAdmin):
    fieldsets = (
        ('ویزیت', {'fields': ['visit']}),
        ('تمپلیت', {'fields': ['template']})
    )


admin.site.register(Diet, DietAdmin)
admin.site.register(DietTemplatePart, DietTemplatePartAdmin)
admin.site.register(VisitTime, VisitTimeAdmin)
admin.site.register(Template, TemplateAdmin)
