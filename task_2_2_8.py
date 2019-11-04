# task - https://stepik.org/lesson/228249/step/8?unit=200781

import time
import os
from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element_by_name('firstname')
    input_first_name.send_keys("Elon")

    input_last_name = browser.find_element_by_name('lastname')
    input_last_name.send_keys("Musk")

    input_email = browser.find_element_by_name('email')
    input_email.send_keys("emusk@gmail.com")

    input_file = browser.find_element_by_id('file')
    input_file.send_keys(os.path.abspath('file.txt'))

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
