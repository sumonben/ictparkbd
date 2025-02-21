from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Subject(models.Model):
    subject_name=models.CharField(max_length=100,unique=True)
    subject_image=models.ImageField(upload_to='media/',blank=True,null=True)
    chapter_number=models.IntegerField()
    def __str__(self):
        return self.subject_name


class Chapter(models.Model):
    chapter_id=models.IntegerField()
    chapter_name=models.CharField(max_length=100)
    chapter_image=models.ImageField(upload_to='media/',blank=True,null=True)
    subject=models.ForeignKey(Subject,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.chapter_id, self.chapter_name)
    def get_absolute_url(self):
        return reverse("chapter", args=[str(self.id)])

    
class Lecture(models.Model):
    topic_id=models.CharField(max_length=10)
    topic_name=models.CharField(max_length=512)
    file_type=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    reference=models.CharField(max_length=100,blank=True,null=True)
    file=models.FileField(upload_to='media/',blank=True,null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    #subject=models.CharField(max_length=100)
    chapter=models.ForeignKey(Chapter,null=True,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("topic", args=[str(self.id)])