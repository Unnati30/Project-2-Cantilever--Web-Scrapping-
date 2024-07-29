import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

#print(r)

def getdata(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    #print(soup)

    products = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")
    # print(len(products))

    data = []

    for product in products:
        title = product.find('a', class_='title').text
        price = product.find('h4', class_='price float-end card-title pull-right').text
        description = product.find('p', class_='description card-text').text
        data.append({
            'title': title,
            'price': price,
            'description': description
        })
    return data

def export_data(data):
    df = pd.DataFrame(data)
    df.to_excel("Web_Scrapping.xlsx")

if __name__ == '__main__':
    data = getdata(url)
    export_data(data)
    print("Done")

    open("Web_Scrapping.xlsx")


