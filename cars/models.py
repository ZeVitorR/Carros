from django.db import models

# Criando o model de informação do carro
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)
    Model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
