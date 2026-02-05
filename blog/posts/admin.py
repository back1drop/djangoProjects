from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','is_published','created_date')
    list_filter=('is_published','created_date')
    search_fields=('title','content')
    prepopulated_fields={'slug':('title',)}
    ordering=('-created_date',)