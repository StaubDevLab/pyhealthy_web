from django.test import TestCase
from general.models import Category, Nutriment, Product, FavoriteUser
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Boissons')

    def test_name_label(self):
        category = Category.objects.get(name='Boissons')
        field_label = category._meta.get_field('name').verbose_name
        assert field_label == 'Catégorie'

    def test_name_label_plural(self):
        field_label_plural = str(Category._meta.verbose_name_plural)
        assert field_label_plural == "Catégories"

    def test_name_max_length(self):
        category = Category.objects.get(name='Boissons')
        max_length = category._meta.get_field('name').max_length
        assert max_length == 80

    def test_object_name_is_name_category(self):
        category = Category.objects.get(name='Boissons')
        expected_object_name = f'{category.name}'
        assert expected_object_name == str(category)


class NutrimentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Nutriment.objects.create(saturated_fat_quantity=12.0, sugars_quantity=10.0, fat_quantity=22.0)

    def test_saturated_fat_quantity_label_(self):
        nutriment = Nutriment.objects.get(id=3)
        field_label = nutriment._meta.get_field('saturated_fat_quantity').verbose_name
        assert field_label == 'Acides gras saturés'

    def test_salt_quantity_label(self):
        nutriment = Nutriment.objects.get(id=3)
        field_label = nutriment._meta.get_field('salt_quantity').verbose_name
        assert field_label == 'Sel'

    def test_sugars_quantity_label(self):
        nutriment = Nutriment.objects.get(id=3)
        field_label = nutriment._meta.get_field('sugars_quantity').verbose_name
        assert field_label == 'Sucre'

    def test_fat_quantity_label(self):
        nutriment = Nutriment.objects.get(id=3)
        field_label = nutriment._meta.get_field('fat_quantity').verbose_name
        assert field_label == 'Matières Grasses/Lipides'

    def test_label_default_value_is_zero(self):
        nutriment = Nutriment.objects.get(id=3)
        salt_value = nutriment.salt_quantity
        assert salt_value == 0


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        nutriment = Nutriment.objects.create()
        Product.objects.create(id=1234556, name='Pizza trois fromages',
                               brand='Sodebo',
                               nutrition_grade='a', ingredients='Pâte à pizza, tomate, emmental, chèvre, mozzarella',
                               nutriment=nutriment, url='http://www.example.com',
                               small_image_url='http://wwwimage.com/200',
                               large_image_url='http://wwwimage.com/400')
        Product.objects.get(id=1234556).categories.create(name='Pizza')

    def test_name_label(self):
        product = Product.objects.get(id=1234556)
        field_name = product._meta.get_field('name').verbose_name
        assert field_name == 'Nom'

    def test_brand_label(self):
        product = Product.objects.get(id=1234556)
        field_name = product._meta.get_field('brand').verbose_name
        assert field_name == 'Marque'

    def test_nutrition_grade_label(self):
        product = Product.objects.get(id=1234556)
        field_name = product._meta.get_field('nutrition_grade').verbose_name
        assert field_name == 'Nutri-Score'

    def test_ingredients_label(self):
        product = Product.objects.get(id=1234556)
        field_name = product._meta.get_field('ingredients').verbose_name
        assert field_name == 'Liste des ingrédients'

    def test_url_label(self):
        product = Product.objects.get(id=1234556)
        field_name = product._meta.get_field('url').verbose_name
        assert field_name == 'Lien vers Open Food Facts'

    def test_small_image_url_label(self):
        product = Product.objects.get(id=1234556)
        field_name = product._meta.get_field('small_image_url').verbose_name
        assert field_name == 'URL small image'

    def test_large_image_url_label(self):
        product = Product.objects.get(id=1234556)
        field_name = product._meta.get_field('large_image_url').verbose_name
        assert field_name == 'URL large image'

    def test_object_name_is_name_product(self):
        product = Product.objects.get(id=1234556)
        expected_object_name = f'{product.name}'
        assert expected_object_name == str(product)

    def test_name_max_length(self):
        product = Product.objects.get(id=1234556)
        max_length = product._meta.get_field('name').max_length
        assert max_length == 100

    def test_brand_max_length(self):
        product = Product.objects.get(id=1234556)
        max_length = product._meta.get_field('brand').max_length
        assert max_length == 100


class FavoriteUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_secret')
        nutriment_1 = Nutriment.objects.create()
        nutriment_2 = Nutriment.objects.create()
        Product.objects.create(id=1234556, name='Pizza trois fromages',
                               brand='Sodebo',
                               nutrition_grade='d', ingredients='Pâte à pizza, tomate, emmental, chèvre, mozzarella',
                               nutriment=nutriment_1, url='http://www.example.com',
                               small_image_url='http://wwwimage.com/200',
                               large_image_url='http://wwwimage.com/400')
        Product.objects.create(id=99999, name='Pizza trois fromages 0%',
                               brand='Sodebo',
                               nutrition_grade='a', ingredients='Pâte à pizza, tomate, emmental, chèvre, mozzarella',
                               nutriment=nutriment_2, url='http://www.example.com',
                               small_image_url='http://wwwimage.com/200',
                               large_image_url='http://wwwimage.com/400')

        FavoriteUser.objects.create(user=User.objects.get(id=1), base_product=Product.objects.get(id=1234556),
                                    substitute_product=Product.objects.get(id=99999))

    def test_object_name_plural(self):
        field_label_plural = str(FavoriteUser._meta.verbose_name_plural)
        assert field_label_plural == "Favorites User"

    def test_object_name(self):
        favorite = FavoriteUser.objects.get(id=1)
        expected_object_name = f'Favoris de {favorite.user.username}'
        assert expected_object_name == str(favorite)
