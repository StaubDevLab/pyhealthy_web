[![Badge langage](https://img.shields.io/static/v1?label=langage&message=Français&color=blue)](https://github.com/GuillaumeStaub/pyhealthy_web/blob/master/README_fr.md)
[![Badge langage](https://img.shields.io/static/v1?label=langage&message=English&color=blue)](https://github.com/GuillaumeStaub/pyhealthy_web/blob/master/README.md)

# PyHealthy with Django for PurBeurre
**Link to the application : *Bientôt disponible***

## Pourquoi ce programme?
PyHealthy une application web de la société Pur Beurre. Cette application, interroge l'API d'[OpenFoodFacts](https://fr.openfoodfacts.org) afin de trouver un substitut plus sain à un aliment recherché. Donc si si vous voulez trouver un substitut à votre boisson américaine préférée vous avez juste à la renseigner et magie l'application vous retourne un équivalent bien meilleur pour vos kilos en trop. En plus d'afficher le substitut, PyHealthy de Pur Beurre, vous propose, son NutriScore, sa photo , ses nutriments et un lien vers Open Food Facts pour visualiser d'avantages d'informations.

## Fonctionnement général
> ### Etape 1: Télécharger, Nettoyer and Insérer les données

Tout d'abord, il faut récupérer les données, pour cela, j'utilise l'API d'OpenFoodFacts qui est libre et 100% gratuite. La documentation est disponible sur leur [site](https://en.wiki.openfoodfacts.org/API/Read/Search).
Il faut ensuite nettoyer les données reçues par l'API et ne garder que les informations essentielles. Certaines informations demandent un traitement supplémentaire notamment pour la mise en forme. 
J'ai créé une **commande Django** qui télécharge, nettoie et instancie les données dans la base. 
Une deuxième commande django est créée pour mettre à jour les données. 

> ### Etape 2: Bienvenue à toi utilisateur, utilise l'auto-complétion

Ensuite **l'utilisateur se rend sur l'application**, utilise la barre de recherche, **l'auto-complétion** propose quelques produits à l'utilisateur qu'il peut choisir. Si l'utilisateur n'est pas satisfait il peut alors taper *Enter* pour arriver sur une page avec d'avantage de choix. 

> ### Etape 3: L'algorithme qui trouve le meilleur du meilleur

L'utilisateur choisit un produit et l'application propose un substitut. Le substitut est basé sur un algorithme simple, il recherche un produit avec un nutriscore moins élevé et qui a le plus de catégories en commun avec le produit à substituer. 
L’utilisateur peut alors accéder au détail des deux produits (substitut et substitué) pour connaître les nutriments et le lien vers Open Food Facts.

> ### Etape 4: Enregistrer votre recherche ou au revoir

L’utilisateur peut alors sauvegarder sa recherche soit, la combinaison du produit recherché et de son substitut.  Pour cela il doit créer un compte et s’authentifier. 

*Diagramme du fonctionnement général*
> #### In progress

## Visuels
Démonstration du parcours utilisateur :

> #### In progress

## Dépendances
* Python 3.7.4
* Django 3.0.6
* Gunicorn 20.0.4
* Django-reverse-admin 2.8.4
* Requests 2.23.0
* Selenium 3.141.0
* Pytest 5.4.1

## Compétences mobilisées
* Développer une application proposant les fonctionnalités attendues par le client
* Mettre en œuvre des tests d’intégration
* Mettre en œuvre des tests unitaires
* Pérenniser son projet web en créant un plan de test
* Produire un rapport de l’exécution des tests
* Créer un site web avec HTML5, le mettre en forme avec CSS3 et le dynamiser avec JavaScript
* Utiliser un Framwork Python (Django)
* Déployer une application sur Heroku

## Contribuer au programme
* Fork le
* Créez votre banche `git checkout -b my-new-feature`
* Commit les changements `git commit -am 'Add some feature'`
* Push ta branche `git push origin my-new-feature`
* Créez une Pull Request