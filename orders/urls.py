from django.urls import path

from .views import charge

urlpatterns = [
    path('charge/', charge, name='charge')
]
