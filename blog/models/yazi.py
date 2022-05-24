from autoslug import AutoSlugField
from django.db import models
from blog.models import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class YazilarModel(models.Model):
    resim = models.ImageField(upload_to='yazi_resimleri')
    title = models.CharField(max_length=50)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    moderated = models.DateTimeField(auto_now=True)
    yazi_slug = AutoSlugField(populate_from='title', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel)
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yazilar')

    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'
        db_table = 'Yazi'

    def __str__(self):
        return self.title
