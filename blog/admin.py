from django.contrib import admin
from blog.models import (KategoriModel, YazilarModel, YorumModel)



admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'moderated')
    search_fields = ('title', 'content')

admin.site.register(YazilarModel, YazilarAdmin)


class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazan', 'created', 'modified')
    search_fields = ('yazan__user',)

admin.site.register(YorumModel, YorumAdmin)