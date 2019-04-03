from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date

# Create your models here.
class Profile(models.Model):
    STATE_CHOICES=(('d','Delhi'),('k','Kolkata'),('c','Chennai'),('p','Punjab'))
    GENDER_CHOICES=(('m','Male'),('f','Female'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    fname=models.CharField(max_length=50,default='')
    adsress=models.CharField(max_length=250,default='')
    city=models.CharField(max_length=10,default='')
    postalcode=models.IntegerField(default=123456)
    mobile=models.IntegerField(default=9798779686)
    dob=models.DateField(default=date.today)
    state=models.CharField(max_length=10,choices=STATE_CHOICES,default='')
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,default='m')
    terms=models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.username} Profile'
