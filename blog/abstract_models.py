from django.db import models

class DateAbstractModal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    moderated = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True
