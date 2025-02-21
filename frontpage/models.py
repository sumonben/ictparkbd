from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Carosel(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=100)
    ctext=models.TextField()
    cimage=models.ImageField(upload_to='media/',blank=True,null=True)
    
class News(models.Model):
    title=models.CharField(max_length=1000)
    body=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    