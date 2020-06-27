[![Badge langage](https://img.shields.io/static/v1?label=langage&message=Français&color=blue)](https://github.com/GuillaumeStaub/pyhealthy_web/blob/master/README_fr.md)
[![Badge langage](https://img.shields.io/static/v1?label=langage&message=English&color=blue)](https://github.com/GuillaumeStaub/pyhealthy_web/blob/master/README.md)



# PyHealthy with Django for Pur Beurre

**Link to the application : *Coming soon***

## Why this program
PyHealthy a web application from the company Pur Beurre.This application, queries the **[OpenFoodFacts](https://fr.openfoodfacts.org)** API to find a healthier substitute for a desired food. So if you want to find a substitute for your favorite American drink you just have to fill it in and the magic app returns you a much better product for your extra pounds. In addition to displaying the substitute, **PyHealthy**, offers, its **nutrition grade**, an image of it, its nutriments and a link to Open Food Facts to view more information.

## General operation
> ### Step 1: Download, Clean and Inject data

First of all, you have to recover the data, for that I use the OpenFoodFacts API which is free and 100% free. The documentation is available on their  [website](https://en.wiki.openfoodfacts.org/API/Read/Search).
Then clean the data received by the API and keep only the essential information. Some informations requires additional processing, particularly for shaping.
I created a **Django command** that downloads, cleans up and instantiates the data in the database.
A second django command is created to update the data.

> ### Step 2: Welcome user, use autocomplete

Then **the user goes to the application**, uses the search bar, the **auto-completion** offers some products to the user that he can choose. If he isn't satisfied he can then type *Enter* to go on a page with more choices.
> ### Step 3: Algorithm that finds better than better


The user chooses a product and the application offers a substitute. The substitute is based on a *simple algorithm*, it searches for a product with a lower nutriscore and which has the most categories in common with the product to be substituted.
The user can then access the detail of the two products (substitute and substituted) to find out the nutrients and the link to Open Food Facts.

> ### Step 4: Save your search or goodbye

The user can then save his search, which is the combination of the product sought and his substitute. For this he must create an account and authenticate.
*General operation diagram:*
> #### In progress

## Visual
User Storie Démo :

> #### In progress

## Dependencies
* Python 3.7.4
* Django 3.0.6
* Gunicorn 20.0.4
* Django-reverse-admin 2.8.4
* Requests 2.23.0
* Selenium 3.141.0
* Pytest 5.4.1

## Skills mobilized
* Develop an application offering the features expected by the client
* Implement integration tests
* Implement unit tests
* Sustain your web project by creating a test plan
* Produce test execution report
* Create a website with HTML5, format it with CSS3 and boost it with JavaScript
* Use a Python framework (Django)
* Deploy a web application on Heroku

## Contribute to the program 

* Fork it
* Create your feature branch (`git checkout -b my-new-feature`)
* Commit your changes (`git commit -am 'Add some feature'`)
* Push to the branch (`git push origin my-new-feature`)
* Create new Pull Request