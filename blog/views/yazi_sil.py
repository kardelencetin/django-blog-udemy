from django.contrib.auth.decorators import login_required
from blog.models import YazilarModel
from django.shortcuts import get_object_or_404, redirect

@login_required(login_url='/')
def yazi_sil(request, yazi_slug):
    get_object_or_404(YazilarModel, yazi_slug=yazi_slug, yazar=request.user).delete()
    return redirect('yazilarim')

