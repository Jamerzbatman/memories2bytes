from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_quote_view, name='add_quote_view'),
    path('fetch/', views.user_quotes_view, name='user_quotes_view'),
] 
