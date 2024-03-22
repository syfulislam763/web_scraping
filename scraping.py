from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
session = HTMLSession()
url = "https://www.daraz.com.bd/womens-traditional-clothing/?page=5&spm=a2a0e.searchlistcategory.pagination.4.615b480366ffGr"


res = session.get(url)
res.html.render()

soup = BeautifulSoup(res.html.html, 'html.parser')

products = []


div = soup.find_all("div", class_="gridItem--Yd0sa")




for item in div:
    image = item.find('img')
    title = image.attrs['alt']
    price = item.find("span", class_="currency--GVKjl").text
    
    products.append([title, price])




df = pd.DataFrame(products, columns=['title', 'price'])
df.to_csv("daraz.csv", index=False)
