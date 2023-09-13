from bs4 import BeautifulSoup as bs
import requests

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

# ---------------------- Test unitaires ----------------------------------#
# execution de info_livre avec une url
# urlexo2 = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
# print(info_livre(urlexo2))
# print(datas_entete)
# print(datas_content)