# Documentation WebScraping pour exemple sur books.toscrape.com
:grinning: Fait par @AmandineGit le 15 septembre 2023

## Utilisation du script de scraping web
Il s'agit d'un script permettant la récupération de données et d'images concernant tous les ouvrages du site https://books.toscrape.com</br>
Les données à extraires sont :
+ <span style="color:orange"> product_page_url ==> </span>url de la page de l'ouvrage
+ <span style="color:orange"> UPC ==> </span> référence de l'ouvrage
+ <span style="color:orange"> title ==> </span> titre de l'ouvrage
+ <span style="color:orange"> Price (incl. tax) ==> </span> prix de l'ouvrage TTC
+ <span style="color:orange"> Price (excl. tax) ==> </span> prix de l'ouvrage HT
+ <span style="color:orange"> Availability ==> </span> disponibilité de l'ouvrage
+ <span style="color:orange"> product_description ==> </span> description de l'ouvrage 
+ <span style="color:orange"> category ==> </span> catégorie de l'ouvrage 
+ <span style="color:orange"> review_rating ==> </span> note de l'ouvrage
+ <span style="color:orange"> image_url ==> </span> url de l'image de couverture de l'ouvrage

Les données seront oragnisées dans des fichiers CSV (avec comme délimiteur : ','), organisés par catégorie en sous-répertoires du dossier projet. </br>
Les fichiers images correpondant aux couvertures des ouvrages sont stockés dans un sous-répertoire du répertoire correpondant à la catégorie de l'ouvrage. 


### Création de l'environnement virtuel necéssaire pour l'execution
- [ ] Créer un environnement virtuel nommé `env` grace à la commande : `>>> python3 -m venv env`
- [ ] Activer l'environnment virtuel crée avec la commande : `>>> source env/bin/activate`
- [ ] Vérifier, votre prompt doit afficher : <span style="color:green">(env)</span> `user@machine:~/repertoire_projet$`


### Installation des paquets necéssaires 
- [ ] Installer les paquets dans la version recommandée dans le requirement.txt grace à la commande pip : </br>
     `(env) user@machine:~/repertoire_projet$ pip install paquet_a_installer==version`</br>
- [ ] Vérifier l'installation des paquets grace à :</br>
       ```(env) user@machine:~/repertoire_projet$ pip freeze```</br>
        Le retour devrait correspondre à :</br>
       `beautifulsoup4==4.12.2`</br>
       `bs4==0.0.1`</br>
       `certifi==2023.7.22`</br>
       `charset-normalizer==3.2.0`</br>
       `csv23==0.3.4`</br>
       `idna==3.4`</br>
       `lxml==4.9.3`</br>
       `requests==2.31.0`</br>
       `soupsieve==2.5`</br>
       `urllib3==2.0.4`</br>

### Execution du script

 - [ ] Lancer le script à partir du répertoire courant (racine du répertoire projet) via la commande :</br>
       `(env) user@machine:~/repertoire_projet$ ./script.py`</br>
### Validation & récupération des fichiers
 - [ ] Controler l'execution via l'affichage écran qui commente les différentes actions réalisées
 - [ ] Controler les fichiers de données et les images téléchargées.</br>
        Le script va créer un répertoire par catégorie d'ouvrage, dans chaque répertoire se trouve un fichier CSV contenant les données extraites, ainsi qu'un sous répertoire nommé "images-catego-_categorie_".