from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re,csv
import pandas as pd
from geotext import GeoText

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      #result = request.form
      location = request.form['Location']
      month = request.form['Month']
      days = request.form['Days']
      result = request.form
      print(location)
      print(month)
      print(days)
      x = location
      y = month
      z = int(days)
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
      highlights = []
      pure = []
      cities = []
      print("\n")
    
      for i in ls:
       
          temp = requests.get(i)
          soup = BeautifulSoup(temp.text,'lxml')
          highlights = soup.find_all('h3', class_ = 'fw9 f14 relative m0 pr24 at_iti_title')
          
    
      for i in highlights:
          p = i.text
          if p not in pure:
              pure.append(p)
              
              
              for data in pure:
                  places = GeoText(data)
                  cities.append(places.cities)

      print(pure)
      print(cities) 
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
