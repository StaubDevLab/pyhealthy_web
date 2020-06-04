import requests
import sys


class DownloadData:

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