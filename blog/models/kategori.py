from enum import unique
import imp
from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    kategori_slug = AutoSlugField(populate_from='isim', unique=True)

    class Meta:
        db_table = 'kategori'
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategori'

    def __str__(self):
        return self.isim