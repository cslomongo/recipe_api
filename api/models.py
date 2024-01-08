from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title