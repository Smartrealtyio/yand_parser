import requests
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import logging
import sys
import os
import re
import random
from settings_local import *


class Yandex_Parser:

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(executable_path=path_to_driver, options=options)

    def str_prepare(self, s):
        return s.replace('ё', 'е').replace('Ё', 'Е')

    def parse_flat_info(self, url):
        pass

    def restart(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def captcha_check(self, url):
        pass

    def get_flats_url(self, url):
        pass

    def parse(self, url, whole_parsed_count, whole_saved_count, whole_count):
        pass

    def flats_closing_check(self):
        pass
