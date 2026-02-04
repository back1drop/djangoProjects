from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    completion_status=models.BooleanField(default=False)
    creation_date=models.DateField(auto_now_add=True)
    due_date=models.DateField(null=False,blank=False)