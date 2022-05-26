from django.shortcuts import render
from django.shortcuts import render

def anasayfa(request):
    context = {
        'isim': 'kardelen cetin'
    }
    return render(request, 'pages/anasayfa.html', context=context)
