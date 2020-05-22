from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80, verbose_name='Catégorie')

    class Meta:
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.name
