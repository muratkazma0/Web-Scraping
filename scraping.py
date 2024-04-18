# Web Scraping - Video 15.12 ; 
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find("tbody", {"class": "lister-list"}).find_all("tr", limit=10)

for item in liste:
    film_adi = item.find("h3", {"class": "titleColumn"}).find("a").text
    film_puan = item.find("span", {"class": "ratingColumn"}).find("strong").text
    print(film_adi, film_puan)
