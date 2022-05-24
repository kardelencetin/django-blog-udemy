from django.contrib import admin
from blog.models import KategoriModel, YazilarModel


class YazilarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'moderated')
    search_fields = ('title', 'content')

admin.site.register(KategoriModel)
admin.site.register(YazilarModel, YazilarAdmin)
