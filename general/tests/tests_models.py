from django.test import TestCase
from general.models import Category


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
