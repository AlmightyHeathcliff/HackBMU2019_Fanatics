# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:08:10 2019

@author: ashie
"""

import requests
from bs4 import BeautifulSoup
import re,csv
import pandas as pd
from geotext import GeoText

 

location = input()
temp = requests.get("https://www.tours4fun.com/tours/"+location+"/?s=kw")
soup = BeautifulSoup(temp.text,'lxml')

geez =  soup.findAll('div', {'class': 'list-product-item product_click ga_tour_code'})
#print(temp)

links = []

for j,i in enumerate(geez):
   link=""
   title=""
   links.append([])
   try:
      link = i.find('a')['href']
      title = i.find('a')['title']
      links[j].append([link,title])
   except:
      link = i.find('a')['href']
      links[j].append([link,""])
      
   
#links fetched alink with title
#Next we fetch itenerary from each link and save it in csv

print('-----------------------')
MainSites=[]
for i in links:
   schleem=[]
   link = i[0][0]
   print(link)
   try:
      temp = requests.get(link)
      soup = BeautifulSoup(temp.text,'lxml')
      
      
      geez =  soup.findAll('div', {'class': 'bt_itinerary'})
      
      for i in geez:
         #print(i)
         print('--------------')
         
         loc = i.find('h3').text
         schleem.append(loc)
         
         print(loc)
         print(Geotext(loc).cities)
      print('control')   
      MainSites.append(schleem)
      #start Extracting
   except:
      pass
   
   