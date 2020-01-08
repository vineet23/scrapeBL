from bs4 import BeautifulSoup
import requests

def scrape():
    l = []
    url = 'https://www.olx.in/cars_c84'

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    list_product = soup.find_all("li",class_="EIR5N")

    for product in list_product:

        obj = { }
        product_name = product.find("span",{"class":"_2tW1I"})
        product_detail = product.find("span",{"class":"_2TVI3"})
        product_price = product.find("span",{"class":"_89yzn"})
        obj['name'] = product_name.text.replace('\n',"").strip()
        obj['detail'] = product_detail.text.replace('\n',"").strip()
        obj['price'] = product_price.text.replace('\n',"").replace('\u20b9 ',"₹ ").strip()

        l.append(obj)

    return l


if __name__ == "__main__":
    print(scrape())



