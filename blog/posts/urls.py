from django.urls import path
from . import views
urlpatterns=[
    path('',views.view_posts,name='post_home'),
    path('add/',views.add_blog,name='add_blog'),
    path('<slug:slug>/',views.single_post,name='single_post'),
]