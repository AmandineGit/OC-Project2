import os.path

from bs4 import BeautifulSoup as bs
import requests
import csv23 as csv

#Variables globales
datas_entetes = []
datas_content = []
urlexo2 = 'https://books.toscrape.com/catalogue/private-paris-private-10_958/index.html'
#input('Veuillez renseigner l URL du livre recherché : '))
nom_csv = 'fichier.csv'
list_urls_catego_livres = []
links_catego = []
url = 'https://books.toscrape.com/'


# definition de la fonction recup_catego qui récupère les URLs des catégories
def recup_catego(url):
    response = requests.get(url)
    # connection à la page contenant les données & récupération du code réponse de la page du produit et test / ok si code 200, sinon stop
    if response.ok:
        # création de mon object soup
        soup = bs(response.content, 'lxml')
        # récupération des datas sous la balise a
        masoupdea = soup.findAll('a')
        # extraction de la partie href et ajout dans la liste links_catego sous forme de liste en position [1]et le nom de la catégorie en [0]
        global links_catego
        for a in masoupdea:
            link_catego = a['href']
            name_catego = a.text
            name_catego = name_catego.lstrip("\n")
            name_catego = name_catego.strip()
            name_catego = name_catego.rstrip('\n')
            links_catego.append([name_catego, 'https://books.toscrape.com/' + link_catego])
        # suppression des données inutiles
        del (links_catego[0:3])
        del (links_catego[50:])
        list(links_catego)


# definition de la fonction urls_catego_livres qui récupère les URLs des livres et leur catégorie
def urls_catego_livres(links_catego):
    for i in range(len(links_catego)):
        link_catego = links_catego[i]
        link = link_catego[1]
        catego_link = link_catego[0]
        # connection à la page contenant les données & récupération du code réponse de la page du produit et test / ok si code 200, sinon stop
        response = requests.get(link)
        if response.ok:
            # création de mon object soup
            soup = bs(response.content, 'lxml')
            # récupération des datas sous la balise h3
            masoupdeh3 = soup.findAll('h3')
            #print(masoupdeh3)
# extraction de la partie a, puis href et ajout de la catégorie
            global list_urls_catego_livres
            for links_catego[i] in masoupdeh3:
                links_catego[i] = links_catego[i].find('a')
                links_catego[i] = links_catego[i]['href']
                # construction de l'url fonctionnelle
                link_livre_lst = list(links_catego[i])
                del (link_livre_lst[:8])
                links_catego[i] = ''.join(link_livre_lst)
                # ajout dans la liste list_urls_catego_livres de l'url des livres et de leur catégorie
                list_urls_catego_livres.append((catego_link,('https://books.toscrape.com/catalogue' + links_catego[i])))
    print(list_urls_catego_livres)


#definition de la fonction info_livre qui récupère les infos d'un livre dont l'url est rnseignée en paramètre
def info_livre(urlexo2) :
    #connection à la page contenant les données & récupération du code réponse de la page du produit et test / ok si code 200, sinon stop
    response = requests.get(urlexo2)
    if response.ok:

        #création de mon object soup
        soup = bs(response.content, 'lxml')

        #sélection des données voulues
        ths = soup.findAll('th')
        tds = soup.findAll('td')

        #extration des balises et création des objects de données
        global entetes
        entetes = []
        for th in ths :
            th2 = bs(th.text, 'lxml').text
            entetes.append(th2)
        datas = []
        for td in tds :
            td2 = bs(td.text, 'lxml').text
            datas.append(td2)
        #intégration de l'URL et de son entête dans la liste
        entetes.insert(0,'product_page_url')
        datas.insert(0,urlexo2)

        #récupération du title
        h1= soup.find('h1')

        #remplacement de Product_type par title
        entetes[2]='title'
        h1b = bs(h1.text, 'lxml').text
        datas[2]=h1b


        #récupération de Product_description, passage en string et suppression des balises
        ProdDesc = soup.findAll('p')
        ProdDesc = ProdDesc[3]
        ProdDesc = str(ProdDesc)
        ProdDesc = ProdDesc[3:-4]
        #print (ProdDesc)

        #Récupération de category
        catego = soup.findAll('li')
        catego = catego[2]
        catego = catego.find('a')
        catego = catego.text
        #print(catego)

        #récupération de review_rating
        rev_rat = soup.findAll('p')
        rev_rat = rev_rat[2].attrs
        rev_rat = rev_rat["class"]
        rev_rat = rev_rat[1]
        #print(rev_rat)

        #recupération de l'url de l'image
        img = soup.img['src']
        link_img = 'https://books.toscrape.com/' + img[6:]
        #print(link_img)

        #Rassemblement des données et mise en forme
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
        datas.insert(8, rev_rat )

        entetes.insert(9, 'image_url')
        datas.insert(9, link_img )
        global datas_entetes
        global datas_content
        datas_entetes = entetes
        datas_content = datas

# fonction de création d'un csv à partir des données retournées par info_livre(urlexo2)
def csv_creation(datas_entetesetdatas_content , nom_csv):
        if os.path.exists(nom_csv) :
            with open(nom_csv, 'a') as CSV1livre:
                writer = csv.writer(CSV1livre)
                data = datas_content
                writer.writerow(data)
                CSV1livre.close()
        else :
            with open(nom_csv, 'w') as CSV1livre:
                writer = csv.writer(CSV1livre)
                headers = datas_entetes
                writer.writerow(headers)
                data = datas_content
                writer.writerow(data)
                CSV1livre.close()
''' Test avec liste d'urls réduide
liste =[]
liste.append(('Crime1', 'https://books.toscrape.com/catalogue/the-long-shadow-of-small-ghosts-murder-and-memory-in-an-american-city_848/index.html'))
liste.append(('Travel1', 'https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html'))
list_urls_catego_livres = liste'''

#pour chaque url de links_catego_livres j'execute info_livre puius csv_creation et les données s'ajoute dans le même fichier csv
def csv_datas_livresbycatego(liste):
    for i in range(len(liste)) :
        occurence = (liste[i])
        catego = occurence[0]
        url_livre = occurence[1]
        global nom_csv
        nom_csv = 'catego' + '_'+ catego +'.csv'
        csv_creation(info_livre(url_livre), nom_csv)



#execution des fonctions - test unitaires
#info_livre(urlexo2)
#print(urlexo2)
#csv_creation(datas_entetes , datas_content , nom_csv)
recup_catego(url)
urls_catego_livres(links_catego)
csv_datas_livresbycatego(list_urls_catego_livres)

