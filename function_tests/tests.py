#-*- coding:utf-8 -*-
import sys
import time

# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):
    
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

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):

        # Edith 听说有个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get(self.server_url)

        # 她注意到网页的标题头和头部都包含 To-Do 这个词
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)        

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在一个文本框内输入"Buy peacock feathers"
        # Edith 的爱好是使用假蝇做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        # 她按回车键后, 页面更新了
        # 待办事项表格中显示了 "1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 页面中又显示了一个文本框，可以输入其他待办事项
        # 她输入了 "Use peacock feathers to make a fly"
        # Edith 做事很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # 页面再次更新，他的清单中显示了这两个待办事项
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # 现在一个叫做 Francis 的新用户访问了网站

        ## 我们使用一个新的浏览器会话
        ## 确保 Edith 的信息不回从 cookie 中泄漏出来
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis 访问首页
        # 页面看不到 Edith 的清单
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis 输入一个新待办事项，新建一个清单
        # 他不像 Edith 那样兴趣盎然
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Francis 获得了他的唯一 URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 这个页面还是没有 Edith 的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # 两人很满意，去睡觉了


    def test_layout_and_styling(self):
        # Edith 访问首页
        self.browser.get(self.server_url)
        time.sleep(5)

        # NOT RESOVLED:selenium.common.exceptions.WebDriverException: Message: setWindowRect
        # self.browser.set_window_size(1024, 768)

        # # 她看到输入框完美的居中显示
        # inputbox = self.browser.find_elements_by_id('id_new_item')
        # self.assertAlmostEqual(
        #     inputbox.location['x'] + inputbox.size['width']/2,
        #     512,
        #     delta=5
        # )

if __name__ == '__main__':
    unittest.main()
