import requests
import re
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
import json
import numpy as np
import math

ids= []

xl = pd.ExcelFile("export_dataframe.xlsx")
df = xl.parse("Sheet1")

names = list(df['Name'])
del df['Name']
del df['Email']

choices = list(df)
df = df.values.tolist()

with open('prices.json') as f:
    data = json.load(f)

personDict = {}
personCount = 0
for person in df:
    count = 0
    total = 0
    perPersonDict = {}

    for products in person:
        if not pd.isna(products):
            total += int(products[:products.find(",")])*float(data[choices[count]])
        count+=1
    perPersonDict["balance"] = total

    personDict[names[personCount]] = perPersonDict
    personCount+=1
    
print(personDict)