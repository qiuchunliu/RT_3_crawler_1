# created for notes

import requests
from bs4 import BeautifulSoup

url = 'string of link'
res = requests.get(url)
res.encoding = 'utf-8'
rest = res.text

resoup = BeautifulSoup(rest, 'html.parser')
# we can do what we want 
