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


class YandexParser:

    mintareas = [i for i in range(11, 110)] + [i for i in range(110, 150, 5)] \
                + [i for i in range(150, 200, 10)] + [i for i in range(200, 250, 25)] + [250, 400]
    maxtareas = [i for i in range(11, 110)] + [i for i in range(115, 155, 5)] \
                + [i for i in range(160, 210, 10)] + [i for i in range(225, 275, 25)] + [400, 3000]

    base_url = 'https://realty.yandex.ru/{city}/kupit/kvartira/?areaMin={min}&areaMax={max}&newFlat={is_new}&page={page}'

    def __init__(self, parser_type, logs_path):
        logging.basicConfig(filename=logs_path, level=logging.INFO)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # self.driver = webdriver.Chrome(executable_path=path_to_driver, options=options)
        self.driver = webdriver.Firefox(executable_path=path_to_driver, options=options)
        self.parser_type = parser_type

    def str_prepare(self, s):
        return s.replace('ё', 'е').replace('Ё', 'Е')

    def parse_flat_info(self, url):
        soup = self.captcha_check(url)

    def restart(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def captcha_check(self, url):
        try:
            logging.info(url)
            self.driver.get(url)
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            if soup.find('div', {'id': 'captcha'}):
                logging.info(' captcha... sleeping')
                time.sleep(10)
                self.captcha_check(url)
            else:
                return soup
        except TimeoutException:
            logging.info(' connection fail... RESTARTING APP')
            time.sleep(20)
            self.driver.quit()
            self.restart()
        except:
            logging.info(' connection fail... RESTARTING APP, UNKNOWN ERROR')
            time.sleep(20)
            self.driver.quit()
            self.restart()

    def get_flats_url(self, url):
        pass

    def parse(self, url, whole_parsed_count, whole_saved_count, whole_count):
        pass

    def flats_closing_check(self):
        pass
