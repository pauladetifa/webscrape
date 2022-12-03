from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from openpyxl import load_workbook, Workbook


for x in range(1, 2):
    url = ("https://www.homeexchange.com/search-v2/everywhere?bounds=-85%2C-180%2C85%2C180&place_id=false")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url + "&page="+str(x))

    soup = BeautifulSoup(driver.page_source, "html.parser")
    lists = soup.findAll(class_="search-result col-sm-6")



    for lists in lists:
        title = lists.find(class_="title").text
        # rating = lists.find(class_="rating").text
        # capacity = lists.find(class_="capacity").text
        location = lists.find(class_="home-location").text
        price = lists.find(class_="homebox-review-gp").text
        # number_of_exchanges = lists.find(class_="icon-home-exchange").text

        homebox = [title, #rating, capacity,
                   location, price, #number_of_exchanges
                   ]

        print(homebox)

