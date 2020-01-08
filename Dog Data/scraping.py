from bs4 import BeautifulSoup
import requests
import pandas as pd
import cv2
import numpy as np
import urllib.request

l = []


def scrape():

    url = 'https://dogtime.com/dog-breeds/profiles'

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
        
    list_product = soup.find_all('div',class_="list-item")
     
    for product in list_product:

        obj = { }
        product_animal = product.find("a", {"class":"list-item-title"})
        product_image = product.find("img",{"class":"list-item-breed-img"})
        product_img = product_image['src']
        obj['name'] = product_animal.text.replace('\n', "").strip()
        obj['image'] = product_img
        l.append(obj)

    my_db = pd.DataFrame(l)
    my_db.to_csv('dog.csv',index=False,header=False)

    print(len(l))
    return l

def imageDownload():
    # opener = urllib.request.build_opener()
    # opener.addheaders = [{'User-Agent' : 'Mozilla'}]
    # urllib.request.install_opener(opener)
    # for dog in l:
    #     urllib.request.urlretrieve(dog['image'], dog['name']+".jpg")
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    for img in l:
        try:
            url = img['image']
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            binary_str = response.read()
            byte_array = bytearray(binary_str)
            numpy_array = np.asarray(byte_array,dtype="uint8")
            image = cv2.imdecode(numpy_array,cv2.IMREAD_UNCHANGED)
            cv2.imwrite('images/'+ img['name'] + '.jpg',image)
        except Exception as ex :
            print(str(ex))
            return
        

if __name__ == "__main__":
    print(scrape())





