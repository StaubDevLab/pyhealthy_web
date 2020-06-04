import pytest
from django.core.management import call_command
from general.models import Product, Nutriment, Category
from django.db import DataError


fake_result_filtered_categories = ["Boissons", "Snacks", "Boissons chaudes"]
fake_result_filtered_nutriments = {'saturated_fat_quantity': 3,
                                   "fat_quantity": 10,
                                   "sugars_quantity": 2,
                                   "salt_quantity": 0
                                   }
fake_data = [{"id": 1,
              "name": "name",
              "brand": "brand_name",
              "nutrition_grade": "a",
              "ingredients": "Ingredient 1, ingredient 2",
              "url": "url_page",
              "small_image_url": "https://static.openfoodfacts.org/images/products/303/371/006"
                                 "/5066/front_fr.143.200.jpg",
              "large_image_url": "https://static.openfoodfacts.org/images/products/303/371/006"
                                 "/5066/front_fr.143.400.jpg",
              "nutriments": fake_result_filtered_nutriments,
              "categories": fake_result_filtered_categories,
              }]

fake_data_error = [{"id": 1,
                    "name": "name",
                    "brand": "brand_name",
                    "nutrition_grade": "a",
                    "ingredients": "Ingredient 1, ingredient 2",
                    "url": "url_page",
                    "small_image_url": "https://static.openfoodfacts.org/images/products/303/371/006"
                                       "/5066/front_fr.143.200.jpg",
                    "large_image_url": "https://static.openfoodfacts.org/images/products/303/371/006"
                                       "/5066/front_fr.143.400.jpg",
                    "nutriments": fake_result_filtered_nutriments,
                    "categories": fake_result_filtered_categories,
                    }]


@pytest.mark.django_db(transaction=True, reset_sequences=True)
class TestCreateCommand:

    def mock_response_main_fake_data(self, *args, **kwargs):
        return fake_data

    def mock_response_main_fake_data_error(self, *args, **kwargs):
        return fake_data_error

    pytestmark = pytest.mark.django_db

    def test_create_data_in_db(self, monkeypatch):
        monkeypatch.setattr('utils.main.main', self.mock_response_main_fake_data)
        call_command('create')
        product = Product.objects.filter(pk=1)
        nutriments = Nutriment.objects.filter(pk=1)
        category = Category.objects.filter(pk=1)
        assert product.exists() == True
        assert nutriments.exists() == True
        assert category.exists() == True

    def test_create_command_success_message(self, capsys, monkeypatch):
        monkeypatch.setattr('utils.main.main', self.mock_response_main_fake_data)
        call_command('create')
        exception_stdout = 'Data has been successfully downloaded and created\n'
        captured = capsys.readouterr()
        assert captured.out == exception_stdout

    """def test_create_command_pass_if_data_error(self, monkeypatch):
            with pytest.raises(DataError):
                monkeypatch.setattr('pyhealthy.utils.main', self.mock_response_main_fake_data_error)
                call_command('create')"""


