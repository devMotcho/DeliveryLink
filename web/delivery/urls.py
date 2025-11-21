from django.urls import path
from .views import home

app_name = 'delivery'

urlpatterns = [
    path('', home, name='home')
]
