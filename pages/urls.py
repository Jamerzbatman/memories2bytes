from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_view, name='about'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('process/', views.process_view, name='process'),


] 
