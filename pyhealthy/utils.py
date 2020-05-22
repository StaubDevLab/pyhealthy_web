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
            "tag_0":category,
            "page_size": 250,
            "action": "process"
        }

    def download(self):
        try:
            products = requests.get(self.api_url_OFF, params=self.api_params_OFF).json()['products']
        except requests.exceptions:
            sys.stdout.write('There is a problem with the OFF servor or your connection')
        except KeyError:
            print('There is a problem with the OFF data return')
        return products

