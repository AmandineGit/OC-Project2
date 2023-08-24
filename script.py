from bs4 import BeautifulSoup as bs
import requests
import csv23 as csv


url='https://books.toscrape.com/catalogue/olio_984/index.html'
# récupération du code réponse de la page et test / ok si code 200, sinon stop
response = requests.get(url)
if response.ok:

    #création de mon object soup
    soup = bs(response.text, 'lxml')

    #sélection des données voulues
    ths = soup.findAll('th')
    tds = soup.findAll('td')

    #extration des balises
    ths2 = []
    for th in ths :
        th2 = bs(th.text, 'lxml').text
        ths2.append(th2)
    tds2 = []
    for td in tds :
        td2 = bs(td.text, 'lxml').text
        tds2.append(td2)

   #création du csv
    with open('nombres.csv', 'w') as CSV1livre :
            writer = csv.writer(CSV1livre)
            headers = ths2
            writer.writerow(headers)
            data = tds2
            writer.writerow(data)
