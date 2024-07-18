import  pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in (2, 12):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_18_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_18_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+under+50000%7CMobiles&requestId=0a924ed3-6881-424d-8dcd-6c20f99d042d&as-searchtext=mobile+under+50000&page="+str(i)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.find("div", class_="DOjaWF gdgoEp")

    # 1.for extracting names from pages
    #names = soup.find_all("div", class_="KzDlHZ")
    names = box.find_all("div", class_ = "KzDlHZ")
    #names = box.find_all("div", class_="KzDlHZ")
    for i in names:
        n = i.text
        Product_name.append(n)

    print(Product_name)     # Names of the mobiles will get print
    print(len(Product_name))    # length of product name --> 24

    # 2. for extracting prices of product from pages
    prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
    for i in prices:
        p = i.text
        Prices.append(p)

    print(Prices)
    print(len(Prices))

    # 3. Extracting description of product
    desc = box.find_all("ul", class_="G4BRas")
    for i in desc:
        d = i.text
        Description.append(d)

    print(Description)
    print(len(Description))

    # 4. Extracting reviews of product
    rev = box.find_all("div", class_="XQDdHH")
    for i in rev:
        r = i.text
        Reviews.append(r)

    print(Reviews)
    print(len(Reviews))

data = pd.DataFrame({"Product_name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews})
print(data)


data.to_csv("Flipkart_mobiles_under_50000.csv")
