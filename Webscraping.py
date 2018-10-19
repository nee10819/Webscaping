
# coding: utf-8

# In[125]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# passing url
r = requests.get("http://property.sulekha.com/property-in-bangalore-for-sale")
c = r.content

soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("li",{"class":"property-list card left"})

# declaring a list for storing all data
l = []
# fetching required data from html tags
for item in all:
    # defining a dictionary for storing data in each loop
    d = {}
    d["Price"]=item.find("div",{"class":"list-price"}).contents[3].text
    d["Landmark"]=item.find("div",{"class":"location truncate"}).contents[1].text
    d["Locality"]=item.find("div",{"class":"location truncate"}).contents[3].text
    d["BHK"]=item.find("div",{"class":"part-detail"}).contents[1].text
    d["Area"]=item.find("div",{"class":"part-detail"}).contents[5].text
    d["Availability"]=item.find("div",{"class":"part-detail"}).contents[7].text
    try:
        d["Property"]=item.find("em",{"class":"builder left truncate"}).contents[3].text
    except IndexError:
        d["Property"]=None
    try:
        d["Builder"]=item.find("em",{"class":"builder left truncate"}).contents[5].text
    except IndexError:
        d["Builder"]=None
    # storing data in list    
    l.append(d)     

# defining a dataframe with list
df = pd.DataFrame(l)

# storing data in a csv file
df.to_csv("Sulekha.csv")


# In[126]:


df

