import requests
import bs4
from bs4 import BeautifulSoup

source = requests.get('https://www.awfarlak.com/ar/c/graphic-cards')
soup = bs4.BeautifulSoup(source.content, 'html.parser')

products = soup.find_all('h3', {'class': 'wd-entities-title'})
prices = soup.find_all('span', {'class': 'price'})

pr_list = []
prices_list = []

for i in range(len(products)):
    pr_list.append(products[i].text)
    prices_list.append(prices[i].text)

for i in range(len(pr_list)):
    print(pr_list[i], '----->>>', prices_list[i])