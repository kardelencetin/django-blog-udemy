from autoslug import AutoSlugField
from django.db import models
from blog.models import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModal

class YazilarModel(DateAbstractModal):
    resim = models.ImageField(upload_to='yazi_resimleri')
    title = models.CharField(max_length=50)
    content = RichTextField()
    yazi_slug = AutoSlugField(populate_from='title', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')
    yazar = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yazilar')

    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'
        db_table = 'Yazi'

    def __str__(self):
        return self.title
