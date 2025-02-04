from django.contrib import admin

from server.models import Category, Source
from server.forms import CategoryForm, SourceForm

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = (
        'id',
        'name',
        'type',
        'group',
        'is_active'
    )


class SourceAdmin(admin.ModelAdmin):
    form = SourceForm
    list_display = (
        'id',
        'name',
        'is_active'
    )


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Source, SourceAdmin)
