from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    disease = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name