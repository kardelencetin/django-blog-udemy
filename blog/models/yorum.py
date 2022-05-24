from django.db import models
from django.contrib.auth.models import User
from blog.models import YazilarModel

class YorumModel(models.Model):
    yazan = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'yorum'
        verbose_name = 'yorum'
        verbose_name_plural = 'yorumlar'
    
    def __str__(self):
        return self.yazan.username