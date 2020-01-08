from bs4 import BeautifulSoup
import requests
import io

response = requests.get("https://www.calories.info/food/pizza")
soup = BeautifulSoup(response.text,"lxml")
with io.open("lxml.txt", "w", encoding="utf-8") as f:
    f.write(soup.prettify())
print("done")