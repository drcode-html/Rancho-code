import requests
from bs4 import BeautifulSoup
url = "https://pokemondb.net/pokedex/all"
page = requests.get(url)
soup = BeautifulSoup(page.text , "html.parser")
print(soup.title.text)