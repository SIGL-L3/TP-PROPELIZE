import json
from django.http import JsonResponse
from rest_framework.views import APIView
from vehicule.models import Vehicule
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


class VehiculeView(APIView):
    def post(self,request):
        data = json.loads(request.body)
        if request.method == "POST":
            required_fields = ["registration_number", "make", "model", "year", "rentalprice"]
            for field in required_fields:
                if field not in data:
                    return JsonResponse({"error": f"Le champ {field} est requis."}, status=400)
            
            vehicules = Vehicule.objects.all()
            vehicule_existe = False
            for vehicule in vehicules:
                if data["registration_number"] == vehicule.registration_number:
                    vehicule_existe = True
                    break  # Sortir de la boucle dès qu'on trouve une correspondance
            
            if vehicule_existe:
                print("vehicule existant")
                return JsonResponse({"error": "Impossible de creer un vehicule deja existant !!!"}, status=400)
            else:
                new_vehicule = Vehicule.objects.create(
                    registration_number=data["registration_number"],
                    make=data["make"],
                    model=data["model"],
                    year=data["year"],
                    rentalprice=data["rentalprice"]
                )
                print(new_vehicule)
                print(data)
                return Response({"Success": "Success Create vehicule !!"})
        print('test')
        
        