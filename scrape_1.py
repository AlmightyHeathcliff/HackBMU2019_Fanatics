import requests
from bs4 import BeautifulSoup
import re,csv
import pandas as pd
from geotext import GeoText



x = input("enter place")
y = input("Month")
z = int(input("day"))
z1 = z+2
temp = requests.get("https://traveltriangle.com/tour-packages/"+x+"?date="+y+"%2C+2019&travelmonth="+y+"%2C+2019&destination_not_decided=&days[]="+str(z)+"-"+str(z1)+"&adult=&children=")
soup = BeautifulSoup(temp.text,'lxml')
text_file = open("Outzero.txt", "w")

ls = []
geez =  soup.findAll('h2', {'class': 'fw9 m0 f16 pfc3'})
x = 'https://traveltriangle.com'
for div in geez:
    y = div.find('a')['href']
    z = x+y
    ls.append(z)




#print(ls)
#print(ls)
print("\n")

for i in ls:
   
   temp = requests.get(i)
   soup = BeautifulSoup(temp.text,'lxml')
   text_file = open("Output.txt", "w")
   highlights = soup.find_all('h3', class_ = 'fw9 f14 relative m0 pr24 at_iti_title')
pure = []

for i in highlights:
    p = i.text
    if p not in pure:
        pure.append(p)
          
cities = []
for data in pure:
    places = GeoText(data)
    cities.append(places.cities)











































