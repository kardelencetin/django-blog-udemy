from django.db import models
from django.contrib.auth.models import User
from blog.models import YazilarModel
from blog.abstract_models import DateAbstractModal

class YorumModel(DateAbstractModal):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()
    

    class Meta:
        db_table = 'yorum'
        verbose_name = 'yorum'
        verbose_name_plural = 'yorumlar'
    
    def __str__(self):
        return self.yazan.username