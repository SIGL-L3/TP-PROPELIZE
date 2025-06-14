import json
from django.core.management.base import BaseCommand
from user.models import User


#la commande externe est python3 manage.py loadFixtures au niveau de manage.py 

class Command(BaseCommand):
    help = 'Charge les données depuis un fichier JSON dans la base de données'

    def handle(self, *args, **options):
        with open('user/fixtures/initial_data.json', 'r', encoding='utf-8') as f:  
            data = json.load(f)

        for item in data:
            if item['model'] == 'user.user':
                try:
                    User.objects.create(
                       
                       name =item['fields']['name'],
                        password=item['fields']['password']

                        
    
                    )
                    self.stdout.write(self.style.SUCCESS(f"user créé : {item['fields']['name']} {item['fields']['password']}"))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Erreur lors de la création de l user: {e}"))

        self.stdout.write(self.style.SUCCESS('Données chargées avec succès !'))