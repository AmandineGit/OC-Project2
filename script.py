from bs4 import BeautifulSoup as bs
import requests
import csv23 as csv

#definition de la fonction recup_catego
def recup_catego(url) :
    response = requests.get(url)
    # connection à la page contenant les données & récupération du code réponse de la page du produit et test / ok si code 200, sinon stop
    if response.ok:
        # création de mon object soup
        soup = bs(response.text, 'lxml')
        # récupération des datas sous la balise a
        masoupdea = soup.findAll('a')
        # extraction de la partie href et ajout dans la liste link_catego
        links_catego = []
        for a in masoupdea :
            link_catego = a['href']
            links_catego.append('https://books.toscrape.com/' + link_catego)
        #suppression des données inutiles
        del(links_catego[0:3])
        del (links_catego[50:])
        list(links_catego)
        return links_catego

def urls_catego_livres(urls_catego):
    for link_catego in links_catego :
        # connection à la page contenant les données & récupération du code réponse de la page du produit et test / ok si code 200, sinon stop
        response = requests.get(link_catego)
        if response.ok:
            # création de mon object soup
            soup = bs(response.text, 'lxml')
            # récupération des datas sous la balise h3
            masoupdeh3 = soup.findAll('h3')
            # extraction de la partie a, puis href
            links_livre = []
            for link_livre in masoupdeh3:
                link_livre = link_livre.find('a')
                link_livre = link_livre['href']
                #construction de l'url fonctionnelle
                link_livre_lst = list(link_livre)
                del(link_livre_lst[:8])
                link_livre = ''.join(link_livre_lst)

                #ajout dans la liste links_livre
                links_livre.append('https://books.toscrape.com/catalogue' + link_livre)
        return links_livre

urlexo2 = ('https://books.toscrape.com/catalogue/private-paris-private-10_958/index.html')
#input('Veuillez renseigner l URL du livre recherché : '))


#definition de la fonction info_livre qui récupère les infos d'un livre dont l'url est rnseignée en paramètre
def info_livre(urlexo2) :
    #connection à la page contenant les données & récupération du code réponse de la page du produit et test / ok si code 200, sinon stop
    response = requests.get(urlexo2)
    if response.ok:

        #création de mon object soup
        soup = bs(response.text, 'lxml')

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
        str(entetes)
        str(datas)
        datasetentetes = entetes + datas
        return datasetentetes

# fonction de création d'un csv à partir des données retournées par info_livre(urlexo2)
def csv_creation(datasetentetes):
    with open(nom_csv, 'w') as CSV1livre:
        datas = info_livre(urlexo2)
        datas_entetes = datas[0:10]
        datas_livre = datas[10:21]
        writer = csv.writer(CSV1livre)
        headers = datas_entetes
        writer.writerow(headers)
        data = datas_livre
        writer.writerow(data)

#execution des fonctions
links_catego = (recup_catego('https://books.toscrape.com/'))
list_urls_catego_livres = []
list_urls_catego_livres = urls_catego_livres(links_catego)
print(list_urls_catego_livres)
#pour chaque url de links_catego_livres j'execute csv_creation, mais il faut voir pour ajouter et non créer à chaque fois
nom_csv = 'livre'
for url_livre in list_urls_catego_livres :
    nom_csv = nom_csv
    csv_creation(info_livre(url_livre))


#csv_creation(info_livre(urlexo2))
