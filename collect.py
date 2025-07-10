# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'tiltle':[], 'price':[],'link':[]}
for file in os.listdir("data"):
    try:
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            content = f.read()
        soup = BeautifulSoup(content, 'html.parser')  # If this line causes an error, run 'pip install html5lib' or install html5lib
        t= soup.find("h2")
        title =t.get_text()

        p = soup.find("span", class_="a-price-whole")
        price = p.get_text()
            
        l = soup.find("a")
        link = "https://amazon.in/"+l['href']

        d['tiltle'].append(title)
        d['price'].append(price)
        d['link'].append(link)
    except Exception as e:
        print(e)
df = pd.DataFrame(d)
df.to_csv("data.csv")
print("Data saved to data.csv")
