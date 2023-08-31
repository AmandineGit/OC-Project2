from bs4 import BeautifulSoup as bs
import requests

url = 'https://books.toscrape.com/'

response = requests.get(url)
#connection à la page contenant les données & récupération du code réponse de la page du produit et test / ok si code 200, sinon stop
if response.ok:
    # création de mon object soup
    soup = bs(response.text, 'lxml')
    # récupération des datas sous la balise a
    masoupdea = soup.findAll('a')
    # extraction de la partie text et ajout dans la liste link_catego
    links_catego = []
    for a in masoupdea :
        link_catego = a['href']
        links_catego.append('https://books.toscrape.com/' + link_catego)

    print(links_catego)