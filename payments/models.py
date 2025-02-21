from django.db import models

# Create your models here.
class Payment(models.Model):

    email=models.EmailField(max_length=100)
    user_id=models.IntegerField()
    phone=models.IntegerField(null=True)
    amount=models.IntegerField(null=True)
    month=models.CharField(max_length=12)
    start_date=models.DateField( null=True)
    end_date=models.DateField(null=True)
    applicable=models.BooleanField(default=True)
    status=models.CharField(max_length=12, default='Not Paid')
    deadline=models.DateField(null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)

