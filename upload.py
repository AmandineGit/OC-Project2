import os
from bs4 import BeautifulSoup as bs
import requests
import re

# Variables globales
datas_content = []
datas_entete = ['product_page_url', 'UPC', 'title', 'Price (incl. tax)', 'Price (excl. tax)', 'Availability,product_description', 'category', 'review_rating', 'image_url']


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
        catego = catego.replace(' ', '_')
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


# Télécharge une image à partir du fichier csv et la place dans le répertoire de la catégorie
def upload_jpg(datas):
    url_jpg = datas[-1]
    upc = datas[1]
    title = datas[2]
    title = title.replace(' ','_')
    title = re.sub(r'\W+', '', title)
    category = datas[-3]
    path = os.getcwd()
    if not os.path.isdir(path + '/' + category + '/images-catego-' + category):
        os.mkdir(path + '/' + category + '/images-catego-' + category)
        print('Le répertoire ' + 'images-catego-' + category + 'a été crée.')
    nom_jpg = path + '/' + category + '/images-catego-' + category + '/' + upc + '_' + title + '.jpg'
    response = requests.get(url_jpg)
    open(nom_jpg, 'wb').write(response.content)
    print('le fichier image du livre : ', title + ' a été enregistré.')


# ---------------------- Test unitaires ----------------------------------#
# -------------execution de info_livre avec une url
# Variables globales de tests
# nom_csv = 'catego_TestUpload.csv'
# urlexo2 = 'https://books.toscrape.com/catalogue/the-constant-princess-the-tudor-court-1_493/index.html'

# print(upload_jpg(info_livre(urlexo2)))
# print(datas_entete)
# print(datas_content)
