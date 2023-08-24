from bs4 import BeautifulSoup as bs
import requests

url='https://books.toscrape.com'

response = requests.get(url)

if response.ok:
    links = []
    soup = bs(response.text, 'lxml')
    h3s = soup.findAll('h3')
    for h3 in h3s :
        a = h3.find('a')
        link = a['href']
        links.append('https://books.toscrape.com/' + link)
    print(links)



