from bs4 import BeautifulSoup as bs
import requests

#def bs_parse(html):
#    return bs(html, 'lxml')

url='https://books.toscrape.com/'
page = requests.get(url).text

soup=bs(page,'lxml')
print(soup.get_text())