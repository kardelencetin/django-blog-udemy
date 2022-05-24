from django.contrib import admin
from blog.models import (KategoriModel, YazilarModel, YorumModel, IletisimModel)



admin.site.register(KategoriModel)


@admin.register(YazilarModel)

class YazilarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'moderated')
    search_fields = ('title', 'content')

# admin.site.register(YazilarModel, YazilarAdmin)

@admin.register(YorumModel)

class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazan', 'created', 'moderated')
    search_fields = ('yazan__user',)

# admin.site.register(YorumModel, YorumAdmin)



@admin.register(IletisimModel)

class IletisimAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    search_fields = ('email',)

# admin.site.register(IletisimModel, IletisimAdmin)