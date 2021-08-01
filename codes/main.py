import requests
import bs4
import tkinter as tk
from PIL import Image, ImageTk

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
    name = textfield.get()
    url = "https://www.worldometers.info/coronavirus/country/"+name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div = bs.find("div",class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data=""
    
    for block in range(3):
        text = info_div[block].find("h1", class_ = None).get_text()
        count = info_div[block].find("span", class_ = None).get_text()
        all_data = all_data + text + " " + count +"\n" 


# Reloading the world's data.
def reload():
    new_data = get_covid_data()
    mainlable['text']=new_data


get_covid_data() 


# Adding tkinter gui to the above code.
root = tk.Tk()
root.geometry("600x600")
root.title("Covid Tracker")
f = ("poppins",25,"bold")


image = Image.open("img\covid.png")
resize_image = image.resize((50, 50))
banner = ImageTk.PhotoImage(resize_image)
bannerlable= tk.Label(root, image=banner)
bannerlable.pack(padx=10,pady=10)

mainlable = tk.Label(root,text=get_covid_data(), font=f)
mainlable.pack(padx=10,pady=10)

textfield = tk.Entry(root,width=50,font=f)
textfield.pack(padx=10,pady=10)

gbtn = tk.Button(root, text="Get Data", font=f, relief="solid", command=get_country_data)
gbtn.pack(pady=10)

rbtn = tk.Button(root, text="Reload", font=f, relief="solid", command=reload)
rbtn.pack()

root.mainloop()