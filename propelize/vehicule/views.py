# vehicules/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vehicule

# Cette vue permet de rechercher un véhicule à partir de son numéro d'immatriculation.
# J'utilise csrf_exempt ici car on fait une simple requête GET sans formulaire.
@csrf_exempt
def search_by_registration(request):
    # Je récupère le paramètre 'registration_number' passé dans l'URL
    reg_number = request.GET.get('registration_number')
    
    if reg_number:
        try:
            # Je recherche dans la base un véhicule avec ce numéro
            vehicule = Vehicule.objects.get(registration_number=reg_number)
            # Je prépare les données à renvoyer sous forme JSON
            data = {
                "registration_number": vehicule.registration_number,
                "model": vehicule.model,
                "brand": vehicule.brand,
                "price_per_day": float(vehicule.price_per_day),
            }
            return JsonResponse(data)
        except Vehicule.DoesNotExist:
            # Si aucun véhicule ne correspond, je renvoie une erreur 404
            return JsonResponse({"error": "Vehicule not found"}, status=404)
    
    # Si le paramètre est manquant, je renvoie une erreur 400
    return JsonResponse({"error": "Missing registration_number parameter"}, status=400)


# Cette vue permet de rechercher tous les véhicules ayant un prix inférieur ou égal à un prix donné
@csrf_exempt
def search_by_price(request):
    # Je récupère le paramètre 'max_price' passé dans l'URL
    max_price = request.GET.get('max_price')
    
    if max_price:
        try:
            # Je transforme la valeur reçue en float pour filtrer les prix
            max_price = float(max_price)
            # Je filtre tous les véhicules dont le prix est <= au prix max donné
            vehicules = Vehicule.objects.filter(price_per_day__lte=max_price)
            # Je construis une liste de dictionnaires pour tous les véhicules trouvés
            data = [
                {
                    "registration_number": v.registration_number,
                    "model": v.model,
                    "brand": v.brand,
                    "price_per_day": float(v.price_per_day),
                }
                for v in vehicules
            ]
            # Je renvoie la liste complète en JSON
            return JsonResponse(data, safe=False)
        except ValueError:
            # Si le prix reçu n'est pas un nombre valide, je renvoie une erreur 400
            return JsonResponse({"error": "Invalid price format"}, status=400)
    
    # Si le paramètre est manquant, je renvoie une erreur 400
    return JsonResponse({"error": "Missing max_price parameter"}, status=400)
