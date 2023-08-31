from bs4 import BeautifulSoup as bs
import requests

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
        return print(links_livre)

#execution des fonctions
links_catego = (recup_catego('https://books.toscrape.com/'))
urls_catego_livres(links_catego)


#print(links_catego)
