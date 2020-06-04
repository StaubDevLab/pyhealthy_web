from django.conf import settings
from .download import DownloadData
from .clean import CleanData


def main():
    clean_products = []
    for category in settings.CATEGORIES:
        downloader = DownloadData(category=category)
        download_products = downloader.download()
        cleaner = CleanData()
        clean_products.append(cleaner.clean(gross_products=download_products))
    return [product for product_items in clean_products for product in product_items]
