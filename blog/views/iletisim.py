from django.shortcuts import render, redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel

def iletisim(request):
    form = IletisimForm(data={
        'isim_soyisim': '',
        'email': 'krdlnctn@gmail.com',
        'mesaj': 'hi world!'

    })

    # print(form.errors) -> ekrana hatayı basar.
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            # print(form) -> html vs inputları döndürür.
            # print(form.cleaned_data.get('email'))
            # iletisim = IletisimModel()
            # iletisim.email = form.cleaned_data['email']
            # iletisim.isim_soyisim = form.cleaned_data['isim_soyisim']
            # iletisim.mesaj = form.cleaned_data['mesaj']
            # iletisim.save()
            form.save()
            return redirect('anasayfa')
        else:
            print('invalid')
    context = {
        'form': form
    }
    return render(request, 'pages/iletisim.html', context=context)
