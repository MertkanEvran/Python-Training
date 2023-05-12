import requests
from bs4 import BeautifulSoup
import json

# Request to web-site
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
movie_list = soup.find("tbody",{"class":"lister-list"}).find_all("tr")

movies_dict = {}

id = 1
for movie in movie_list:
    title = movie.find("td",{"class":"titleColumn"}).find("a").text
    year = movie.find("td",{"class":"titleColumn"}).find("span").text
    rating = movie.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    movies_dict[id] = {"name:":title,"year":year,"rating":rating}
    id +=1

with open("movie_list.json","w",encoding="utf-8") as movie_database:
    json.dump(movies_dict, movie_database, ensure_ascii=False, indent=4)


