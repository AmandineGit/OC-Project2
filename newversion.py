from bs4 import BeautifulSoup as bs
import requests

# Variables globales
url = 'https://books.toscrape.com/'
nameLinks_catego = []


# Récupère les URLs des catégories et le nom de la catégories associées dans
def recup_catego(url):
    response = requests.get(url)
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
        #print(nameLinks_catego)
        print('urls des différentes catégories - Extraction : terminé')

#def recup_url_livre(list_urls):

recup_catego(url)
#recup_url_livre