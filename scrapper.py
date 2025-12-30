import requests
from bs4 import BeautifulSoup

def fetch_quote():
    res = requests.get("https://quotes.toscrape.com/")
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.find("span", class_="text").text
