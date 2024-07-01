from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class openapp():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open_site(self):
        self.driver.get('https://docs.google.com/forms/d/e/1FAIpQLSc7eQITwhjFF8VYD_XibnKBSKNcKS8y1SLdlt44aZ5f57m54Q/viewform?usp=send_form') 
        time.sleep(0.1)
        self.answers()

    def exit(self):
        input("Naciśnij dowolny klawisz, aby zakończyć...")
        self.driver.quit()
    
            

bot = openapp()
bot.open_site()
bot.exit()

