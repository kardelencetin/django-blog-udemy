from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import YaziGuncelleModelForm
from django.contrib.auth.decorators import login_required
from blog.models import YazilarModel

@login_required(login_url='/')
def yazi_guncelle(request, yazi_slug):
    yazi = get_object_or_404(YazilarModel, yazi_slug=yazi_slug, yazar=request.user)
    form = YaziGuncelleModelForm(request.POST or None, files=request.FILES or None, instance=yazi)
    if form.is_valid():
        form.save()
        return redirect('detay', yazi_slug=yazi.yazi_slug)
    return render(request, 'pages/yazi-guncelle.html', context={
        'form': form
    })

