from bs4 import BeautifulSoup as bs
import requests

url='https://books.toscrape.com/catalogue/olio_984/index.html'

response = requests.get(url)

if response.ok:
    UPCs = []
    soup = bs(response.text, 'lxml')
    tds = soup.findAll('td')

    '''for h3 in h3s :
        a = h3.find('a')
        link = a['href']
        links.append('https://books.toscrape.com/' + link)
        '''
    print(tds)



