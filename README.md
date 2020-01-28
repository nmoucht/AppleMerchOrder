# AppleMerchOrder

Repo for parsing excell spreadsheet of orders, and hopefully balance tracking as well.

createDoc.py- parse website and create excell sheet of all products

createJson.py- create price json for each item- TODO: merge createJson and getProductInfo

getProductInfo.py-get whether size and color are necessary for each item

getPersonFromExcell- get person object {"balance":owed, "items":[(size,color,amount)]}

TODOS:
finish getPersonFromExcell
merge createJson and getProductInfo
investigate venmo tracking
