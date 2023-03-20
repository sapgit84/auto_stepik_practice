import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

try:

    def test_item_page_have_submit_button(browser):
        browser.implicitly_wait(5)
        browser.get(link)
        # find Submit button
        submit_button = browser.find_elements(By.XPATH, "//button[@type='submit'][@class='btn btn-lg btn-primary "
                                                        "btn-add-to-basket']")
        assert len(submit_button) > 0, 'button not found'
        time.sleep(4)


finally:
    time.sleep(5)
