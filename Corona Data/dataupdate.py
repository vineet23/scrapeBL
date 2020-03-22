import requests
import json

url = "https://www.bing.com/covid/data"

response = requests.get(url)

resp = response.json()

with open("results2.json",'w') as f:
    json.dump(resp,f)

with open("results2.json",'r') as f:
    ditc = json.load(f)

data = []

areas = list(ditc['areas'])
for area in areas:
    totald = area['totalConfirmed']
    death = area['totalDeaths']
    rec = area['totalRecovered']
    active = int(totald)-int(death)-int(rec)
    name = area['displayName']
    lat = area['lat']
    lng = area['long']
    if totald<10:
        for i in range(totald):
            data.append({"latitude":lat,"longitude":lng,"place":name})
    else:    
        for i in range((totald%10)+2):
            data.append({"latitude":lat,"longitude":lng,"place":name})
    aras = list(area['areas'])
    for ar in aras:
        totald = ar['totalConfirmed']
        death = ar['totalDeaths']
        rec = ar['totalRecovered']
        active = int(totald)-int(death)-int(rec)
        name = ar['displayName']
        lat = ar['lat']
        lng = ar['long']
        if totald<10:
            for i in range(totald):
                data.append({"latitude":lat,"longitude":lng,"place":name})
        else:    
            for i in range((totald%10)+2):
                data.append({"latitude":lat,"longitude":lng,"place":name})
        region = list(ar['areas'])
        for rg in region:
            rtotald = rg['totalConfirmed']
            rdeath = rg['totalDeaths']
            rrec = rg['totalRecovered']
            ractive = int(totald)-int(death)-int(rec)
            rname = rg['displayName']
            rlat = rg['lat']
            rlng = rg['long']
            if rtotald<10:
                for i in range(rtotald):
                    data.append({"latitude":rlat,"longitude":rlng,"place":rname})
            else:    
                for i in range((rtotald%10)+2):
                    data.append({"latitude":rlat,"longitude":rlng,"place":rname})

url = "https://api.papersqueeze.com/corona/addlocation/"
headers = {"Authorization":"Token da0646e9548cb3fca6ac7e15ed2810a2fd53d2f5"}
dat = {"usertype":"admin","condition":"active","place":"","latitude":"","longitude":""}


#response = requests.post(url,headers=headers,data=data)
#print(response.json())
for row in data:
    dat['place'] = row["place"]
    dat['latitude'] = float(row["latitude"])
    dat['longitude'] = float(row["longitude"])
    response = requests.post(url,headers=headers,data=dat)
    print(response.json())