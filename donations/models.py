from django.db import models
from django.contrib.auth.models import User


INSTITUTIONS = [
    (1, 'Fundacja'),
    (2, 'Organizacja pozarządowa'),
    (3, 'Zbiórka lokalna'),
]


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField(choices=INSTITUTIONS, default=1)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
