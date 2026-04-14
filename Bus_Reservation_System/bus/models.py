from django.db import models

class Bus(models.Model):
    bus_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    seats = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.bus_name