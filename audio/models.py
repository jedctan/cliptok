from django.db import models

# Create your models here.

from django.db import models

class Audio(models.Model):
    '''Core model for downloading audio clips'''
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='audio/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
