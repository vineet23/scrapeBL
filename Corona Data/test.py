import requests
import csv

url = "https://api.papersqueeze.com/corona/addlocation/"
headers = {"Authorization":"Token da0646e9548cb3fca6ac7e15ed2810a2fd53d2f5"}
data = {"usertype":"admin","condition":"active","place":"","latitude":"","longitude":""}


#response = requests.post(url,headers=headers,data=data)
#print(response.json())
with open ('covid_19_clean_complete.csv','r') as csv_file:
    reader =csv.reader(csv_file)
    next(reader) # skip first row
    for row in reader:
        data['place'] = row[1]
        data['latitude'] = float(row[2])
        data['longitude'] = float(row[3])
        response = requests.post(url,headers=headers,data=data)
        print(response.json())
