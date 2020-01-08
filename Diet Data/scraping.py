from bs4 import BeautifulSoup
import requests
import pandas as pd

l = []


def scrape():

    url = 'https://www.calories.info/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    #get the list of categories  
    list_calorieGroup = soup.find_all('div',class_="calorie-group")
    #for each category
    for category in list_calorieGroup:

        obj = { }
        #get the category name
        caloriegrp_name = category.find("h2", {"class":"calorie-group-name"})
        name = caloriegrp_name.text.replace('\n', "").strip()
        #get all the sub categories
        caloriegrp_sub = category.find_all("div",{"class":"col-sm-6"})
        sb = []
        for sub in caloriegrp_sub:
            sb_obj = {}
            #get the sub category link
            link = sub.find("a",{"class":"calorie-link"})
            link_text = link['href']
            #get the sub category title
            title = sub.find("div",{"class":"calorie-text"})
            title_text = title.find("h3").text.replace('\n', "").strip()
            #get the sub category description
            desc = sub.find("p",{"class":"calorie-excerpt"})
            desc_text = desc.text.replace('\n', "").strip()
            #get the image link of the sub category
            image_div = sub.find("div",{"class":"calorie-img"})
            image_url = image_div.find("img")
            img = image_url['data-src']
            #add data of the sub category
            sb_obj["link"] = link_text
            sb_obj["image"] = img[:-10]+img[-4:]
            sb_obj["description"] = desc_text
            sb_obj["title"] = title_text
            #add sub category to category
            sb.append(sb_obj)
        #add data of the category
        obj["data"] = sb
        #add name of the category
        obj["name"] = name
        l.append(obj)
    return l