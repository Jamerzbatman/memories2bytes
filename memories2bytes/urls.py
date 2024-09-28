from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('quotes/', include('quotes.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('pages.urls')),
]
