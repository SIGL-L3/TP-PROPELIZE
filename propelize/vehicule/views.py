from django.shortcuts import render

# Create your views here.

#mes modifs

from vehicule.models import Vehicule

def delete_vehicule(vehicule_id):
    try:
        vehicule = Vehicule.objects.get(id=vehicule_id)
        vehicule.delete()
        print(f"Véhicule avec l'ID '{vehicule_id}' supprimé avec succès.")
    except Vehicule.DoesNotExist:
        print(f"Véhicule avec l'ID '{vehicule_id}' introuvable.")
    except Exception as e:
        print(f"Erreur lors de la suppression : {str(e)}")