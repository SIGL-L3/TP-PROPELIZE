from django.db import  models

class Vehicule(models.Model):
    registration_number = models.CharField(max_length=127)
    make = models.TextField()
    model = models.CharField(max_length=127)
    year = models.PositiveIntegerField()
    rentalprice = models.DecimalField(max_digits=15,decimal_places=5)
    vol = models.CharField(max_length=127)
    
    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"