# task - https://stepik.org/lesson/228249/step/3?unit=200781

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(num1 + num2))

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
