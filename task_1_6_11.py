# task - https://stepik.org/lesson/138920/step/11?unit=196194

from selenium import webdriver
import time

NORMAL_LINK = 'http://suninjuly.github.io/registration1.html'
LINK_WITH_BUG = 'http://suninjuly.github.io/registration2.html'

try:
    link = LINK_WITH_BUG  # для тестирования второй ссылки поменять на LINK_WITH_BUG
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('.first_block .first')
    input1.send_keys('first_name')
    input2 = browser.find_element_by_css_selector('.first_block .second')
    input2.send_keys('last_name')
    input3 = browser.find_element_by_css_selector('.first_block .third')
    input3.send_keys('email')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
