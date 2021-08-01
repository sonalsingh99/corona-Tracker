import requests
import bs4
import tkinter as tk

# Requesting data from worldmeters.
def get_html_data(url):
    data = requests.get(url)
    return data


# Parsing the world's data from worldmeters.
def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div = bs.find("div",class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data=""
    
    for block in info_div:
        text = block.find("h1",class_=None).get_text()
        count = block.find("span",class_=None).get_text()

        all_data = all_data + text + " " + count +"\n" 
    return all_data    


# Parsing individual country's data from worldmeter.
def get_country_data():
    url = "https://www.worldometers.info/coronavirus/country/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div = bs.find("div",class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data=""
    
    for block in range(3):
        text = info_div[block].find("h1", class_ = None).get_text()
        count = info_div[block].find("span", class_ = None).get_text()
        all_data = all_data + text + " " + count +"\n" 

get_covid_data() 