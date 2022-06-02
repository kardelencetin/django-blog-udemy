from dataclasses import fields
from django import forms
from blog.models import IletisimModel

class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = ['isim_soyisim', 'email', 'mesaj']

    
# class IletisimForm(forms.Form):
#     email = forms.EmailField(label='E-Posta', max_length=100)
#     isim_soyisim = forms.CharField(label='İsim Soyisim',max_length=25)
#     mesaj = forms.CharField(label='Mesajınız',widget=forms.Textarea)