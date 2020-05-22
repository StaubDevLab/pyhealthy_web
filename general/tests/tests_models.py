from django.test import TestCase
from general.models import Category, Nutriment, Product


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Boissons')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        assert field_label == 'Catégorie'

    def test_name_label_plural(self):
        field_label_plural = str(Category._meta.verbose_name_plural)
        assert field_label_plural == "Catégories"

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        assert max_length == 80

    def test_object_name_is_name_category(self):
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.name}'
        assert expected_object_name == str(category)


class NutrimentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Nutriment.objects.create(saturated_fat_quantity=12, sugars_quantity=10, fat_quantity=22)

    def test_name_label_saturated_fat_quantity(self):
        nutriment = Nutriment.objects.get(id=1)
        field_label = nutriment._meta.get_field('saturated_fat_quantity').verbose_name
        assert field_label == 'Acides gras saturés'

    def test_name_label_salt_quantity(self):
        nutriment = Nutriment.objects.get(id=1)
        field_label = nutriment._meta.get_field('salt_quantity').verbose_name
        assert field_label == 'Sel'

    def test_name_label_sugars_quantity(self):
        nutriment = Nutriment.objects.get(id=1)
        field_label = nutriment._meta.get_field('sugars_quantity').verbose_name
        assert field_label == 'Sucre'

    def test_name_label_fat_quantity(self):
        nutriment = Nutriment.objects.get(id=1)
        field_label = nutriment._meta.get_field('fat_quantity').verbose_name
        assert field_label == 'Matières Grasses/Lipides'

    def test_default_label_value_is_zero(self):
        nutriment = Nutriment.objects.get(id=1)
        salt_value = nutriment.salt_quantity
        assert salt_value == 0


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass