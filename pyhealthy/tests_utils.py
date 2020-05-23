import pytest
import requests
from .utils import Utils


@pytest.fixture(autouse=True)
def initialize_utils_class():
    utils = Utils("Pizza")
    return utils


class MockRequestsGet:
    def __init__(self, url=None, params=None, result=None, st_code=200):
        self.result = result
        self.st_code = st_code

    def json(self):
        if self.st_code != 200:
            raise requests.exceptions.HTTPError
        return self.result


results_download = {
    "RESULTS_OK": {
        "page_size": 250,
        "page": 1,
        "count": 276,
        "products": [{"product_name": "product_1"}, {"product_name": "product_2"}]},
    "RESULTS_KEYERROR": {
        "page_size": 250,
        "page": 1,
        "count": 276}
}
fake_received_nutriments = {
    "fat_100g": "10,5",
    "saturated-fat_100g": "3,5",
    "sugars_100g": "2,5",
    "salt_100g": "1,8",
    "other_nutriment1": "X,Y",
    "other_nutriment2": "X,Y",
    "other_nutriment3": "X,Y"
}
fake_received_nutriments_prepared = {
    "fat_prepared_100g": "10,5",
    "saturated-fat_100g": "3,5",
    "sugars_prepared_100g": "2,5",
    "salt_prepared_100g": "1,8",
    "other_nutriment1": "X,Y",
    "other_nutriment2": "X,Y",
    "other_nutriment3": "X,Y"
}
fake_received_categories = "fr:Boissons,Snacks,en:Sugar Snacks,Boissons chaudes,en: Hot Drink"

fake_received_data = {"products": [{"code": 1,
                                    "product_name_fr": "name",
                                    "brands": "brand_name",
                                    "nutrition_grades": "a_to_e",
                                    "ingredients_text_fr": "ingredients",
                                    "url": "url_page",
                                    "small_image": "url_small_image",
                                    "large_image": "url_large_image",
                                    "nutriments": fake_received_nutriments,
                                    "categories": "oder_categorie",
                                    "countries_lc": "fr",
                                    "categories_lc": 'fr',
                                    "other_param_x": "param_x",
                                    "other_param_y": "param_y"
                                    }]
                      }

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
                              "ingredients": "ingredients",
                              "url": "url_page",
                              "small_image_url": "url_small_image",
                              "large_image_url": "url_large_image",
                              "nutriments": fake_result_filtered_nutriments,
                              "categories": "oder_categorie",
                              }]


def test_download_status_is_ok(monkeypatch, initialize_utils_class):
    correct_result = [{"product_name": "product_1"}, {"product_name": "product_2"}]

    def mock_response_ok(*args, **kwargs):
        return MockRequestsGet(result=results_download["RESULTS_OK"])

    monkeypatch.setattr('requests.get', mock_response_ok)

    assert initialize_utils_class.download() == correct_result


def test_download_return_status_not_ok(monkeypatch, initialize_utils_class, capsys):
    exception_request_stdout = "There is a problem with the OFF servor or your connection"

    def mock_response_not_ok(*args, **kwargs):
        return MockRequestsGet(st_code=400)

    monkeypatch.setattr('requests.get', mock_response_not_ok)

    initialize_utils_class.download()
    captured = capsys.readouterr()
    assert captured.out == exception_request_stdout


def test_download_with_keyerror_in_result(monkeypatch, initialize_utils_class, capsys):
    exception_stdout = "There is a problem with the OFF data return"

    def mock_response_keyerror(*args, **kwargs):
        return MockRequestsGet(result=results_download["RESULTS_KEYERROR"])

    monkeypatch.setattr('requests.get', mock_response_keyerror)

    initialize_utils_class.download()
    captured = capsys.readouterr()
    assert captured.out == exception_stdout


def test_clean_nutriments_return_good_format(initialize_utils_class):
    assert initialize_utils_class.clean_nutriments(**fake_received_nutriments) == fake_result_filtered_nutriments


def test_clean_nutriments_prepared_return_good_format(initialize_utils_class):
    assert initialize_utils_class.clean_nutriments(
        **fake_received_nutriments_prepared) == fake_result_filtered_nutriments


def test_clean_categories_return_good_format(initialize_utils_class):
    assert initialize_utils_class.clean_categories(fake_received_categories) == fake_result_filtered_categories
