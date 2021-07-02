from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas as pd
Start_Url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(Start_Url)
print(page)
soup = BeautifulSoup(page.text,'html.parser')
start_table =soup.find("table")
temp_list = []

start_table_rows = start_table.find_all("tr")

for tr in start_table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    
print(temp_list)

star_name = []
distance = []
radius = []
mass = []
lum = []

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    radius.append(temp_list[i][6])
    mass.append(temp_list[i][5])
    lum.append(temp_list[i][7])
df = pd.DataFrame(list(zip(star_name,distance,radius,mass,lum)),columns = ["star_name","distance","radius","mass","lum"])
df.to_csv("bright_starts.csv")     


