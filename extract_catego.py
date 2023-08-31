from bs4 import BeautifulSoup as bs
import requests

url = 'https://books.toscrape.com/'

response = requests.get(url)
#connection à la page contenant les données & récupération du code réponse de la page du produit et test / ok si code 200, sinon stop
if response.ok:
    # création de mon object soup
    soup = bs(response.text, 'lxml')

    #definition de la fonction recup_catego
    def recup_catego(url) :
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
        return links_catego


print(recup_catego('url'))