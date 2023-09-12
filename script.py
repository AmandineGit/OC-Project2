import os.path
from bs4 import BeautifulSoup as bs
import requests
import csv23 as csv
import geturlsslist

# Variables globales
datas_entetes = []
datas_content = []
nom_csv = 'fichier.csv'
url = 'https://books.toscrape.com/'
list_urls_catego_livres = []


def info_livre(urlexo2):
    # definition de la fonction info_livre qui récupère les infos d'un livre dont l'url est rnseignée en paramètre
    # connection à la page contenant les données & récupération du code réponse de la page du produit et test si ok
    response = requests.get(urlexo2)
    if response.ok:

        # création de mon object soup
        soup = bs(response.content, 'lxml')

        # sélection des données voulues
        ths = soup.findAll('th')
        tds = soup.findAll('td')

        # extration des balises et création des objects de données
        entetes = []
        for th in ths:
            th2 = bs(th.text, 'lxml').text
            entetes.append(th2)
        datas = []
        for td in tds:
            td2 = bs(td.text, 'lxml').text
            datas.append(td2)
        # intégration de l'URL et de son entête dans la liste
        entetes.insert(0, 'product_page_url')
        datas.insert(0, urlexo2)

        # récupération du title
        h1 = soup.find('h1')

        # remplacement de Product_type par title
        entetes[2] = 'title'
        h1b = bs(h1.text, 'lxml').text
        datas[2] = h1b

        # récupération de Product_description, passage en string et suppression des balises
        ProdDesc = soup.findAll('p')
        ProdDesc = ProdDesc[3]
        ProdDesc = str(ProdDesc)
        ProdDesc = ProdDesc[3:-4]
        # print (ProdDesc)

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
        entetes.insert(3, entetes[4])
        entetes.pop(5)
        datas.insert(3, datas[4])
        datas.pop(5)
        entetes.pop(5)
        datas.pop(5)

        entetes.pop(6)
        datas.pop(6)

        entetes.insert(6, 'product_description')
        datas.insert(6, ProdDesc)

        entetes.insert(7, 'category')
        datas.insert(7, catego)

        entetes.insert(8, 'review_rating')
        datas.insert(8, rev_rat)

        entetes.insert(9, 'image_url')
        datas.insert(9, link_img)
        global datas_entetes
        global datas_content
        datas_entetes = entetes
        datas_content = datas
    else:
        print('response not ok for : ' + urlexo2)


def csv_creation(entete, data, name_csv):
    # fonction de création d'un csv à partir des données retournées par info_livre(urlexo2)
        if os.path.exists(nom_csv):
            with open(name_csv, 'a') as CSV1livre:
                writer = csv.writer(CSV1livre)
                data = data
                writer.writerow(data)
                CSV1livre.close()
        else:
            with open(name_csv, 'w') as CSV1livre:
                writer = csv.writer(CSV1livre)
                headers = entete
                writer.writerow(headers)
                data = data
                writer.writerow(data)
                CSV1livre.close()



# pour chaque url de links_catego_livres j'execute info_livre puius csv_creation et les données s'ajoute dans le même fichier csv
def csv_datas_livresbycatego(liste):
    for i in range(len(liste)):
        occurence = (liste[i])
        catego = occurence[0]
        url_livre = occurence[1]
        global nom_csv
        nom_csv = 'catego' + '_' + catego + '.csv'
        # print('nom csv : ', nom_csv)
        # print('le lien est : ', url_livre)
        csv_creation(info_livre(url_livre), nom_csv)

#------------------- Lancement du programme -----------------------------#
# csv_datas_livresbycatego(geturlsslist.recup_urlallcatego(geturlsslist.recup_catego(url)))

#---------------------- Test unitaires ----------------------------------#

# execution de info_livre avec une url
# urlexo2 = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
# info_livre(urlexo2)
# print(datas_entetes)
# print(datas_content)

# execution de csv_creation avec un echantillon dans le fichier nommé fichier.csv
# datas_entetes = ('product_page_url', 'UPC,title', 'Price (incl. tax)')
# datas_content = ('https://books.toscrape.com/catalogue/sharp-objects_997/index.html', 'e00eb4fd7b871a48', 'Sharp Objects', '£47.82')
# csv_creation(datas_entetes , datas_content , nom_csv)

# execution de recup_urlallcatego depuis script.py
# print(geturlsslist.recup_urlallcatego(geturlsslist.recup_catego(url)))

# execution de csv_datas_livresbycatego
listetest = [['mystery_3', 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'],['travel_2', 'https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html']]
csv_datas_livresbycatego(listetest)
# les print sont à de-commenter dans la boucle dans la boucle
# print('nom csv : ', nom_csv)
# print('le lien est : ',url_livre)
