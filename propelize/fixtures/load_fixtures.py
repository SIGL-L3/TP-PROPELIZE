from typing import Any
from django.core.management import call_command
from django.core.management import BaseCommand

class command (BaseCommand):
    help='Charger les fictures automatiquement dans la base de donnees'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'fixtures/initial_data.json')


        