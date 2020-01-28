import requests
import re
from bs4 import BeautifulSoup
from pandas import DataFrame
import json
ids= []

for i in range(2017,2025):
    ids.append(str(i))
allNames = []
allPrices = []
dictionary = {}
print(ids)

for id in ids:
    URL = 'http://stg.apple.corpmerchandise.com/ProductList.aspx?catid='+id
    page = requests.get(URL)
    print(page)

    soup = BeautifulSoup(page.text, "html.parser")
    print(soup)

    ok = soup.findAll('h4')

    count = 0
    for elt in ok:
        elt = str(elt)
        name = elt[[m.start() for m in re.finditer(r">",elt)][0]+1:elt.find("</h4>")]
        if count % 2 == 0:
            allNames.append(name)
        if count % 2 == 1:
            allPrices.append(name.replace("$",""))
        count += 1

print(allNames)
print(allPrices)

for i in range(0,len(allNames)):
    dictionary[allNames[i]] = allPrices[i]

with open('prices.json', 'w') as outfile:
    json.dump(dictionary, outfile)
