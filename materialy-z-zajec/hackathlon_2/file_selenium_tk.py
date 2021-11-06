from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from tkinter import*
import pdfkit

sciezka_chrome = "D:\Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=sciezka_chrome)




miasto = input("Podaj miasto dla którego chcesz znać pogodę na dziś: ")






# driver.get("https://www.yr.no/nb")
# driver.get("https://www.accuweather.com")
# driver.get("https://www.trojmiasto.pl")
# driver.get("https://openweathermap.org")
# driver.get("https://en.wikipedia.org")
driver.get("https://m.meteo.pl/")


def pobierz_pogode_z_meteo():
   miasto_uzytkownik = driver.find_element_by_name("miastoPL")
   miasto_uzytkownik.send_keys(miasto)
   miasto_uzytkownik.send_keys(Keys.ENTER)
   pliki_cookies = driver.find_element_by_xpath('//button[text()="ZGADZAM SIĘ"]')
   pliki_cookies.click()
   obraz = driver.find_element_by_xpath('//*[@id="image_60"]')
   link = obraz.get_attribute("src")
   print(link)

#


   data = requests.get(link).content
   local_filename = 'filename_on_your_computer.jpg'

   with open(local_filename, 'wb') as file:
      file.write(data)

pobierz_pogode_z_meteo()




