from django.urls import path, include
from blog.views import iletisim, anasayfa, kategori, yazilarim, detay, yazi_ekle, yazi_guncelle, yazi_sil

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim/', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim/', yazilarim, name='yazilarim'),
    path('detay/<slug:yazi_slug>', detay, name='detay'),
    path('yazi-ekle/', yazi_ekle, name='yazi-ekle'),
    path('yazi-guncelle/<slug:yazi_slug>', yazi_guncelle, name='yazi-guncelle'),
    path('yazi-sil/<slug:yazi_slug>', yazi_sil, name='yazi-sil'),
    
]
