from bs4 import BeautifulSoup as bs
import requests
import csv

url='https://books.toscrape.com/catalogue/olio_984/index.html'
# récupération du code réponse de la page et test / ok si code 200, sinon stop
response = requests.get(url)

if response.ok:
    #création de mon object soup
    soup = bs(response.text, 'lxml')
    #sélection des données voulues
    ths = soup.findAll('th')
    tds = soup.findAll('td')
    #création d'une liste contenant les entêtes et les données
    infos = []
    infos.append(ths)
    infos.append(tds)

   #création du csv
    with open('nombres.csv', 'w') as CSV1livre :
        writer = csv.writer(CSV1livre)

'''for h3 in h3s :
        a = h3.find('a')
        link = a['href']
        links.append('https://books.toscrape.com/' + link)
        '''
