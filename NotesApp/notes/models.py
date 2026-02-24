from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=7,default='#6366f1')
    def __str__(self):
        return self.name

class Note(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notes')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='notes'
    )
    title=models.CharField(max_length=200)
    body=RichTextField()
    is_pinned=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

