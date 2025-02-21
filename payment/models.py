from django.db import models

# Create your models here.
class Payment():

    email=models.EmailField(max_length=100, unique=True)
    user_id=models.IntegerField(max_length=100)
    phone=models.IntegerField(max_length=100)
    amount=models.IntegerField(max_length=10,null=True)
    month=models.CharField(max_length=12, )
    start_date=models.DateField( null=True)
    end_date=models.DateField(null=True)
    applicable=models.BooleanField(default=True,null=True)
    status=month=models.CharField(max_length=12, default='Not Paid')
    deadilne=models.DateField(null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)

