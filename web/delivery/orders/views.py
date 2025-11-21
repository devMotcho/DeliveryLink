from django.shortcuts import render
from django.views import View

# Create your views here.
def home(request):
    context = {
        'title': 'Hello world'
        }
    return render(request, 'orders/index.html', context)

class OrdersListView(View):
    def get(self, request):
        
        orders = [
            {"name": '24" Monitor', "price": 129.90, "available": True},
            {"name": "Mechanical Keyboard", "price": 89.50, "available": False},
            {"name": "Wireless Mouse", "price": 29.99, "available": True},
        ]
        
        context = {
            "orders": orders,
        }
        return render(request, "orders/list.html", context)
