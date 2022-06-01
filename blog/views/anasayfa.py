from turtle import title
import django
from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel
from django.core.paginator import Paginator
from django.db.models import Q

def anasayfa(request):
    sorgu = request.GET.get('sorgu')
    print(sorgu)
    yazilar = YazilarModel.objects.order_by('-id')
    if sorgu:
        yazilar = yazilar.filter(
            Q(title__icontains=sorgu) |
            Q(content__icontains=sorgu)
        ).distinct()
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 2)
    return render(request, 'pages/anasayfa.html', context={
        'yazilar': paginator.get_page(sayfa)
    })
