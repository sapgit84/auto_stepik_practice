import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.open = webdriver.Chrome.get(url)
