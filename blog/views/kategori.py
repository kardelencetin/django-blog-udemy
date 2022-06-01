from django.shortcuts import get_object_or_404, render
from blog.models import YazilarModel, KategoriModel
from django.core.paginator import Paginator

def kategori(request, kategoriSlug):
    kategori = get_object_or_404(KategoriModel, kategori_slug=kategoriSlug)
    # yazilar = YazilarModel.objects.order_by('-id')
    yazilar = kategori.yazi.order_by('-id')
    print(yazilar)
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 2)
    return render(request, 'pages/kategori.html', context={
        'yazilar': paginator.get_page(sayfa),
        'kategori_isim': kategori.isim
    })
