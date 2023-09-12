from bs4 import BeautifulSoup as bs
import requests
import csv23 as csv
import os.path


# Variables globales
nameLinks_catego = []
nameLinks_allpages = []
namelinks_allbooks = []
# Variable pour test unitaire
url = 'https://books.toscrape.com/'
listetest = [['mystery_3', 'https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html'], ['travel_2', 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html']]


# Récupère les URLs des catégories et le nom de la catégories associées dans nameLinks_catego
def recup_catego(urlsite):
    response = requests.get(urlsite)
    # test / ok si code 200, sinon stop
    if response.ok:
        # création de mon object soup
        soup = bs(response.content, 'lxml')
        # récupération des datas sous la balise a
        masoupdea = soup.findAll('a')
        # extraction de la partie href et ajout dans la liste nameLinks_catego sous forme de liste
        # avec le lien de la catégorie en position [1]et le nom de la catégorie en [0]
        global nameLinks_catego
        # la variable i va ajouter le numéro de la catégorie afin qu'il puisse etre utilisé pour créer d'autres urls
        i = -2
        for a in masoupdea:
            i = i + 1
            istr = str(i)
            link_catego = a['href']
            name_catego = a.text
            name_catego = name_catego.lstrip("\n")
            name_catego = name_catego.strip()
            name_catego = name_catego.rstrip('\n')
            name_catego = name_catego+'_'+istr
            nameLinks_catego.append([name_catego, 'https://books.toscrape.com/' + link_catego])
        # suppression des données inutiles
        del (nameLinks_catego[0:3])
        del (nameLinks_catego[50:])
        list(nameLinks_catego)
# Test unitaire de la fontion retirer le # pour executer le print
        # print(nameLinks_catego)
        # print(nameLinks_catego[0], nameLinks_catego[-1])
        print('1. Les urls des différentes catégories ont été extraites')
        return nameLinks_catego


# génére les urls des 4 pages suivantes à partir de nameLinks_catego et renvoi nameLinks_allcatego
def recup_urlallpages(list_urls):
    global nameLinks_allpages
    for i in range(50):
        p = 1
        namelink = list_urls[i]
        link = (namelink[1])[:-10]
        name = (namelink[0])
        # le IF charge les indexs et traite la première page
        if i == 0:

            nameLinks_allpages = list_urls
            print('2. La liste_urls index est chargée')

        p = p + 1
        nextlink = link + 'page-' + str(p) + '.html'
        nameLinks_allpages.append([name, nextlink])
        # print('Liste ', name , 'complétée avec : ' , 'la page' , p , nextlink)
        while p <= 7:
            p = p + 1
            nextlink2 = link + 'page-' + str(p) + '.html'
            nameLinks_allpages.append([name, nextlink2])
            # print('Liste ', name , 'complétée avec : ' , 'la page' , p , nextlink2)
        # print('La liste comporte maintenant :', len(nameLinks_allcatego),'URL(s)')

    print('3. La liste commence par :', nameLinks_allpages[0], '\n', 'et se termine par :', nameLinks_allpages[-1])
    print('4. La liste comporte maintenant :', len(nameLinks_allpages), 'URL(s) de pages')
    return nameLinks_allpages


# definition de la fonction urls_catego_livres qui récupère les URLs des livres et leur catégorie pour chaque page
def urls_catego_livres(links_catego):
    global namelinks_allbooks
    exist = 'y'
    categooflink = 'Travel_2'
    categooflinkPrec = ''
    for i in range(len(links_catego)):
        link_catego = links_catego[i]
        link = link_catego[1]
        categooflink = link_catego[0]
        if exist == 'y' or categooflink != categooflinkPrec:
            # connection à la page contenant les données & récupération du code réponse de la page du produit et test
            response = requests.get(link)
            if response.ok:
                # création de mon object soup
                soup = bs(response.content, 'lxml')
                # récupération des datas sous la balise h3
                masoupdeh3 = soup.findAll('h3')
                exist = 'y'
    # extraction de la partie a, puis href et ajout de la catégorie

                for links_catego[i] in masoupdeh3:
                    links_catego[i] = links_catego[i].find('a')
                    links_catego[i] = links_catego[i]['href']
                    # construction de l'url fonctionnelle
                    link_livre_lst = list(links_catego[i])
                    del (link_livre_lst[:8])
                    links_catego[i] = ''.join(link_livre_lst)
                    # ajout dans la liste namelinks_allbooks de l'url des livres et de leur catégorie
                    namelinks_allbooks.append([categooflink, ('https://books.toscrape.com/catalogue' + links_catego[i])])
                    print('Il y a maintenant ',len(namelinks_allbooks) , ' URLs de books dans la liste')
            else:
                print('XXX La page : ', link, 'n existe pas.')
                exist = 'n'
                categooflinkPrec = categooflink
    print('4. La liste comporte maintenant les url(s) de :', len(namelinks_allbooks), 'book(s)')
    return namelinks_allbooks


# fontion permettant d'envoyer nameLinks_allcatego ou namelinks_allbooks dans un csv pour controle
def csv_creation(datas, nom_csv):
    # fonction de création d'un csv à partir des données retournées par info_livre(urlexo2)
    # Test si le fichier existe déjà rien ne sera fait
    if os.path.exists(nom_csv):
        print('Le fichier CSV n a pas été crée car il existe déjà un fichier du meme nom dans le répertoire')
    else:
        with open(nom_csv, 'w') as CSV1livre:
            writer = csv.writer(CSV1livre)
            data = datas
            writer.writerow(data)
            CSV1livre.close()
        print('5. Un fichier csv a été créé dans le répertoire courant, il se nomme : ', nom_csv)


# ------------------- Lancement du programme -----------------------------#
if os.path.exists('nameLinks_allpages.csv'):
    print('Le fichier nameLinks_allpages.csv existe déjà, veuillez le supprimer ou le renommer avant de relancer')
    exit()
else:
    csv_creation(urls_catego_livres(recup_urlallpages(recup_catego(url))), 'nameLinks_allpages.csv')


# ---------------------- Test unitaires ----------------------------------#
# recup_catego(url)
# recup_urlallpages(recup_catego(url))
# urls_catego_livres(recup_urlallpages(recup_catego(url)), 'nameLinks_allpages.csv'))
# csv_creation(urls_catego_livres(listetest),'nameLinks_allpages.csv')

# ---------------------- Test fichier avec echantillon de données ----------------------------------#
# csv_creation(urls_catego_livres(listetest), 'nameLinks_allpages.csv')
