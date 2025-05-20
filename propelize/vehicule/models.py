from django.db import models

class Vehicule(models.Model):
    registration_number = models.CharField(max_length=127, unique=True, null=False, blank=False)
    make = models.TextField()
    model = models.CharField(max_length=127)
    year = models.PositiveIntegerField()
    rentalprice = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return f'Model:{self.model},{self.rentalprice}'