import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

links = input("Enter you link:")
tags = input("Enter the tag you want of the video:")
store = []

driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
driver.maximize_window()
driver.get(links)

elem = driver.find_element_by_id("react-select-2-input")
elem.send_keys("tags")
elem.send_keys(Keys.ENTER)

if elem:
    for link in elem.find_all(tags):
        done = link.get(elem)[:25]
        store.append(done)
        print(done)

        with open('links.json', 'w') as write_file:
            json.dump(store, write_file)

        try:
            with open('links.json', 'r') as read_file:
                data = json.load(read_file)
                print(data)

        except FileNotFoundError:
            print("You haven't used this before.")

driver.close()