from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_contacts, name='contacts_list'),
    path('add/', views.add_contacts, name='add_contact'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]