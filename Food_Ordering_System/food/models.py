from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name