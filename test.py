import os.path

from bs4 import BeautifulSoup as bs
import requests
import csv23 as csv

# Variables globales
datas_entetes = []
datas_content = []
urlexo2 = 'https://books.toscrape.com/catalogue/private-paris-private-10_958/index.html'
# input('Veuillez renseigner l URL du livre recherché : '))
nom_csv = 'fichier.csv'
list_urls_catego_livres = []
links_catego = []
url = 'https://books.toscrape.com/'
catego_link = []
link = 'a'
page_suiv = ''
next =''
link2 = ''



# definition de la fonction recup_catego qui récupère les URLs des catégories
def recup_catego(url):
    response = requests.get(url)
    # connection à la page contenant les données & récupération du code réponse et test / ok si code 200, sinon stop
    if response.ok:
        # création de mon object soup
        soup = bs(response.content, 'lxml')
        # récupération des datas sous la balise a
        masoupdea = soup.findAll('a')
        # extraction de la partie href
        # ajout dans la liste links_catego sous forme de liste en position [1]et le nom de la catégorie en [0]
        global links_catego
        i=-2
        for a in masoupdea:
            i=i+1
            istr = str(i)
            link_catego = a['href']
            name_catego = a.text
            name_catego = name_catego.lstrip("\n")
            name_catego = name_catego.strip()
            name_catego = name_catego.rstrip('\n')
            name_catego = name_catego+'_'+istr
            links_catego.append([name_catego, 'https://books.toscrape.com/' + link_catego])
        # suppression des données inutiles
        del (links_catego[0:3])
        del (links_catego[50:])
        list(links_catego)
        # print(links_catego)
        print('urls des différentes catégories - Extraction : terminé')


# definition de la fonction qui récupère les URLs des livres et leur catégorie avec recup_urls_livresbypage
def urls_catego_livres(links_catego):
# iteration sur les catégories et recup des urls des livres de la page index creation de link et catego_link
    for i in range(len(links_catego)):
        link_catego = links_catego[i]
        global link
        link = link_catego[1]
        global catego_link
        catego_link = link_catego[0]
    # connection à la page catégorie index & récupération de list_urls_catego_livres
        recup_urls_livresbypage(link, catego_link)
        next=search_next(link)
        print('1er test, next : ', next)
        print('1er test, link : ', link)
        print('1er test, link2 : ', link2)

    # si next = next alors recup des urls de livres de la page et retourne next et l'url suivante dans link
        while next =='next':
            # cherche un bouton next et prepare l'url de la page 2
            recup_urls_livresbypage(link2,catego_link)
            print('Page ',link2,' ajoutée, la liste fait maitenant : ',len(list_urls_catego_livres),' caractère(s)')
            next = search_next(link2)
            print('2nd test next = ',next)
            print('2nd test link = ',link2)


        else :
            print('La liste ',catego_link,' fait maintenant : ',(len(list_urls_catego_livres)),' caractères(s)')

def search_next(page):
    response = requests.get(page)
    soup = bs(response.content, 'lxml')
    masoupdeli = soup.findAll('li')
    soup2 = bs(response.content, 'lxml')
    masoupdeli2 = soup.findAll('li')
    li = masoupdeli[-1]
    li=li.text
    if li ==('next'):
        global next
        global link2
        next = li
        li2 = masoupdeli2[-1]
        link2 = li2.a
        link2 = link2['href']
        global catego_link
        catego_link = catego_link.replace(" ", "")
        link2 = 'https://books.toscrape.com/' + 'catalogue/category/books/' + catego_link.lower() + "/" + link2
        return(next)


# création de mon object soup pour récupérer les urls des livres d'une page de catégorie
def recup_urls_livresbypage(link, catego_link):
    response = requests.get(link)
    print(link)
    soup = bs(response.content, 'lxml')
    # récupération des datas sous la balise h3
    masoupdeh3 = soup.findAll('h3')
    # extraction de la partie a, puis href et ajout de la catégorie
    global list_urls_catego_livres
    for link_catego in masoupdeh3:
        link_catego = link_catego.find('a')
        link_catego = link_catego['href']
        # construction de l'url fonctionnelle
        link_livre_lst = list(link_catego)
        del (link_livre_lst[:8])
        link_catego = ''.join(link_livre_lst)
        # ajout dans la liste list_urls_catego_livres de l'url des livres et de leur catégorie
        list_urls_catego_livres.append((catego_link, ['https://books.toscrape.com/catalogue' + link_catego]))


#catego_link = 'sequential-art_5'
recup_catego(url)
urls_catego_livres(links_catego)
#link2,next=search_next('https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html')

