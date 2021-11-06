from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from tkinter import*
import pdfkit

sciezka_chrome = "D:\Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=sciezka_chrome)

def pobierz_pogode_z_meteo(miasto):
   driver.get("https://m.meteo.pl/")
   miasto_uzytkownik = driver.find_element_by_name("miastoPL")
   miasto_uzytkownik.send_keys(miasto)
   miasto_uzytkownik.send_keys(Keys.ENTER)
   pliki_cookies = driver.find_element_by_xpath('//button[text()="ZGADZAM SIĘ"]')
   pliki_cookies.click()
   obraz = driver.find_element_by_xpath('//*[@id="image_60"]')
   link = obraz.get_attribute("src")
   print(link)


   data = requests.get(link).content
   local_filename = 'filename_on_your_computer.jpg'

   with open(local_filename, 'wb') as file:
      file.write(data)

# pobierz_pogode_z_meteo()


from tkinter import*
root = Tk()
root.title("Pogoda na dziś ")
root.config(padx=20, pady=20)
canvas = Canvas(height=200, width=570)
logo_img = PhotoImage(file="pogoda3.png")
# logo_entry = Entry(width=30)
canvas.create_image(220, 80, image =logo_img)
canvas.grid(row =0, column=1)
# canvas.pack()
city_label = Label(root, text="Podaj miasto ")
city_entry = Entry(city_label, width=20)
city_entry.pack(side= LEFT)
city_entry.grid(row=2, column=2)
city_label.grid(row=1, column=1)
wprowadzanie = city_entry.get()
przycisk = Button(root, text="szukaj", command=lambda: pobierz_pogode_z_meteo(city_entry.get()))
przycisk.grid(column=2, row=2)  # położenie przycisku

root.mainloop()



# driver.get("https://www.yr.no/nb")
# driver.get("https://www.accuweather.com")
# driver.get("https://www.trojmiasto.pl")
# driver.get("https://openweathermap.org")
# driver.get("https://en.wikipedia.org")

