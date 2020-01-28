import requests
import re
from bs4 import BeautifulSoup
from pandas import DataFrame
ids= []

for i in range(2017,2025):
    ids.append(str(i))
allNames = ["Name"]
print(ids)

for id in ids:
    URL = 'http://stg.apple.corpmerchandise.com/ProductList.aspx?catid='+id
    page = requests.get(URL)
    print(page)

    soup = BeautifulSoup(page.text, "html.parser")
    # print(soup)

    ok = soup.findAll('h4')[::2]


    for elt in ok:
        elt = str(elt)
        # print(elt)
        # print(elt[2:10])
        # print(len(elt))
        # print(elt.rfind(">"))
        # print(elt.find("</h4>"))
        
        name = elt[[m.start() for m in re.finditer(r">",elt)][0]+1:elt.find("</h4>")]
        allNames.append(name)
print(allNames)

df = DataFrame(columns= allNames)

export_excel = df.to_excel (r'/Users/nikosm/Documents/Apple/export_dataframe.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path

print (df)