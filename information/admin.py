from django.contrib import admin
from .models import Information, Docs


class InlineDocs(admin.TabularInline):
    model = Docs
    extra = 0


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'phone',
        'fax',
        'whatsapp',
        'email',
    ]
    list_display_links = [
        'id',
        'name',
    ]
    list_editable = [
        'phone',
        'fax',
        'whatsapp',
        'email',
    ]
    inlines = [
        InlineDocs,
    ]
