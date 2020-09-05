from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser
from django.conf import settings


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
    id = models.BigIntegerField(unique=True, primary_key=True)
    categories = models.ManyToManyField(Category, related_name="Products")
    name = models.CharField(max_length=100, verbose_name="Nom")
    brand = models.CharField(max_length=100, verbose_name="Marque")
    nutrition_grade = models.CharField(max_length=1, verbose_name="Nutri-Score")
    ingredients = models.TextField(verbose_name="Liste des ingrédients")
    nutriment = models.OneToOneField(Nutriment, on_delete=models.CASCADE, default=0, related_name='nutriment')
    url = models.URLField(verbose_name="Lien vers Open Food Facts")
    small_image_url = models.URLField(verbose_name="URL small image")
    large_image_url = models.URLField(verbose_name="URL large image")

    def __str__(self):
        return self.name


class FavoriteUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    base_product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='substituted')
    substitute_product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='substitute')

    def __str__(self):
        return f"Favoris de {self.user}"

    class Meta:
        verbose_name_plural = "Favorites User"
