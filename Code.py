import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
import operator

#Web-Scrapping
Titles=[]
Prices=[]
specs=[]

for i in range(1,21):
    url="https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&page="+str(i)
    print (i)
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, "html.parser")
    mobile_div = soup.find_all('a',href=True, attrs={'class':'_31qSD5'})
    for container in mobile_div:
        name=container.find('div',attrs={'class':'_3wU53n'}).text
        Titles.append(name)
        spec=container.ul.li.text
        specs.append(spec)
        price=container.find('div',{"class":"_1vC4OE _2rQ-NK"}).text
        Prices.append(price)
for i in range(0,len(specs)):
    specs[i]=specs[i][0:2]
for i in range(0,len(specs)):
    specs[i].rstrip()
for i in range(0,len(Prices)):
    Prices[i]=Prices[i][1:]
print (Prices)

df = pd.DataFrame({'Product Name':Titles,'Price (Rs)':Prices,'Ram (GB)':specs}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

#Printing the Mobile phone with Highesh Ram and Lowest Price.
data=pd.read_csv('Products.csv')
data= data.sort_values(['Ram (GB)', 'Price (Rs)'], ascending=[False, True])
print (data)
print ("Top 3 Lowest Priced Phones with highest RAM" )
print (data.iloc[0:3,0:])

