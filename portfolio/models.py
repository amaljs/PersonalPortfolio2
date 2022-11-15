from django.db import models

# Create your models here.

class Slider(models.Model):
    image=models.ImageField(upload_to='slider_pics',blank=True)
    name=models.CharField(unique=True,max_length=50)
    class Meta:
        ordering=['name',]
        verbose_name='photos'

    def __str__(self):
        return self.name