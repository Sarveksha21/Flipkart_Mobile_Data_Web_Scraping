import requests
from bs4 import BeautifulSoup

for i in range(2, 10):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_18_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_18_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+under+50000%7CMobiles&requestId=0a924ed3-6881-424d-8dcd-6c20f99d042d&as-searchtext=mobile+under+50000&page="+str(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')
    np = soup.find("a", class_='_9QVEpD').get("href")
    #print(np)
    cnp = "https://www.flipkart.com"+np
    print(cnp)
