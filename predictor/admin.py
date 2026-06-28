from django.contrib import admin

from .models import GuiaReparto


@admin.register(GuiaReparto)
class GuiaRepartoAdmin(admin.ModelAdmin):
    list_display = ('clave', 'modificado_en')
    readonly_fields = ('modificado_en',)
