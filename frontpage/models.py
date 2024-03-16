from django.db import models

# Create your models here.
class Carosel(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=40)
    ctext=models.CharField(max_length=256)
    cimage=models.ImageField(upload_to='media/',blank=True,null=True)
    
    