from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('features/', views.features, name='features'),
    path('blog/', views.blog, name='blog'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testmonial, name='testimonial'),
    path('contact/',views.contact, name='contact')
]