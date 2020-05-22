from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80, verbose_name='Catégorie')

    class Meta:
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.name


class Nutriment(models.Model):
    saturated_fat_quantity = models.FloatField(verbose_name='Acides gras saturés', default=0)
    salt_quantity = models.FloatField(verbose_name='Sel', default=0)
    sugars_quantity = models.FloatField(verbose_name="Sucre", default=0)
    fat_quantity = models.FloatField(verbose_name="Matières Grasses/Lipides", default=0)

class Product(models.Model):
    pass