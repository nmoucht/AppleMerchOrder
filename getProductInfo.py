import requests
import re
from bs4 import BeautifulSoup
from pandas import DataFrame
ids= []

for i in range(2017,2025):
    ids.append(str(i))

# soup = BeautifulSoup(page.text, "html.parser")
# # print(soup)
# ok = soup.findAll('h4')
# ok =soup.find_all(re.compile(r"simpleProductImage"))
# print(ok)




# allLinks = []
# for id in ids:
#     URL = 'http://stg.apple.corpmerchandise.com/ProductList.aspx?catid='+id
#     page = requests.get(URL)
#     print(page)

#     soup = BeautifulSoup(page.text, "html.parser")
#     # print(soup)

# #     ok = soup.findAll('h4')[::2]
#     ok = soup.findAll('h4')

#     for elt in ok:
#         elt = str(elt)
#         if elt.find("custompage.aspx?")!=-1:
#             thing = elt[elt.find("custompage.aspx?"):[m.start() for m in re.finditer(r">",elt)][0]]
#             allLinks.append(thing[:-2])
# print(len(set(allLinks)))

finalDict = {}
URL = "http://stg.apple.corpmerchandise.com/custompage.aspx?cpn=productDetail&amp;pid=43558"
page = requests.get(URL)
# print(links)
print(page.text)
# soup = BeautifulSoup(page.text, "html.parser")
# for links in allLinks:
#     page = requests.get("http://stg.apple.corpmerchandise.com/"+links)
#     print(links)
#     # print(page)
#     soup = BeautifulSoup(page.text, "html.parser")

#     # print(soup)
#     ok = str(soup.findAll("h1", {"class": "prodName"})[0])
#     tup = [0,0]
#     print()
#     if page.text.find("XS-XL")!=-1:
#         tup[0] = 1
#     if len(soup.find_all("option"))!=0:
#         tup[1] = 1
#     finalDict[ok[ok.find(">")+1:ok.rfind("<")]] = tup

# with open('types.json', 'w') as outfile:
#     json.dump(finalDict, outfile)
#     for elt in ok:
#         elt = str(elt)
#         # print(elt)
#         # print(elt[2:10])
#         # print(len(elt))
#         # print(elt.rfind(">"))
#         # print(elt.find("</h4>"))
        
#         name = elt[[m.start() for m in re.finditer(r">",elt)][0]+1:elt.find("</h4>")]
#         allNames.append(name)
# print(allNames)

# df = DataFrame(columns= allNames)

# export_excel = df.to_excel (r'/Users/nikosm/Documents/Apple/export_dataframe.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path

# print (df)