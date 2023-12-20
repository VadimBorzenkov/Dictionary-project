from django.db import models

class Dictionary(models.Model):
    english = models.CharField(max_length=128, unique=True)
    russian = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.english} - {self.russian}'
   