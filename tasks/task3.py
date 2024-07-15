import requests
from bs4 import BeautifulSoup

try:
    base_url = "https://quotes.toscrape.com/"
    response = requests.get(base_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content,'html.parser')
except requests.exceptions.RequestException as e:
    print(f"error fetching results , {e}")

quotes = soup.find_all('div',class_="quote")
for quote in quotes :
    author = quote.find('small',class_="author")
    Qtext = quote.find("span",class_="text")
    print(f"\n{Qtext.text.strip()}",end="\nby ")
    print(author.text.strip(),end="\n\n"+"-"*30)