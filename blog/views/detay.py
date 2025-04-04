from django.shortcuts import get_object_or_404, redirect, render


from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel
from blog.forms import YorumEkleModelForm

def detay(request, yazi_slug):
    yazi = get_object_or_404(YazilarModel, yazi_slug=yazi_slug)
    yorumlar = yazi.yorumlar.all()
    if request.method == 'POST':
        yorum_ekle_form = YorumEkleModelForm(data=request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()
    
    yorum_ekle_form = YorumEkleModelForm()
    return render(request, 'pages/detay.html', context={
        'yazi': yazi,
        'yorumlar': yorumlar,
        'yorum_ekle_form': yorum_ekle_form
    })