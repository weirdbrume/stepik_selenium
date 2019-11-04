# task - https://stepik.org/lesson/165493/step/7?unit=140087

import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_tag_name('img').get_attribute('valuex'))

    input = browser.find_element_by_id('answer')
    input.send_keys(str(calc(x)))

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
