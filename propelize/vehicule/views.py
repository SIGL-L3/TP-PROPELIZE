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

            vehicule = Vehicule.objects.create(
                registration_number=data["registration_number"],
                make=data["make"],
                model=data["model"],
                year=data["year"],
                rentalprice=data["rentalprice"]
            )
            print(data)
        print('test')
        print(vehicule)
        return Response({"Success Create vehicule"})