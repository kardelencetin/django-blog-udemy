from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def yazilarim(request):
    yazilar = request.user.yazilar.order_by('-id')
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 1)
    return render(request, 'pages/yazilarim.html', context={
        'yazilar': paginator.get_page(sayfa),
        
    })
