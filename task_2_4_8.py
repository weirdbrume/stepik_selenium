# task - https://stepik.org/lesson/181384/step/8?unit=156009

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

    button = browser.find_element_by_tag_name('button')
    button.click()

    value = int(browser.find_element_by_id('input_value').text)
    input = browser.find_element_by_id('answer')
    input.send_keys(str(calc(value)))

    button = browser.find_element_by_id('solve')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
