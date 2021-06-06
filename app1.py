from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password    
        self.bot = webdriver.Chrome(r'C:\Users\Shahd\OneDrive\Desktop\Scraping\chromedriver')

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        bot.find_element_by_class_name('cmbtv').click()
        time.sleep(2)
        bot.find_element_by_class_name('mt3GC').click()
        time.sleep(3)

    def like_post(self):
        bot = self.bot
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            posts = bot.find_elements_by_class_name('eo2As')
            likes = [elem.get_attribute('aria-label') for elem in posts]
            for like in likes:
                bot.find_elements_by_class_name
                try:
                    bot.find_elements_by_class_name('wpO6b').click()
                    time.sleep(3)
                except Exception as ex:
                    time.sleep(60)

ds = InstaBot('_darshil_shah_', 'darsh2210')
ds.login()
ds.like_post()