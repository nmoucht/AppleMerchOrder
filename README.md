# AppleMerchOrder

Repo for parsing excell spreadsheet of orders, and hopefully balance tracking as well.

createDoc.py- parse website and create excell sheet of all products

createJson.py- create price json for each item- TODO: merge createJson and getProductInfo

getProductInfo.py-get whether size and color are necessary for each item

getPersonFromExcell- get person object {"balance":owed, "items":[(amount,color,size)]}

TODOS:

merge createJson and getProductInfo

add extra error handling in getPersonFromExcell

investigate auto email creation- https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/

investigate venmo tracking
