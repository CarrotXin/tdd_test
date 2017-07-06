#-*- coding:utf-8 -*-
import sys
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    # in Django 1.11 removed manage.py test --liveserver option
    # @classmethod
    # def setUpClass(cls):
    #     for arg in sys.argv:
    #         if 'liveserver' in arg:
    #             cls.server_url = "http://" + arg.split('=')[1]
    #             return
    #     super().setUpClass()
    #     cls.server_url = cls.live_server_url

    # @classmethod
    # def tearDownClass(cls):
    #     if cls.server_url == cls.live_server_url:
    #         super().tearDownClass()

    def setUp(self):
        self.server_url = "http://amy.com"
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')
