from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import threading
import interaction
import importlib

chromedriver_path = '/usr/bin/chromedriver'
brave_path = '/usr/bin/brave'
option = webdriver.ChromeOptions()
option.binary_location = brave_path
browser = webdriver.Chrome(executable_path=chromedriver_path, options=option)
browser.get("https://inspire.vitero.de/")
sleep(1)
inputElement = browser.find_element_by_id("username")
inputElement.send_keys('')
inputElement = browser.find_element_by_id("password")
inputElement.send_keys('')
inputElement.send_keys(Keys.ENTER)
sleep(1)
inputElement = browser.find_element_by_id("room-entry-0").click()
inputElement = browser.find_element_by_css_selector("button[type='submit']").click()
sleep(1)
while (True):
    inp = input("Hier was eingeben: ")
    if inp == "start":
        importlib.reload(interaction)
        x = threading.Thread(target=interaction.main, args=(browser, ))
        x.start()
        x.join()
