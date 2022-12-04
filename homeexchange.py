from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from openpyxl import Workbook
from requests_html import HTMLSession
s=HTMLSession()

#function to get the html data from urls

def get_url(url):
    r=s.get(url)
    soup=BeautifulSoup(r.text, 'html.parser')
    return soup
def getnextpages(url):
    page=soup.find('ul', {'class': 'pages'})
    if not page.find('li', {'class': "class="active" data-page='70' "}):
        url = 'https://www.homeexchange.com' + str(page.find('li', {'class': "class="active" data-page='70'"}).find('a')['href']) 
        return url
    else: 
        return 
properties = []

wb = Workbook()
ws = wb.active
ws.title = "Extracted Data"
ws.append(["Title", "Rating","Capacity", "Location", "Price", "Number of Reviews"])



for link in links:
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
