import pytest
from ..main import main

fake_result_filtered_nutriments = {'saturated_fat_quantity': "3,5",
                                   "fat_quantity": "10,5",
                                   "sugars_quantity": "2,5",
                                   "salt_quantity": "1,8"
                                   }
fake_result_filtered_categories = ["Boissons", "Snacks", "Boissons chaudes"]
fake_result_filtered_data = [{"id": 1,
                              "name": "name",
                              "brand": "brand_name",
                              "nutrition_grade": "a_to_e",
                              "ingredients": "Ingredient 1, ingredient 2",
                              "url": "url_page",
                              "small_image_url": "https://static.openfoodfacts.org/images/products/303/371/006"
                                                 "/5066/front_fr.143.200.jpg",
                              "large_image_url": "https://static.openfoodfacts.org/images/products/303/371/006"
                                                 "/5066/front_fr.143.400.jpg",
                              "nutriments": fake_result_filtered_nutriments,
                              "categories": fake_result_filtered_categories,
                              }]


def mock_download_data_class(*args, **kwargs):
    pass


def mock_clean_data_class(*args, **kwargs):
    return fake_result_filtered_data


def test_main_return_correct_data(monkeypatch):
    monkeypatch.setattr('utils.download.DownloadData.download', mock_download_data_class)
    monkeypatch.setattr('utils.clean.CleanData.clean', mock_clean_data_class)
    assert len(main()) == 6


def test_main_return_list_of_dict(monkeypatch):
    monkeypatch.setattr('utils.download.DownloadData.download', mock_download_data_class)
    monkeypatch.setattr('utils.clean.CleanData.clean', mock_clean_data_class)
    assert type(main()[0]) is dict
