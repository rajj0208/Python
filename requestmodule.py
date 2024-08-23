import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/2024_Tour_de_France_Femmes"
r = requests.get(url)
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)
