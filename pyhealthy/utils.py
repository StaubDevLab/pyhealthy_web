import requests
from django.conf import settings
import sys


class Utils:

    def __init__(self, category):
        self.api_url_OFF = 'https://fr.openfoodfacts.org/cgi/search.pl'
        self.api_params_OFF = {
            "json": 1,
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": category,
            "page_size": 250,
            "action": "process"
        }

    def download(self):
        try:
            products = requests.get(self.api_url_OFF, params=self.api_params_OFF).json()['products']
            return products
        except requests.exceptions.HTTPError:
            sys.stdout.write('There is a problem with the OFF servor or your connection')
        except KeyError:
            sys.stdout.write('There is a problem with the OFF data return')

    def clean_nutriments(self, **kwargs):
        clean_nutriments = {}
        search_nutriments = ['salt_100g', 'sugars_100g', 'fat_100g', "saturated-fat_100g", "salt_prepared_100g",
                             "sugars_prepared_100g", "fat_prepared_100g", "saturated-fat_prepared_100g"]
        for key, value in kwargs.items():
            if key in search_nutriments:
                if key == "saturated-fat_100g":
                    clean_nutriments['saturated_fat_quantity'] = value
                elif "prepared" in key:
                    clean_nutriments[key.replace("prepared_100g", "quantity")] = value
                else:
                    clean_nutriments[key.replace("100g", "quantity")] = value
            else:
                pass
        return clean_nutriments

    def clean_categories(self, cat):
        return [cat.lstrip('fr: ').capitalize() for cat in cat.split(',') if not cat.startswith((' en:', 'en:'))]