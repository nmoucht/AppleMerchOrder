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

#{"balance":owed, "items":[(name, amount,color,size)]}
personDict = {}
errorList = []
personCount = 0
for person in df:
    count = 0
    total = 0
    perPersonDict = {}
    perPersonDict["items"] = []
    error =0
    for products in person:
        if not pd.isna(products):
            total += int(products[:products.find(",")])*float(data[choices[count]])
            splitCommas = [x.strip() for x in products.split(',')]
            #Only count- (ex. pen)
            if len(splitCommas) == 1:
                try:
                    numItems = int(products)
                    perPersonDict["items"].append((choices[count],numItems, "NA", "NA"))
                except:
                    error = 1

            elif len(splitCommas) == 2:
                try:
                    numItems = int(splitCommas[0])
                    if(len(splitCommas[1])>3):
                        perPersonDict["items"].append((choices[count],numItems, splitCommas[1], "NA"))
                    else:
                        perPersonDict["items"].append((choices[count],numItems,"NA", splitCommas[1]))
                except:
                    error = 1
            elif len(splitCommas) == 3:
                try:
                    numItems = int(splitCommas[0])
                    if(len(splitCommas[1])>3):
                        perPersonDict["items"].append((choices[count],numItems, splitCommas[1], splitCommas[2]))
                    else:
                        perPersonDict["items"].append((choices[count],numItems, splitCommas[2], splitCommas[1]))
                except:
                    error = 1
            else:
                error
        count+=1
    perPersonDict["balance"] = total

    if error==0:
        personDict[names[personCount]] = perPersonDict
    else:
        errorList.append(names[personCount])

    personCount+=1
file1 = open("errorList.txt","w") 
  
file1.writelines(errorList) 
file1.close()

with open('people.json', 'w') as outfile:
    json.dump(personDict, outfile)
print(personDict)
print()