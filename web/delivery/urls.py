from django.urls import path, include
from .views import home

app_name = 'delivery'

urlpatterns = [
    path('', home, name='home'),
    path("orders/", include(("delivery.orders.urls", "orders"), namespace="orders"),),
]
