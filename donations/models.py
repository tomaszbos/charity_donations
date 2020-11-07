from django.db import models


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
