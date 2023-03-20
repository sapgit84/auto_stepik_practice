import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
browser = webdriver.Chrome()
try:

    browser.get(link)

finally:
    # успеваем скопировать код за 30 секунд
        time.sleep(10)
    # закрываем браузер после всех манипуляций
        browser.quit()