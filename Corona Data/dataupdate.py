import requests
import json

url = "https://www.bing.com/covid/data?ig=FCD0C7C0703D46D39DAC70FFC094FC66"

headers = {"Accept-Language": "en,en;q=0.8","Authorization":"Basic ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBaeUk2SWtaRFJEQkROME13TnpBelJEUTJSRE01UkVGRE56QkdSa013T1RSR1F6WTJJaXdpYzJsa0lqb2lNakE1UkRWRVJqVkRNRVZFTmtWR016RXlNREExTXpVelF6RTBNVFpHUWtRaUxDSnBZWFFpT2pFMU9EWXpNVFEyTkRBc0ltVjRjQ0k2TVRVNE5qUXdNVEEwTUgwLjVzVGlEQ0I4N2g3UnpuSWU0R09KbldCOTlPdG1JU2hvQlVGbHhVQ0M2SDg=","cookie":"MUID=2C3E26285200620A3B2B2D5E56006120; MUIDB=2C3E26285200620A3B2B2D5E56006120; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=BBBEAA367EC045AEAF87F07EC943EE19&dmnchg=1; MSCC=1; _BINGNEWS=SW=1184&SH=796; SRCHUSR=DOB=20200318&T=1584539629000; _EDGE_CD=m=en-in&u=en-in; SRCHHPGUSR=HV=1584539634&WTS=63720136429; _EDGE_S=SID=11EFA9648BBC616639B6A7FB8A106091; _clarity=e157844d32b745de8e445240038668f3; _SS=SID=11EFA9648BBC616639B6A7FB8A106091","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
response = requests.get(url,headers=headers)

resp = response.json()

with open("results4.json",'w') as f:
    json.dump(resp,f)

with open("results4.json",'r') as f:
    ditc = json.load(f)

data = []

areas = list(ditc['areas'])
for area in areas:
    totald = area['totalConfirmed']
    #death = area['totalDeaths']
    #rec = area['totalRecovered']
    #active = int(totald)-int(death)-int(rec)
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
        #death = ar['totalDeaths']
        #rec = ar['totalRecovered']
        #active = int(totald)-int(death)-int(rec)
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
            #rdeath = rg['totalDeaths']
            #rrec = rg['totalRecovered']
            #ractive = int(totald)-int(death)-int(rec)
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