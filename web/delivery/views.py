from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Hello world'
        }
    return render(request, 'delivery/index.html')