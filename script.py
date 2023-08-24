from bs4 import BeautifulSoup as bs
import requests
import csv23 as csv


url='https://books.toscrape.com'
# récupération du code réponse de la page index.html et test / ok si code 200, sinon stop
response = requests.get(url)
if response.ok:
#recup des urls dans links
    links = []
    soup = bs(response.text, 'lxml')
    h3s = soup.findAll('h3')
    for h3 in h3s:
        a = h3.find('a')
        link = a['href']
        links.append('https://books.toscrape.com/' + link)

    #Récupérer l'URL d'un livre
    urlexo1 = links[0]

    #connection à la page contenant les données & récupération du code réponse de la page du produit et test / ok si code 200, sinon stop
    response = requests.get(urlexo1)
    if response.ok:
    
        #création de mon object soup
        soup = bs(response.text, 'lxml')
    
        #sélection des données voulues
        ths = soup.findAll('th')
        tds = soup.findAll('td')
    
        #extration des balises et création des objects de données
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
        datas.insert(0,urlexo1)
        #récupération du title
        h1= soup.find('h1')
        #remplacement de Product_type par title
        entetes[2]='title'
        h1b = bs(h1.text, 'lxml').text
        datas[2]=h1b
        print(entetes)
        print(datas)


       #création du csv
'''       with open('nombres.csv', 'w') as CSV1livre :
                writer = csv.writer(CSV1livre)
                headers = entetes
                writer.writerow(headers)
                data = datas
                writer.writerow(data)
    
'''