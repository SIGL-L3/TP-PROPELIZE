from django.apps import AppConfig


class VehiculeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicule'
    
    # def ready(self):
    #     from .views import load_initial_data
    #     load_initial_data()
