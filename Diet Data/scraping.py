from bs4 import BeautifulSoup
import requests


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
            title_text = title.find("h3").text.replace('\n', "").replace("\u2019","'").strip()
            #get the sub category description
            desc = sub.find("p",{"class":"calorie-excerpt"})
            desc_text = desc.text.replace('\n', "").replace("\u2019","'").strip()
            #get the image link of the sub category
            image_div = sub.find("div",{"class":"calorie-img"})
            image_url = image_div.find("img")
            img = image_url['data-src']
            #add data of the sub category
            sb_obj["link"] = link_text
            sb_obj["image"] = img[:-10]+img[-4:]
            sb_obj["description"] = desc_text
            sb_obj["title"] = title_text
            sb_obj["data"] = scrape_sub(link_text)
            #add sub category to category
            sb.append(sb_obj)
        #add data of the category
        obj["data"] = sb
        #add name of the category
        obj["name"] = name
        l.append(obj)
    return l

def scrape_sub(url):
    s = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    #get the description in detail
    container = soup.find("div",{"class":"entry-content"})
    #get the description detail div
    desc = container.find("div",{"id":"calories-desc-before-wrapper"})
    #get the text and replace all the required things
    desc_text = desc.text.replace('\n',"").replace("\u2019","'").strip()

    table = container.find("table",{"id":"calories-table"})
    tablebody = table.find('tbody')
    table_data = tablebody.find_all("tr",{"class":"kt-row"})

    for data in table_data:
        sb={}
        nametd = data.find('td',{"class":"food"})
        name = nametd.a.text.replace('\n',"").replace("\u2019","'").strip()
        serving100td = data.find('td',{"class":"serving 100g"})
        serving100 = serving100td.text.replace('\n',"").strip()
        servingportiontd = data.find('td',{"class":"serving portion"})
        servingportion = servingportiontd.text.replace('\n',"").replace('\u00a0'," ").strip()
        servingoztd = data.find('td',{"class":"serving oz"})
        servingoz = servingoztd.text.replace('\n',"").replace('\u00a0'," ").strip()
        kcaltd = data.find('td',{"class":"kcal"})
        kcal = kcaltd.text.replace('\n',"").strip()
        kjtd = data.find('td',{"class":"kj"})
        kj = kjtd.text.replace('\n',"").strip()
        sb['name'] = name
        sb['serving_100'] = serving100
        sb['serving_portion'] = servingportion
        sb['serving_oz'] = servingoz
        sb['kcal'] = kcal
        sb['kj'] = kj
        s.append(sb)
    return ({"detail":desc_text,"list":s})