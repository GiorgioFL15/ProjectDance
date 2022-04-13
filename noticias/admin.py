from django.contrib import admin
from .models import Noticia

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_noticia', 'categoria', 'publicada')
    list_display_links = ('id', 'nome_noticia')
    search_fields = ('nome_noticia',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10
admin.site.register(Noticia, ListandoReceitas)

