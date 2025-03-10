
from django.contrib import admin
from django.urls import path
from quickapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('Gallery/', views.Gallery,name='Gallery'),
    path('about/', views.about,name='about'),
    path('form/', views.form,name='form'),
    path('products/', views.product,name='products'),
    path('services/', views.service,name='services'),
]
