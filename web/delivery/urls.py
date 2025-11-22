from django.urls import path, include
from .views import HomeView

app_name = 'delivery'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("orders/", include(("delivery.orders.urls", "orders"), namespace="orders"),),
    path("restaurant/", include(("delivery.restaurant.urls", "restaurant"), namespace="restaurant"),),
    path("auth/", include(("delivery.auth.urls", "auth"), namespace="auth"),),
]
