# task - https://stepik.org/lesson/184253/step/6?unit=158843

import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name('button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num = int(browser.find_element_by_id('input_value').text)
    input = browser.find_element_by_id('answer')
    input.send_keys(str(calc(num)))

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
