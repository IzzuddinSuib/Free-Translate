# from helium import *
# from time import sleep
# # from selenium import *
# from bs4 import BeautifulSoup
# import pandas as pd
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver

# raw_word = 'Saya suka makan kacang'
# print(f"Initial words: ",raw_word)

# start_chrome("https://translate.google.com")
# sleep(2)
# write(raw_word, into=S('.er8xn'))
# sleep(5)

# driver = get_driver()
# # Use Selenium functionality through Helium's browser object to find the element by its class name
# element = driver.find_element(By.CLASS_NAME, 'ryNqvb')

# # Extract the text from the element
# text = element.text

# print(f'Translation: ',text)  # Prints "Good morning"

# kill_browser()

# ---------- OOP -----------
from helium import *
from time import sleep
# from selenium import *
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from helium import start_chrome, write, get_driver, kill_browser, S
from selenium.webdriver.common.by import By
import time

class GoogleTranslator:
    def __init__(self):
        self.driver = None

    def translate(self, raw_words):
        print(f"Initial words: {raw_words}")
        start_chrome("https://translate.google.com")
        time.sleep(2)
        write(raw_words, into=S('.er8xn'))
        time.sleep(5)
        self.driver = get_driver()
        element = self.driver.find_element(By.CLASS_NAME, 'ryNqvb')
        translation = element.text
        print(f"Translation: {translation}")
        kill_browser()
        
def main():
    raw_words = input("Enter the words to translate: ")
    translator = GoogleTranslator()
    translator.translate(raw_words)

if __name__ == "__main__":
    main()
