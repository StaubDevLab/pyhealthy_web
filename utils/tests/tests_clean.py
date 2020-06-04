import pytest
from ..clean import CleanData


@pytest.fixture(autouse=True)
def initialize_clean_data_class():
    cleaner = CleanData()
    return cleaner


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

fake_received_data = [{"code": 1,
                                    "product_name_fr": "name",
                                    "brands": "brand_name",
                                    "nutrition_grades": "a_to_e",
                                    "ingredients_text_fr": "   Ingredient_1, ingredient 2",
                                    "url": "url_page",
                                    "selected_images": {
                                        "front": {
                                            "display": {
                                                "fr": "https://static.openfoodfacts.org/images/products/303/371/006"
                                                      "/5066/front_fr.143.400.jpg",
                                                "es": "https://static.openfoodfacts.org/images/products/303/371/006"
                                                      "/5066/front_es.130.400.jpg "
                                            },
                                            "small": {
                                                "fr": "https://static.openfoodfacts.org/images/products/303/371/006"
                                                      "/5066/front_fr.143.200.jpg",
                                                "es": "https://static.openfoodfacts.org/images/products/303/371/006"
                                                      "/5066/front_es.130.200.jpg "

                                            }}},
                                    "large_image": "url_large_image",
                                    "nutriments": fake_received_nutriments,
                                    "categories": fake_received_categories,
                                    "countries_lc": "fr",
                                    "categories_lc": 'fr',
                                    "other_param_x": "param_x",
                                    "other_param_y": "param_y"
                                    },
                                   {"code": 2,
                                    "product": "name",
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

def test_clean_nutriments_return_good_format(initialize_clean_data_class):
    assert initialize_clean_data_class.clean_nutriments(**fake_received_nutriments) == fake_result_filtered_nutriments


def test_clean_nutriments_prepared_return_good_format(initialize_clean_data_class):
    assert initialize_clean_data_class.clean_nutriments(
        **fake_received_nutriments_prepared) == fake_result_filtered_nutriments


def test_clean_categories_return_good_format(initialize_clean_data_class):
    assert initialize_clean_data_class.clean_categories(fake_received_categories) == fake_result_filtered_categories


def test_clean_select_good_products(initialize_clean_data_class):
    assert len(initialize_clean_data_class.clean(fake_received_data)) == 1


def test_clean_return_good_format(initialize_clean_data_class):
    assert initialize_clean_data_class.clean(fake_received_data) == fake_result_filtered_data