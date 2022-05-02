from django.contrib import admin

from .models import Tag, Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['subject', 'context', 'thumbnail']}),
        ('تگ‌ها', {'fields': ['tags']}),
        ('نویسنده', {'fields': ['writer']})
    ]
    list_display = ['subject', 'writer', 'get_tags', 'thumbnail']
    list_filter = ['subject', 'tags']
    search_fields = ['tags__name', ]


admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
