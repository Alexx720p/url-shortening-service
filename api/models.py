from django.db import models

# Create your models here.

class Url(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    access_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.short_url_code} -> {self.original_url}'