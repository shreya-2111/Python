from django.db import models

class Food(models.Model):

    category_choice = [
        ('veg','veg'),
        ('non-veg','non-veg'),
        ('drinks','drinks'),    
    ]

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category= models.CharField(max_length=20,choices=category_choice)
    description = models.TextField()

    def __str__(self):
        return self.name