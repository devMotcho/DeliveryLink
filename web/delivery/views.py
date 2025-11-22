from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        localidades = 100
        restaurantes = 500
        estafetas = 1500
        distritos = 50

        context = {
            'title': 'O seu restaurante não precisa de estafetas. Agora tem o',
            'project_name': 'DeliveryLink',
            'localidades': localidades,
            'restaurantes': restaurantes,
            'estafetas': estafetas,
            'distritos': distritos
        }
        return render(request, 'delivery/index.html', context)