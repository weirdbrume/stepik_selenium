# task - https://stepik.org/lesson/228249/step/6?unit=200781

import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id('input_value').text)
    input = browser.find_element_by_id('answer')
    input.send_keys(str(calc(x)))

    browser.execute_script("window.scrollBy(0, 100);")

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
