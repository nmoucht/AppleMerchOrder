# AppleMerchOrder

Repo for parsing excell spreadsheet of orders, and hopefully balance tracking as well.

createDoc.py- parse website and create excell sheet of all products

createJson.py- create price json for each item- TODO: merge createJson and getProductInfo

getProductInfo.py-get whether size and color are necessary for each item

getPersonFromExcell- get person object {"balance":owed, "items":[(amount,color,size)]}

TODOS:

finish getPersonFromExcell

merge createJson and getProductInfo

investigate auto email creation

investigate venmo tracking
