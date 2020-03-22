import requests
import json

url = "https://www.bing.com/covid/data"

response = requests.get(url)

resp = response.json()

with open("results2.json",'w') as f:
    json.dump(resp,f)

with open("results2.json",'r') as f:
    ditc = json.load(f)

total = int(ditc['totalConfirmed'])
deaths = int(ditc['totalDeaths'])
recov = int(ditc['totalRecovered'])
active = total - deaths - recov
print(str(total)+" "+str(deaths)+" "+str(recov)+" "+str(active)+"\n")
areas = list(ditc['areas'])
for area in areas:
    totald = area['totalConfirmed']
    death = area['totalDeaths']
    rec = area['totalRecovered']
    active = int(totald)-int(death)-int(rec)
    name = area['displayName']
    lat = area['lat']
    lng = area['long']
    print(name+" "+str(lat)+" "+str(lng)+" "+str(totald)+" "+str(death)+" "+str(rec)+" "+str(active)+" \n")
    aras = list(area['areas'])
    for ar in aras:
        totald = ar['totalConfirmed']
        death = ar['totalDeaths']
        rec = ar['totalRecovered']
        active = int(totald)-int(death)-int(rec)
        name = ar['displayName']
        lat = ar['lat']
        lng = ar['long']
        print(name+" "+str(lat)+" "+str(lng)+" "+str(totald)+" "+str(death)+" "+str(rec)+" "+str(active)+" \n")
        region = list(ar['areas'])
        for rg in region:
            rtotald = rg['totalConfirmed']
            rdeath = rg['totalDeaths']
            rrec = rg['totalRecovered']
            ractive = int(totald)-int(death)-int(rec)
            rname = rg['displayName']
            rlat = rg['lat']
            rlng = rg['long']
            print(rname+" "+str(rlat)+" "+str(rlng)+" "+str(rtotald)+" "+str(rdeath)+" "+str(rrec)+" "+str(ractive)+" \n")
    