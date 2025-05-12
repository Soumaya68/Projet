from django.db import models

class Vehicule(models.Model):
    marque = models.CharField(max_length=100)
    date_achat = models.DateField()
    nb_places = models.IntegerField()
    description = models.TextField()
    longueur = models.FloatField()
    climatisation = models.BooleanField()

    def __str__(self):
        return f"{self.marque} - {self.date_achat}"
