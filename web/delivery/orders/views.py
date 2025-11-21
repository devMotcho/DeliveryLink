from django.shortcuts import render
from django.views import View
from .models import Order

# Create your views here.
def home(request):
    context = {
        'title': 'Hello world'
        }
    return render(request, 'orders/index.html', context)

class OrdersListView(View):
    def get(self, request):
        
        orders = Order.objects.filter()
        
        context = {
            "orders": orders,
        }
        return render(request, "orders/list.html", context)
