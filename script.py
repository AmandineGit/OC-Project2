import os.path
from bs4 import BeautifulSoup as bs
import requests
import csv23 as csv
import geturlsslist

# Variables globales
datas_entete = ['product_page_url', 'UPC', 'title', 'Price (incl. tax)', 'Price (excl. tax)', 'Availability,product_description', 'category', 'review_rating', 'image_url']
datas_content = []
nom_csv = 'fichier.csv'
url = 'https://books.toscrape.com/'
list_urls_catego_livres = []
compteur = 0


def info_livre(urlexo2):
    # definition de la fonction info_livre qui récupère les infos d'un livre dont l'url est rnseignée en paramètre
    # connection à la page contenant les données & récupération du code réponse de la page du produit et test si ok
    response = requests.get(urlexo2)
    if response.ok:

        # création de mon object soup
        soup = bs(response.content, 'lxml')

        # sélection des données voulues
        tds = soup.findAll('td')

        # extration des balises et création des objects de données
        datas = []
        for td in tds:
            td2 = bs(td.text, 'lxml').text
            datas.append(td2)
        # intégration de l'URL dans la liste
        datas.insert(0, urlexo2)
        # récupération du title
        h1 = soup.find('h1')

        # remplacement de Product_type par title
        h1b = bs(h1.text, 'lxml').text
        datas[2] = h1b

        # récupération de Product_description, passage en string et suppression des balises
        proddesc = soup.findAll('p')
        proddesc = proddesc[3]
        proddesc = str(proddesc)
        proddesc = proddesc[3:-4]
        # print (proddesc)

        # Récupération de category
        catego = soup.findAll('li')
        catego = catego[2]
        catego = catego.find('a')
        catego = catego.text
        # print(catego)

        # récupération de review_rating
        rev_rat = soup.findAll('p')
        rev_rat = rev_rat[2].attrs
        rev_rat = rev_rat["class"]
        rev_rat = rev_rat[1]
        # print(rev_rat)

        # recupération de l'url de l'image
        img = soup.img['src']
        link_img = 'https://books.toscrape.com/' + img[6:]
        # print(link_img)

        # Rassemblement des données et mise en forme
        datas.insert(3, datas[4])
        datas.pop(5)
        datas.pop(5)
        datas.pop(6)
        datas.insert(6, proddesc)
        datas.insert(7, catego)
        datas.insert(8, rev_rat)
        datas.insert(9, link_img)
        global datas_content
        datas_content = datas
        return datas_content
    else:
        print('response not ok for : ' + urlexo2)


def csv_creationwithentete(entete, datas, name_csv):
    # fonction de création d'un csv à partir des données retournées par info_livre(urlexo2)
    if os.path.exists(nom_csv):
        with open(name_csv, 'a') as CSV1livre:
            writer = csv.writer(CSV1livre)
            data = datas
            writer.writerow(data)
            CSV1livre.close()
        print('Le fichier CSV : ', nom_csv, ' a été mis à jour.')
    else:
        global compteur
        with open(name_csv, 'w') as CSV1livre:
            writer = csv.writer(CSV1livre)
            headers = entete
            writer.writerow(headers)
            data = datas
            writer.writerow(data)
            CSV1livre.close()
        compteur = compteur + 1
        print('Le fichier CSV : ', nom_csv, ' a été crée.')


# pour chaque url de links_catego_livres j'execute info_livre puius csv_creation et les données s'ajoute dans le même fichier csv
def csv_datas_livresbycatego():
    liste = geturlsslist.namelinks_allbooks
# decommenter si besoin de test sur une liste restreinte
# liste = listetest
    for line in range(len(liste)):
        listline = liste[line]
        catego = listline[0]
        url_livre = listline[1]
        global nom_csv
        nom_csv = 'catego' + '_' + catego + '.csv'
        print('le lien est : ', url_livre)
        csv_creationwithentete(datas_entete, info_livre(url_livre), nom_csv)
    global compteur
    print(compteur, 'fichiers CSV ont été crées.')


# ------------------- Lancement du programme -----------------------------#
geturlsslist.urls_catego_livres(geturlsslist.recup_urlallpages(geturlsslist.recup_catego(url)))
csv_datas_livresbycatego()

# ---------------------- Test unitaires ----------------------------------#

# execution de info_livre avec une url
# urlexo2 = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
# info_livre(urlexo2)
# print(datas_entete)
# print(datas_content)

# execution de csv_creation avec un echantillon
# entete = ('product_page_url', 'UPC,title', 'Price (incl. tax)')
# datas = ('https://books.toscrape.com/catalogue/sharp-objects_997/index.html', 'e00eb4fd7b871a48', 'Sharp Objects', '£47.82')
# csv_creationwithentete(entete, datas, name_csv)

# execution de urls_catego_livres depuis script.py pour charger la variable namelinks_allbooks ou la fournir en retour
# geturlsslist.urls_catego_livres(geturlsslist.recup_urlallpages(geturlsslist.recup_catego(url)))

# execution de csv_datas_livresbycatego avec un echantillon
# listetest = [['mystery_3', 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'],['travel_2', 'https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html']]
# les print sont à de-commenter dans la boucle dans la boucle
# print('nom csv : ', nom_csv)
# print('le lien est : ',url_livre)

# execution de info_livre avec une url de test
# urlexo2 = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
# print(info_livre(urlexo2))
# print(datas_entetes)
# print(datas_content)
