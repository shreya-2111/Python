from django.db import models

class Job(models.Model):

    CATEGORY_CHOICES = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Marketing', 'Marketing'),
    ]

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.title