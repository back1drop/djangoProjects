from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=[
            'title',
            'author',
            'content',
            ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter post title'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Author name'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your blog content here...',
                'rows': 6
            }),
        }