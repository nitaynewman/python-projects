import os
import time
import pickle
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WhatsAppSender:
    def __init__(self, project_dir=None, user_data_dir='User_Data', cookie_path='whatsapp_cookies.pkl'):
        self.project_dir = project_dir or os.path.dirname(os.path.abspath(__file__))
        self.cookie_path = os.path.join(self.project_dir, cookie_path)
        self.user_data_dir = os.path.join(self.project_dir, user_data_dir)
        self.driver = None
        self.init_driver()
        self.open_whatsapp()

    def init_driver(self):
        options = uc.ChromeOptions()
        options.add_argument(f'--user-data-dir={self.user_data_dir}')
        self.driver = uc.Chrome(options=options)

    def save_cookies(self):
        with open(self.cookie_path, 'wb') as filehandler:
            pickle.dump(self.driver.get_cookies(), filehandler)

    def load_cookies(self):
        if os.path.exists(self.cookie_path):
            with open(self.cookie_path, 'rb') as cookiesfile:
                cookies = pickle.load(cookiesfile)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
        else:
            print("No cookie file found. Please log in to WhatsApp Web first.")

    def open_whatsapp(self):
        self.driver.maximize_window()
        self.driver.get('https://web.whatsapp.com')
        
        if not os.path.exists(self.cookie_path):
            print("No cookies found. Please log in manually.")
            time.sleep(30)  # Wait for manual login (adjust time as needed)
            self.save_cookies()
        else:
            print("Loading cookies.")
            self.load_cookies()
            self.driver.refresh()
            time.sleep(10)  # Wait for cookies to be loaded

    def send_msg(self, name, msg, is_gif=False, gif=None):
        wait = WebDriverWait(self.driver, 30)
        print("Opening WhatsApp")

        search = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
        print("Entering name in the search bar")
        search.send_keys(name)
        time.sleep(3)

        contact = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"span[title='{name}']")))
        contact.click()
        print("Entering chat with the contact")
        time.sleep(3)

        text_input = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
        print("Entering message in the text bar")
        text_input.send_keys(msg)
        time.sleep(3)

        if not is_gif:
            send_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')))
        else:
            self.get_gif(gif)
            send_button = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))

        send_button.click()
        print('Message sent successfully')
        time.sleep(5)

    def get_gif(self, gif_link):
        wait = WebDriverWait(self.driver, 30)

        attachment_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')))
        attachment_box.click()
        print('Clicked on attachment box')
        time.sleep(3)

        image_box = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
        image_box.send_keys(gif_link)
        print('Selected image to send')
        time.sleep(5)

    def close(self):
        self.driver.quit()

# Initialize an instance of WhatsAppSender for immediate use
sender = WhatsAppSender()
