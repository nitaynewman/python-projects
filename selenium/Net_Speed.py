from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import pywhatkit
# import datetime
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.speedtest.net")

while True:
    go_button = driver.find_element("xpath",
        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
    go_button.click()
    sleep(60)
    DOWNLOAD = driver.find_element("xpath"
        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

    UPLOAD = driver.find_element("xpath",
                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

    sleep(2)
    print(DOWNLOAD, UPLOAD)


    # if int(DOWNLOAD) < 150 or int(UPLOAD) < 10:
    #     '''sending whatsapp message at the time of the time it sucks'''
    #     current_time = datetime.datetime.now()
    #     hour = current_time.hour
    #     minute = current_time.minute
    #     msg = f"your internet sucks at {hour}:{minute} \n your internt download is {DOWNLOAD} Mbps \n and UPLOAD is {UPLOAD} Mbps"
    #     pywhatkit.sendwhatmsg("+972584680232", msg, hour, minute)
