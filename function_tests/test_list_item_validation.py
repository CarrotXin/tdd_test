#-*- coding:utf-8 -*-
import time

from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith 访问首页，不小心提交了一个空待办事项 
        # 输入框中没输入任何内容，它就按下了回车键
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(0.5)

        # 首页刷新了，显示一个错误消息
        # 提示待办事项不能为空
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))

        # error = self.browser.find_element_by_css_selector('.has-error')
        # self.assertEqual(error.text, "You can't have an empty list item")

        # 她输入了一些文字，然后再次提交，这次没有问题了
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(0.5)
        self.check_for_row_in_list_table('1: Buy milk')

        # 她有点调皮，又提交了一个空待办事项
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(0.5)

        # 在清单页面她看到了一个类似的错误信息
        self.check_for_row_in_list_table('1: Buy milk')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))
        # error = self.browser.find_element_by_css_selector('.has-error')
        # self.assertEqual(error.text, "You can't have an empty list item")

        # 输入文字后就没有问题了
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(0.5)
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
