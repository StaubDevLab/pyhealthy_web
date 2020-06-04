class CleanData:

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

    def clean(self, gross_products):
        clean_products = []
        need_field = {"code": "id", 'categories': "categories", 'product_name_fr': "name",
                      'nutrition_grades': "nutrition_grade", 'ingredients_text_fr': "ingredients", 'brands': "brand",
                      'url': "url", "small_image": "small_image_url",
                      "large_image": "large_image_url", "nutriments": "nutriments"}

        for product in gross_products:
            product_item = {}
            try:
                if product["product_name_fr"] and product["countries_lc"] == "fr" and product["code"] \
                        and product["categories_lc"] == "fr":
                    for key, value in need_field.items():

                        if key == "ingredients_text_fr":
                            product_item[value] = product[key].replace('_', ' ').lstrip()
                        elif key == "nutriments":
                            product_item[value] = self.clean_nutriments(**product[key])
                        elif key == "large_image":
                            product_item[value] = product["selected_images"]["front"]["display"]['fr']
                        elif key == "small_image":
                            product_item[value] = product["selected_images"]["front"]["small"]['fr']
                        elif key == "code":
                            product_item[value] = int(product[key])
                        elif key == "categories":
                            product_item[value] = self.clean_categories(product[key])
                        else:
                            product_item[value] = product[key]
                    clean_products.append(product_item)

            except KeyError:
                continue
        return clean_products
