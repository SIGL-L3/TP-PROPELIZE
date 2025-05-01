from django.http import JsonResponse
from django.views import View
from .models import Vehicule

# Recherche par immatriculation (exact match)
class SearchByRegistrationView(View):
    def get(self, request):
        registration_number = request.GET.get('registration_number')
        if not registration_number:
            return JsonResponse({'error': 'registration_number parameter is required'}, status=400)
        
        vehicules = Vehicule.objects.filter(registration_number=registration_number)
        data = list(vehicules.values())
        return JsonResponse(data, safe=False)

# Recherche par prix maximum
class SearchByPriceView(View):
    def get(self, request):
        max_price = request.GET.get('max_price')
        if not max_price:
            return JsonResponse({'error': 'max_price parameter is required'}, status=400)
        
        try:
            max_price = float(max_price)
        except ValueError:
            return JsonResponse({'error': 'max_price must be a number'}, status=400)

        vehicules = Vehicule.objects.filter(rentalprice__lte=max_price)
        data = list(vehicules.values())
        return JsonResponse(data, safe=False)