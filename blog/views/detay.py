from django.shortcuts import get_object_or_404, render


from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel

def detay(request, yazi_slug):
    yazi = get_object_or_404(YazilarModel, yazi_slug=yazi_slug)
    yorumlar = yazi.yorumlar.all()
    return render(request, 'pages/detay.html', context={
        'yazi': yazi,
        'yorumlar': yorumlar
    })