import json
from django.core.management.base import BaseCommand
from vehicule.models import Vehicule  

#la commande externe est python3 manage.py load_fixtures dau niveau de manage.py 

class Command(BaseCommand):
    help = 'Charge les données depuis un fichier JSON dans la base de données'

    def handle(self, *args, **options):
        with open('vehicule/fixtures/initial_data.json', 'r', encoding='utf-8') as f:  
            data = json.load(f)

        for item in data:
            if item['model'] == 'vehicule.vehicule':
                try:
                    Vehicule.objects.create(
                        registration_number=item['fields']['registration_number'],
                        make=item['fields']['make'],
                        model=item['fields']['model'],
                        year=item['fields']['year'],
                        rentalprice=item['fields']['rentalprice']

                        
    
    
                    )
                    self.stdout.write(self.style.SUCCESS(f"Véhicule créé : {item['fields']['registration_number']} {item['fields']['make']}  {item['fields']['model']}  {item['fields']['year']} {item['fields']['rentalprice']}"))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Erreur lors de la création du véhicule: {e}"))

        self.stdout.write(self.style.SUCCESS('Données chargées avec succès !'))