# task - https://stepik.org/lesson/228249/step/8?unit=200781

import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name('button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    num = int(browser.find_element_by_id('input_value').text)
    input = browser.find_element_by_id('answer')
    input.send_keys(str(calc(num)))

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
