import pandas as pd
import requests
from bs4 import BeautifulSoup

#url = "https://www.flipkart.com/"  -->first url run

url ="https://www.flipkart.com/search?q=mobile+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_18_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_18_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+under+50000%7CMobiles&requestId=0a924ed3-6881-424d-8dcd-6c20f99d042d&as-searchtext=mobile%20under%2050000"

r = requests.get(url)
#print(r)   ->first

soup = BeautifulSoup(r.text,"lxml")
#print(soup)       ->second                  # second url run 

while True :
    # link of next page
    np = soup.find('a',class_ = "_9QVEpD").get("href")
    #  print(np)        ->third

    # link of complete next page
    cnp = "https://www.flipkart.com" + np
    print(cnp)          # fourth

    url = cnp
    r =requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
