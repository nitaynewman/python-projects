from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pywhatkit
import datetime
from time import sleep
import requests
from bs4 import BeautifulSoup

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
web_html = response.text
soap = BeautifulSoup(web_html, 'html.parser')
all_links = soap.find_all(name='a', class_="StyledPropertyCardDataArea-anchor")
all_prices = soap.find_all(name='span', class_="PropertyCardWrapper__StyledPriceLine")
all_addresses = soap.find_all(name='a', class_="StyledPropertyCardDataArea-anchor")

all_links = [link.getText() for link in all_links]
all_prices = [price.getText().strip('m o / b d +') for price in all_prices]
all_addresses = [address.getText() for address in all_addresses]

'''seleniom fill up the forms'''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# chrome_driver_path = "C:/webDriver/chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)


for element in range(len(all_links)):
    driver.get(
        'https://docs.google.com/forms/d/e/1FAIpQLScSHBqvyA65l73bReBJAnGGlDrxb2tCOweDsuj5ZRxXETaN_g/viewform?vc=0&c=0&w=1&flr=0')
    sleep(10)
    element_to_delete = driver.find_element("xpath", "/html/body/div[2]")
    driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", element_to_delete)
    sleep(2)

    address = driver.find_element("xpath",
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price = driver.find_element("xpath",
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')


    link = driver.find_element("xpath",
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[element])
    price.send_keys(all_prices[element])
    link.send_keys(all_links[element])
    submit.click()

