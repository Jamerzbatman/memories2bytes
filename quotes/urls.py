from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_quote_view, name='add_quote_view'),
] 
