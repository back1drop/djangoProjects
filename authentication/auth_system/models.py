from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='uploads/', blank=True,null=True)
    bio=models.TextField(blank=True)
    phoneNumber=models.CharField(max_length=15,blank=True)
    def __str__(self):
        return self.user.username


