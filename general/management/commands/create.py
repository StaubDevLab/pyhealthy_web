from django.core.management.base import BaseCommand, CommandError
from utils.main import main
from general.models import Product, Nutriment, Category
from django.db import DataError


class Command(BaseCommand):
    help = 'Create data in the database from the OpenFoodFacts data'

    def handle(self, *args, **options):
        products = main()

        for product in products:

            if not Product.objects.filter(id=product['id']):
                product_db = Product(**{key: value for (key, value) in product.items() if
                                        key in [fields.name for fields in
                                                Product._meta.get_fields()] and key != "categories"
                                        and key != "nutriments"})

                nutriment_db = Nutriment(**{key: value for (key, value) in product['nutriments'].items() if
                                            key in [fields.name for fields in
                                                    Nutriment._meta.get_fields()]})

                product_db.nutriment = nutriment_db
                nutriment_db.save()
                product_db.save()

                for category in product['categories']:
                    category_db, category_created = Category.objects.update_or_create(name=category)
                    product_db.categories.add(category_db)
                    product_db.save()

            self.stdout.write(self.style.SUCCESS('Data has been successfully downloaded and created'))
