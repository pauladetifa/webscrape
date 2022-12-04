from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from openpyxl import Workbook

properties = []

wb = Workbook()
ws = wb.active
ws.title = "Extracted Data"
ws.append(["Title", "Rating","Capacity", "Location", "Price", "Number of Reviews"])



for page in range(2,6):
    #notice the URL has no page number on the first page. So its best to use url for page two. 
    # "https://www.homeexchange.com/search-v2/everywhere?bounds=-85%2C-180%2C85%2C180&place_id=false"- old url
    #now we have to loop through page=2
    url = ("https://www.homeexchange.com/search-v2/everywhere?bounds=-85%2C-180%2C85%2C180&place_id=false&page=2") 
   
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url + "&page="+str(x))

    soup = BeautifulSoup(driver.page_source, "html.parser")
    lists = soup.findAll(class_="search-result col-sm-6")

    for lists in lists:
        title = lists.find(class_="title").text
        try:
            rating = lists.find(class_="rating").text
        except AttributeError:
            rating = "Not Available"
        try:
            capacity = lists.find(class_="capacity").text
        except AttributeError:
            capacity = "Not Available"

        location = lists.find(class_="home-location").text
        price = lists.find(class_="homebox-review-gp").text

        try:
            number_of_reviews = lists.find(itemprop="reviewCount").text
        except AttributeError:
            number_of_reviews = "Not Available"



        homebox = [title, rating,  capacity,
                    location, price,  number_of_reviews
                    ]
        properties.append(homebox)
        ws.append(homebox)


df = pd.DataFrame(properties)
df.columns = ["Title", "Rating","Capacity", "Location", "Price", "Number of Reviews"]




wb.save("Home Exchange.xlsx")
